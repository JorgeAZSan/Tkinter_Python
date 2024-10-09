import tkinter as tk
from tkinter import ttk, messagebox
from time import sleep

#We create an object of Tk class
window = tk.Tk()

#Size 2
Wide = 500
Height = 400
Size = str(Wide) + "x" + str(Height)
window.geometry(Size)

#Title
window.title('Progress Bar')
#Icon
window.iconbitmap('./Img/Crown.ico')

def start():
    bar.start()
    bar['maximum']=10
    for value in range(11):
        sleep(0.1)
        bar['value'] = value
        bar.update()
    bar['value'] = 0
    bar.stop()

def stop():
    bar.stop()

bar = ttk.Progressbar(window, orient='horizontal', length=450)
bar.grid(row=0, column=1, padx=15, pady=15, columnspan=3)

#Start button
btn_start = ttk.Button(window, text='Start', command=start)
btn_start.grid(row=1, column=2)

#Stop button
btn_stop = ttk.Button(window, text='Stop', command=stop)
btn_stop.grid(row=1, column=3)







#Always put at the end
window.mainloop()
