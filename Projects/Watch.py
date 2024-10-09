import tkinter as tk
from tkinter import messagebox, simpledialog
import time

class Digitalwatch:
    def __init__(self, window):
        self.window = window
        self.window.title('Digital Watch')
        self.window.geometry("300x200")

        #Time tag
        self.lbl_time=tk.Label(window, text="", font=("Arial",24))
        self.lbl_time.pack(pady=20)

        #Cronometer´s buttons
        self.btn_startCronometer = tk.Button(window, text="Start Cronometer", command=self.start_cronometer)
        self.btn_startCronometer.pack()
        self.btn_stopCronometer = tk.Button(window, text="Stop Cronometer", command=self.stop_cronometer, state="disabled")
        self.btn_stopCronometer.pack()

        #Alarm's buttons
        self.btn_setAlarm = tk.Button(window, text="Set the alarm Up", command=self.setupAlarm)
        self.btn_setAlarm.pack()
        self.btn_activeAlarm = tk.Button(window, text="Active alarm", command=self.activeAlarm, state="disabled")
        self.btn_activeAlarm.pack()

        #Cronometer varial state
        self.activeCronometer = False
    

    def start_watch(self):
        if self.activeCronometer==False:
            current_date = time.strftime("%H:%M:%S")
            self.lbl_time.config(text=current_date)
            self.lbl_time.after(1000, self.start_watch)

    def start_cronometer(self):
        self.start_time = time.time()
        self.btn_startCronometer.config(state="disabled")
        self.btn_stopCronometer.config(state="normal")
        self.activeCronometer = True
        self.updateCronometer()


    def stop_cronometer(self):
        self.btn_startCronometer.config(state="normal")
        self.btn_stopCronometer.config(state="disabled")
        self.activeCronometer=False
        self.start_watch()

    def updateCronometer(self):
        if self.activeCronometer:
            time_transcurrido = time.time() - self.start_time
            format_time = time.strftime("%H:%M:%S", time.gmtime(time_transcurrido))
            self.lbl_time.config(text=format_time)
            self.lbl_time.after(1000, self.updateCronometer)

    def setupAlarm(self):
        self.time_alarm = tk.simpledialog.askstring("Set alarm up", "Introduce the alarm's time (format: HH:MM )")
        self.btn_activeAlarm.config(state="normal")

    def activeAlarm(self):
        current_time = time.strftime("%H:%M")
        if current_time == self.time_alarm:
            messagebox.showinfo("Alarm", "It's the time you set up")
            self.btn_activeAlarm.config(state="disabled")
        else:
            self.window.after(60000, self.activeAlarm)




if __name__ == "__main__":
    window = tk.Tk()
    digitalwatch = Digitalwatch(window)
    digitalwatch.start_watch()
    window.mainloop()