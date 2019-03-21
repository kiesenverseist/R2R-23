import graphics as g
import time
import numpy as np 

print("hello")

win = g.GraphWin(width=400, height=300)

pt = g.Point(200, 150)
pt.draw(win)

cr = g.Circle(pt, 25)
cr.draw(win)

cr.setOutline('blue')
cr.setFill('red')

line = g.Line(pt, g.Point(100, 45))
line.draw(win)

def step(i):
    i /= 20
    cr.move(2*np.sin(i),2*np.cos(i))

def exit():
    win.close()