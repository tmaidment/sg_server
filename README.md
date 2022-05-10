# Speech and Gesture Server

This server handles all of the speech *(sent via TCP socket from the web* *interface)*, and computes the gesture, using the original gesture logic, and forwards it to Emma over the ALProxy interfaces.

This server methodology is much more efficient, since it stops the requirement for re-negotiating the ALProxy connections on each action, by keeping the proxies open, and allows for 
control of Emma outside of singular gestures.

This is done in the main server loop - if a gesture is requested from the web interface, perform it, otherwise, stick to randomly gazing.

In addition, since the speech is handled here, we can modify the lines from pandorabots to randomly select a student to reference. Here, we make sure to look at that student as well.

### Running the Server

Before the server, Emma **MUST** be online and reachable, otherwise the server will crash, and inform you to turn Emma on. The web interface can be started before or after the server, without any issues.

Next, edit the file `speech_gesture_server.py`, if needed, to update any of the server parameters (see file for details - there are comments describing each parameter. *Make sure that the IP and port are correct if having connection issues.*

To use this server, simply run `python speech_gesture_server.py` using Python 2.7, specifically the environment that was originally used for the project. 

### Logging

Each time the server is started, it creates a new log file. The idea is to run the server for the entirety of one session, and then close it afterwards. This ensures that all of the information about the session is contained in one, easy-to-parse, log file. After a session is complete, close and restart the server. Log files are dated, and contain all information about the session. **UNDER NO CONDITION SHOULD YOU DELETE THE LOGS FOLDER**.
