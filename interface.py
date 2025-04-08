class Gui:
	def __init__(self):

	def create_window(self):

	def create_labels(self):
		#create instructions and sequence's stimuli labels

	def create_buttons(self):
		#creates all buttons used

	def choose_task(self):
		#waits for button press and returns task type

	def show_instructions(self):
		#shows intstructions and waits for button press

	def show_sequence(self, correct_order, key_list, record_data):
		#shows the sequence one stimulus at a time, takes text input and records results

	def check_for_valid_number(self, key_input):
		#makes sure the key input is an integer and returns True/False

	def check_for_valid_word(self, word_input):
		#makes sure the key input is a valid word and returns True/False