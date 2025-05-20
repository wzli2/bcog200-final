#Test that check_answer logic works correctly

#Choose 0-4:
# 0 is digit-span
# 1 is reverse digit-span
# 2 is Stroop
# 3 is reverse Stroop
selected_task = 1

def check_answer(correct_sequence, given_answer):
	if selected_task == 0:
		return correct_sequence == int(given_answer)

	elif selected_task == 1:
		correct_sequence = str(correct_sequence)[::-1]
		return correct_sequence == str(given_answer)

	elif selected_task == 2:
		return correct_sequence == given_answer

	elif selected_task == 3:
		correct_sequence = correct_sequence.split()[::-1]
		return correct_sequence == given_answer.split()

def main():
	correct = check_answer(123, "321")
	# if  0: (int, "int string") == True
	# if 1: (int, "(reverse) int string") == True
	# if 2: ("color color", "color color") == True
	# if 3: ("color color", "(reverse) color color") == True


	if correct == True:
		print(f"Successful checking. Task {selected_task} works as intended")
	else:
		print(f"Error. Task {selected_task} DOES NOT work as intended")

if __name__ == '__main__':
    main()