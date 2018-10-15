import os.path
import io

INSTALL_DIR = os.getcwd() + "/"

def load(filename):
	try:
		save_file = open(INSTALL_DIR+filename, "r")
	except FileNotFoundError:
		return "No save file exists."
	else:
		
		try:
			loadednum = float(save_file.read())
		except (TypeError, ValueError):
			save_file.close()
			return "Save file is corrupted. Please start a new game."
		else:
			save_file.close()
			if loadednum < 1 or loadednum > 12.4:
				return "Save file is corrupted. Please start a new game."

			return "success"