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

#Always put at the end
window.mainloop()
