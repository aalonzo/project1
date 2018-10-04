''' author: Adrian Alonzo 												'''
''' 10/3/18 - creation of the Page object 								'''
''' basically is where all the pieces of the plot will be contained in. '''
''' so all the dialogs, potential events, ordering, etc.				'''

class Page:

	def __init__(self, number, plot_dialog, events_list):
		''' unit test case for position variable being an integer >= 0 will go here  '''
		''' we do not want there to be a negative plot position, that would be ridiculous '''
		# code for this goes here

		''' unit test case for checking that plot dialog is a string will go here '''
		# code for this goes here

		''' unit test case for checking that the events_list list is '''
		''' a) a list, b) a list which contains only Event objects   '''  
		# and code for this goes here

		# lets us know where in the plot we are based on its specified position in the plot.csv file.
		self.number = number   

		# the dialog associated with this plot element.  this is the dialog output on each "page" of the visual novel.        
		self.plot_dialog = plot_dialog

		# this will be a list containing the set of Event object associated with this point in the plot line.
		self.events_list = events_list.copy() 

		def get_page_number(): 
			return number

		def get_plot_dialog():
			return plot_dialog

		''' this function runs a specified event. events are designed  '''
		''' to run in order, starting of course with the first event   '''
		''' and ending with the last event.  with the way these will   '''
		''' be loaded into memory, these should be in order by default.'''
		''' this allows us to step forward or backward through events  '''
		''' on the fly.												   '''
		def run_event_id(event_id):
			event_list[event_id].run()


		''' this functions runs all of the events set up for this page. '''
		''' the Event object will be designed to run individually (as   '''
		''' called using the function above), or all at once (as this.  '''
		''' does. 														'''
		def run_all_events():
			for event in events_list:
				event.run()




