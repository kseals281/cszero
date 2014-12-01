# Name: Khari

# See the README file for instructions.

from main import TurnOn
from main import TurnOff
from main import TurnLeft
from main import Move
from main import PickUp
from main import PutDown

from main import IsAtPickUp
from main import IsAtDeposit
from main import IsAtEnd
from main import IsClearAhead
from main import IsClearLeft
from main import IsClearRight
from main import HasPickUps
from main import HasError


from glob import UP
from glob import RIGHT
from glob import LEFT
from glob import DOWN

# This can be any value 0-7.  Chane it to test each function.
CURRENT_GAME = 3

# Set this to False to just test all your results without a GUI.  When set to True
# it will test one puzzle at a time.
SHOW_GUI = True

# The number of miliseconds between each step.  Raise it to slow things down.
# Lower it to speed it up.
STEP_TIME = 500

def Forward():
    while IsClearAhead() == True:
        Move()
        if IsAtEnd() == True:
            break
        if IsAtPickUp() == True:
            PickUp()
            break


def Wall():
    if IsClearAhead() == False:
        TurnRight()
        Move()
        TurnRight()


def TurnAround():
    TurnLeft()
    TurnLeft()


def GoGet(Steps):
    Forward()
    for i in xrange(Steps):
        if IsClearAhead() == False:
            TurnRight()
        Move()
    item()


def BringBack(Steps):
    TurnAround()
    for i in xrange(Steps):
        Move()
    if IsClearAhead() == False:
        TurnLeft()
    Move()
    Move()

    
def TurnRight():
    for i in xrange(3):
        TurnLeft()
    

def Solve0():
    TurnOn()
    TurnRight()
    while IsAtEnd() != True:
        Wall()
        Forward()
    TurnOff()


def item():
    if IsAtPickUp() == True:
        PickUp()


def drop():
    if IsAtDeposit() == True:
        PutDown()

def Solve1():
    TurnOn()
    TurnRight()
    while IsAtEnd() != True:
        Move()
        Wall()
        item()
        drop()
    TurnOff()
  

def Solve2():
    TurnOn()
    TurnLeft()
    while IsAtEnd() != True:
        Move()
        if IsClearAhead() == False:
            TurnRight()
    TurnOff()


def Solve3():
    TurnOn()
    Move()
    for i in xrange(5):
        GoGet(i)
        BringBack(i)
        drop()
        TurnAround()
    TurnRight()
    Forward()
    TurnOff()

def Solve4():
    TurnOn()
    TurnRight()
    while IsClearRight() == False:
        Move()
    TurnRight()
    while IsAtDeposit() == False:
        Forward()
    TurnRight()
    while IsAtEnd() == False:
        while HasPickUps() == True:
            drop()
        Forward()
    TurnOff()


def Solve5():
    TurnOn()
    TurnAround()
    Move()
    while IsAtEnd() != True:
        TurnLeft()
        Move()
        item()
        while HasPickUps() == True and IsAtDeposit() == True:
                drop()
        if IsAtEnd() == True:
            break
        TurnRight()
        Move()
    TurnOff()


def Solve6():
    TurnOn()
    while IsAtEnd() != True:
        while IsClearAhead() == True:
            Forward()
        TurnRight()
        while HasPickUps() == True and IsAtDeposit() == True:
            drop()
    TurnOff()
    pass


def Solve7():
    TurnOn()
    TurnRight()
    while IsClearAhead() == True:
        Forward()
    TurnLeft()
    while IsClearRight() == False:
        if IsClearAhead() == False:
            TurnLeft()
        Move()
        if IsAtDeposit() == False:
            item()
        drop()
    TurnRight()
    for i in xrange(4):
        Move()
    TurnRight()
    while IsAtEnd() != True:
        Move()
        while HasPickUps() == True:
            drop()
    TurnOff()
