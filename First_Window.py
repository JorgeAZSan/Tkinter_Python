#Libraries
import tkinter as tk
from tkinter import ttk, messagebox
#We create an object of Tk class
window = tk.Tk()
#Size
# window.geometry('800x600') #Wide - Height
#Size 2
Wide = 400
Height = 300
Size = str(Wide) + "x" + str(Height)
window.geometry(Size)


#Title
window.title('Juego De Tronos')
#Icon
window.iconbitmap('./Img/Crown.ico')

#Text one
text1 = ttk.Entry(window, width=40, justify=tk.LEFT)
text1.grid(row=2,column=4, padx=20, pady=10, ipadx=10, ipady=10)
text1.insert(0, 'Chain text for prederminate')

#Others properties
text2 = ttk.Entry(window, width=40, justify=tk.RIGHT, show='*')
text2.grid(row=3,column=4, padx=20, pady=10, ipadx=10, ipady=10)
#Only read
text2.config(state='readonly')

#Click function
def Enter ():
    Message = 'You have found it'
    print (Message)

def Message ():
    Alert = "Hi: " + txtNombre.get(), "This is an avoid, welcome"
    messagebox.showinfo("Alert",Alert)


#First button
button1 = ttk.Button(window, text='Press me', command=Enter)
# button1.pack()
button1.grid(row=5, column=4)

#Second button
button2 = ttk.Button(window, text='Message', command=Message)
# button1.pack()
button2.grid(row=5, column=3)


#Varials
txtNombre = tk.StringVar()
#Tags
lblNombre = ttk.Label(window, text='Nombre')
lblNombre.grid(row=2,column=1, columnspan=2)

lblApellido = ttk.Label(window, text='Apellido')
lblApellido.grid(row=3,column=1, columnspan=2)

#Entry texts
cajaNombre = ttk.Entry(window,width=20, justify=tk.RIGHT)
cajaNombre.grid(row=2,column=3, padx=20, pady=10, ipadx=10, ipady=10)

cajaApellido = ttk.Entry(window,width=20, justify=tk.RIGHT)
cajaApellido.grid(row=3,column=3, padx=30, pady=20, ipadx=10, ipady=10)

#Always put at the end
window.mainloop()