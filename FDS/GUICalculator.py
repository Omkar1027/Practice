from tkinter import *

expression=""

def press(num):
    global expression

    expression = expression+str(num)

    equation.set(expression)

def clear():
    global expression

    expression = ""

    equation.set("")

def equal():
    try: 
        global expression

        total=str(eval(expression))

        equation.set(total)

        expression=""

    except:
        equation.set("error")
        equation=""

if __name__ == "__main__":
    Calci = Tk()
    Calci.configure(background="green")
    Calci.title("Calculator_27")
    Calci.geometry("500x500")

    equation=StringVar()
    ans = Entry(Calci,textvariable=equation)
    ans.grid(columnspan=4,row=0)

    button1 = Button(Calci, text=' 1 ', fg='white', bg='black',command=lambda: press(1),  height='5', width='10') 
    button1.grid(column=0, row=1)

    button1 = Button(Calci, text=' 2 ', fg='white', bg='black',command=lambda: press(2), height='5', width='10') 
    button1.grid(column=1, row=1)

    button1 = Button(Calci, text=' 3 ', fg='white', bg='black',command=lambda: press(3), height='5', width='10') 
    button1.grid(column=2, row=1)

    button1 = Button(Calci, text=' + ', fg='white', bg='black',command=lambda: press('+'), height='5', width='10') 
    button1.grid(column=3, row=1)

    button1 = Button(Calci, text=' 4 ', fg='white', bg='black',command=lambda: press(4), height='5', width='10') 
    button1.grid(column=0, row=2)

    button1 = Button(Calci, text=' 5 ', fg='white', bg='black',command=lambda: press(5), height='5', width='10') 
    button1.grid(column=1, row=2)

    button1 = Button(Calci, text=' 6 ', fg='white', bg='black',command=lambda: press(6), height='5', width='10') 
    button1.grid(column=2, row=2)

    button1 = Button(Calci, text=' - ', fg='white', bg='black',command=lambda: press('-'), height='5', width='10') 
    button1.grid(column=3, row=2)

    button1 = Button(Calci, text=' 7 ', fg='white', bg='black',command=lambda: press(7), height='5', width='10') 
    button1.grid(column=0, row=3)

    button1 = Button(Calci, text=' 8 ', fg='white', bg='black',command=lambda: press(8), height='5', width='10') 
    button1.grid(column=1, row=3)

    button1 = Button(Calci, text=' 9 ', fg='white', bg='black',command=lambda: press(9), height='5', width='10') 
    button1.grid(column=2, row=3)

    button1 = Button(Calci, text=' * ', fg='white', bg='black',command=lambda: press('*'), height='5', width='10') 
    button1.grid(column=3, row=3)

    button1 = Button(Calci, text=' AC ', fg='white', bg='black',command=equal, height='5', width='10') 
    button1.grid(column=0, row=4)

    button1 = Button(Calci, text=' 0 ', fg='white', bg='black',command=lambda: press(0), height='5', width='10') 
    button1.grid(column=1, row=4)

    clear = Button(Calci, text=' = ', fg='white', bg='black',command=clear, height='5', width='10') 
    clear.grid(column=2, row=4)

    button1 = Button(Calci, text=' / ', fg='white', bg='black',command=lambda: press('/'), height='5', width='10') 
    button1.grid(column=3, row=4)

    Calci.mainloop()


