from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizmaster")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: 0", fg="white", font=("Helvetica", 16), bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300,bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here", fill=THEME_COLOR)

        self.true_button = Button(image=PhotoImage(file="images/true.png"))
        self.true_button.grid(row= 2, column=0)

        self.false_button = Button(image=PhotoImage(file="images/false.png"))
        self.false_button.grid(row=2, column=1)


        self.window.mainloop()