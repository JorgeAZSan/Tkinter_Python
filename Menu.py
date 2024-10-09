#Libraries
import tkinter as tk
from tkinter import ttk, Menu
import sys #For leaving of the aplicaction
#We create an object of Tk class
window = tk.Tk()
#Size 
Wide = 400
Height = 300
Size = str(Wide) + "x" + str(Height)
window.geometry(Size)


#Title
window.title('Game Of Thrones')
#Icon
window.iconbitmap('./Img/Crown.ico')

def exit ():
    print ('You have left of the aplication')
    window.quit()#Leave the window
    window.destroy()#Destroy the object created
    sys.exit()#Leave the process


def menu():
    main_menu = Menu(window)
    file_menu = Menu(main_menu, tearoff=0  )#File option
    file_menu.add_command(label='New') 
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=exit) 
    help_menu = Menu(main_menu, tearoff=0) #Help option
    help_menu.add_command(label='About') 
    main_menu.add_cascade(menu=file_menu,label='File')
    main_menu.add_cascade(menu=help_menu,label='Help')
    window.config(menu=main_menu)

menu()


#Always put at the end
window.mainloop()