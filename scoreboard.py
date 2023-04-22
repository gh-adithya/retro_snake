from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score = {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()


