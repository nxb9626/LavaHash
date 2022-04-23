import cv2
import threading
from flask import Flask
from imagehash import captureImage
app = Flask(__name__)


@app.route("/lamp")
async def random():
    cam = cv2.VideoCapture(CAM_PORT)
    image = captureImage(cam)
    
    cv2.imwrite("lavaLamp.png",image)
    # x.start()
    x = str(hash(str(image)))
    print(x)
    return x
    # return "<p>Hello, World!</p>"

if __name__=="__main__":
    CAM_PORT = 0
    app.run(port=8080)