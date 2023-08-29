# Import Libraries
from tkinter import *
import datetime
import time
from pygame import mixer
from threading import Thread

#Start library
mixer.init()

#Enter load of music
mixer.music.load("/Users/yusufceker/Desktop/sounds/alarm.mp3")

# Create Main Window
window = Tk()

#Enter title
window.title("Alarm App")

# Set geometry
window.geometry("400x250")
 
#Create a func for threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()

#Create alarm func
def alarm():
    # Infinite Loop for alarm func
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Wait for one seconds
        time.sleep(1)
 
        # Print current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Check whether set alarm is equal to current time
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            mixer.music.play()
#You can create your own label for your app.         
yclabel = Label(window,text="Yusuf Çeker",fg="Red",font=("Comic Sans MS",20,"bold")) 

# Add Labels, Frame, Button, Optionmenus for our app
Label(window,text="Alarm Clock",font=("Helvetica 20 bold"),fg="cyan").pack(pady=10)
Label(window,text="Set Time",font=("Helvetica 15 bold")).pack()

#Create exit func
def exit():
    window.quit()

frame = Frame(window)
frame.pack()

exit_btn = Button(window,text="Exit",fg="red",command=exit)

hour = StringVar(window)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)#create a optionmenu for
hrs.pack(side=LEFT)
 
minute = StringVar(window)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)#create a option menu for minutes
mins.pack(side=LEFT)
 
second = StringVar(window)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)#create a optionmenu for seconds
secs.pack(side=LEFT)
 
Button(window,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)

yclabel.pack()
exit_btn.pack()
window.mainloop()