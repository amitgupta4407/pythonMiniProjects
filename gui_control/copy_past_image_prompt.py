
import pyautogui as py
py.click(1243, 11)
py.click(343, 685)


filePath = "C:/Users/ek440/Desktop/prompt_day5.txt"
# "C:\Users\ek440\Desktop\prompt_day5.txt"
file_content = open(filePath, 'r', encoding='utf-8')
def type_prompt(s):
    py.write("/imagine")
    py.sleep(2)
    py.press('tab')
    py.sleep(2)
    py.write(prompt, interval=0.05)
    py.sleep(0.5)
    py.press("enter")
    py.sleep(30)
c = 0
for line in file_content:
    prompt = str(line)[:-1] + " --ar 3:2 --q 2 --s 750"
    type_prompt(prompt)
    c+=1
    print(f"done {c}")