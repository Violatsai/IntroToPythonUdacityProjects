import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("pink")
	Brad = turtle.Turtle()
	Brad.shape("turtle")
	Brad.color("purple")
	Brad.speed(5)
	i = 0
	while (i<=75):
		for j in range(4):
			Brad.forward(100)
			if j != 3:
				Brad.right(90)
			else:
				Brad.right(95)
		i = i + 1
	window.exitonclick()

draw_square()