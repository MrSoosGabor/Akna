import turtle


def szinez(x, y):
    for s in matrix:
        for o in s:
            if o.distance(x, y) < 10:
                o.color("green")


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgpic("closing.png")

matrix = []
screen.tracer(0)
for sor in range(-100, 100, 20):
    sorom = []
    for oszlop in range(-100, 100, 20):
        hely = turtle.Turtle()
        hely.shape("circle")
        hely.color("red")
        hely.penup()
        hely.goto(oszlop, sor)
        sorom.append(hely)
    matrix.append(sorom)


screen.listen()
screen.onclick(szinez)

while True:

    screen.update()
