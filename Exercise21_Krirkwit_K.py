from tkinter import *
import math

def calculateBMI(event):
    height = float(TextboxHeight.get())
    weight = float(TextboxWeight.get())
    calculateBMI = round((weight / (math.pow(height/100,2))),2)
    print(calculateBMI)
    if calculateBMI < 18.5:
        labelResult.configure(text=[calculateBMI, '= Too Skinny'])
    elif calculateBMI < 22.9:
        labelResult.configure(text=[calculateBMI, "= Normal weight"])
    elif calculateBMI < 24.9:
        labelResult.configure(text=[calculateBMI, "= overweight"])
    elif calculateBMI < 29.9:
        labelResult.configure(text=[calculateBMI, "= fat"])
    else:
        labelResult.configure(text=[calculateBMI, "= Too fat"])

MainWindow = Tk()
LabelHeight = Label(MainWindow, text= "Height (cm.)")
LabelHeight.grid(row= 0, column= 0)
TextboxHeight = Entry(MainWindow)
TextboxHeight.grid(row= 0, column= 1)

LabelWeight = Label(MainWindow, text= "Weight (kg.)")
LabelWeight.grid(row= 1, column= 0)
TextboxWeight = Entry(MainWindow)
TextboxWeight.grid(row= 1, column= 1)

CalculateButton = Button(MainWindow, text= "Calculate")
CalculateButton.bind('<Button-1>', calculateBMI)
CalculateButton.grid(row= 2, column= 0)

labelResult = Label(MainWindow, text="Result")
labelResult.grid(row= 2, column= 1)

MainWindow.mainloop()



























