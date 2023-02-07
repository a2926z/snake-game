from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.my_score = Turtle()
        self.my_score.hideturtle()
        self.my_score.setposition(-200, 270)
        self.my_score.color('white')
        self.write_score()

    def write_score(self):
        self.my_score.write(f'Score: {self.score}', align='center', font=('Arial', 18, 'normal'))

    def update_score(self):
        self.score += 1
        self.my_score.clear()
        self.write_score()

    def get_highscore(self):
        with open('high_score.txt', 'r') as f:
            contents = f.readlines()
            self.highscore = int(contents[0])
            return self.highscore

    def high_score(self):
        self.get_highscore()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.setposition(75, 270)
        self.write(f'High Score: {self.highscore}', font=('Arial', 18, 'normal'))
        self.set_new_highscore()

    def set_new_highscore(self):
        if self.score >= self.highscore:
            self.clear()
            self.write(f'High Score: {self.score}', font=('Arial', 18, 'normal'))
            self.color('cyan2')
            # with open('high_score.txt', 'w') as f:
            #     f.write(str(self.score))

    def game_over(self):
        self.my_score.goto(0, 0)
        self.my_score.write(f'GAME OVER', align='center', font=('Arial', 18, 'normal'))

    def pause_game(self):
        self.pause = Turtle()
        self.pause.hideturtle()
        self.pause.penup()
        self.pause.goto(0, 0)
        self.pause.color('white')
        self.pause.write(f'Paused', align='center', font=('Arial', 18, 'normal'))

    def keys_info(self):
        self.keys = Turtle()
        self.keys.hideturtle()
        self.keys.penup()
        self.keys.goto(0, -290)
        self.keys.color('white')
        self.keys.write(f"press  'p'  to pause and  'c'  to continue", align='center', font=('Arial', 12, 'normal'))



