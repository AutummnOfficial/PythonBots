#######################################
# NOTE: USE https://cookie-clicker2.com AND SCROLL UNTIL THE AUTOPLAYER IS CORRECTLY POSITIONED
from PIL import ImageGrab
from directKeys import click, queryMousePosition
import time
import keyboard as kb
import pyautogui
import cv2


def check(image):
    global clickCookie

    if image.getpixel(xy=clickerP) == (81, 57, 109) and not debug:
        clickCookie = False
        click(x=clickerP[0], y=clickerP[1])
    else:
        if not debug:
            clickCookie = True

    if image.getpixel(xy=clickerUp) == upgradableColor and not debug:
        clickCookie = False
        click(x=clickerUp[0], y=clickerUp[1])
    else:
        if not debug:
            clickCookie = True

    if image.getpixel(xy=grandmaUp) == upgradableColor and not debug:
        clickCookie = False
        click(x=grandmaUp[0], y=grandmaUp[1])
    else:
        if not debug:
            clickCookie = True

    if image.getpixel(xy=mineUp) == upgradableColor and not debug:
        clickCookie = False
        click(x=mineUp[0], y=mineUp[1])
    else:
        if not debug:
            clickCookie = True

    if image.getpixel(xy=farmUp) == upgradableColor and not debug:
        clickCookie = False
        click(x=farmUp[0], y=farmUp[1])
    else:
        if not debug:
            clickCookie = True


# upgrades
clickerUp = (772, 328)
grandmaUp = (772, 394)
farmUp = (772, 457)
mineUp = (772, 520)
cookiePos = (557, 359)
upgradableColor = (192, 192, 192)

# point
clickerP = (766, 250)

# properties
clickCookie = True
debug = False
while True:
    pos = queryMousePosition()
    image = ImageGrab.grab()
    # gray = cv2.cvtColor(Screen, cv2.COLOR_BGR2GRAY)
    check(image)
    if clickCookie and not debug:
        click(x=cookiePos[0], y=cookiePos[1])

    if kb.is_pressed('Esc'):
        break
    if kb.is_pressed("N"):
        click(x=690, y=641)

    if kb.is_pressed("Ctrl") and debug:
        print(pyautogui.position())
        print(image.getpixel(pyautogui.position()))
