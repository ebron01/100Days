from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        #Label
        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        #Canvas
        self.canvas = Canvas( )
        self.canvas.config(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 
                                                     125, 
                                                     width=280,
                                                     text="question goes here!", 
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
        #Buttons
        true_image = PhotoImage(file="/home/beast/100Days/quizzler/images/true.png")
        false_image = PhotoImage(file="/home/beast/100Days/quizzler/images/false.png")
        self.true_img = Button(image=true_image, command=self.true_pressed)
        self.false_img = Button(image=false_image, command=self.false_pressed)
        self.true_img.grid(column=0, row=2)
        self.false_img.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()     
            self.score_label.config(text=f"Score: {self.quiz.score}")
            
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached to the end of the quiz!")
            self.true_img.config(state="disabled")
            self.false_img.config(state="disabled")
        self.canvas.config(bg="white")
        
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)