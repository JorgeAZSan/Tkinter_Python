import tkinter as tk
from tkinter import ttk, messagebox

#We create an object of Tk class
window = tk.Tk()

#Size 2
Wide = 400
Height = 300
Size = str(Wide) + "x" + str(Height)
window.geometry(Size)

#Title
window.title('Tabs')
#Icon
window.iconbitmap('./Img/Crown.ico')

#Varials
user = tk.StringVar()
code = tk.StringVar()
user_saved = "jorge"
code_saved = "4321"

def message (title, message, Pass):
    if Pass ==1:
        messagebox.showinfo(title, message)
    else:
        messagebox.showerror(title,message)


def enter ():
    if (user.get()==user_saved)&(code.get()==code_saved):
        message('Access allowed' , 'You can enter', 1)
    else:
        message('Access denied', 'Try again', 0)
        delete()

def delete ():
    user.set('')
    code.set('')

#Fields
lbl_user = ttk.Label(window, text='User')
lbl_user.grid(row=2, column=2, padx=20, pady=20)
txt_user = ttk.Entry(window, textvariable=user, width=20, justify=tk.RIGHT)
txt_user.grid(row=2, column=3, padx=20, pady=20)

lbl_code = ttk.Label(window, text='Code')
lbl_code.grid(row=3, column=2, padx=20, pady=20)
txt_code = ttk.Entry(window, textvariable=code, width=20, justify=tk.RIGHT, show='*')
txt_code.grid(row=3, column=3, padx=20, pady=20)

#Buttons
btn_enter = ttk.Button(window, text='Enter', command=enter)
btn_enter.grid(row=4, column=2, padx=20, pady=20, ipadx=10, ipady=10)

btn_delete = ttk.Button(window, text='Delete', command=delete)
btn_delete.grid(row=4, column=3, padx=20, pady=20, ipadx=10, ipady=10)















#Always put at the end
window.mainloop()
