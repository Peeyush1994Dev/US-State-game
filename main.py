from turtle import Turtle , Screen
import turtle
import pandas

screen = Screen()

screen.title("Us State game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# answer_state = screen.textinput("Guess the State","what is the another state name")

data = pandas.read_csv("50_states.csv")

data_state_list = data.state.to_list()

answer_state_list = []

# print(data_state_list)
while len(answer_state_list) < 50:
    answer_state = screen.textinput(f"{len(answer_state_list)}/50 the State remaining","what is the another state name")

    if answer_state in data_state_list:

        tur = turtle.Turtle()
        answer_state_list.append(answer_state)
        tur.hideturtle()
        tur.penup()
        row_answer_state = data[data.state == answer_state]
        tur.goto(int(row_answer_state.x), int(row_answer_state.y))
        tur.write(answer_state)


screen.exitonclick()

