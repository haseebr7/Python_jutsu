THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class Interface:
    def __init__(self,n_quiz: QuizBrain):
        self.next_quiz = n_quiz
        self.bg_alarm = "white"


        self.window = Tk()
        self.window.title("Donnno(as usual)")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)


        self.score_label = self.text = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.text.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250,bg=self.bg_alarm)
        self.q_text = self.canvas.create_text(150,125,width=280, text="Question",fill=THEME_COLOR,font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.true_img,highlightthickness=0,command= self.if_ans_is_right)
        self.true.grid(column=0,row=2)

        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img,highlightthickness=0,command= self.if_ans_is_wrong)
        self.false.grid(column=1,row=2)
        self.next_question()


        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.next_quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.next_quiz.score}")
            next_q = self.next_quiz.next_question()
            self.canvas.itemconfig(self.q_text,text=next_q)

        else:
            self.canvas.itemconfig(self.q_text,text="No question Remain")
            self.false.config(state="disabled")
            self.true.config(state="disabled")

    def if_ans_is_right(self):
        self.feedback(self.next_quiz.check_answer("True"))

    def if_ans_is_wrong(self):
        self.feedback(self.next_quiz.check_answer("False"))

    def feedback(self,is_right):
        print(is_right)
        
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.next_question)






