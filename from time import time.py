from time import *
#for gui components
from tkinter import * 
#for datetime objects
from datetime import datetime
#for timezone conversions
from dateutil import tz
#for time picker
from tkcalendar import *
#for time picker
from tktimepicker import AnalogPicker, AnalogThemes

#top level window
root = Tk()
root.title("Time Zone Comparator")
root.geometry("500x400")

titleLabel = Label(root, text="Time Zone Comparator", font=25)
#string message of first timezone
otherTime = StringVar()
#formatting
otherTimeLabel = Label(root, textvariable=otherTime, font=('Helvetica bold',17))
#placement
otherTimeLabel.grid(row=11, column= 1, columnspan=3)
#second timezone string message to user
anotherTime = StringVar()
#formatting
anotherTimeLabel = Label(root, textvariable=anotherTime, font=('Helvetica bold',17))
#placement in grid
anotherTimeLabel.grid(row=12, column= 1, columnspan=3)
#function when user presses submit button
def comparator():
    #save date selected by user using date picker
    s = cal.get_date()
    t = time_picker.time()
    #parse out month, day, year
    month1 = s.month
    day1 = s.day
    year1 = s.year
    #parse out hour, minute
    hour1 = t[0]
    minute1 = t[1]
    #add 12 hours to evening times
    if t[2] == 'PM':
        hour1 = hour1 + 12
  
    #which menu item/ timezone did user select
    tz1 = tz.gettz(tzSelected.get())
    #get string of selected time zone
    stringtz1 = tzSelected.get()
    #get second time zone that user selected
    tz2 = tz.gettz(tzSelected2.get())
    #put selected time zone into string for message
    stringtz2 = tzSelected2.get()
   
    #create date time object with user inputted values as first time zone
    x = datetime(year1,month1,day1,hour1,minute1).astimezone(tz1)
    #display message to user
    stringXX = x.strftime("If it's %B %d, %Y, @%H:%M HRS in")
    #take first datetime object and translate into second time zone
    xxx = x.astimezone(tz2)
    #string message to user regarding second time zone
    stringXXX = xxx.strftime("Then it's %B %d, %Y, @%H:%M HRS")
    #full messages
    otherTime.set(" " +stringXX +" " +stringtz1)
    anotherTime.set(" "+stringXXX +" in " +stringtz2)
#label for date picker
homeLabel = Label(root, text="Choose date to compare")  
#placement
homeLabel.grid(row=2, column=1, columnspan=2) 
#date picker object
cal=DateEntry(root,selectmode='day',year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, date_pattern='MM/dd/yyyy', foreground="blue")
#placement of date picker
cal.grid(row=2, column=2, columnspan=3, rowspan=3)

changeHourLabel = Label(root, text="Select Time to compare")
changeHourLabel.grid(row=5, column=1, columnspan=2)
#adding built in time picker object
time_picker = AnalogPicker(root)
time_picker.grid(row=5, column=3, columnspan=2)
#timezones for comparison
timeZones = ["America/Montreal", "Asia/Bangkok", "Europe/Paris", "Africa/Algiers", "Israel"]
tzSelected = StringVar()
tzSelected.set(timeZones[0])
#time zone menu
tzMenu = OptionMenu(root, tzSelected, *timeZones )
tzLabel = Label(root, text="Select Home TimeZone")
tzLabel.grid(row=1, column=1, columnspan=2)
tzMenu.grid(row=1, column=3)
#timezone to compare
timeZone2Label = Label(root, text= "Select TimeZone to Compare")
timeZone2Label.grid(row=8, column=1, columnspan=2)
timeZones2 = ["America/Montreal", "Asia/Bangkok", "Europe/Paris", "Africa/Algiers", "Israel"]
tzSelected2 = StringVar()
tzSelected2.set(timeZones2[2])
tzMenu2 = OptionMenu(root, tzSelected2, *timeZones2 )
tzMenu2.grid(row=8, column=3)
#submit button
submitDateTime = Button(root, text="Submit", command=comparator).grid(row=9, column=3)
#run the above code
root.mainloop()