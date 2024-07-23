from tkinter import *
from tkinter import ttk
import datetime
import time
import winsound
from tkinter.messagebox import showinfo
from threading import *

#main wndow that will hold all the widgets
main_window= Tk()
main_window.title("Python Alarm Clock")

#main window will contain five columns of equal widths
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)
main_window.columnconfigure(3, weight=1)

# creating a label for title and attaching it the main window
my_label= Label(main_window, text = "Python Alarm Clock",bg="#b3b3b3",fg="#ff3300", font=("Courier",20))
my_label.grid(row=0, column=1,columnspan=3,padx=5,pady=5)
# creating a label for a message and attaching it the main window
my_labe2 = Label(main_window, text ="Set Time\n(24hFormat)",bg="#cccccc",fg="#3399ff", font=("Courier",20))
my_labe2.grid(row=1, column=2,padx=5,pady=5)

# creating a label for hours and attaching it the main window
lbl_hours= Label(main_window, text ="Hour",bg="#6699ff",fg="#595959",font=("Courier",14))
lbl_hours.grid(row=2, column=1,padx=5,pady=5)

# creating a label for minutes and attaching it the main window
lbl_mins= Label(main_window, text ="Minutes",bg="#6699ff",fg="#595959",font=("Courier",14))
lbl_mins.grid(row=2, column=2,padx=5,pady=5)

# creating a label for seconds and attaching it the main window
lbl_sec= Label(main_window, text ="Seconds",bg="#6699ff",fg="#595959",font=("Courier",14))
lbl_sec.grid(row=2, column=3,padx=5,pady=5)

# creating a text field for hours and #attaching it to the main window
txt_hours=StringVar()
tf_hours=ttk.Entry(main_window,textvariable=txt_hours)
tf_hours.grid(row=3, column=1,padx=15,pady=15)
# creating a text field for minutes and #attaching it to the main window
txt_mins=StringVar()
tf_mins=ttk.Entry(main_window,textvariable=txt_mins)
tf_mins.grid(row=3, column=2,padx=15,pady=15)
# creating a text field for minutes and #attaching it to the main window
txt_sec=StringVar()
tf_se=ttk.Entry(main_window,textvariable=txt_sec)
tf_se.grid(row=3, column=3,padx=15,pady=15)

def set_alarm():
    while True:
        # Set Alarm
        alarm_time= f"{txt_hours.get()}:{txt_mins.get()}:{txt_mins.get()}"
        # get current time after every 1 second
        time.sleep(1)
        # get time in hours minutes and seconds format
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        # print current time in a text field
        txt_ct.set(current_time)
        # Check if current system time is equal to the alarm time
        if current_time==alarm_time:
        # playing sound
            winsound.PlaySound('E:/Datasets/siren.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)

def start_alarm_thread():
    t1=Thread(target=set_alarm)
    t1.start()


#creating a button for setting an alarm and attaching it to the main window
btn_Set_alarm = Button(main_window,text = "SET ALARM", bg = "#ff9966", fg = "#595959",font =("Courier",14),command = start_alarm_thread)
btn_Set_alarm.grid(row = 4, column = 1,columnspan = 3, padx = 5, pady = 5)

# creating a label for seconds and attaching it the main window
lbl_ct= Label(main_window, text ="Currenttime",bg="#6699ff",fg="#595959", font=("Courier",10))
lbl_ct.grid(row=5, column=1,padx=5,pady=5)
# creating a text field for minutes and attaching it to the main window
txt_ct=StringVar()
tf_ct=ttk.Entry(main_window,textvariable=txt_ct, width=20)
tf_ct.grid(row=5, column=2,padx=15,pady=15)

# displaying the main window
main_window.mainloop()