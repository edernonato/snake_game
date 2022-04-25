from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("new.txt", mode="r") as save_score:
            self.record = save_score.read()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.color("white")
        self.update_scoreboard()
        self.new_record()

    def update_scoreboard(self):
        self.clear()
        self.setpos(-100, 270)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        self.new_record()

    def new_record(self):
        self.setpos(100, 270)
        self.write(f"RECORD: {self.record}", align=ALIGNMENT, font=FONT)
        with open("new.txt", mode="w") as save_score:
            save_score.write(f"{self.record}")

    def restart(self):
        if self.score > int(self.record):
            self.record = self.score
            self.update_scoreboard()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()







