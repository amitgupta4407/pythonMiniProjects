
import pyautogui as py
import time
t1 = time.time()
# time.sleep(2)
# print()
# py.alert('This is the message to display.') use for exit at a point of program
while time.time()-t1 < 4:
    # print(time.time()-t1)
    currentMouseX, currentMouseY = py.position()
    print(currentMouseX, currentMouseY)
# discord chat box 343 685