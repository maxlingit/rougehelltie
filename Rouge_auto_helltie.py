import pyautogui
import time
import random
import keyboard
import math
import numpy as np
pyautogui.FAILSAFE=True

def hellshot(xm,ym):
    

        #move to 1st location
        pyautogui.moveTo(x=xm, y=ym)
        time.sleep(np.random.normal(0.2, 0.025))

        #press bink
        pyautogui.keyDown('1')
        time.sleep(np.random.normal(0.2, 0.025))
        pyautogui.keyUp('1')
        
        #start shooting
        pyautogui.keyDown('4')
        mouse_cycle()
        #shot shooting
        pyautogui.keyUp('4')
        time.sleep(np.random.normal(0.5, 0.025))
        
def hellshot_rep():

    time.sleep(np.random.normal(4, 0.025))
    n=0
    while n<100:
        print('resting for 3 second')
        time.sleep(np.random.normal(3, 0.025))
        hellshot(400,200)
        time.sleep(np.random.normal(0.3, 0.025))
        hellshot(1400,200)
        time.sleep(np.random.normal(0.3, 0.025))
        hellshot(1400,800)        
        time.sleep(np.random.normal(0.3, 0.025))
        hellshot(400,800)
def mouse_cycle():
    R = 400
    # measuring screen size
    (x,y) = pyautogui.size()
    # locating center of the screen 
    (X,Y) = pyautogui.position(x/2,y/2)
    # offsetting by radius 
    pyautogui.moveTo(X+R,Y)

    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            time.sleep(np.random.normal(0.05, 0.005))
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))



## Run this

hellshot_rep()
