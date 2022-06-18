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
    
    if selectedTimeZone.get():
        #check if selection matches a list item
        for z in timeZoneList:
            
            if str(z.name) == selectedTimeZone.get():
                #set variables to timezone attributes
                title.set(z.name)
                time.set(z.current_time)
                #change cuurent icon
                logos=ImageTk.PhotoImage(file=z.logo)
                #change variable in label
                logoLabel.config(image=logos)
                #must keep a reference to change icon picture not sure why
                logoLabel.photo_ref = logos
            

#main container aspect of gui
root = Tk()
# we want the main display to be x pixels in size
root.geometry("300x300")
root.title("Project TZ Comparator")

#list of time zones, when initialized objects add self to list
timeZoneList = []
#just names in an array
timeZoneNames = []

#create timeZone objects
timeZone(pytz.timezone("Europe/Berlin"), "/Users/aladahmoore/Desktop/ProjectDraft/germany.png")
timeZone(pytz.timezone("Asia/Bangkok"), "/Users/aladahmoore/Desktop/ProjectDraft/thail.png")
timeZone(pytz.timezone("America/Montreal"), "/Users/aladahmoore/Desktop/ProjectDraft/canada.png")
timeZone(pytz.timezone("Europe/Madrid"), "/Users/aladahmoore/Desktop/ProjectDraft/thail.png")
timeZone(pytz.timezone("America/Vancouver"), "/Users/aladahmoore/Desktop/ProjectDraft/thail.png")

#create variable to hold selected menu item
selectedTimeZone = StringVar()
#set default to an array item
selectedTimeZone.set(timeZoneNames[1])
#create menu atttached to root, picked item is held in what variable, and displays array timeZoneNames
timeZoneMenu = OptionMenu(root, selectedTimeZone, *timeZoneNames)
#display the menu
timeZoneMenu.pack()
#variable for title
title = StringVar()
titleLabel = Label(root, textvariable=title)
#display the title
titleLabel.pack()
#variable for time
time = StringVar()
timeLabel = Label(root, textvariable=time)
#display the time
timeLabel.pack()
#variable for logo
logologo=PhotoImage(file="/Users/aladahmoore/Desktop/ProjectDraft/hk.png")
logoLabel=Label(root, image=logologo)
#display the logo
logoLabel.pack()

#select button to submit menu item choices
selectButton = tkinter.Button(root, text='Submit', command=getZone)
selectButton.config(width=20, height=2)
selectButton.pack()
#run the main window until user exits
root.mainloop()

