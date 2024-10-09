#Libraries
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

#Tab instance
control_tab = ttk.Notebook(window)

#First tab
tab01 = ttk.Frame(control_tab)
control_tab.add(tab01, text='Tab 01')
control_tab.pack(fill='both') #Fill the space
txt_nombre = ttk.Entry(tab01, width=40)
txt_nombre.grid(row=0, column=0, padx=10, pady=10)

#Second tab
tab02 = ttk.Labelframe(control_tab, text='Tab with tag')
control_tab.add(tab02, text='tab 02')
txt_nombre = ttk.Entry(tab02, width=40)
txt_nombre.grid(row=1, column=0, padx=10, pady=10)
btn_press = ttk.Button(tab02, text='Press')
btn_press.grid(row=0, column=0, padx=10, pady=10)

#Always put at least
window.mainloop()