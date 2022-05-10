import almath
import time

# made by Tristan (5/9/22)
# from original motion control files
# NOTE THAT THERE IS NO HEAD MOVEMENT SENT - this is so that the gazing still works
# Do NOT add motions without moving head from names, angleLists, and timeLists!!!

def largeShrug(motionProxy):
    names = [
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [

                  [65.0 * almath.TO_RAD, 65.0 * almath.TO_RAD],
                  [-4.0 * almath.TO_RAD, -4.0 * almath.TO_RAD],
                  [-119.8 * almath.TO_RAD, -119.8 * almath.TO_RAD],
                  [-79.8 * almath.TO_RAD, -79.8 * almath.TO_RAD],
                  [-49.6 * almath.TO_RAD, -49.6 * almath.TO_RAD],
                  [1],

                  [65.0 * almath.TO_RAD, 65.0 * almath.TO_RAD],
                  [4.0 * almath.TO_RAD, 4.0 * almath.TO_RAD],
                  [119.8 * almath.TO_RAD, 119.8 * almath.TO_RAD],
                  [79.8 * almath.TO_RAD, 79.8 * almath.TO_RAD],
                  [49.6 * almath.TO_RAD, 49.6 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5],

                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5, 1.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I don't know how to solve it")
    time.sleep(2.0)


def handsOnHips(motionProxy):
    names = [
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [

                  [75.0 * almath.TO_RAD],
                  [27.0 * almath.TO_RAD],
                  [-5.8 * almath.TO_RAD],
                  [-86.8 * almath.TO_RAD],
                  [0.6 * almath.TO_RAD],
                  [0],

                  [84.0 * almath.TO_RAD],
                  [-29.9 * almath.TO_RAD],
                  [18.5 * almath.TO_RAD],
                  [79.2 * almath.TO_RAD],
                  [1.8 * almath.TO_RAD],
                  [0]]

    # *almath.TO_RAD
    timeLists = [

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]
    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know what to do!")
    time.sleep(2.0)

def handsOut(motionProxy):
    names = [
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [

                  [12.4 * almath.TO_RAD],
                  [19.1 * almath.TO_RAD],
                  [-119.5 * almath.TO_RAD],
                  [-82.5 * almath.TO_RAD],
                  [39.9 * almath.TO_RAD],
                  [1],

                  [9.5 * almath.TO_RAD],
                  [-19.8 * almath.TO_RAD],
                  [119.1 * almath.TO_RAD],
                  [87.0 * almath.TO_RAD],
                  [-49.5 * almath.TO_RAD],
                  [1]]

    # *almath.TO_RAD
    timeLists = [

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.0]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("I think I know the answer!")
    time.sleep(2.0)

def waveRight(motionProxy):
    names = [
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [

                  [80.0 * almath.TO_RAD],
                  [6.5 * almath.TO_RAD],
                  [-46.8 * almath.TO_RAD],
                  [-57.8 * almath.TO_RAD],
                  [7.6 * almath.TO_RAD],
                  [0],

                  [2.3 * almath.TO_RAD],
                  [-18.9 * almath.TO_RAD],
                  [73.5 * almath.TO_RAD, 112.5 * almath.TO_RAD, 73.5 * almath.TO_RAD, 112.5 * almath.TO_RAD],
                  [86.2 * almath.TO_RAD],
                  [-66.8 * almath.TO_RAD],
                  [1]]


    timeLists = [

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],

                 [0.5],
                 [0.5],
                 [0.5, 1.0, 1.5, 2.0],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("Hello! Nice to meet you.")
    time.sleep(2.0)

def handOutLeft(motionProxy):
    names = [
             "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand",
             "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
    angleLists = [

                  [62.1 * almath.TO_RAD],
                  [-1.2 * almath.TO_RAD],
                  [-110.7 * almath.TO_RAD],
                  [-49.2 * almath.TO_RAD],
                  [-69.8 * almath.TO_RAD],
                  [1],

                  [80.7 * almath.TO_RAD],
                  [0.2 * almath.TO_RAD],
                  [54.8 * almath.TO_RAD],
                  [49.6 * almath.TO_RAD],
                  [4.3 * almath.TO_RAD],
                  [0]]

    timeLists = [

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [1.5],

                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5],
                 [0.5]]

    isAbsolute = True
    # the post is so it happens at the same time as the speech
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, isAbsolute)
    ## tts.say("She ran three kilometers")
    time.sleep(2.0)