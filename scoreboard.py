from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.current_score}", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))

    def score_count(self):
        self.clear()
        self.current_score += 1
        self.update_scoreboard()
