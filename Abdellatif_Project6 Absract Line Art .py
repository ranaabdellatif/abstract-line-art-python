import dudraw
from random import random
dudraw.clear_rgb(203, 210, 245)
dudraw.set_pen_color_rgb(242, 90, 15)

x_cord = []
y_cord = []

for i in range(10):
    x_cord.append(random())
    y_cord.append(random())

x_speed = []
y_speed = []
for i in range(10):
    x_speed.append(random()*0.03)
    y_speed.append(random()*0.03)



for i in range(100):

    for i in range(len(x_cord)):
        dudraw.line(x_cord[i], y_cord[i], x_cord[i-1], y_cord[i-1])
        dudraw.show(50)
        
        x_cord[i] += x_speed[i]
        y_cord[i] += y_speed[i]
        #bouncing off boundaries
        if x_cord[i] > 1 or x_cord[i] < 0:
            x_speed[i] *= -1
            dudraw.set_pen_color_rgb(17, 255, 0)
        if y_cord[i] > 1 or y_cord[i] < 0:
            y_speed[i] *= -1
            dudraw.set_pen_color_rgb(194, 3, 252)
