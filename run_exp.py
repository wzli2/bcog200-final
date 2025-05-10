import experiment
import interface

def main():
    gui = interface.Gui()
    the_experiment = experiment.Exp(gui)
    gui.root.mainloop()

if __name__ == '__main__':
    main()
