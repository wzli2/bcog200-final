def show_instructions(selected_task):
	#shows intstructions and waits for button press
	instruction_file_path_list = [
								"../instructions/digit_span.txt", 
								"../instructions/reverse_digit.txt",
								"../instructions/stroop_span.txt",
								"../instructions/reverse_stroop.txt"
								]

	instruction_filename = instruction_file_path_list[selected_task]
	with open(instruction_filename, 'r') as file:  # open the instruction file in read mode
		for line in file:  # for each line in the file
			line = line.strip('\n')  # strip off the newlines from each line in the file
			line = line.replace(".", ".\n")  # replace every period in the current line with a period followed by \n
			instructions = line # add the string to the instruction list

	return instructions

def main():
	task_selection_buttons = [0, 1, 2, 3]
	for task in task_selection_buttons:
		selected_task = task
		print(f"Task {selected_task} text:")
		print(show_instructions(selected_task), "\n")

if __name__ == '__main__':
    main()