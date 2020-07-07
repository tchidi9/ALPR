import numpy as np
import cv2 as vCapture
import datetime

class Capture():
    """
    When this class is called, it captures video for the number of seconds specified and
    saves it to a remote location accessible by the program 

    # captureDuration - The duration in seconds of the video captured
    """
    def video(self, captureDuration, savePath, displayVideo):
	if (captureDuration > 0):
		__date__ = str(datetime.datetime.today())

		#set file name
		fileName = "%s_Cam1_%s.avi" % (savePath, (__date__))

		#initialize video capture
		cap = vCapture.VideoCapture(0)

		# set video writer source
		fourcc = vCapture.VideoWriter_fourcc(*'XVID')
		out = vCapture.VideoWriter(file_name, fourcc, 20.0, (640,480))

		# set timer to monitor length of capture 
		startTime = time.time()		

		# set variable to monitor whento stop the capture once the time is up to the specified time
		stopCapture = False

		# keep capturing video until the video capture time is up		
		while( not stopCapture ):
		    ret, frame = cap.read()
		    if ret==True:
			# flip capture frame from being up-side-down
			frame = vCapture.flip(frame,0)

			# write frame to specified video path
			out.write(frame)

			# Show ovideo if display video variable is set
			if(displayVideo):
			    vCapture.imshow(('frame_%s', (__date__)),frame)
		    else:
			break

		    stopCapture = int(time.time() - startTime) < captureDuration

		cap.release()
		out.release()
		vCapture.destroyAllWindows()
	return fileName
