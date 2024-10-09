import tkinter as tk
from tkinter import ttk, messagebox

#We create an object of Tk class
window = tk.Tk()

#Size 2
Wide = 400
Height = 250
Size = str(Wide) + "x" + str(Height)
window.geometry(Size)

#Title
window.title('Calculator')
#Icon
window.iconbitmap('./Img/Crown.ico')

#No resizable
window.resizable(0,0)

#Varials
text = tk.StringVar()
firstOperator = True
operator1 = 0
operator2 = 0
total = 0
optionSelected = ''

#funciones
def delete():
    text.set('')


def operation(option):
    global firstOperator
    global optionSelected
    global operator1
    if (option != '') and (text.get!='') and (firstOperator) :
        optionSelected = option
        operator1 = float(text.get())
        delete()
        firstOperator = False


def number_pressed(number):
    number = text.get()+ number
    text.set(number) 

def dot ():
    if '.' not in text.get():
        number = text.get() + '.'
        text.set(number)

def result():
    global operator1, operator2, optionSelected, firstOperator, result
    if (firstOperator == False) and (text.get() != ''):
        operator2 = float(text.get())
        if optionSelected == '+':
            result = operator1 + operator2
        if optionSelected == '-':
            result = operator1 - operator2
        if optionSelected == '/':
            try:
                result = operator1 / operator2
            except:
                messagebox.showerror('Eror','You can`t divide for 0')
        if optionSelected == '*':
            result = operator1 * operator2
        text.set(int(result))
        optionSelected = ''
        operator1 = 0
        operator2 = 0
        firstOperator = True

#Create frames
frm_sup = tk.Frame(window, height=50)
frm_inf = tk.Frame(window)

#Position
frm_sup.pack(side=tk.TOP, fill='x')
frm_sup.config(height=50)
frm_inf.pack(fill='both')
frm_inf.config(bg='gray')

#Buttons
txt_result = ttk.Entry(frm_sup, font=('arial',22,'bold'), state="readonly", textvariable=text, justify=tk.RIGHT, width=24)
txt_result.grid(row=0, column=0, padx=5, pady=5,  ipadx=5, ipady=5)

btn_delete = ttk.Button(frm_inf, text='Delete', command=delete, width=10)
btn_delete.grid(row=0, column=0, padx=5, pady=5)

#Division
btn_division = ttk.Button(frm_inf, text='/', command=lambda:operation('/'), width=10)
btn_division.grid(row=0, column=1, padx=5, pady=5)

#Multiplication
btn_multiplicaction = ttk.Button(frm_inf, text='*', command=lambda:operation('*'), width=10)
btn_multiplicaction.grid(row=0, column=2, padx=5, pady=5)

#Addition
btn_addition = ttk.Button(frm_inf, text='+', command=lambda:operation('+'), width=10)
btn_addition.grid(row=0, column=3, padx=5, pady=5)

#Subtraction
btn_subtraction = ttk.Button(frm_inf, text='-', command=lambda:operation('-'), width=10)
btn_subtraction.grid(row=0, column=4, padx=5, pady=5)

#Numbers
btn_0 = ttk.Button(frm_inf, text='0', command=lambda:number_pressed('0'), width=10)
btn_0.grid(row=1, column=0, padx=5, pady=5)

btn_01 = ttk.Button(frm_inf, text='1', command=lambda:number_pressed('1'), width=10)
btn_01.grid(row=1, column=1, padx=5, pady=5)

btn_02 = ttk.Button(frm_inf, text='2', command=lambda:number_pressed('2'), width=10)
btn_02.grid(row=1, column=2, padx=5, pady=5)

btn_03 = ttk.Button(frm_inf, text='3', command=lambda:number_pressed('3'), width=10)
btn_03.grid(row=1, column=3, padx=5, pady=5)

btn_04 = ttk.Button(frm_inf, text='4', command=lambda:number_pressed('4'), width=10)
btn_04.grid(row=1, column=4, padx=5, pady=5)

btn_05 = ttk.Button(frm_inf, text='5', command=lambda:number_pressed('5'), width=10)
btn_05.grid(row=2, column=0, padx=5, pady=5)

btn_06 = ttk.Button(frm_inf, text='6', command=lambda:number_pressed('6'), width=10)
btn_06.grid(row=2, column=1, padx=5, pady=5)

btn_07 = ttk.Button(frm_inf, text='7', command=lambda:number_pressed('7'), width=10)
btn_07.grid(row=2, column=2, padx=5, pady=5)

btn_08 = ttk.Button(frm_inf, text='8', command=lambda:number_pressed('8'), width=10)
btn_08.grid(row=2, column=3, padx=5, pady=5)

btn_09 = ttk.Button(frm_inf, text='9', command=lambda:number_pressed('9'), width=10)
btn_09.grid(row=2, column=4, padx=5, pady=5)

btn_dot = ttk.Button(frm_inf, text='.', command=dot, width=10)
btn_dot.grid(row=3, column=0, padx=5, pady=5)

btn_total = ttk.Button(frm_inf, text='=',command= result, width=10)
btn_total.grid(row=3, column=1, padx=5, pady=5)











#Always put at the end
window.mainloop()
