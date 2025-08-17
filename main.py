import tkinter as tk

entered_amount = 0
entered_grades = []
entered_weightings = []


def get_amount():
    global entered_amount

    try:
        entered_amount = int(amount_input.get("1.0", "end-1c"))

    except ValueError:
        message("That value is not an integer...", 65)


def get_grade():
    global entered_grades

    try:
        entered_grades.append(float(grade_input.get("1.0", "end-1c")))

    except ValueError:
        message("That value is not a decimal...", 170)


def get_weightings():
    global entered_weightings

    try:
        entered_weightings.append(float(weighting_input.get("1.0", "end-1c")))

    except ValueError:
        message("That value is not a decimal...", 170)


def calculation():
    global entered_grades
    global entered_weightings
    adjusted_averages = 0

    entered_grades = entered_grades[0:entered_amount]
    entered_weightings = entered_weightings[0:entered_amount]

    if len(entered_weightings) < entered_amount:
        final_grade = round(sum(entered_grades)/entered_amount, 2)
        statement = tk.Label(text="Your average grade is " + str(final_grade))
    else:
        for i in range(0, entered_amount):
            adjusted_averages += entered_grades[i] * entered_weightings[i]

        statement = tk.Label(text="Your average grade is " + str(round(adjusted_averages, 2)))
    statement.place(x=5, y=340)


def message(text, y):
    msg = tk.Label(root, text=text)
    msg.place(x=5, y=y)
    msg.after(3000, lambda: msg.destroy())


def labelAndButton(text, y, func):
    statment = tk.Label(text=text)
    input = tk.Text(root, height=1, width=5)
    enter = tk.Button(root, text="Enter", command=lambda: func())
    statment.place(x=0, y=y)
    input.place(x=5, y=y+33.5)
    enter.place(x=55, y=y+30)
    return input


root = tk.Tk()
root.title('Grade Calculator')
root.geometry('650x425+50+50')

amount_input = labelAndButton("How many graded course materials do you have? (Please enter an integer value.)", 0, get_amount)
grade_input = labelAndButton("What grade (as a decimal) did you receive on each graded course material?", 105, get_grade)
weighting_input = labelAndButton("What is the weighting (as a decimal) of each different graded course material?", 210, get_weightings)

calculate = tk.Button(root, text="When you have entered all of your grades, press me to calculate your average grade.", command=lambda: calculation())
calculate.place(x=5, y=305)

root.mainloop()
