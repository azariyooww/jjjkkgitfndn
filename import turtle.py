import turtle
t = turtle.Turtle()
for i in range (180):
    t.speed(0)
    t.color('#E90074')
    t.circle(190 - i, 90)
    t.left(90)
    t.color('#F19ED2')
    t.circle(190 - i, 90)
    t.left(18)