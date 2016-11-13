#!/usr/bin/python3
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

class HumanGuess():
    def __init__(self, interaction):
        self.humanScore = 0
        self.interaction = interaction

    def robotSelecting(self, robotColor):
        if robotColor == 1:
            api.PlayAction(44) ## TODO: raise left hand slightly (with long pause)
        else:
            api.PlayAction(45) ## TODO: raise right hand slightly (with long pause)

        api.PlayAction(46) ##TODO: raise both hands over head

    def correctGuess(self):
        if self.interaction == 1:
            api.PlayAction(37)
        else:
            api.PlayAction(70)

    def wrongGuess(self):
        if self.interaction == 1:
            api.PlayAction(38)
        else:
            api.PlayAction(71)

    def startGuess(self):
        print 'the robot is now picking a color block'

        blocks = BlockArray(100)

        robotColor = random.randint(1, 2)
        print robotColor
        self.robotSelecting(robotColor)

        flag = True

        print 'please select a color block'

        while 1:
            count = pixy_get_blocks(100, blocks)
            if count > 0:
            # Blocks found #
                for index in range (0, count):
                    if blocks[index].signature == robotColor:
                        print('sig got: ')
                        print blocks[index].signature
                        self.correctGuess()
                        self.humanScore += 1
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

        time.sleep(3)
