import requests
import pyautogui as py
import pyperclip
# location of first tab 74 23
# location of url 190 57
# exit()
def copy_clipboard():
    py.hotkey('ctrl', 'c')
    py.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()


py.click(11, 30)
py.tripleClick(253, 56)
var = copy_clipboard()
print(var)

for i in range(3):
    py.click(70, 340)
    py.sleep(1)
    py.hotkey('ctrl','s')
    py.sleep(2)
    py.click(534,684)
    py.sleep(2)
    py.click(350,350)
    py.hotkey('ctrl','w')

