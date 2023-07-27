from currency_converter import CurrencyConverter
from tkinter import *

MainWindow = Tk()


c = CurrencyConverter()

def ConvertMoney(event):
    conversion_1 = c.convert(TextboxMoneydefault.get(), CurrencyUnit.get(), CurrencyUnit_1.get())
    print(conversion_1)
    Result.configure(text=conversion_1)

Title_1 = Label(MainWindow, text= "Money converter")
Title_1.grid(row= 0, column= 0)
Title_2 = Label(MainWindow, text= "Amount")
Title_2.grid(row= 0, column= 1)
Title_3 = Label(MainWindow, text= "Currency")
Title_3.grid(row= 0, column= 2)

MoneyDefault = Label(MainWindow, text= "Money original currency")
MoneyDefault.grid(row= 1, column= 0)
TextboxMoneydefault = Entry(MainWindow)
TextboxMoneydefault.grid(row= 1, column=1)
CurrencyUnit = Entry(MainWindow)
CurrencyUnit.grid(row= 1, column= 2)

MoneyConvert = Label(MainWindow, text= "Money convert currency")
MoneyConvert.grid(row= 2, column= 0)
Result = Label(MainWindow, text= "Result")
Result.grid(row= 2, column= 1)
CurrencyUnit_1 = Entry(MainWindow)
CurrencyUnit_1.grid(row= 2, column= 2)

Calculate = Button(MainWindow, text= "Convert")
Calculate.bind('<Button-1>', ConvertMoney)
Calculate.grid(row= 3, column= 0)

MainWindow.mainloop()