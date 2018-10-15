# this unit tests the logic for valid commands.
# these are designed to be run at any point during the game
# thus, we want to be sure that we only accept supported commands laid out.

def check_input_verbose(current_input):

	# intro scene, which starts out asking the player whether they want to play
	# or just tell the corgi to go away
	if current_input == "start":
		return "scene1"

	# tells the program to quit.  Can take place at any time.
	if current_input == "quit":
		return "end"

	# tells the program to save wherever the user is at.
	if current_input == "save":
		return "save"
		return None

	# branching stuff will go here (see actual check_input)
	if current_input.upper() == "A":
		return "A"
	if current_input.upper() == "B":
		return "B"

	if current_input != "start" and current_input != "quit" and current_input != "save" and current_input != "load" and current_input.upper() != "A" and current_input.upper() != "B":
		return "\"" + current_input + "\" is not a valid input."

	