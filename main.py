import tkinter as tk

entered_amount = 0
entering_grades = 0
entering_weightings = 0
entered_grades = []
entered_weightings = []
adjusted_averages = []


def get_amount():
    global entered_amount

    try:
        entered_amount = int(amount_input.get("1.0", "end-1c"))

    except ValueError:
        error_msg = tk.Label(root, text="That value is not an integer...")
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
        error_msg = tk.Label(root, text="That value is not a decimal...")
        error_msg.place(x=5, y=170)
        error_msg.after(3000, lambda: error_msg.destroy())


def get_weightings():
    global entering_weightings
    global entered_weightings

    try:
        entering_weightings = float(weighting_input.get("1.0", "end-1c"))

        if len(entered_weightings) < entered_amount:
            entered_weightings.append(entering_weightings)

    except ValueError:
        error_msg = tk.Label(root, text="That value is not a decimal...")
        error_msg.place(x=5, y=170)
        error_msg.after(3000, lambda: error_msg.destroy())


def calculation():
    global entered_grades
    global entered_weightings
    global adjusted_averages

    if len(entered_weightings) <= 0:
        final_grade = round(sum(entered_grades)/entered_amount, 2)
        statement = tk.Label(text="Your average grade is " + str(final_grade))
    else:
        for i in range(0, entered_amount):
            adjusted_grades = (entered_grades[i] * entered_weightings[i])

            adjusted_averages.append(adjusted_grades)

        statement = tk.Label(text="Your average grade is " + str(round(sum(adjusted_averages), 2)))
    statement.place(x=5, y=340)


root = tk.Tk()
root.title('Grade Calculator')
root.geometry('650x425+50+50')

courseCountStat = tk.Label(text="How many graded course materials do you have? (Please enter an integer value.)")
amount_input = tk.Text(root, height=1, width=5)
amount_enter = tk.Button(root, text="Enter", command=lambda: get_amount())

courseCountStat.place(x=0, y=0)
amount_input.place(x=5, y=33.5)
amount_enter.place(x=55, y=30)

gradeStat = tk.Label(text="What grade (as a decimal) did you receive on each graded course material?")
grade_input = tk.Text(root, height=1, width=5)
grade_enter = tk.Button(root, text="Enter", command=lambda: get_grade())

gradeStat.place(x=0, y=105)
grade_input.place(x=5, y=138.5)
grade_enter.place(x=55, y=135)

weightsStat = tk.Label(text="What is the weighting (as a decimal) of each different graded course material?")
weighting_input = tk.Text(root, height=1, width=5)
weighting_enter = tk.Button(root, text="Enter", command=lambda: get_weightings())

weightsStat.place(x=0, y=210)
weighting_input.place(x=5, y=243.5)
weighting_enter.place(x=55, y=240)

calculate = tk.Button(root, text="When you have entered all of your grades, press me to calculate your average grade.", command=lambda: calculation())
calculate.place(x=5, y=305)

root.mainloop()
