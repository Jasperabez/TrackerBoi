GO TO <a href="https://github.com/weijuinlee/EA_Projects">hhttps://github.com/weijuinlee/EA_Projects</a>

**New to python?**

Useful links for Thonny IDE:

[![](http://img.youtube.com/vi/lWaCl0WjNZI/0.jpg)](http://www.youtube.com/watch?v=lWaCl0WjNZI "")

 * Complete guide to downloading and setting up Thonny IDE
 * Basic walk-through into simple arithmetic and functions

[![alt text](http://img.youtube.com/vi/dGvQPp0zEM4/0.jpg)](http://www.youtube.com/watch?v=dGvQPp0zEM4 "thonnyvideo")

 * Knowing that themes are so **critical** to programmers, this video guides you to select your preferred look in Thonny IDE

Useful links to learn Python:

[![alt text](http://img.youtube.com/vi/yE9v9rt6ziw/0.jpg)](http://www.youtube.com/watch?v=yE9v9rt6ziw "pythonvideo")

 * Illustrative programming educational material - Clear and Concise
 * Includes programming exercises, questions and cheat sheet

## Space Impact Game

**Demo Video:**

[![alt text](http://img.youtube.com/vi/H4Yo7XGbGSM/0.jpg)](https://www.youtube.com/watch?v=H4Yo7XGbGSM "spaceimagedemo")

**Code:**

```python

from microbit import *

def controls():
    sleep(100)
    (a,b) = (button_a.was_pressed(),button_b.was_pressed())   
    if a and b:
        return 10
    elif a:
        return -1
    elif b:
        return 1
    else:
        return 0
    
def shooting():
    if controls() == 10:
        return 0

def printBoard (move,previousPost):
    x=0
    y=0
    if move == 10:
        move = 0
    currentPost = previousPost + move
    if currentPost > 4:
        currentPost = 4
    if currentPost < 0:
        currentPost = 0
    boardStatus1[previousPost][4] = 0
    boardStatus1[currentPost][4] = 1
    killFactor = shooting()
    if killFactor == 0:
        boardStatus1[currentPost][0]=0
    for row in boardStatus1:
        for status in boardStatus1[x]:
            if status == 1:
                display.set_pixel(x,y,9)
            elif status == 0:
                display.set_pixel(x,y,0)
            y += 1            
            if y > 4:
                y = 0
        x += 1
        if x > 5:
            x=0
    return currentPost
    print("Current Post: "+ str(currentPost))
    
def initFunction(startPoint):
    boardStatus1[startPoint][4]=1
        
display.scroll("Start!!!")
boardStatus1 = [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
boardStatus2 = [[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
boardStatus3 = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
boardStatus4 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
boardStatus5 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,0]]
boardStatus6 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1]]
initCompleted=0
 
while True:
    if initCompleted == 1:
        prevPosition=postNow
        postNow=printBoard(controls(),prevPosition)
    if initCompleted == 0:
        prevPosition=2
        postNow=printBoard(controls(),prevPosition)
        initCompleted=1
    if boardStatus1 == boardStatus2:
        display.scroll("Won!!!")
    if boardStatus1 == boardStatus3:
        display.scroll("Won!!!")
    if boardStatus1 == boardStatus4:
        display.scroll("Won!!!")
    if boardStatus1 == boardStatus5:
        display.scroll("Won!!!")
    if boardStatus1 == boardStatus6:
        display.scroll("Won!!!")
```

What were your problems and how did i fix the bugs:

 1. As there are 5 scenarios for the player to win,I had to think about how to determining if the player has won. For know, I have simply checked the status of the board to all 5 scenarios

 2. To prevent the pointer from going out of list, I simply checked and set a minimum and maximum to the pointer range

My obstacles:

 1. Understanding the logic behind the game

Tips to the aspiring coders out there:

 * Write the program structure out before you start
 * Use print statements to check your program and fix bugs
