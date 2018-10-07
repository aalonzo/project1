from tkinter import *
from PIL import ImageTk, Image
import os.path



WINDOW_TITLE = "Corgi Simulator"
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

	if current_input == "start":
		scene1_intro()
		return None
	if current_input == "quit":
		master.destroy()
	if current_input == "save":
		status_text.set("Progress was saved.")
		return None
	if scene_number.getNum() == 1:
		if current_input == "A":
			scene2()
		if current_input == "B":
			scene10()

	if scene_number.getNum() == 2:
		if current_input == "A":
			scene3_1()
		if current_input == "B":
			scene3_2()

def scene1_intro():
	global status_text
	global current_input
	global entry_field
	global path
	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = os.getcwd()+"/1.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(1)
	
def scene10():
	global status_text
	global current_input
	global entry_field
	global path
	status_text.set("Type \"A\" to pick the left choice, or \"B\" to pick the right choice.")
	path = os.getcwd()+"/10.png"
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
	path = os.getcwd()+"/3_2.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path))
	panel.config(image=img2)
	panel.image=img2
	scene_number.changeScene(3.2)
	



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

path = os.getcwd()+"\home.png"
status_text = StringVar()

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(master, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "top", fill = "both", expand="yes")

status = Label(master, textvariable=status_text, background=WINDOW_COLOR)
status.pack(side="bottom", anchor="sw")
status_text.set("Welcome to " + WINDOW_TITLE + "!  Type \"start\" to begin or \"quit\" to exit.")

entry_field = Entry(master, textvariable=current_input)
entry_field.configure(bd=3,width=WINDOW_WIDTH)
entry_field.pack(side="bottom", anchor='s')

entry_field.bind('<Return>', lambda event: check_input())





master.mainloop()
# #Start the GUI
