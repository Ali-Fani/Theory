import turtle
from math import pi, sin, cos

t = turtle.Turtle()

t.speed(2)
t.shape("turtle")
t.penup()


def draw(side: int, radius: int):
    for num in range(side + 1):
        angel = num * 360 / side
        print(f"slide angle is {angel}")
        if num:
            t.pendown()
        y = sin(angel * pi / 180) * radius
        x = cos(angel * pi / 180) * radius
        t.setheading(t.towards(x, y))
        t.setpos(x, y)


m = 30
scope = 0
for i in range(3, m):
    print(f"index is {i}")
    scope = i * 10 + scope * .4
    print(f"scope is {scope}")
    draw(i, scope)
    t.penup()
t.Screen().exitonclick()
