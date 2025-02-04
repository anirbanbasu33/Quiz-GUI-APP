from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, bg= THEME_COLOR)

        self.score_label = Label(text= "Score: 0", fg= "white", bg= THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg= "white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125, width= 280, text="Your Text", font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)

        false_image= PhotoImage(file = "images/false.png")
        self.false_button = Button(image= false_image, highlightthickness=0, command= self.falsy)
        self.false_button.grid(row=2, column=0)

        # Why not use self.false_image ? because add 'self.' makes it a property to be accesses witin class
        # for multiple uses, whereas false/true_image is one time functionality

        true_image= PhotoImage(file = "images/true.png")
        self.true_button = Button(image= true_image, highlightthickness=0, command= self.truthy)
        self.true_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
        #After 1 sec, bg back to normal
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():            
            self.score_label.config(text=f"Score:{self.quiz.score}")
            
            # Taps into quiz_brain.py and calls the next_question()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Ended")
            # After Quiz Ends, need to disable buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def truthy(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def falsy(self):
        response = self.quiz.check_answer("False")
        self.give_feedback(response)

    def give_feedback(self, response):

        # Cant use time.sleep inside tkinter mainloop
        if response == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



