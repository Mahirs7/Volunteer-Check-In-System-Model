# Modules 

from tkinter import *
from tkinter.messagebox import *
import pandas as pd

import datetime

# Lists 
NamesList = []
EmailsList = []
EventTypeList = []
DatesList = []
TimesList = []
TimeCalculateList = []

# Functions

def CheckIn():
    Name = NameEntry.get()
    Email = EmailEntry.get()
    if Name != '' and Email != '':
        NamesList.append(Name)
        EmailsList.append(Email)
        EventTypeList.append('CheckIn')
        DatesList.append(datetime.datetime.now().strftime("%Y-%m-%d"))
        TimesList.append(datetime.datetime.now().strftime("%H:%M:%S"))
        print (NamesList)
        print (EmailsList)
        print (EventTypeList)
        print (DatesList)
        print (TimesList)
        NameVar.set('')
        EmailVar.set('')
    else:
        showinfo('Error', 'Please enter your name and email')



def CheckOut():
    Name = NameEntry.get()
    Email = EmailEntry.get()
    if Name != '' and Email != '':
        NamesList.append(Name)
        EmailsList.append(Email)
        EventTypeList.append('CheckOut')
        DatesList.append(datetime.datetime.now().strftime("%Y-%m-%d"))
        TimesList.append(datetime.datetime.now().strftime("%H:%M:%S"))
        print (NamesList)
        print (EmailsList)
        print (EventTypeList)
        print (DatesList)
        print (TimesList)
        NameVar.set('')
        EmailVar.set('')
    else:
        showinfo('Error', 'Please enter your name and email')

# Setup 
root = Tk()
mainframe = Frame(root)

root.title("Volunteer Check-In System")

# Widgets 

Intro = Label(mainframe, text="Volunteer Portal", font=("Helvetica", 32, "bold"))

NameLabel = Label(mainframe, text="Name:")
NameVar = StringVar()
NameEntry = Entry(mainframe, textvariable=NameVar)

EmailLabel = Label(mainframe, text="Email:")
EmailVar = StringVar()
EmailEntry = Entry(mainframe, textvariable=EmailVar)


CheckInButton = Button(mainframe, text="Check In", command=CheckIn, )
CheckOutButton = Button(mainframe, text="Check Out", command=CheckOut)


# Gridding

mainframe.grid(padx = 20, pady=20)

Intro.grid(row=1, column=1, columnspan=2, pady=20)

NameLabel.grid(row=2, column=1, sticky=W)
NameEntry.grid(row=2, column=2, sticky=W, pady=20)
EmailLabel.grid(row=3, column=1, sticky=W)
EmailEntry.grid(row=3, column=2, sticky=W, pady=20)

CheckInButton.grid(row=4, column=2, sticky=W, pady=20, ipadx=35, ipady=10)
CheckOutButton.grid(row=5, column=2, sticky=W, ipadx=30, ipady=10)

root.mainloop()

# list to csv 

dict = {"Names": NamesList, "Emails": EmailsList, "EventType": EventTypeList, "Dates": DatesList, "Times": TimesList}

df = pd.DataFrame(dict)
df.to_csv('CheckInOut.csv')
