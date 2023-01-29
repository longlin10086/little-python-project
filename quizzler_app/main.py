from question_model import Question
from data import get_url
from quiz_brain import QuizBrain
from ui import QuizInterface
from tkinter import messagebox

is_on = True
while is_on:
    question_bank = []
    question_data = get_url()
    for question in question_data["results"]:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)


    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    is_on = messagebox.askyesno(title="choose", message="Do you want to play a new game?")
