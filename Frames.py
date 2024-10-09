import tkinter as tk
from tkinter import ttk, Frame, PhotoImage

#We create an object of Tk class
window = tk.Tk()

#Size 2
Wide = 400
Height = 300
Size = str(Wide) + "x" + str(Height)
window.geometry(Size)

#Title
window.title('Frames')
#Icon
window.iconbitmap('./Img/Crown.ico')

#Create frame
frame = Frame(window)

#Position
frame.pack(padx=10,pady=10)
frame.config(bg='lightblue')
frame.config(width=400, height=300)
frame.config(cursor="pirate") # arrow
frame.config(relief="sunken") #relief
frame.config(bd=25)

#image
img = PhotoImage(file='./Img/Owl.png')
lbl_img = ttk.Label(frame, image=img).pack()

















#Always put at the end
window.mainloop()
