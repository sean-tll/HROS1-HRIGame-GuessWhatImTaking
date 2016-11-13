import sys, os, time, ctypes
import api
import humanGuess
import robotGuess
import time
from pixy import *
from ctypes import *

if api.Initialize():
    print("Initialized")
else:
    print("Initialization failed")
    sys.exit(1)

if pixy_init() == 0:
    print("Pixy Initialized")
else:
    print("Pixy Initialization failed")
    sys.exit(1)

api.PlayAction(2)

interaction = 0

if interaction == 1:
    api.PlayAction(25)

time.sleep(5)

hg = humanGuess.HumanGuess(interaction)
for ii in range(3):
    hg.startGuess()

humanScore = hg.humanScore
print 'humanScore:'
print humanScore

time.sleep(10)

rg = robotGuess.RobotGuess(interaction)
for ii in range(3):
    rg.startGuess()

robotScore = rg.robotScore
print 'robotScore:'
print robotScore

time.sleep(5)

if robotScore > humanScore:
    if interaction == 1:
        api.PlayAction(40)
    else:
        api.PlayAction(70)
elif robotScore < humanScore:
    if interaction == 1:
        api.PlayAction(66)
    else:
        api.PlayAction(71)
else:
    if interaction == 1:
        api.PlayAction(30)
    else:
        api.PlayAction(70)

api.ServoShutdown()
print('Finished')
