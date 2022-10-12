from tkinter import Label, Tk
import time
import pytz
from datetime import datetime
from os import times

app_window = Tk()
app_window.title("Sk's Digital Clock")
app_window.geometry("600x380")
app_window.configure(background='yellow')
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "yellow"
foreground= "#363529"
border_width = 25

current_time_label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
current_time_label.grid(row=0, column=1)

def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   current_time_label.config(text=time_live)
   current_time_label.after(200, digital_clock)



def get_time():
    home = pytz.timezone('Asia/Kolkata')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    name.config(text="India")
    clock.after(50, get_time)

    home = pytz.timezone('Africa/timbuktu')
    local_time = datetime.now(home)
    Current_time = local_time.strftime('%H:%M:%S')
    clock2.config(text=Current_time)
    name2.config(text="South Africa")
    clock.after(50, times)

    home = pytz.timezone('America/New_york')
    local_time = datetime.now(home)
    Current_time = local_time.strftime('%H:%M:%S')
    clock3.config(text=Current_time)
    name3.config(text="USA")
    clock.after(50, times)

    home = pytz.timezone('Australia/Victoria')
    local_time = datetime.now(home)
    Current_time = local_time.strftime('%H:%M:%S')
    clock4.config(text=Current_time)
    name4.config(text="Australia")
    clock.after(50, times)


name = Label(app_window, text="india", font=("time", 20, "bold"),bg='yellow')
name.grid(row=2,column=1)
clock = Label(app_window, font=("time", 25, "bold"), bg='yellow')
clock.grid(row=3, column=1)
note = Label(app_window, text="Hours minutes seconds", font=("time 10 bold"),bg='yellow')
note.grid(row=4,column=1)

name2 = Label(app_window, text="Africa", font=("time", 20, "bold"),bg='yellow')
name2.grid(row=2, column=2)
clock2 = Label(app_window, font=("time", 25, "bold"),bg='yellow')
clock2.grid(row=3, column=2)
note2 = Label(app_window, text="Hours minutes seconds", font=("time 10 bold"),bg='yellow')
note2.grid(row=4, column=2)

name3 = Label(app_window, text="America", font=("time", 20, "bold"),bg='yellow')
name3.grid(row=5,column=1)
clock3 = Label(app_window, font=("time", 25, "bold"),bg='yellow')
clock3.grid(row=6,column=1)
note13 = Label(app_window, text="Hours minutes seconds", font=("time 10 bold"),bg='yellow')
note13.grid(row=7,column=1)

name4 = Label(app_window, text="Australia/Victoria", font=("time", 20, "bold"),bg='yellow')
name4.grid(row=5,column=2)
clock4 = Label(app_window, font=("time", 25, "bold"),bg='yellow')
clock4.grid(row=6,column=2)
note14 = Label(app_window, text="Hours minutes seconds", font=("time 10 bold"),bg='yellow')
note14.grid(row=7,column=2)


get_time()
digital_clock()
app_window.mainloop()
