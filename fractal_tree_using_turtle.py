import turtle as tu
my_turtle = tu.Turtle()
my_turtle.screen.bgcolor('orange')
my_turtle.left(90)
my_turtle.speed(28)
my_turtle.color('red')
my_turtle.pensize(6)
my_turtle.screen.title('Fractal tree')


def draw_fractal(blen):
    if (blen < 10):
        return
    else:
        my_turtle.forward(blen)
        my_turtle.left(30)
        draw_fractal(3*blen/4)
        my_turtle.right(60)
        draw_fractal(3*blen/4)
        my_turtle.left(30)
        my_turtle.backward(blen)


draw_fractal(72)
my_turtle = tu.done()
