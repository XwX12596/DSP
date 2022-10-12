import requests

od = {'action':'snapshot'}

authe = ('xmh','xmhxmhxmh')

response = requests.get("http://mc.xwxstudio.com/?",params=od, auth=authe)
response.raise_for_status()
with open('./Monthly1/code/snapshot.jpg','wb') as f:
    f.write(response.content)

# from picamera.array import PiRGBArray
# from picamera import PiCamera
# import cv2

# # define resolution
# resX = 320
# resY = 240

# def main():
#     camera = PiCamera()
#     camera.resolution = (resX, resY)
#     camera.framerate = 24
#     # Use this as our output
#     rawCapture = PiRGBArray(camera, size=(resX, resY))

#     # capture frames from the camera
#     for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#         image = frame.array

#         # show the frame
#         cv2.imwrite("snapshot" + ".jpg", image)

import cv2
import numpy

#init
camera = cv2.VideoCapture(1)

#read the camera
ret,img = camera.read()

#保save to snapshot.jpg
cv2.imwrite('./img.jpg',img)

#release the camera
camera.release()
cv2.destroyAllWindows()