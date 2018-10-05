''' author: Adrian Alonzo 												'''
''' 10/3/18 - creation of the Event object 								'''
''' a framework for us to create any Events we think we'll need without '''
''' any additional work. 												'''
import @abstractmethod

class Event:
	def __init__(self, event_id, event_type, event_data, supported_events):
		''' unit test case for event_id variable being an integer >= 0 will go here  '''
		''' we do not want there to be a negative event_id.                          '''
		# code for this goes here

		''' unit test case for checking that plot dialog is a string will go here '''
		# code for this goes here

		''' unit test case for checking that the events_list list is '''
		''' a) a list, b) a list which contains only Event objects   '''  
		# and code for this goes here

		# an integer, this variable allows us to specify the order events are to go in.
		# doing this allows us to run them either all at once (such as during the actual game) 
		# and/or independently.  
		self.event_id = event_id 

		# a string, this variable is a label for an event's type. it helps us organize each kind of 
		# event we make and also allows us to get, look at, or run particular groups of Events if we 
		# need to.  This means we will need to agree on what Events we want to support.
		# Thoughts right now are "messagebox" and "minigame". 
		self.event_type = event_type

		# event_data is designed to contain the pieces relevant to the event.
		# this can include stuff like text (such as for dialog that shows during 
		# the event, choices for user input, etc.).  Sanity checking of data will need
		# to be performed on a subclass by subclass basis; this can be done by 
		# implementing the verify_data_integrity() method below.  
		self.event_data = event_data.copy()

		# a list, this variable will define all the Events which we want to support in our program.
		# we can raise an exception in sanity_check_data for any events which are not supported or
		# specified incorrectly.  Supported events will be specified as a column either in a separate
		# supported_events.csv file, or by populating all the events listed in the plot.csv file.
		# this may or may not be needed, but this would give us another thing to unit test ;)
		self.supported_events = supported_events.copy()

		def get_event_id():
			return event_id

		def get_event_type():
			return event_type

		def get_event_name():
			return event_name

		''' this method is to be implemented by any subclasses using this Event class.  			'''
		''' in the context of this program, an Event is anything which requires user interaction.   '''
		@abstractmethod
		def run():
			pass

		''' if this method is implemented, sanity checking of data will automatically be handled by '''
		''' the program.  the idea is that this method can be called any time an Event object       '''
		''' is being created from specified data.  By doing it this way, debugging becomes a heck   '''
		''' of a lot easier since exception raising for each type of event will be contained in.    '''
		''' one location.  																			'''
		@abstractmethod
		def sanity_check_data():
			pass