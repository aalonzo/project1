from tkinter import *
from PIL import ImageTk,Image
import os.path
import io

# some global variables for us to use throughout the program.
BUTTON_SPACING = 100
INSTALL_DIR = os.getcwd() + "/"
WINDOW_TITLE = "Corgi Adventures"
WINDOW_WIDTH = "720"
WINDOW_HEIGHT = "1024"
WINDOW_COLOR = '#BEBEBE'

# this function updates the text box to whatever we want.
# to make it read only, we have to set the state to normal so the text can be edited.
# according to the documentation, you delete text by specifying the arguments below.
# once written, you set the state to disabled, giving you a read-only dialog box!
def update_text_box(dialog_widget, text_dialog):
	dialog_widget.configure(state='normal') 
	dialog_widget.delete(1.0, END)
	dialog_widget.insert(END, text_dialog)
	dialog_widget.configure(state='disabled') 

# method for updating image given the widget for background iamge, the image's filename 
# (with extension), and text you want to show in the dialog box for this scene.
def update_scene(bg_image_widget, dialog_widget, image_name, text_dialog):
	# update the text using the above function.
	update_text_box(dialog_widget, text_dialog)

	# the standard image opening code used in the last release.
	img = ImageTk.PhotoImage(Image.open(INSTALL_DIR + image_name))
	bg_image_widget.config(image=img)
	bg_image_widget.image=img


# method to hide the text box.  to give the appearance of hiding it within the same scene,
# pass the same background image placed under the dialog box, and an empty string ("", NOT None)
# for the dialog.  
def hide_text_box(bg_image_widget, dialog_widget, image_name, text_dialog):
	update_scene(bg_image_widget, dialog_widget, image_name, text_dialog)
	dialog_widget.pack_forget()

# method to show the text box.
# as you can see, it's basically the reverse of the hide_text_box function.
# should be self-explanatory, but if not, feel free to ask questions.
def show_text_box(bg_image_widget, dialog_widget, image_name, text_dialog):
	dialog_widget.pack(side="bottom", anchor="s", fill="none", ipadx=5, ipady=5)
	update_scene(bg_image_widget, dialog_widget, image_name, text_dialog)



# # theoretical method for updating image given a window, bg_image, and the widget.
# def update_scene_nodialog(bg_image_widget, image_name, text_dialog):
# 	# dialog_widget.text=text_dialog

# 	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
# 	img = ImageTk.PhotoImage(Image.open(INSTALL_DIR + image_name))
# 	bg_image_widget.config(image=img)
# 	bg_image_widget.image=img


def main():
	window = Tk() # create window
	window.title(WINDOW_TITLE)
	window.geometry(WINDOW_HEIGHT+"x"+WINDOW_WIDTH) # set window dimensions

	# this makes a Label widget for the image to go on.  
	# using the Place method, we are able to make it the background image on the window.
	bg_image = Label(window)
	bg_image.place(relx=0.5, rely=0.5, anchor=CENTER)

	# the widget for the dialog box.  I've specified a width and height for it here, 
	# but we can adjust it accordingly depending on the scene.
	dialog_box = Text(window, bd=10, highlightbackground="black", height=10, width=80)
	
	# frame for the buttons.  made so they can be all on the same line.
	# the background has been filled with red to demonstrate how the frame
	# is laid onto the window.
	bottom_button_frame = Frame(window, background="#ffd3d3", width=100)
	
	# the starting image for the scene, along with the initial dialog we want to show.
	update_scene(bg_image, dialog_box, "corgi_backyard_right.png", "Hi, I'm playing on the right side of the backyard!")

	# these are the buttons for this demo.
	# using the functions above, I am able to update the scene accordingly
	# and/or hide/show the text box by assigning the appropriate functions to their commands.
	# each function's functionality will be explaind above.
	prev = Button(text="Right", command=lambda: update_scene(bg_image, dialog_box, "corgi_backyard_right.png", "Hi, I'm playing on the right side of the backyard!"))
	next = Button(text="Left", command=lambda: update_scene(bg_image, dialog_box, "corgi_backyard_left.png", "Now I'm on the left side!"))
	hide = Button(text="Hide", command=lambda: hide_text_box(bg_image, dialog_box, "corgi_backyard_right.png", ""))
	show = Button(text="Show", command=lambda: show_text_box(bg_image, dialog_box, "corgi_backyard_right.png", "And I'm back!"))
	
	# pack the buttons in the container. 
	# since we want them to be in the bottom frame, we use in_ to achieve this.
	# we then do some magic with padding to get the configuration you'll see in the window.
	next.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)
	hide.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)
	show.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)
	prev.pack(in_=bottom_button_frame, side="left", ipadx=5, ipady=5, padx=BUTTON_SPACING)

	# pack the frame we made onto the window
	bottom_button_frame.pack(side="bottom", anchor="s", fill="none", pady=50)

	#then pack the dialog box and boom, we have a workable interface!
	dialog_box.pack(side="bottom", anchor="s", fill="none", ipadx=5, ipady=5)


	

	
	window.mainloop()

# main function, pretty self-explanatory.
main()