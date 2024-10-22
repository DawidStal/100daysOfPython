import writer

# Setup Screen
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=730, height=500)

# Set background (USA map)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read file
data = pandas.read_csv("50_states.csv")

# Create writer and scoreboard
writer = writer.Writer()

# make variable to keep track of states guessed
guesses = []

game_on = True
while len(guesses) < 50:
    input_answer = screen.textinput(f"States guessed {len(guesses)}/50", "Enter the name of a state")
    # Check if the csv file contains the state
    if not data[data["state"].str.lower() == input_answer.lower()].empty:
        # get answer
        answer = data[data.state.str.lower() == input_answer.lower()]
        # get answer state
        answer_state = answer.state.item()
        # get answer xcor
        xcor = answer.x.item()
        # get answer state ycor
        ycor = answer.y.item()
        # write state on the map and increment the number of guessed states
        if answer_state not in guesses:
            writer.name_state(answer_state, xcor, ycor)
            guesses.append(answer_state)
    elif input_answer.lower() == "exit":
        # create a list with states that weren't guessed
        states_to_learn = [state for state in data.state if state not in guesses]
        print(states_to_learn)
        # Create a csv file of not guessed states
        saved_data = pandas.DataFrame(states_to_learn)
        saved_data.to_csv("States_To_Learn.csv")
        break
