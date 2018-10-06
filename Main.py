import csv

player_name = "PLAYER_NAME"
corgi_name = "CORGI_NAME"

def scene1_intro():
	choices = ["A", "B"]
	user_choice = ""

	print('''Hiya I was taken and brought here by you. I’m so excited to take a look around! Everything looks so brand new and fun! Will you help me take a look around the house and play with me? 

			A. YES!!!
			B. Nah. Bye.''')

	while user_choice not in choices:
		user_choice = str(input("Choose an option: "))


	return user_choice

def scene2_wheretoplayfirst():
	choices = ["A", "B"]
	user_choice = ""

	print('''Where should we go play first?

			A. Let’s go to the bathroom for a bath.
			B. Let’s stay in the living room and play with toys''')

	while user_choice not in choices:
		user_choice = str(input("Choose an option: ")).upper()

	return user_choice

def scene3_1_tobackyardorstairs():
	choices = ["A", "B"]
	user_choice = ""

	print('''Let’s head to the backyard to play more catch please

		A. Sure buddy, anything for you! 
		B. Why don’t we get some stairs exercises done for that booty instead!''')

	while user_choice not in choices:
		user_choice = str(input("Choose an option: ")).upper()

	return user_choice

def scene3_2_bath_aftermealornap():
	choices = ["A", "B"]
	user_choice = ""

	print(corgi_name + " is taking a bath.")
	print('''Yay, I love being all nice and clean!

		A. Let's dry off and have a nice meal in the kitchen. 
		B. Awe, my puppy must be tired, why don't we take a nap in the bedroom?''')

	while user_choice not in choices:
		user_choice = str(input("Choose an option: ")).upper()

	return user_choice

def scene4_1_playinbackyard_aftereatornap():
	choices = ["A", "B"]
	user_choice = ""

	print(player_name + " throws a tennis ball for " + corgi_name + " to catch in the backyard.")
	print('''I'm getting exhausted!  Can I have something to eat and drink please?

		A. Ok doggo, let's hop into the kitchen for a nice meal and cold water. 
		B. I'm tired, why don't we take a nap first and I'll feed you after?''')

	while user_choice not in choices:
		user_choice = str(input("Choose an option: ")).upper()

	return user_choice

def scene4_2_climbstairs_motivationorscrewoff():
	choices = ["A", "B"]
	user_choice = ""

	print(player_name + " is looking down the stairs at " + corgi_name + " which is running up the stairs with its cute booty.")
	print('''I'm climbing as fast I can, + ''' + player_name + '''!  These tiny sort legs are making it hard for me to hop up to you!
		Will you give me motivation?

		A. Yes!  Come on ''' + corgi_name + ''', you can do it! 
		B. Nah, I think you can do it on your own.''')

	while user_choice not in choices:
		user_choice = str(input("Choose an option: ")).upper()

	return user_choice

def scene5_1_corgieating_isnowsleepy():
	choices = ["A", "B"]
	user_choice = ""

	print(player_name + " makes theirself some food while " + corgi_name + " is eating and drinking water from their bowl.")
	print('''Mmm, so yummy, thank you so much, ''' + player_name + '''!  I'm sleepy now, though.  *yawn*
		Will you give me motivation?

		A. Awww, okay, ''' + corgi_name + ''', let's get a nap in.  *yawn*
		B. Not so fast, ''' + corgi_name + ''', let's get a good bath first!''')

	while user_choice not in choices:
		user_choice = str(input("Choose an option: ")).upper()

	return user_choice


def anagram_minigame():
	print("---ANAGRAM MINIGAME GOES HERE---")


def end_game():
	print("Thank you for playing this short game with us! Hope to see you again!")

def game_over():
	print("Game over!  You made your new pet sad by mistreating it!!!")

def stop():
	print("---END BRANCH---")


start = scene1_intro()

if start == "A":
	scene2_choice = scene2_wheretoplayfirst()

	if scene2_choice == "B":
		print("---SCENE 3,1 (going to backyard) GOES HERE ---")
		scene31_choice = scene3_1_tobackyardorstairs()

		if scene31_choice == "A":
			print("---SCENE 4,1 (user/character throws a tennis ball for corgi to catch) GOES HERE---")
			scene41_choice = scene4_1_playinbackyard_aftereatornap()

			stop()
		elif scene31_choice == "B":
			print("---SCENE 4,2 (user looks down at corgi to go upstairs GOES HERE---")
			scene42_choice = scene4_2_climbstairs_motivationorscrewoff()

			if scene42_choice == "A":
				anagram_minigame()
			elif scene42_choice == "B":
				game_over()

	elif scene2_choice == "A":
		print("---SCENE 3,2 (corgi takes bath) GOES HERE---")
		scene32_choice = scene3_2_bath_aftermealornap()

		if scene32_choice == "A":
			print("---SCENE 5,1 (user cooks food while corgi eating and drinking water) GOES HERE---")
			scene51_choice = scene5_1_corgieating_isnowsleepy()

			if scene51_choice == "A":
				print("---SCENE 5,2 (user takes corgi upstairs) -> SCENE 6 (corgi asleep in room) -> SCENE 10 (end game) GOES HERE---")
				
		elif scene32_choice == "B":
			print("---SCENE 5,2 (user takes corgi upstairs) -> SCENE 6 (corgi asleep in room) -> SCENE 10 (end game) GOES HERE---")


	# if s2_choice == "A":
	# 	s32_choice = scene3_2_afterbath_mealornap()

	# 	if ( s32_choice == "A" ):
	# 		#scene5_1()
	# 		stop()
	# 	elif ( s32_choice == "B" ):
	# 		#scene5_2()
	# 		#scene6()
	# 		#scene10()
	# 		stop()

	# elif s2_choice == "B":
	# 	s31_choice = scene3_1_backyardorstairs()

	# 	if s31_choice == "A":
	# 		s41_choice = scene4_1_mealornap()

	# 		if ( s41_choice == "A" ):
	# 			stop()

	# 		elif ( s41_choice == "B" ):
	# 			s42_choice = scene4_2_motivationorscrewoff()

	# 			if s42_choice == "A":
	# 				anagram_minigame()

	# 			elif s42_choice == "B":
	# 				game_over()
	# 	elif s31_choice == "B":
	# 		stop()
elif start == "B":
	end_game()