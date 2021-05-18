from turtle import Turtle
import time


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.score = 0
        with open("data.txt") as highest:
            self.high_score = int(highest.read())
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.update_score(self.point)

    def update_score(self, point):
        self.score += point
        self.clear()
        self.write(arg=f"Score : {self.score} High Score = {self.high_score}", align="center", font=("Arial", 12, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("Arial", 15, "normal"))
        time.sleep(1.5)
        self.goto(0, 280)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as highest:
                highest.write(f"{self.high_score}")
        self.score = 0
        self.update_score(0)
