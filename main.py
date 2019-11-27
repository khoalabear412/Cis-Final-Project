from tkinter import *
from tkinter import messagebox
def runButtonCallback():
    print('hi')


def getTotal(income, expense):
    return income - expense

def formatTotal(total):
    return "You Monthly Net Income is %f" % total

def getInputIncome():
    flag = True 

    while flag:
        anInput = input("Please Enter Your Monthly Income: ")
        if not anInput.isnumeric():
            print("Invalid input")
            continue

        income = float(anInput)
        if income >= 0:
            return income
        else:
            print("Invalid income")

def getInputExpense():
    flag = True

    while flag:
        anInput = input("Please Enter Your Monthly Expense: ")
        if not anInput.isnumeric():
            print("Invalid input")
            continue

        expense = float(anInput)
        if expense >= 0:
            return expense
        else:
            print("Invalid expense")

def runApp():
    income = getInputIncome()
    expense = getInputExpense()
    total = getTotal(income, expense)

    print(formatTotal(total))

def runUI():
    window = Tk()
    window.title('Budget App')
    # Set size
    window.geometry('500x500')

    # Add labels
    Label(window, text="Income:  ").grid(row=0)
    Label(window, text="Expense: ").grid(row=1)

    income = StringVar()
    income.set('')

    expense = StringVar()
    expense.set('')

    def callback():
        total = getTotal(float(income.get()), float(expense.get()))
        messagebox.showinfo("Result", formatTotal(total))

        # Add more logic here




    e1 = Entry(window, textvariable=income)
    e2 = Entry(window, textvariable=expense)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    # Add button

    Button(window, text='Run', command=callback).grid(row=3, column=0, sticky=W, pady=4)

    # Run 
    window.mainloop()

def main():
    runUI()
    # runApp()
    pass


if __name__ == "__main__":
    main()