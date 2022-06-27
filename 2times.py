from time import time
#for gui components
from tkinter import * 
#for datetime objects
from datetime import datetime
import tkinter
#for timezone conversions
import pytz
# for time related tasks
import time
# to use file paths 
from PIL import Image, ImageTk

#top level window
root = Tk()

L1 = Label(root, text= "If its ")
L1.grid(row=2, column=1)
L3 = Label(root, text = "in")
L3.grid(row=2, column=3)
L2 = Label(root, text = "Then its ")
L2.grid(row=2, column=5)
L4 = Label(root, text = "in")
L4.grid(row=2, column=7)
#list of time zones, when initialized objects add self to list
timeZoneList = []
#just names in an array
timeZoneNames = []

#class for timezone Objects
class timeZone:
    
    #when object created initialization code
    def __init__(self, home, logo):
        self.home=home
        self.local_time=datetime.now(home)
        self.current_time=datetime.now(home).strftime("%a %b %Y %H:%M:%S")
        self.name=home
        self.logo=logo
        timeZoneList.append(self)
        timeZoneNames.append(self.name)

#called when item selected from menu       
def getZone():
    #if a .get() returns a value
    if selectedTimeZone1.get():
        #check if selection matches a list item
        for z in timeZoneList:
            
            if str(z.name) == selectedTimeZone1.get():
                #set variables to timezone attributes
                title1.set(z.name)
                time1.set(z.current_time)
                #change cuurent icon
                logos=ImageTk.PhotoImage(file=z.logo)
                #change variable in label
                logoLabel1.config(image=logos)
                #must keep a reference to change icon picture not sure why
                logoLabel1.photo_ref = logos
    
    #if a .get() returns a value
    if selectedTimeZone2.get():
        #check if selection matches a list item
        for z in timeZoneList:
            
            if str(z.name) == selectedTimeZone2.get():
                #set variables to timezone attributes
                title2.set(z.name)
                time2.set(z.current_time)
                #change cuurent icon
                logos2=ImageTk.PhotoImage(file=z.logo)
                #change variable in label
                logoLabel2.config(image=logos2)
                #must keep a reference to change icon picture not sure why
                logoLabel2.photo_ref = logos2
    
                


#create timeZone objects
timeZone(pytz.timezone("Europe/Berlin"), "/Users/aladahmoore/Desktop/ProjectDraft/germany.png")
timeZone(pytz.timezone("Asia/Bangkok"), "/Users/aladahmoore/Desktop/ProjectDraft/thail.png")
timeZone(pytz.timezone("America/Montreal"), "/Users/aladahmoore/Desktop/ProjectDraft/canada.png")
timeZone(pytz.timezone("Europe/Madrid"), "/Users/aladahmoore/Desktop/ProjectDraft/spain.png")
timeZone(pytz.timezone("America/Vancouver"), "/Users/aladahmoore/Desktop/ProjectDraft/canada.png")


#create variable to hold selected menu item
selectedTimeZone1 = StringVar()
#set default to an array item
selectedTimeZone1.set(timeZoneNames[2])
#variable for title
title1 = StringVar()
titleLabel1 = Label(root, textvariable=title1)
titleLabel1.grid(row=2, column=4)
#variable for time
time1 = StringVar()
timeLabel1 = Label(root, textvariable=time1)
timeLabel1.grid(row=2, column=2)
#variable for logo
logologo1=PhotoImage(file="/Users/aladahmoore/Desktop/ProjectDraft/hk.png")
logoLabel1=Label(root, image=logologo1)
logoLabel1.grid(row=3, column=2)
#create menu atttached to root, picked item is held in what variable, and displays array timeZoneNames
timeZoneMenu1 = OptionMenu(root, selectedTimeZone1, *timeZoneNames)
timeZoneMenu1.grid(row=4, column=2)
#button
#select button to submit menu item choices
selectButton1 = tkinter.Button(root, text='Submit', command=getZone)
selectButton1.config(width=20, height=2)
selectButton1.grid(row=5, column=2)

#create variable to hold selected menu item
selectedTimeZone2 = StringVar()
#set default to an array item
selectedTimeZone2.set(timeZoneNames[1])
#variable for title
title2 = StringVar()
titleLabel2 = Label(root, textvariable=title2)
titleLabel2.grid(row=2, column=8)
#variable for time
time2 = StringVar()
timeLabel2 = Label(root, textvariable=time2)
timeLabel2.grid(row=2, column=6)
#variable for logo
logologo2=PhotoImage(file="/Users/aladahmoore/Desktop/ProjectDraft/hk.png")
logoLabel2=Label(root, image=logologo2)
logoLabel2.grid(row=3, column=6)
#create menu atttached to root, picked item is held in what variable, and displays array timeZoneNames
timeZoneMenu2 = OptionMenu(root, selectedTimeZone2, *timeZoneNames)
timeZoneMenu2.grid(row=4, column=6)
#button
#select button to submit menu item choices
selectButton2 = tkinter.Button(root, text='Submit', command=getZone)
selectButton2.config(width=20, height=2)
selectButton2.grid(row=5, column=6)
#run the main window until user exits
root.mainloop()