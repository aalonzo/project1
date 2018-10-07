from tkinter import *
from PIL import ImageTk, Image
import os.path

WINDOW_TITLE = "Corgi Simulator"
WINDOW_WIDTH = "820"
WINDOW_HEIGHT = "1124"
WINDOW_COLOR = '#BEBEBE'

current_input = ""

def check_input():
    global status_text
    global current_input
    global entry_field

    current_input = entry_field.get()
    entry_field.delete(0, END)

    print("egg")

    if current_input == "start":
        scene1_intro()
        return None
    if current_input == "quit":
        master.destroy()
    if current_input == "save":
        status_text.set("Progress was saved.")
        return None
    if ( current_input != "A") and (current_input != "B"):
        status_text.set("\"" + current_input + "\" is not a valid choice.")
        return None
        if current_input.upper() == "A":
            current_input = "A"
            return "A"
        if current_input.upper() == "B":
            current_input = "B"
            # status_text.set("We will branch off into choice B.")
            return "B"

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



# def scene2_wheretoplayfirst():
#       global path
#       path = "2_2.png"
#       #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#       img = ImageTk.PhotoImage(Image.open(path))

#       #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#       panel = Label(master, image = img)

#       choice = entry_field.get()
#       # entry_field.bind('<Return>', lambda event: scene2_wheretoplayfirst(panel, check_input(entry_field.get())))




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



if current_input == "start":
    scene1_intro()

print("yeehaw")



master.mainloop()
# #Start the GUI
