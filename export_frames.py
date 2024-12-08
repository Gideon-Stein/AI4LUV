import numpy as np
import cv2



vidcap = cv2.VideoCapture('resources/Vector graphics Eyes animation.mp4')
success,image = vidcap.read()
count = 0
success = True
stack = []
while success:
  try:
    success,image = vidcap.read()
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = image[230:490, 700:1150]
    stack.append(image)
  except:
    pass
stack = np.array(stack)

size = 260,450
fps = 25
np.save( 'resources/eyes/move.npy',stack[30:250])


import numpy as np
import cv2
size = 260,450
fps = 25
np.save( 'resources/eyes/think.npy',stack[0:6])
