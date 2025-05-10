import random

class Exp:
	def __init__(self, gui):
		self.gui = gui

	def choose_task(self):
		#presents task options, waits for button press and returns task type
		self.gui.task_selection_frame.pack(pady=20)
		self.gui.root.wait_window(self.gui.task_selection_frame)

	def show_instructions(self):
		#shows intstructions and waits for button press
		instruction_file_path_list = [
									"../instructions/digit_span.txt", 
									"../instructions/reverse_digit.txt",
									"../instructions/stroop_span.txt",
									"../instructions/reverse_stroop.txt"
									]

		instruction_filename = instruction_file_path_list[self.gui.selected_task]
		with open(instruction_filename, 'r') as file:  # open the instruction file in read mode
			for line in file:  # for each line in the file
				line = line.strip('\n')  # strip off the newlines from each line in the file
				line = line.replace(".", ".\n")  # replace every period in the current line with a period followed by \n
				instructions = line # add the string to the instruction list

		self.gui.instructions_text_label.configure(text=instructions)
		self.gui.instructions_text_label.pack() # make the label appear in the window
		self.gui.instructions_text_label.pack_propagate(False) # prevent the label from changing size to fit the text

		self.gui.next_button.pack(pady=30)

		self.gui.root.update()

	def create_digit_sequence(self, iteration):
		#generates sequence for digit-span tasks
		sequence = ""
		for i in range(iteration):
			digit = random.randint(0, 9)
			sequence += str(digit)

		return int(sequence)

	def create_stroop_sequence(self, iteration):
		pass

	def show_sequence(self, iteration, sequence):#, key_list, record_data):

		self.gui.stimulus_label.configure(text=sequence) #need to configure text if digits, image if stroop
		self.gui.stimulus_label.pack()
		self.gui.stimulus_label.pack_propagate(False)
		self.gui.root.update()

		duration = iteration * 4000
		self.gui.root.after(duration, self.gui.root.quit)
		self.gui.root.mainloop()
		self.gui.stimulus_label.pack_forget()

	def request_answer(self):
		self.gui.answer_entry.pack(pady=10)
		self.gui.submit_button.pack(pady=10)
		self.gui.root.update()

	def check_answer(self, correct_sequence, given_answer):
		if self.gui.selected_task == 0:
			return correct_sequence == int(given_answer)

		elif self.gui.selected_task == 1:
			correct_sequence = str(correct_sequence)[::-1]
			return correct_sequence == int(given_answer)

		elif self.gui.selected_task == 2:
			return str(correct_sequence) == given_answer

		elif self.gui.selected_task == 3:
			correct_sequence = correct_sequence.split()[::-1]
			return correct_sequence == given_answer.split()



	def run_experiment(self):
		#runs choose_task, show_instructions, and show_sequence from Gui
		self.choose_task()
		self.show_instructions()
		correct = True
		iteration = 1
		while correct:
			if self.gui.selected_task in [0,1]:
				sequence = self.create_digit_sequence(iteration)
			else:
				sequence = self.create_stroop_sequence(iteration)
			self.show_sequence(iteration, sequence)#, key_list, record_data):
			self.request_answer()
			correct = self.check_answer(sequence, self.gui.answer)
			iteration += 1

		self.save_data()
		self.make_plots()
		self.save_plots()



	def save_data(self):
		pass

	def make_plots(self):
		pass

	def save_plots(self):
		pass

