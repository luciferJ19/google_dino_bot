import mss
import pyautogui
import cv2
import keyboard
import numpy as np
import time

def grabFrame(region):
    with mss.mss() as sct:
        frame = np.array(sct.grab(region))
        screenGrayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return screenGrayscale

def detectObstacle(frameGray):
    for z in [0, frame.shape[0]-1]:
        if len(set(frameGray[z])) > 1:
            return True
    return False

def instantiateJump(collisionStatus):
    if collisionStatus == True:
        pyautogui.keyDown("space")

region = {"top": 392, "height": 54, "left": 244, "width": 115}
prevTime = 0
if __name__ == "__main__":
    time.sleep(3)
    while True:
        timeStart = time.time()
        if keyboard.is_pressed("q"):
            break

        frame = grabFrame(region)
        collisionStatus = detectObstacle(frame)
        instantiateJump(collisionStatus)
        deltaTime = timeStart - prevTime

        if deltaTime>80:
            region["width"]+=50
            prevTime = timeStart
        #print(pyautogui.position())