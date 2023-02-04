# copy line by line from a text file and
#  past on (x,y) after a particular time 
#  hit enter hot key 
import time
import pyautogui as py
# discord chat box 343 685
py.click(343, 685)
# py.write('kkkkkkkkkkkkkkkkkkctnxndvcgwerucyngikusgirynsgf', interval=0.05)  # Type with quarter-second pause in between each key.
# py.press('enter')

filePath = "C:/Users/ek440/Desktop/query.txt"
# filePath = filePath.replace( "\\" , "/") 
# print("C:\Users\ek440\Desktop\query.txt".replace("\\","/"))
file_content = open(filePath, 'r')
for line in file_content:
    # txt = line
    py.write(line, interval=0.09)
    py.press('enter')
    time.sleep(1)
