import pyautogui as py
screenWidth, screenHeight = py.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = py.position() # Returns two integers, the x and y of the mouse cursor's current position.
# py.alert('This is an alert box.')
# py.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
# py.click() # Click the mouse at its current location.
# py.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
# py.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# py.doubleClick() # Double click the mouse at the
# py.moveTo(500, 500, duration=2, tween=py.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.
# py.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
# py.press('esc') # Simulate pressing the Escape key.
# py.keyDown('shift')
# py.write(['left', 'left', 'left', 'left', 'left', 'left'])
# py.keyUp('shift')
# py.hotkey('ctrl', 'c')

"""Display Message Boxes
    >>> pyautogui.alert('This is an alert box.')
    'OK'
    >>> pyautogui.confirm('Shall I proceed?')
    'Cancel'
    >>> pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
    'B'
    >>> pyautogui.prompt('What is your name?')
    'Al'
    >>> pyautogui.password('Enter password (text will be hidden)')
    'swordfish'
"""

"""Screenshot Functions
(PyAutoGUI uses Pillow for image-related features.)

    >>> import pyautogui
    >>> im1 = pyautogui.screenshot()
    >>> im1.save('my_screenshot.png')
    >>> im2 = pyautogui.screenshot('my_screenshot2.png')
You can also locate where an image is on the screen:

    >>> import pyautogui
    >>> button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
    >>> button7location
    (1416, 562, 50, 41)
    >>> buttonx, buttony = pyautogui.center(button7location)
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
The locateCenterOnScreen() function returns the center of this match region:

    >>> import pyautogui
    >>> buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching region
    >>> buttonx, buttony
    (1441, 582)
    >>> pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
"""