from tkinter import *
from tkinter import messagebox as mb
import json


def display_title():
    title = Label(root, text="iQuiz Application", font=("Arial", 30, "bold"),
                width=40, bg="green", fg="white")

    title.place(x=0, y=2)


class Quiz:
    def __init__(self):
        self.q_no = 0

        display_title()
        self.display_question()

        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()

        self.display_options()
        self.buttons()

        self.data_size = len(question)
        self.correct = 0

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"

        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"

        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1

        self.q_no += 1

        if self.q_no == self.data_size:
            self.display_result()
            root.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(root, text="Next", font=("Arial", 20, "bold"),
                             width=10, bg="green", fg="white", command=self.next_btn)

        next_button.place(x=350, y=380)

        quit_button = Button(root, text="Quit", font=("Arial", 15, "bold"),
                             command=root.destroy, width=5, bg="red", fg="white")

        quit_button.place(x=800, y=60)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = Label(root, text=question[self.q_no], font=("Arial", 20, "bold"),
                     width=60, anchor='w')

        q_no.place(x=70, y=100)

        # This method displays the title of the quiz

    def radio_buttons(self):
        q_list = []
        y_pos = 200

        while len(q_list) < 4:
            radio_btn = Radiobutton(root, text=" ",
                                    variable=self.opt_selected, value=len(q_list) + 1, font=("Arial", 20, "bold"))

            q_list.append(radio_btn)
            radio_btn.place(x=70, y=y_pos)
            y_pos += 50

        return q_list


root = Tk()
root.geometry("900x500")
root.title("iQuiz App")
with open('data.json') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = Quiz()
root.mainloop()
