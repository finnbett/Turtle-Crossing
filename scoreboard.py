from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.up()
        self.hideturtle()
        self.score = 0

    def display_score(self):
        self.clear()
        self.goto(-250, 230)
        self.write(f"Score: {self.score}", align="left", font=FONT)


    def level_up(self):
        self.score += 1
        self.clear()
        self.write(f"Score{self.score}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER \nFinal Score: {self.score}", align="center", font=FONT)

