import tkinter as tk
from tkinter import *

entered_amount = 0
entering_grades = 0
entered_grades = []

def get_amount():
    global entered_amount

    try:
        entered_amount = int(amount_input.get("1.0", "end-1c"))

    except ValueError:
        error_msg = Label(root, text="That value is not an interger...")
        error_msg.place(x=5, y=65)
        error_msg.after(3000, lambda: error_msg.destroy())

def get_grade():
    global entering_grades
    global entered_grades

    try:
        entering_grades = float(grade_input.get("1.0", "end-1c"))

        if len(entered_grades) < entered_amount:
            entered_grades.append(entering_grades)

    except ValueError:
        error_msg = Label(root, text="That value is not an decimal...")
        error_msg.place(x=5, y=170)
        error_msg.after(3000, lambda: error_msg.destroy())

def calculation():
    final_grade = round(sum(entered_grades)/entered_amount, 2)

    statement4 = Label(text="Your average grade is ")
    statement5 = Label(text=final_grade)
    statement4.place(x=5, y=235)
    statement5.place(x=157, y=235)

root = Tk()
root.title('Grade Calculator')
root.geometry('650x325+50+50')

statement = Label(text="How many courses/graded course materials do you have? (Please enter and integer value.)")
amount_input = Text(root, height=1, width=5)
amount_enter = Button(root, text="Enter", command=lambda: get_amount())

statement.place(x=0, y=0)
amount_input.place(x=5, y=33.5)
amount_enter.place(x=55, y=30)

statement2 = Label(text="What grade (as a decimal) did you receive on each course/graded course material?")
grade_input = Text(root, height=1, width=5)
grade_enter = Button(root, text="Enter", command=lambda: get_grade())

statement2.place(x=0, y=105)
grade_input.place(x=5, y=138.5)
grade_enter.place(x=55, y=135)

calculate = Button(root, text="When you have entered all of your grades, press me to calculate your average grade.", command=lambda: calculation())
calculate.place(x=5, y=200)

root.mainloop()
