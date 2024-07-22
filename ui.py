from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizmaster")
        self.canvas = Canvas()
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas.config(background=THEME_COLOR)
        self.true_button = Button(image=PhotoImage(file="images/true.png"))
        self.true_button.grid(row= 2, column=0)
        self.false_button = Button(image=PhotoImage(file="images/false.png"))
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()