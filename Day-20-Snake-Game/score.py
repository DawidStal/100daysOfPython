from turtle import Turtle

Font = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(0, 255)
        self.high_score = 0
        with open("Day-20-Snake-Game\\highscores.txt") as file:
            self.high_score = int(file.read())
        self.write_score()

    # Clear the old score text and write the new one
    def write_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.high_score}", align="center", font=Font)

    # Increment the score and update the text
    def add_score(self):
        self.score = self.score + 1
        self.write_score()

    # Make new highscore if score is greater than highscore
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Day-20-Snake-Game\\highscores.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.write_score()

    # Stop the game
    def game_over(self):
        self.setposition(0, 0)
        self.write("Game Over", align="center", font=Font)
