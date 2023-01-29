from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(height=300, width=350, bg="white")
        self.create_canvas()
        image_right = PhotoImage(file="images/true.png")
        image_wrong = PhotoImage(file="images/false.png")
        self.right = Button(image=image_right, highlightthickness=0, command=self.press_right)
        self.wrong = Button(image=image_wrong, highlightthickness=0, command=self.press_wrong)
        self.create_button()
        self.create_label()
        self.get_next_question()
        self.window.mainloop()

    def create_canvas(self):

        self.question_text = self.canvas.create_text(175, 150, text="Question", width=300, font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def create_button(self):

        self.right.config(height=100, width=100)
        self.wrong.config(height=100, width=100)
        self.right.grid(row=2, column=0)
        self.wrong.grid(row=2, column=1)

    def create_label(self):
        self.label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 13, "bold"))
        self.label.grid(row=0, column=1)

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.right.config(state="normal")
        self.wrong.config(state="normal")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
            self.window.after(1000, self.reach_end)


    def press_right(self):
        is_right = self.quiz.check_answer("true")
        self.check_answer(is_right)
        self.label.config(text=f"Score: {self.quiz.score}")

    def press_wrong(self):
        is_right = self.quiz.check_answer("false")
        self.check_answer(is_right)
        self.label.config(text=f"Score: {self.quiz.score}")

    def check_answer(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green2")
        else:
            self.canvas.config(bg="orange red")
        self.right.config(state="disabled")
        self.wrong.config(state="disabled")
        self.window.after(1000, self.get_next_question)

    def reach_end(self):
        self.canvas.itemconfig(self.question_text, text=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")

