import turtle
# import time
#
# turtle.pensize(5)
# turtle.pencolor("yellow")
# turtle.fillcolor("red")
#
# turtle.begin_fill()
#
# for _ in range(5):
#     turtle.forward(200)
#     turtle.right(144)
# turtle.end_fill()
# time.sleep(2)
#
# turtle.penup()
# turtle.goto(-150, -120)
# turtle.color("violet")
# turtle.write("Done", font=('Arial', 40, 'normal'))
# turtle.done()


# x = 360/10
# y = 120
# for i in range(10):
#     if i %10 ==0:
#         turtle.color("skyblue")
#     else:
#         turtle.color("pink")
#     turtle.begin_fill()
#     turtle.forward(y)
#     turtle.left(x)
#     turtle.forward(y)
#     turtle.left(180-x)
#     turtle.forward(y)
#     turtle.left(x)
#
#     turtle.forward(y)
#     turtle.left(180-x)
#     turtle.forward(y)
#     turtle.left(x)
# turtle.done()


# x = 360 / 10
# y = 120
# for i in range(10):
#     if i % 2 == 0:
#         turtle.color("skyblue")
#     else:
#         turtle.color("pink")
#     turtle.begin_fill()
#     turtle.forward(y)
#     turtle.left(x)
#     turtle.forward(y)
#     turtle.left(180 - x)
#     turtle.forward(y)
#     turtle.left(x)
#
#     turtle.forward(y)
#     turtle.left(x)
#     turtle.forward(y)
#     turtle.left(180 - x)
#     turtle.forward(y)
#     turtle.left(x)
#
# turtle.done()

x = 360 / 10
y = 120
for i in range(10):
    if i % 2 == 0:
        turtle.color("skyblue")
    else:
        turtle.color("pink")

    print(f'x={x},y={y}')
    turtle.begin_fill()
    turtle.forward(y)
    turtle.left(x)
    turtle.forward(y)
    turtle.left(180 - x)
    turtle.forward(y)
    turtle.left(x)

    turtle.forward(y)
    turtle.left(x)
    turtle.forward(y)
    turtle.left(180 - x)
    turtle.forward(y)
    turtle.left(x)

turtle.done()
