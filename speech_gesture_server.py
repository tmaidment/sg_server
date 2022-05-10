import sys
import os
from naoqi import ALProxy
import zmq
import time
import almath
from gensim.summarization.textcleaner import get_sentences
from datetime import datetime, timedelta
from gestures import *
import logging
from numpy import random

# added by Tristan (5/9/22)
ROBOT_IP = "10.216.112.110"
PORT = 9559

LOG_PATH = './logs'

STUDENT_A_ENABLED = True
STUDENT_B_ENABLED = True
MONITOR_ENABLED = True

#
STUDENT_A_REFERENCE_ENABLED = True
STUDENT_B_REFERENCE_ENABLED = True

STUDENT_A_NAME = "Student A." # keep the trailing period so that the timing from TTS isn't too fast
STUDENT_B_NAME = "Student B." # e.g. "Timmy." or "Spongebob."

MEAN_ACTION_TIME = 10 # The average amount of time between actions
STD_ACTION_TIME = 4 # Standard deviation for sampling time between actions

# YAW, PITCH
# This needs to be set up for the specific table setup
# http://doc.aldebaran.com/2-1/_images/hardware_headjoint_3.3.png
STUDENT_A_ANGLES = [[ -55 * almath.TO_RAD], [2 * almath.TO_RAD]]
STUDENT_B_ANGLES = [[ -15 * almath.TO_RAD], [2 * almath.TO_RAD]]
MONITOR_ANGLES = [[ 55 * almath.TO_RAD], [20 * almath.TO_RAD]]

def run_server(robot_IP, port):
    ## connect to robot
    try:
        motionProxy = ALProxy("ALMotion", robot_IP, port)
    except Exception as e:
        logging.error("Could not create proxy to ALMotion")
        logging.error("MAKE SURE EMMA IS ON AND CAN BE REACHED")
        logging.error( str(e))
        sys.exit(1)

    try:
        postureProxy = ALProxy("ALRobotPosture", robot_IP, port)
    except Exception as e:
        logging.error("Could not create proxy to ALRobotPosture")
        logging.error("MAKE SURE EMMA IS ON AND CAN BE REACHED")
        logging.error( str(e))
        sys.exit(1)

    try:
        tts = ALProxy("ALTextToSpeech", robot_IP, port)
    except Exception as e:
        logging.error("Could not create proxy to ALTextToSpeech")
        logging.error("MAKE SURE EMMA IS ON AND CAN BE REACHED")
        logging.error( str(e))
        sys.exit(1)

    try:
        faceProxy = ALProxy("ALFaceDetection", robot_IP, port)
    except Exception as e:
        logging.error("Error when creating face detection proxy")
        logging.error("MAKE SURE EMMA IS ON AND CAN BE REACHED")
        logging.error(str(e))
        sys.exit(1)

    # Attempt to disable functions of robot, enable breathing for just body.
    faceProxy.enableTracking(False)
    faceProxy.enableRecognition(False)
    motionProxy.killAll()
    motionProxy.setBreathEnabled("Body", True)
    motionProxy.setBreathEnabled("Head", False)

    ## Open server socket, to allow commands from web interface
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    ## Set last motion time
    motion_time = datetime.now()
    time_to_next_action = MEAN_ACTION_TIME

    names = ["HeadYaw", "HeadPitch"]
    angleLists = [[ 0 * almath.TO_RAD], [0 * almath.TO_RAD]]

    while True:
        try:
            #  Wait for next request from client
            message = socket.recv(flags=zmq.NOBLOCK)
            logging.info("From Socket: " + str(message))

            # clean input
            args = message.split("$")
            robot_IP = args[0]
            port = args[1]
            line = args[2]
            user_ID = args[3]
            date = args[4]
            typeEnt = args[5]
            adj = args[6]

            motionProxy.killTasksUsingResources([
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"])
            nonProbabilisticMovement(motionProxy, faceProxy, tts, line)
            motion_time = datetime.now()
            time_to_next_action = random.normal(MEAN_ACTION_TIME, STD_ACTION_TIME)
            logging.info("Wait Time: " + str(time_to_next_action))

            #  Send reply back to client
            socket.send(b"complete")
        except:
            # if no commands, look around
            if datetime.now() > motion_time + timedelta(0,time_to_next_action):
                roll = random.uniform(0, 1)
                if roll < 0.375 and STUDENT_A_ENABLED:
                    angleLists = STUDENT_A_ANGLES
                    logging.info("Focus: Student A")
                elif roll < 0.75 and STUDENT_B_ENABLED:
                    angleLists = STUDENT_B_ANGLES
                    logging.info("Focus: Student B")
                elif MONITOR_ENABLED:
                    angleLists = MONITOR_ANGLES
                    logging.info("Focus: Monitor")
                motion_time = datetime.now()
                time_to_next_action = random.normal(MEAN_ACTION_TIME, STD_ACTION_TIME)
                logging.info("Wait Time: " + str(time_to_next_action))
            
            motionProxy.post.angleInterpolation(names, angleLists, [1,1], True)
            time.sleep(1)
            
# mostly from previous code, some changes to enable referencing (head movement)
def nonProbabilisticMovement(motionProxy, faceProxy, tts, line):

    tokenized = list(get_sentences(line))
    if len(tokenized) > 1:
        for idx, token in enumerate(reversed(tokenized)):
            if '?' in token or 'help me' in token.lower():
                roll = random.uniform(0, 1)
                names = ["HeadYaw", "HeadPitch"]
                #faceProxy.enableTracking(False)
                if roll < 0.25 and STUDENT_A_REFERENCE_ENABLED:
                    tokenized.insert(-idx-1, STUDENT_A_NAME)
                    angleLists = STUDENT_A_ANGLES
                    motionProxy.post.angleInterpolation(names, angleLists, [1,1], True)
                    #faceProxy.enableTracking(True)
                    logging.info("Focus: Student A (Referenced)")
                elif roll < 0.5 and STUDENT_B_REFERENCE_ENABLED:
                    tokenized.insert(-idx-1, STUDENT_B_NAME)
                    angleLists = STUDENT_B_ANGLES
                    motionProxy.post.angleInterpolation(names, angleLists, [1,1], True)
                    #faceProxy.enableTracking(True)
                    logging.info("Focus: Student B (Referenced)")
                break
    ref_line = ' '.join(tokenized)

    ## gesture categories
    question = ["?", "So is"]
    makeAPoint = ["I think ", "I thought ", "I know ", "I get it ", "I will ", "Oh okay ", "Ohhh. ", "Oh ", "Maybe "]
    agree = ["yes", "Yes ", "I agree ", "you're right ", " good ", " great "]
    disagree = [" no ", "No ", "I disagree "]
    greet = ["Hello", " hello", "Hey", " hey ", "Hi", " hi "]

    ## number of times this gesture TYPE found in line
    counts = {"greet":0,"agree":0,"disagree":0, "makePoint":0,"question":0}

    movement = True

    if any(word in line for word in greet):
        counts["greet"] += 1
    elif any(word in line for word in agree):
        counts["agree"] += 1
    elif any(word in line for word in disagree):
        counts["disagree"] += 1
    elif any(word in line for word in makeAPoint):
        counts["makePoint"] += 1
    elif any(word in line for word in question):
        counts["question"] += 1
    else:
        movement = False

    if movement:
        gestures = {}
        for key, val in counts.iteritems():
             if val > 0:
                 gestures[key] = val

        maxGesture = max(gestures, key=gestures.get)


        if maxGesture == "greet":
            tts.post.say(line)
            logging.info('Response: ' + line)
            waveRight(motionProxy)
        elif maxGesture == "agree":
            tts.post.say(line)
            logging.info('Response: ' + line)
            handsOut(motionProxy)
        elif maxGesture == "disagree":
            tts.post.say(line)
            logging.info('Response: ' + line)
            handOutLeft(motionProxy)
        elif maxGesture == "makePoint":
            tts.post.say(line)
            logging.info('Response: ' + line)
            handsOnHips(motionProxy)
        elif maxGesture == "question":
            tts.post.say(ref_line)
            logging.info('Response: ' + ref_line)
            largeShrug(motionProxy)

        logging.info('Gesture: ' + maxGesture)
        

    else:
        tts.say(line)

if __name__ == '__main__':
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)
    filename = os.path.join(LOG_PATH, '{}.log'.format(datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S")))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M:%S',
                        filename=filename,
                        filemode='w')
    logging.getLogger().addHandler(logging.StreamHandler())
    run_server(ROBOT_IP, PORT)
    