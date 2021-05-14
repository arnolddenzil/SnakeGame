from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.update_score(self.point)

    def update_score(self, point):
        self.score += point
        self.clear()
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("Arial", 15, "normal"))