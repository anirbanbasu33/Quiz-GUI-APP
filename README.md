# Quiz-GUI-APP
Quiz App, using Open Trivia Db, API and Tkinter

Commit1: API usage before HTML unescape
Commit2: My Tkinter Version
Commit3: Updated Tkinter from Angela
Commit4: Question placed on GUI...Class parameter passing
Commit5: My attempt to track right/wrong at GUI
Commit6: Final version


Post commit- "Updated tkinter from Angela"
------------------------------------------

def get_next_question(self):
        
        # Taps into quiz_brain.py and calls the next_question()
        pass/


But, how do we get hold of the quiz_brain that we craete at main.py
we can pass its object ad input when we create QuizInterface object --> quiz_ui

Changes at main=
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


Catch this at ui.py= add another parameeter at init which calls quizbrain 
and then create a property self.quiz = quiz_brain (received)
class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain



One more change-
we need to specify the datatype of passed parameter quiz_brain....to access all the methods of QuizBrain class

from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):