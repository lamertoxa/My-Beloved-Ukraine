from turtle import Turtle

class City(Turtle):
    def __init__(self,city,x,y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setx(x)
        self.sety(y)
        self.write(f"{city}", align="center", font=("Arial", 16, "normal"))

