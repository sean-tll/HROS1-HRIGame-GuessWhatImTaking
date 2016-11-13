import sys, os, time, ctypes
import api
from pixy import *
from ctypes import *
import random
import time

class Blocks (ctypes.Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]

class RobotGuess():
    def __init__(self, interaction):
        self.robotScore = 0
        self.interaction = interaction

    def correctGuess(self):
        if self.interaction == 1:
            api.PlayAction(23)
        else:
            api.PlayAction(70)

    def wrongGuess(self):
        if self.interaction == 1:
            api.PlayAction(66)
        else:
            api.PlayAction(71)

    def robotRaiseHand(self, robotColor):
        if robotColor == 1:
            api.PlayAction(49) ## TODO: raise left hand slightly (with long pause)
        else:
            api.PlayAction(50) ## TODO: raise right hand slightly (with long pause)

    def startGuess(self):
        print 'please select a color block'
        time.sleep(5)
        print 'the robot is now selecting a block'
        robotColor = random.randint(1, 2)
        self.robotRaiseHand(robotColor)
        time.sleep(2)
        print 'please show robot the block your selected'

        blocks = BlockArray(100)

        flag = True

        while 1:
            count = pixy_get_blocks(100, blocks)
            if count > 0:
            # Blocks found #
                for index in range (0, count):
                    if blocks[index].signature == robotColor:
                        print('sig got: ')
                        print blocks[index].signature
                        self.correctGuess()
                        self.robotScore += 1
                        flag = False
                    if blocks[index].signature != robotColor:
                        print('sig got: ')
                        print blocks[index].signature
                        self.wrongGuess()
                        flag = False
                    if flag == False:
                        break

                if flag == False:
                    break
