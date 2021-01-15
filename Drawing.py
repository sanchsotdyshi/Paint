import argparse
import cv2 
import numpy as np

# Create a canvas 
x = np.empty((800,600,3), np.uint8)
canvas = np.full_like(x, [255, 255, 255])

# Stub function
def nothing(x):
    pass

# Drawing function
def draw(event,x,y,flags,param):
	global drawing, eraser
	
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True

	if event == cv2.EVENT_RBUTTONDOWN:
		eraser = True

	if event == cv2.EVENT_MOUSEMOVE:
		if eraser == True:
			cv2.rectangle(canvas,(x + size, y + size),(x - size, y - size),(255, 255, 255),-1)

		if drawing == True:
			if mode == 0:
				cv2.circle(canvas,(x,y), size,(b, g, r),-1)
			if mode == 1:
				cv2.rectangle(canvas,(x + size, y + size),(x - size, y - size),(b, g, r),-1)

	if event == cv2.EVENT_LBUTTONUP:
		drawing = False

	if event == cv2.EVENT_RBUTTONUP:
		eraser = False

# Processing mouse actions
cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint',draw)

# Create Trackbars
cv2.createTrackbar('R','Paint',0,255,nothing)
cv2.createTrackbar('G','Paint',0,255,nothing)
cv2.createTrackbar('B','Paint',0,255,nothing)
cv2.createTrackbar('Size','Paint',1,10,nothing)
cv2.createTrackbar('Mode','Paint',0,1,nothing)

# Variables for defining the size and shape of the brush
size = 1
mode = 0

# Main program loop
while(1):

	# Show canvas
	cv2.imshow('Paint', canvas)

	# Collecting data from trackbars
	r = cv2.getTrackbarPos('R','Paint')
	g = cv2.getTrackbarPos('G','Paint')
	b = cv2.getTrackbarPos('B','Paint')
	size = cv2.getTrackbarPos('Size','Paint')
	mode = cv2.getTrackbarPos('Mode','Paint')
	
	# Save the key that the user pressed
	k = cv2.waitKey(10)

	# If key is "Esc" - exit
	if k == 27:
		break

	# If key is "S" - save file
	if k == ord('s'):
		cv2.imwrite("picture.png", canvas)

	# If key is "C" - clear canvas
	if k == ord('c'):
		canvas = np.full_like(x, [255, 255, 255])

cv2.destroyAllWindows()






