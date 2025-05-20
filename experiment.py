import random
import tkinter as tk

class Exp:
	def __init__(self, gui):
		self.gui = gui
		self.stroop_labels = []

		self.run_experiment()

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

		self.gui.root.wait_window(self.gui.instructions_frame)

	def create_digit_sequence(self, iteration):
		#generates sequence for digit-span tasks
		sequence = ""
		for i in range(iteration):
			digit = random.randint(0, 9)
			sequence += str(digit)

		return int(sequence)

	def create_and_display_stroop_sequence(self, iteration):
		colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black"]
		color_list = random.choices(colors, k=iteration)
		self.sequence = " ".join(color_list)

		#I asked chatgpt for help with formatting because I was only using pack(), and counting columns using grid() is a nice solution
		row = 0
		column = 0
		row_limit = 6
		for color in color_list:
			word = random.choice(colors)
			stroop_label = tk.Label(self.gui.root, anchor='center', text=word, bg="white", fg=color, font=("helvetica", 40))
			stroop_label.grid(row=row, column=column, padx=40, pady=40)
			self.stroop_labels.append(stroop_label)

			column +=1
			if column >= row_limit:
				column = 0
				row += 1
		
		self.gui.root.update()

		duration = iteration * 2500

		self.gui.root.after(duration, self.request_answer)


	def show_sequence(self, iteration, sequence):#, key_list, record_data):

		self.gui.stimulus_label.configure(text=sequence)
		self.gui.stimulus_label.pack()
		self.gui.stimulus_label.pack_propagate(False)
		self.gui.root.update()

		duration = iteration * 1500

		self.gui.root.after(duration, self.request_answer)

	def request_answer(self):
		if self.gui.selected_task in [0,1]:
			self.gui.stimulus_label.pack_forget()
		else:
			for label in self.stroop_labels:
				label.destroy()
			self.stroop_labels.clear()

		#from asking chatgpt how to get rid of tkinter entry text
		self.gui.answer_entry.delete(0, tk.END)
		self.gui.answer_entry.pack(pady=10)
		#From asking chatgpt "tkinter how to make a frame not overlap a widget":
		self.gui.answer_entry.focus_set()

		self.gui.submit_button.pack(pady=10)
		self.gui.root.update()

		self.answer_loop()

	def answer_loop(self):
		if self.gui.answer is not None:
			self.correct = self.check_answer(self.sequence, self.gui.answer)
			self.iteration += 1
			self.gui.answer = None
			self.experiment_loop()
		else:
			self.gui.root.after(100, self.answer_loop)

	def check_answer(self, correct_sequence, given_answer):
		if self.gui.selected_task == 0:
			return correct_sequence == int(given_answer)

		elif self.gui.selected_task == 1:
			correct_sequence = str(correct_sequence)[::-1]
			return correct_sequence == str(given_answer)

		elif self.gui.selected_task == 2:
			return correct_sequence == given_answer

		elif self.gui.selected_task == 3:
			correct_sequence = correct_sequence.split()[::-1]
			return correct_sequence == given_answer.split()



	def run_experiment(self):
		#runs choose_task, show_instructions, and show_sequence from Gui
		self.choose_task()
		self.show_instructions()
		self.correct = True
		if self.gui.selected_task in [0,1]:
			self.iteration = 3
		else:
			self.iteration = 2
		self.experiment_loop()

	def experiment_loop(self):
		#if incorrect answer, exit experiment
		if not self.correct:

			self.gui.root.destroy()


		#0 and 1 are digit-test conditions, 2 and 3 are stroop
		if self.gui.selected_task in [0,1]:
			self.sequence = self.create_digit_sequence(self.iteration)
			self.show_sequence(self.iteration, self.sequence)

		else:
			self.create_and_display_stroop_sequence(self.iteration)

