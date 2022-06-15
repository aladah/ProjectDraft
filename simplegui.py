from time import time
#for gui components
from tkinter import * 
#for datetime objects
from datetime import datetime
#for timezone conversions
import pytz
# for time related tasks
import time


#root aspect of gui
root = Tk()
# we want the main display to be 1200x400 pixels in size
root.geometry("1200x400")
#application icon in left corner windows, mac its the icon in bottom bar
image_icon=PhotoImage(file="/Users/aladahmoore/Desktop/ProjectDraft/appIcon.png")
#iconphoto sets title bar icon
#false arg means this only applies to root display
root.iconphoto(False, image_icon)



#function to state time zones for comparison
def times():
  #sets home time zone to bangkok
  home=pytz.timezone("Asia/Bangkok")
  #get local time of bangkok
  local_time=datetime.now(home)
  #formatting time
  #a refers to day, b month, ...
  current_time=local_time.strftime("%a %d %b %Y %H:%M:%S")
  #config method used to access objects attributes after initialization
  #this refers to clock variable in the timezone
  clock.config(text=current_time)
  #this refers to name variable in the timezone
  name.config(text="Bangkok")
  #allows for seconds to cycle
  clock.after(200,times)
  #sets home time zone to bangkok
  home2=pytz.timezone("America/Montreal")
  #get local time of bangkok
  local_time2=datetime.now(home2)
  #formatting time
  #a refers to day, b month, ...
  current_time2=local_time2.strftime("%a %d %b %Y %H:%M:%S")
  #config method used to access objects attributes after initialization
  #this refers to clock variable in the timezone
  clock2.config(text=current_time2)
  #this refers to name variable in the timezone
  name2.config(text="Montreal")
  #allows for seconds to cycle
  clock2.after(200,times)


 
#first time zone
#frame to group timezone info together
f=Frame(root,bd=5)
#place method to place frame inside root
f.place(x=10,y=118,width=250,height=150)
#label is a tkinter widget
#label(parent, options)
name=Label(f,font=("Helvetica", 30,"bold"))
name.place(x=20,y=100)

logo=PhotoImage(file="/Users/aladahmoore/Desktop/ProjectDraft/thail.png")
#label(parent, options)
image_label=Label(root,image=logo)
image_label.place(x=50,y=120)
#creating clock variable
clock=Label(f,font=("Helvetica", 20))
clock.place(x=20,y=80)


#second time zone
#frame to group timezone info together
f2=Frame(root,bd=5)
#place method to place frame inside root
f2.place(x=300,y=118,width=250,height=150)
#label is a tkinter widget
#label(parent, options)
name2=Label(f2,font=("Helvetica", 30,"bold"))
name2.place(x=30,y=100)

logo2=PhotoImage(file="/Users/aladahmoore/Desktop/ProjectDraft/canada.png")
#label(parent, options)
image_label2=Label(root,image=logo2)
image_label2.place(x=310,y=120)
#creating clock variable
clock2=Label(f2,font=("Helvetica", 20))
clock2.place(x=5,y=80)

#selectable time zone
#new frame
f3=Frame(root,bd=5)
f3.grid(column=0,row=0, sticky=(N,W,E,S))
f3.columnconfigure(0, weight = 1)
f3.rowconfigure(0, weight = 1)
f3.pack(pady = 100, padx = 100)
# create tkinter variable
tkvar = StringVar(f3)
#menu choices
choices = {'Choose TimeZone','Paris', 'Zimbabwee'}
#default option
tkvar.set('Choose TimeZone')

popupMenu = OptionMenu(f3, tkvar, *choices)
Label(f3, text="Choose a time zone").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column = 1)

f3.place(x=600,y=118,width=250,height=150)
#label is a tkinter widget
#label(parent, options)
name3=Label(f3,font=("Helvetica", 30,"bold"))
name3.place(x=40,y=100)
#placeholder for image
#logo3=PhotoImage(file)
#creating clock variable
clock3=Label(f3,font=("Helvetica", 20))
clock3.place(x=5,y=80)
#run this function now


#function to change time zone based on user input
def changeTime(value):
  if value=="Paris":
    #sets home time zone to bangkok
    home3=pytz.timezone("Europe/Paris")
    #get local time of bangkok
    local_time3=datetime.now(home3)
    #formatting time
    #a refers to day, b month, ...
    current_time3=local_time3.strftime("%a %b %Y %H:%M:%S")
    #config method used to access objects attributes after initialization
    #this refers to clock variable in the timezone
    #clock3.config(text=current_time3)
    #this refers to name variable in the timezone
    name3.config(text="Paris")
    #allows for seconds to cycle
    #clock3.after(200,times)
  if value=="Zimbabwe":
    #sets home time zone to bangkok
    home3=pytz.timezone("Africa/Harare")
    #get local time of bangkok
    local_time3=datetime.now(home3)
    #formatting time
    #a refers to day, b month, ...
    current_time3=local_time3.strftime("%a %b %Y %H:%M:%S")
    #config method used to access objects attributes after initialization
    #this refers to clock variable in the timezone
    #clock3.config(text=current_time3)
    #this refers to name variable in the timezone
    name3.config(text="Zimbabwee")
    #allows for seconds to cycle
    #clock3.after(200,times)







times()
#tells python to run the tkinter event loop
root.mainloop()
