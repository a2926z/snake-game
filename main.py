from turtle import Turtle, Screen
from snake import Snake
from time import sleep
from food import Food
from scoreboard import Scoreboard
from pygame import mixer

mixer.init()
mixer.music.load('pacman_intro2.mp3')
mixer.music.play()

screen = Screen()
screen.setup(600, 600)
screen.title('My Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()

my_score = Scoreboard()
my_score.high_score()
my_score.keys_info()
old_high_score = my_score.get_highscore()

def pause():
    global game_is_on
    if game_is_on:
        game_is_on = False
        my_score.pause_game()


def to_continue():
    global game_is_on
    if not game_is_on:
        game_is_on = True
        my_score.pause.clear()
        run_game()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(pause, "p")
screen.onkey(to_continue, "c")

game_is_on = True

def run_game():
    global game_is_on
    while game_is_on:
        screen.update()
        sleep(0.05)
        snake.move_snake()

        if snake.head.distance(food) < 15:
            # mixer.music.stop()

            mixer.Channel(0).play(mixer.Sound('eat2.wav'))
            # code to make distance between snake body and food larger than 15
            distances = []
            new_food = True
            while new_food:
                food.refresh()
                for segment in snake.my_snake:
                    distance = food.distance((segment))
                    distances.append(distance)
                if min(distances) > 12:
                    # print(f'Normal pos: {food.pos()}')
                    new_food = False
                    break
                    # print(distances)
                else:
                    distances = []
                    # print(f'Regenerated pos: {food.pos()}')
                    # food.refresh()

            my_score.update_score()
            my_score.set_new_highscore()
            snake.extend_snake()

            if my_score.score-1 == old_high_score:
                mixer.music.load('new_high_score.mp3')
                mixer.music.play()

        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            game_is_on = False
            my_score.game_over()
            mixer.Channel(1).play(mixer.Sound('pacman_death2.wav'))
            if my_score.score > my_score.highscore:
                with open('high_score.txt', 'w') as f:
                    f.write(str(my_score.score))

        for segment in snake.my_snake[1:]:
            if snake.head.distance(segment) < 2:
                game_is_on = False
                my_score.game_over()
                mixer.Channel(1).play(mixer.Sound('pacman_death2.wav'))
                if my_score.score > my_score.highscore:
                    with open('high_score.txt', 'w') as f:
                        f.write(str(my_score.score))

run_game()

screen.exitonclick()
