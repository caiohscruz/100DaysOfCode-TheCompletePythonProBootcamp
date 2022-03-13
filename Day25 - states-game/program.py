import turtle
import pandas as pd
from pointer import Pointer

screen = turtle.Screen()
screen.title("Brazil States Game")
image = "mapa-brasil.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states_with_coordinates.csv", index_col=0)

print(data)

pointer = Pointer()
NUM_STATES = len(data.state)
guessed_states = []

while len(guessed_states) < NUM_STATES:
    guess = screen.textinput(title=f"{len(guessed_states)}/{NUM_STATES} States Correct", prompt="Guess a state name:")
    search = data[data.state == guess.title()]
    if (len(search) > 0) and (guess not in guessed_states):
        x_cor = int(search["X_cor"].to_list()[0])
        y_cor = int(search["Y_cor"].to_list()[0])
        state = search["state"].to_list()[0]
        pointer.write_at(state, x_cor, y_cor)
        guessed_states.append(guess)


# TO CREATE A CSV WITH THE STATES NAMES AND COORDINATES
#
# x_coordinates = []
# y_coordinates = []
# counter_states = 0
#
# def get_mouse_click_coord(x, y):
#     x_coordinates.append(x)
#     y_coordinates.append(y)
#     increment_counter(counter_states)
#     print(counter_states)
#
#
# def increment_counter(counter):
#     counter += 1
#
#
# def generate_states_list(filename):
#     with open(filename) as states_file:
#         states = states_file.readlines()
#     for index in range(len(states)):
#         states[index] = states[index].strip()
#     return states
#
#
# def create_states_csv():
#     states = generate_states_list("brazil-states.txt")
#     df = pd.DataFrame({
#         "state": states,
#         "X_cor": x_coordinates,
#         "Y_cor": y_coordinates
#     })
#     df.to_csv('states_with_coordinates.csv')
#
#
# turtle.listen()
# turtle.onkeypress(key="space", fun=create_states_csv)
# turtle.onscreenclick(get_mouse_click_coord)

turtle.mainloop()
