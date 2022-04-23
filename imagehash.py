import cv2
import time

def captureImage(cam):
    result, image = cam.read()

    if result:
        return image

        # cv2.imshow("OutputCapture", image)
        # cv2.waitKey(0)
        # cv2.destroyWindow("OutputCapture")


    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

if __name__=="__main__":
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    while True:
        captureImage(cam)