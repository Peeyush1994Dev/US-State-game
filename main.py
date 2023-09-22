from turtle import Turtle , Screen
import turtle
import pandas
import csv

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


    ##Purpose is to end the game by typing Exit. Post that it give which all states we miss as a learing documents

    if answer_state == "Exist":
        set_state = set(data_state_list)
        set_answer_state = set(answer_state_list)

        left_states = set_state ^ set_answer_state

        left_states_data = pandas.DataFrame(left_states)
        left_states_data.to_csv("left state CSV data.csv")
        # print(left_states_data)


        break


    if answer_state in data_state_list:

        tur = turtle.Turtle()
        answer_state_list.append(answer_state)
        tur.hideturtle()
        tur.penup()
        row_answer_state = data[data.state == answer_state]
        tur.goto(int(row_answer_state.x), int(row_answer_state.y))
        tur.write(answer_state)


screen.exitonclick()

