import pyautogui as py
def openApp(appName):
    py.press("win")
    py.sleep(0.5)
    py.write(appName,0.05)
    py.sleep(0.5)
    py.press("enter")
print("from brave script")
openApp("Brave")
py.sleep(1)
py.hotkey('win',"left")
py.sleep(1)
openApp("notepad")
py.sleep(1)
py.hotkey('win',"right")