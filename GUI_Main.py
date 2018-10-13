from tkinter import *
from PIL import ImageTk, Image
import os.path
import io
from Riddles import Riddle

BUTTON_SPACING = 50
INSTALL_DIR = os.getcwd() + "/"
WINDOW_TITLE = "Corgi Adventures"
WINDOW_COLOR = '#BEBEBE'
WINDOW_WIDTH = "820"
WINDOW_HEIGHT = "1124"

current_input = ""

theriddle = Riddle(0)


class scene_num():
	
	def __init__(self):
		self.num = 0
	
	def changeScene(self, x):
		self.num = x

	def getNum(self):
		return self.num

# this function updates the text box to whatever we want.
# to make it read only, we have to set the state to normal so the text can be edited.
# according to the documentation, you delete text by specifying the arguments below.
# once written, you set the state to disabled, giving you a read-only dialog box!
# def update_text_box(text_dialog):
# 	global dialog_box
# 	dialog_box.configure(state='normal') 
# 	dialog_box.delete(1.0, END)
# 	dialog_box.insert(END, text_dialog)
# 	dialog_box.configure(state='disabled') 

# this function updates the status bar to whatever we want.
# to make it read only, we have to set the state to normal so the text can be edited.
# according to the documentation, you delete text by specifying the arguments below.
# once written, you set the state to disabled, giving you a read-only dialog box!
def update_status_bar(sb_text):
	global status 

	status.config(text="")
	status.update_idletasks()
	status.config(text=sb_text)
	status.update_idletasks()

def update_sceneimg(img_filepath):
	# the standard image opening code used in the last release.
	img = ImageTk.PhotoImage(Image.open(img_filepath))
	bg_image_widget.config(image=img)
	bg_image_widget.image=img
		
def check_input():
	# global status_text
	global current_input
	global entry_field
	global theriddle

	# print(theriddle.getSolution("gamer"))
	current_input = entry_field.get()
	entry_field.delete(0, END)

	# intro scene, which starts out asking the player whether they want to play
	# or just tell the corgi to go away
	if current_input == "start":
		scene1_intro()
		return None

	# tells the program to quit.  Can take place at any time.
	if current_input == "quit":
		master.destroy()

	# tells the program to save wherever the user is at.
	if current_input == "save":
		save_file = open(os.getcwd()+"/save.txt", "w+")
		save_file.write(str(scene_number.getNum()))
		save_file.close()
		update_status_bar("Your progress was saved.")
		return None

	# tells the program to save wherever the user is at.
	if current_input == "load":
		viableSaves = ["1","2","3.1"]
		save_file = open(os.getcwd()+"/save.txt", "r")
		loadednum = save_file.read(scene_number.getNum())
		save_file.close()
		if not loadednum in viableSaves:
			return "error, save corrupted"
		return "Take me to the correct scene don't return anything"
	# the choice branch for the first scene.
	# if choice A, goes to the scene where it asks to play in the backyard.
	# if choice B, ends the game and gives the user the option to play again 
	# or quit the game entirely.
	if scene_number.getNum() == 1:
		if current_input.upper() == "A":
			scene2()
		if current_input.upper() == "B":
			scene11_game_over()
	# triggers the choices for the second scene, where the corgi asks the user 
	# what they want to do.
	# if choice A, it goes to the scene where they play in the backyard.
	# if choice B, it goes to the stair climbing scene, which is where the minigame takes place.
	elif scene_number.getNum() == 2:
		if current_input.upper() == "A":
			scene3_1_takeabath()
		if current_input.upper() == "B":
			scene3_2_backyardorbath()
	elif scene_number.getNum() == 3.1:
		if current_input.upper() == "A":
			scene5_1_kitchenformeal()
		if current_input.upper() == "B":
			scene6_1_takeanap()
	elif scene_number.getNum() == 3.2:
		if current_input.upper() == "A":
			scene4_1_playinbackyard()
		if current_input.upper() == "B":
			scene4_2_exercisethatbooty()
	elif scene_number.getNum() == 4.1:
		if current_input.upper() == "A":
			scene5_1_kitchenformeal()
		if current_input.upper() == "B":
			scene6_1_takeanap()
	elif scene_number.getNum() == 4.2:
		if current_input.upper() == "A":
			# if not enough time, fall back to skipping straight to nap.
			scene12_anagramgame_instructions()
		if current_input.upper() == "B":
			scene11_game_over()
	elif scene_number.getNum() == 5.1:
		if current_input.upper() == "A":
			scene6_1_takeanap()
		if current_input.upper() == "B":
			scene3_1_takeabath()
	elif scene_number.getNum() == 6.1:
		if current_input.upper() == "A":
			scene6_2_feedafternap()
		if current_input.upper() == "B":
			scene11_game_over()	
	elif scene_number.getNum() == 12:
		if current_input == "begin":
			scene12_1_anagramgame_firstanagram()
		else:
			update_status_bar("\""+ current_input + "\" doesn't begin the game.")

	elif scene_number.getNum() == 12.1:
		if theriddle.getSolution(current_input):
			scene12_2_anagramgame_secondanagram()
		else:
			update_status_bar("Oh no! That guess was wrong!")
	elif scene_number.getNum() == 12.2:
		if theriddle.getSolution(current_input):
			scene12_3_anagramgame_thirdanagram()
		else:
			update_status_bar("Oh no! That guess was wrong!")
	elif scene_number.getNum() == 12.3:
		if theriddle.getSolution(current_input):
			scene12_4_anagramgame_success()
		else:
			update_status_bar("Oh no! That guess was wrong!")
	elif scene_number.getNum() == 12.4:
			scene6_1_takeanap()
	# if the input given does not match anything we don't support, we tell the user it is invalid input.
	if current_input != "start" and current_input != "quit" and current_input != "save" and current_input.upper() != "load" and current_input.upper() != "A" and current_input.upper() != "B" and (scene_number.getNum() < 12 or scene_number.getNum() > 12.4):
		update_status_bar("\"" + current_input + "\" is not a valid input.")


def scene0_instructions():
	global choiceA
	global choiceB
	global bottom_button_frame
	# global status_text
	global current_input
	global entry_field
	# global path

	# whoever had this one, I ended up adding the buttons for you!
	# this should give you an idea of what we want for now.
	# you use the global keywords on choiceA and choiceB (the variables for these
	# are in the code at the very bottom)
	# to change the button text at any time, simply call the config function,
	# change the text attribute to whatever you want, and call the appropriate scene 
	# as demonstrated below.
	choiceA.config(text="Start Game", command=lambda: scene1_intro())
	choiceB.config(text="Quit", command=lambda: master.destroy())

	# scene0 is where we want the buttons and the frame they're in to be packed,
	# as we don't want them to show on the title screen.
	choiceA.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)
	choiceB.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)

	# pack the frame we made onto the window
	# !!!! DO NOT COPY AND PASTE THIS IN ANY OTHER SCENE EXCEPT WHERE NOTED !!!!!!!
	bottom_button_frame.pack(side="bottom", anchor="s")

	entry_field.config(state=NORMAL, bg="white")
	update_status_bar("Type \"start\" to begin or \"quit\" to exit.")
	path = INSTALL_DIR +"inst.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

def scene1_intro():
	# global status_text
	global current_input
	global entry_field
	# global dialog_box

	# dialog_box.pack(side="bottom", anchor="s", fill="none", ipadx=5, ipady=5)
	# update_text_box("Hiya! I was brought home by you!  I'm so excited to take a look around!  Everything looks so brand new and fun!  Will you help me look around and play with me?")


	# whoever had this one, I ended up adding the buttons for you!
	# this should give you an idea of what we want for now.
	# you use the global keywords on choiceA and choiceB (the variables for these
	# are in the code at the very bottom)
	# to change the button text at any time, simply call the config function,
	# change the text attribute to whatever you want, and call the appropriate scene 
	# as demonstrated below.
	choiceA.config(text="Yes!", command=lambda: scene2())
	choiceB.config(text="Nah, bye.", command=lambda: scene11_game_over())

	# global path
	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = INSTALL_DIR +"1_button.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(1)

def scene2():
	# global status_text
	global current_input
	global entry_field
	# global path
	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = INSTALL_DIR +"2_button.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(2)
	
def scene10():
	# global status_text
	global current_input
	global entry_field
	# global path
	update_status_bar("Thanks for playing!  Type \"start\" to play again, or \"quit\" to quit the game.")
	path = INSTALL_DIR +"end.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(10)
	
def scene3_1_takeabath():
	# global status_text
	global current_input
	global entry_field
	# global path

	# scene0 is where we want the buttons and the frame they're in to be packed,
	# as we don't want them to show on the title screen.
	choiceA.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)
	choiceB.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)
	
	interval = 3000 
	update_status_bar('')
	update_status_bar("You and Max go to the bathroom for a bath!")
	status.pack()
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = INSTALL_DIR +"corgi_outside_bath.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	path = INSTALL_DIR +"corgi_inside_bath.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	entry_field.after(interval, entry_field.config(state=NORMAL, bg="white"))
	path = INSTALL_DIR +"corgi_button_bath.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

	choiceA.config(text="Dry off in the kitchen", command=lambda: scene5_1_kitchenformeal())
	choiceB.config(text="Take a nap in the bedroom", command=lambda: scene6_1_takeanap())
		
	scene_number.changeScene(3.1)
	
def scene3_2_backyardorbath():
	# global status_text
	global current_input
	global entry_field
	# global path
	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = INSTALL_DIR +"corgi_ask_backyard.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(3.2)

def scene4_1_playinbackyard():
	# global status_text
	global current_input
	global entry_field
	# global path

	interval = 2000 
	update_status_bar("You and Max are having fun in the backyard!")
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = INSTALL_DIR +"corgi_backyard_left.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())
	
	path = INSTALL_DIR +"corgi_backyard_right.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	path = INSTALL_DIR +"corgi_backyard_left.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	# path = INSTALL_DIR +"corgi_backyard_right.png"
	# #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	# img2 = ImageTk.PhotoImage(Image.open(path))
	# panel.config(image=img2) 
	# panel.image=img2	

	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	entry_field.after(interval, entry_field.config(state=NORMAL, bg="white"))
	path = INSTALL_DIR +"corgi_backyard_button.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	# panel.update_idletasks()

	 # after 1000ms
	scene_number.changeScene(4.1)
	
	choiceA.config(text="Head to the kitchen", command=lambda: scene5_1_kitchenformeal())
	choiceB.config(text="Take a nap", command=lambda: scene6_1_takeanap())

def scene4_2_exercisethatbooty():
	# global status_text
	global current_input
	global entry_field
	# global path
	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = INSTALL_DIR +"corgi_motivation_screwoff.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(4.2)
	
	choiceA.config(text="Lets go for it!", command=lambda: scene12_anagramgame_instructions())
	choiceB.config(text="You can do it on your own", command=lambda: scene11_game_over())

def scene5_1_kitchenformeal():
	# global status_text
	global current_input
	global entry_field
	# global path

	interval = 3000 
	update_status_bar('')
	update_status_bar("You and Max go to the kitchen to eat food.")
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = INSTALL_DIR +"corgi_waiting_food.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	path = INSTALL_DIR +"corgi_gets_food.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	entry_field.after(interval, entry_field.config(state=NORMAL, bg="white"))
	path = INSTALL_DIR +"corgi_kitchen_question.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

	scene_number.changeScene(5.1)
	
	choiceA.config(text="Take a nap", command=lambda: scene6_1_takeanap())
	choiceB.config(text="Take a bath", command=lambda: scene3_1_takeabath())

def scene6_1_takeanap():
	# global status_text
	global current_input
	global entry_field
	# global path

	interval = 2000 
	 
	update_status_bar("You carried Max upstairs to your bedroom.")
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = INSTALL_DIR +"corgi_off_bed.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())
	
	update_status_bar("Max goes to sleep.")
	path = INSTALL_DIR +"corgi_sleeping_bed.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	update_status_bar("")
	path = INSTALL_DIR +"corgi_love_bed.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())


	update_status_bar("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	entry_field.after(interval, entry_field.config(state=NORMAL, bg="white"))
	path = INSTALL_DIR +"corgi_question_bed.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	# panel.update_idletasks()

	 # after 1000ms
	scene_number.changeScene(6.1)

def scene6_2_feedafternap():
	# global status_text
	global current_input
	global entry_field
	# global path

	interval = 4000 
	update_status_bar("You fed Max.")
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = INSTALL_DIR +"corgi_getsfood_bed.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	scene_number.changeScene(6.2)
	entry_field.config(state=NORMAL, background="white")
	scene10()



# def scene4_motivationorscrewoff():
# 	# global status_text
# 	global current_input
# 	global entry_field
# 	# global path

# 	entry_field.config(state=NORMAL, bg="white")
# 	update_status_bar("Type \"start\" to begin or \"quit\" to exit.")
# 	path = INSTALL_DIR +"corgi_motivation_screwoff.png"
# 	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
# 	img2 = ImageTk.PhotoImage(Image.open(path))
# 	panel.config(image=img2)
# 	panel.image=img2

# 	scene_number.changeScene(11.1)

def scene11_game_over():
	# global status_text
	global choiceA
	global choiceB
	global current_input
	global entry_field
	# global path

	# whoever had this one, I ended up adding the buttons for you!
	# this should give you an idea of what we want for now.
	# you use the global keywords on choiceA and choiceB (the variables for these
	# are in the code at the very bottom)
	# to change the button text at any time, simply call the config function,
	# change the text attribute to whatever you want, and call the appropriate scene 
	# as demonstrated below.
	choiceA.config(text="Play Again", command=lambda: scene1_intro())
	choiceB.config(text="Quit", command=lambda: master.destroy())

	entry_field.config(state=NORMAL, bg="white")
	update_status_bar("You're a bad owner!  Click \"Play Again\" to start over, or \"Quit\" to quit.")
	path = INSTALL_DIR +"sad.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

	scene_number.changeScene(11.1)

def scene12_anagramgame_instructions():
	# global status_text
	global current_input
	global entry_field
	# global path

	entry_field.config(state=NORMAL, bg="white")
	update_status_bar("Type \"begin\" to start the mini game.")
	path = INSTALL_DIR +"corgi_instructions_game.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

	scene_number.changeScene(12)

def scene12_1_anagramgame_firstanagram():
	# global status_text
	global current_input
	global entry_field
	# global path
	global theriddle

	entry_field.config(state=NORMAL, bg="white")
	update_status_bar("Solve this anagram: " + theriddle.getRiddle())
	path = INSTALL_DIR +"corgi_firstframe_game.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

	scene_number.changeScene(12.1)

def scene12_2_anagramgame_secondanagram():
	# global status_text
	global current_input
	global entry_field
	# global path
	global theriddle

	theriddle = Riddle(1)
	entry_field.config(state=NORMAL, bg="white")
	update_status_bar("Solve this anagram: " + theriddle.getRiddle())
	path = INSTALL_DIR +"corgi_secondframe_game.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

	scene_number.changeScene(12.2)

def scene12_3_anagramgame_thirdanagram():
	# global status_text
	global current_input
	global entry_field
	# global path
	global theriddle

	theriddle = Riddle(2)
	entry_field.config(state=NORMAL, bg="white")
	update_status_bar("Solve this anagram: " + theriddle.getRiddle())
	path = INSTALL_DIR +"corgi_thirdframe_game.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2


	scene_number.changeScene(12.3)

def scene12_4_anagramgame_success():
	# global status_text
	global current_input
	global entry_field
	# global path

	panel.after(1000, panel.update_idletasks())

	interval = 3000 
	update_status_bar("*bork bork bork* (Thank you for encouraging me!)")
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = INSTALL_DIR +"corgi_win_game.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	update_status_bar("")
	path = INSTALL_DIR +"corgi_success_game.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(4000, panel.update_idletasks())

	scene_number.changeScene(12.4)
	entry_field.config(state=NORMAL, disabledbackground="white")
	scene6_1_takeanap()

scene_number = scene_num()


# #This creates the main window of an application
master = Tk()

master.title(WINDOW_TITLE)
master.geometry(WINDOW_HEIGHT+"x"+WINDOW_WIDTH)
master.configure(background=WINDOW_COLOR)

path = INSTALL_DIR +"home.png"
# status_text = StringVar()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(master, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "top", fill = "both", expand="yes")

# dialog_box = Text(master, bd=10, highlightbackground="black", height=10, width=80)

''' USE THIS FRAME TO PACK YOUR BUTTONS ONTO!!! '''
''' Access this in your methods via global bottom_button_frame '''
# frame for the buttons.  made so they can be all on the same line.
# the background has been filled with red to demonstrate how the frame
# is laid onto the window.
bottom_button_frame = Frame(master, background=WINDOW_COLOR, width=100)

choiceA = Button(text="")
choiceB = Button(text="")

status = Label(master, textvariable="", relief=SUNKEN, bd=1, anchor="w", background=WINDOW_COLOR)
status.pack(side="bottom", anchor="s", fill="x")
update_status_bar("Welcome to " + WINDOW_TITLE + "! Starting up..." )

entry_field = Entry(master, textvariable=current_input, disabledbackground="gray", state=DISABLED)
entry_field.configure(bd=3,width=WINDOW_WIDTH)
entry_field.pack(side="bottom", anchor='s')

panel.after(5000, lambda: scene0_instructions() ) # after 1000ms

entry_field.bind('<Return>', lambda event: check_input())

master.mainloop()
# #Start the GUI
