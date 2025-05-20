import tkinter as tk

class Gui:
	def __init__(self):

		self.root = None
		self.stimulus_label = None
		self.instructions_text_label = None
		self.task_selection_buttons = []
		self.next_button = None
		self.submit_button = None
		self.selected_task = None
		self.answer = None

		self.create_window()
		self.create_labels()
		self.create_buttons()
		self.create_entries()

	def create_window(self):
		self.root = tk.Tk()
		self.root.geometry(f"{1200}x{775}")
		self.root.title("Experiment")
		self.root.configure(bg="white")
		self.root.resizable(False, False)

	def create_labels(self):
		#create instructions and sequence's stimuli labels
		self.instructions_text_label = tk.Label(self.root, anchor='center',
												height = 10,
												width = 1200,
												bg="white",
												fg="black",
												font=f"{"helvetica"} {18}")

		self.stimulus_label = tk.Label(self.root, anchor='center',
										height = 775,
										width = 1200,
										bg="white",
		    							fg="black",
		    							font=f"{"helvetica"} {30}")


	def create_buttons(self):
		#creates all buttons used

		self.task_selection_frame = tk.Frame(self.root, bg="white")
		self.instructions_frame = tk.Frame(self.root, bg="white")


		task_names = ["Digit-span task", "Reverse digit-span", "Stroop-span task", "Reverse Stroop-span"]
		for i, name in enumerate(task_names):
			button = tk.Button(self.task_selection_frame, text = name, width=15, height=2, command=lambda i=i: self.task_button_command(i))
			self.task_selection_buttons.append(button)
		self.task_selection_buttons[0].grid(row=0, column=0, padx=10, pady=10)
		self.task_selection_buttons[1].grid(row=0, column=1, padx=10, pady=10)
		self.task_selection_buttons[2].grid(row=1, column=0, padx=10, pady=10)
		self.task_selection_buttons[3].grid(row=1, column=1, padx=10, pady=10)

		self.next_button = tk.Button(self.root, text="Next", width=20, height=2, command=self.next_button_command)

		self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_button_command)


	def create_entries(self):
		self.answer_entry = tk.Entry(self.root, font=("helvetica", 18), width=20, bd=2, relief="solid")

	def task_button_command(self, i):
		self.selected_task = i
		self.task_selection_frame.destroy()

	def next_button_command(self):
		self.next_button.pack_forget()
		self.instructions_text_label.destroy()
		self.instructions_frame.destroy()

	def submit_button_command(self):
		self.answer = self.answer_entry.get()
		self.answer_entry.pack_forget()
		self.submit_button.pack_forget()

	def check_for_valid_number(self, key_input):
		#makes sure the key input is an integer and returns True/False
		pass

	def check_for_valid_word(self, word_input):
		#makes sure the key input is a valid word and returns True/False
		pass