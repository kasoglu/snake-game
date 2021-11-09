from turtle import Turtle
ALIGNMENT = "center"
FONT = "Times New Roman", 30, "bold"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-60, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over..", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
