# What is a digit-span test?
A digit-span test is a cognitive task that tests one's memory. Typically, a series of numbers is presented in some manner, and the testee is asked to recite the digits in order. The test continues until incorrect recitation, and can be modified to occur in reverse order.

# What is a Stroop test?
In a Stroop test, names of colors are presented in colors incongruent with the name. For example, the word "black" but in red text, and the testee is often asked to recite the color of the text.

The Stroop test and digit span tests are both classics in cognitive psychology and neuroscience. From these basic tasks, experiments concerning the speed and accuracy of memory consolidation and retrieval can be designed. For example, one could compare the results from a population to research the differences in working memory regarding numbers, words, and colors.

# Installation
Download the experiment_main and instructions folders into the same directory. Run "run_exp.py" with python to run the test.

# Testing
After running run_exp.py, four buttons will appear. Each corresponds to a different test and when clicked, will make the corresponding instructions appear on screen.

To begin, choose the top-left "Digit-span" task. You will see a sequence of numbers, and after a few seconds, be prompted to repeat them back in order. If correct, the number of digits will increase until you fail. Once comfortable with the basics, you can choose between alternative tasks such as reciting the sequence backwards or a Stroop-test variant, in which you will be shown a sequence of names of colors in a color conflicting with the name and be prompted to repeat the given words in order.

# Code Strucuture
experiment_main/
* This program is built from an interface.py (GUI) file, an experiment.py file, and a run_exp.py file. The first two code for classes that run_exp.py use to run the experiment. interface.py is primarily responsible for the GUI and most of the frames and widgets. experiment.py is responsible for everything else in addition to the Stroop-specific widgets.

instructions/
* This file contains the .txt files that contain the intruction texts for each task, and is accessed from experiment.py

# Controls
Buttons must be pressed with the mouse to progress in the test, and the test itself takes keyboard input.
