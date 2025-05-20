# Creates a sequence of colored words and displays them
import random
import tkinter as tk

root = tk.Tk()
root.geometry(f"{1200}x{775}")
root.title("Stroop test")
root.configure(bg="white")
root.resizable(False, False)

stroop_labels = []

def create_and_display_stroop_sequence(iteration):
	colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "black"]
	color_list = random.choices(colors, k=iteration)
	sequence = " ".join(color_list)

# make sure sequence (correct answers) is correct
	print(f"Correct sequence string: {sequence}")

	row = 0
	column = 0
	row_limit = 6
	for color in color_list:
		word = random.choice(colors)
		stroop_label = tk.Label(root, anchor='center', text=word, bg="white", fg=color, font=("helvetica", 40))
		stroop_label.grid(row=row, column=column, padx=40, pady=40)
		stroop_labels.append(stroop_label)

		column +=1
		if column >= row_limit:
			column = 0
			row += 1
	
	root.update()

	duration = iteration * 2500

	root.after(duration, lambda: after_display(duration))


def after_display(duration):
	print(f"Display test successful. Elapsed time: {duration} milliseconds.")
	root.destroy()


def main():
	# The number of words that will appear
	iteration = 3
	
	create_and_display_stroop_sequence(iteration)

if __name__ == '__main__':
    main()
    root.mainloop()
