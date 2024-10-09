import tkinter as tk
from tkinter import ttk, messagebox
#Clase que hereda de la clase tk


class Window(tk.Tk):
    def __init__(self,title,wide,height):
        super().__init__()
        size = wide + 'x' + height
        self.geometry(size)
        self.title(title)
        self._create_button()

    def _create_button(self):
        self.btn_click=ttk.Button(self,text='click', command=self.click)
        self.btn_click.grid(row=3,column=3,padx=20,pady=20, ipadx=10, ipady=10)

    def click(self):
        print ('Has pulsado el boton')



if __name__=='__main__':
    #Title
    title = 'Game Of Thrones 2'
    #Size 
    Wide = str(400)
    Height = str(300)
    Window = Window(title,Wide,Height)    
    #Always put at the end
    Window.mainloop()