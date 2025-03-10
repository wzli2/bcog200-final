# bcog200-final
1. I would like to make a simple digit-span task. This is a cognitive task that tests one's memory by displaying a sequence of numbers and prompting the user to repeat them in order. I can increase the complexity of this by introducing alternative tasks, such as reciting the number backwards, or combining this task with something Stroop test-like. For example, the user is shown a sequence of color names in a color conflicting with the word, and the user has to repeat the given words in order.
2. a) def generate_task()
   this function would be passed the round number and either a digit or colored word (depending on the task) generated from separate functions, displaying them and returning the entire sequence as a reference for the "correct answer." in short, this function plays the first half of one round of the task.
   b) def answer()
   this function would be called soon after generate_task and prompt the user to input their answer: either a sequence of numbers or a sequence of words. This function would also check to see if the answer is correct and return either outcome. basically, this function plays the second half of one round of the task.
   c) def stroop()
   this function would randomly generate and display a word-color combo (e.g. word: yellow, color: green) and return it
