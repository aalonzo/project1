from tkinter import *
from PIL import ImageTk, Image
import os.path

WINDOW_TITLE = "Corgi Adventure"
WINDOW_WIDTH = "820"
WINDOW_HEIGHT = "1124"
WINDOW_COLOR = '#BEBEBE'

current_input = ""

class scene_num():
	
	def __init__(self):
		self.num = 0
	
	def changeScene(self, x):
		self.num = x

	def getNum(self):
		return self.num
		
def check_input():
	global status_text
	global current_input
	global entry_field

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
		status_text.set("Saving not yet implemented.")
		return None

	# the choice branch for the first scene.
	# if choice A, goes to the scene where it asks to play in the backyard.
	# if choice B, ends the game and gives the user the option to play again 
	# or quit the game entirely.
	if scene_number.getNum() == 1:
		if current_input.upper() == "A":
			scene2()
		if current_input.upper() == "B":
			scene10()

	# triggers the choices for the second scene, where the corgi asks the user 
	# what they want to do.
	# if choice A, it goes to the scene where they play in the backyard.
	# if choice B, it goes to the stair climbing scene, which is where the minigame takes place.
	elif scene_number.getNum() == 2:
		if current_input.upper() == "A":
			scene3_1()
		if current_input.upper() == "B":
			scene3_2()

	elif scene_number.getNum() == 3.1:
		if current_input.upper() == "A":
			scene10()
		if current_input.upper() == "B":
			scene10()
	elif scene_number.getNum() == 3.2:
		if current_input.upper() == "A":
			scene4_1_playinbackyard()
		if current_input.upper() == "B":
			scene_exercisethatbooty()
	elif scene_number.getNum() == 4.1:
		if current_input.upper() == "A":
			scene5_1_kitchenformeal()
		if current_input.upper() == "B":
			scene5_2_napthenmeal()
	elif scene_number.getNum() == 5.1:
		if current_input.upper() == "A":
			scene10()
		if current_input.upper() == "B":
			scene10()


	# if the input given does not match anything we don't support, we tell the user it is invalid input.
	if current_input != "start" and current_input != "quit" and current_input != "save" and current_input.upper() != "A" and current_input.upper() != "B":
		status_text.set("\"" + current_input + "\" is not a valid input.")

def scene0_instructions():
	global status_text
	global current_input
	global entry_field
	global path
	entry_field.config(state=NORMAL, bg="white")
	status_text.set("Type \"start\" to begin or \"quit\" to exit.")
	path = os.getcwd()+"/inst.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2

def scene1_intro():
	global status_text
	global current_input
	global entry_field
	global path
	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = os.getcwd()+"/1_button.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(1)

def scene2():
	global status_text
	global current_input
	global entry_field
	global path
	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = os.getcwd()+"/2_button.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(2)
	
def scene10():
	global status_text
	global current_input
	global entry_field
	global path
	status_text.set("Thanks for playing!  Type \"start\" to play again, or \"quit\" to quit the game.")
	path = os.getcwd()+"/end.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(10)
	
def scene3_1():
	global status_text
	global current_input
	global entry_field
	global path
	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = os.getcwd()+"/3_1.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(3.1)
	
def scene3_2():
	global status_text
	global current_input
	global entry_field
	global path
	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = os.getcwd()+"/corgi_ask_backyard.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(3.2)

def scene4_1_playinbackyard():
	global status_text
	global current_input
	global entry_field
	global path

	interval = 2000 
	status_text.set('')
	status_text.set("You and Max are having fun in the backyard!")
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = os.getcwd()+"/corgi_backyard_left.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.update_idletasks()


	
	path = os.getcwd()+"/corgi_backyard_right.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	path = os.getcwd()+"/corgi_backyard_left.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	panel.after(interval, panel.update_idletasks())

	# path = os.getcwd()+"/corgi_backyard_right.png"
	# #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	# img2 = ImageTk.PhotoImage(Image.open(path))
	# panel.config(image=img2) 
	# panel.image=img2	

	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	entry_field.after(interval, entry_field.config(state=NORMAL, bg="white"))
	path = os.getcwd()+"/corgi_backyard_button.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	# panel.update_idletasks()

	 # after 1000ms
	scene_number.changeScene(4.1)

def scene5_1_kitchenformeal():
	interval = 2000 
	status_text.set('')
	status_text.set("You and Max go to the kitchen to eat some food.")
	entry_field.config(state=DISABLED, disabledbackground="gray")
	path = os.getcwd()+"/corgi_waiting_food.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img3 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img3)
	panel.image=img3
	panel.update_idletasks()


	
	path = os.getcwd()+"/corgi_gets_food.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img3 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img3)
	panel.image=img3
	panel.after(interval, panel.update_idletasks())

	# path = os.getcwd()+"/corgi_backyard_right.png"
	# #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	# img2 = ImageTk.PhotoImage(Image.open(path))
	# panel.config(image=img2) 
	# panel.image=img2	

	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	entry_field.after(interval, entry_field.config(state=NORMAL, bg="white"))
	path = os.getcwd()+"/corgi_kitchen_question.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img3 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img3)
	panel.image=img3
	panel.after(interval, panel.update_idletasks())

	scene_number.changeScene(5.1)



	



# def scene2_wheretoplayfirst():
#       global path
#       path = "2_2.png"
#       #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#       img = ImageTk.PhotoImage(Image.open(path))

#       #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#       panel = Label(master, image = img)

#       choice = entry_field.get()
#       # entry_field.bind('<Return>', lambda event: scene2_wheretoplayfirst(panel, check_input(entry_field.get())))



scene_number = scene_num()


# #This creates the main window of an application
master = Tk()

master.title(WINDOW_TITLE)
master.geometry(WINDOW_HEIGHT+"x"+WINDOW_WIDTH)
master.configure(background=WINDOW_COLOR)

path = os.getcwd()+"/home.png"
status_text = StringVar()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(master, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "top", fill = "both", expand="yes")

status = Label(master, textvariable=status_text, background=WINDOW_COLOR)
status.pack(side="bottom", anchor="sw")
status_text.set("Welcome to " + WINDOW_TITLE + "! Starting up..." )

entry_field = Entry(master, textvariable=current_input, disabledbackground="gray", state=DISABLED)
entry_field.configure(bd=3,width=WINDOW_WIDTH)
entry_field.pack(side="bottom", anchor='s')

panel.after(5000, lambda: scene0_instructions() ) # after 1000ms

entry_field.bind('<Return>', lambda event: check_input())

master.mainloop()
# #Start the GUI
