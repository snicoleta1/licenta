from tkinter import *
from tkinter import ttk
import actions as act
import pandas as pd
from tkcalendar import Calendar,DateEntry
from ttkthemes import ThemedStyle
import tkinter.font as font
import matplotlib.pyplot as plt
import datetime
import requests, json 
import pyowm
import tkinter.font as font

import time
import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS

data = pd.read_csv("date.csv", sep=',')
dataDf = pd.DataFrame(data)

window = Tk()
window.geometry("1360x800")
window['background']='#B7FCF8'
window.title("Health Indicator")


lbl = Label(window, text="Welcome to Health Indicator", font=("Arial Bold", 25), bg='#B7FCF8')
lbl.config(anchor=CENTER)
lbl.grid(column=1, row=0)

myFont = font.Font(size=40)

def clicked():
	lbl.configure(text="Button was clicked !!")

#######HEALTH_START###############	

def getHealth():
	windowHealth = Toplevel(window)
	windowHealth.geometry("700x700")
	windowHealth['background']='#B7FCF8'

	lblHealthTitle = Label(windowHealth, text="Health", bg='#B7FCF8', font=("Arial Bold", 30))
	lblHealthTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblHealth = Label(windowHealth, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblHealth.place(relx=0.5, rely=0.4, anchor=CENTER)

	lblHealthCustom = Label(windowHealth, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblHealthCustom.place(relx=0.5, rely=0.95, anchor=CENTER)

	health = StringVar(windowHealth)
	health.set("Choose day")

	w = OptionMenu(windowHealth, health, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date = cal.get_date().split("/")
		dateS = int(date[1]) + 2
		data = dataDf.at[dateS, 'health']
		lblHealthCustom.config(text="Your health was " + data)

	def callback(*args):
		if health.get() == 'Today':
			lblHealth.config(text="Your health is " + dataDf.at[0, 'health'])
		if health.get() == 'Yesterday':
			lblHealth.config(text="Your health was " + dataDf.at[1, 'health'])
		if health.get() == 'Custom':
			cal.place(relx=0.35, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	health.trace("w", callback)

	cal = Calendar(windowHealth, selectmode="day", year=2020)
	buttonCalendar = Button(windowHealth, text = "Check Health", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonHealth = Button(window, text="Health", height=2, width=12,
	bg = '#E7C7FC', command=getHealth)
buttonHealth['font'] = myFont
buttonHealth.grid(column=0, row=3)

#########HEALTH_END#############



########PULSE_START############

def getPulse():
	windowpulse = Toplevel(window)
	windowpulse.geometry("700x700")
	windowpulse['background']='#B7FCF8'

	lblpulseTitle = Label(windowpulse, text="Pulse", bg='#B7FCF8', font=("Arial Bold", 30))
	lblpulseTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblpulse = Label(windowpulse, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblpulse.place(relx=0.5, rely=0.4, anchor=CENTER)

	pulse = StringVar(windowpulse)
	pulse.set("Choose day")

	w = OptionMenu(windowpulse, pulse, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date1 = cal1.get_date().split("/")
		dateS1 = int(date1[1])
		date2 = cal2.get_date().split("/")
		dateS2 = int(date2[1])
		datePulse = []
		for x in range(dateS1, dateS2):
			datePulse.append(dataDf.at[x + 2, 'pulse'])
		plt.plot(range(dateS1, dateS2), datePulse)
		plt.show()

	def callback(*args):
		if pulse.get() == 'Today':
			lblpulse.config(text="Your pulse is " + str(dataDf.at[0, 'pulse']))
		if pulse.get() == 'Yesterday':
			lblpulse.config(text="Your pulse was " + str(dataDf.at[1, 'pulse']))
		if pulse.get() == 'Custom':
			cal1.place(relx=0.15, rely=0.45)
			cal2.place(relx=0.55, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	pulse.trace("w", callback)

	cal1 = Calendar(windowpulse, selectmode="day", year=2020)
	cal2 = Calendar(windowpulse, selectmode="day", year=2020)
	buttonCalendar = Button(windowpulse, text = "Check Pulse", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonPulse = Button(window, text="Pulse", height=2, width=12,
	bg = '#E7C7FC', command=getPulse)
buttonPulse['font'] = myFont
buttonPulse.grid(column=1, row=3)

########PULSE_END############


########DBP_START############

def getDBP():
	windowDBP = Toplevel(window)
	windowDBP.geometry("700x700")
	windowDBP['background']='#B7FCF8'

	lblDBPTitle = Label(windowDBP, text="Diastolic Blood Pressure", bg='#B7FCF8', font=("Arial Bold", 30))
	lblDBPTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblDBP = Label(windowDBP, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblDBP.place(relx=0.5, rely=0.4, anchor=CENTER)

	DBP = StringVar(windowDBP)
	DBP.set("Choose day")

	w = OptionMenu(windowDBP, DBP, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date1 = cal1.get_date().split("/")
		dateS1 = int(date1[1])
		date2 = cal2.get_date().split("/")
		dateS2 = int(date2[1])
		dateDBP = []
		for x in range(dateS1, dateS2):
			dateDBP.append(dataDf.at[x + 2, 'diastolic_pressure'])
		plt.plot(range(dateS1, dateS2), dateDBP)
		plt.show()

	def callback(*args):
		if DBP.get() == 'Today':
			lblDBP.config(text="Your Diastolic Blood Pressure is " + str(dataDf.at[0, 'diastolic_pressure']))
		if DBP.get() == 'Yesterday':
			lblDBP.config(text="Your Diastolic Blood Pressure was " + str(dataDf.at[1, 'diastolic_pressure']))
		if DBP.get() == 'Custom':
			cal1.place(relx=0.15, rely=0.45)
			cal2.place(relx=0.55, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	DBP.trace("w", callback)

	cal1 = Calendar(windowDBP, selectmode="day", year=2020)
	cal2 = Calendar(windowDBP, selectmode="day", year=2020)
	buttonCalendar = Button(windowDBP, text = "Check Diastolic Blood Pressure", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

#buttonDBP = Button(window, text="Diastolic Blood Pressure", height = 6, width = 44, bg = '#E7C7FC', command=getDBP)
#buttonDBP.grid(column=2, row=3)

buttonDBP = Button(window, text="Diastolic \nBlood Pressure", height=2, width=12,
	bg = '#E7C7FC', command=getDBP)
buttonDBP['font'] = myFont
buttonDBP.grid(column=2, row=3)

########DBP_END############


########SBP_START############

def getSBP():
	windowSBP = Toplevel(window)
	windowSBP.geometry("700x700")
	windowSBP['background']='#B7FCF8'

	lblSBPTitle = Label(windowSBP, text="Systolic Blood Pressure", bg='#B7FCF8', font=("Arial Bold", 30))
	lblSBPTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblSBP = Label(windowSBP, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblSBP.place(relx=0.5, rely=0.4, anchor=CENTER)

	SBP = StringVar(windowSBP)
	SBP.set("Choose day")

	w = OptionMenu(windowSBP, SBP, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date1 = cal1.get_date().split("/")
		dateS1 = int(date1[1])
		date2 = cal2.get_date().split("/")
		dateS2 = int(date2[1])
		dateSBP = []
		for x in range(dateS1, dateS2):
			dateSBP.append(dataDf.at[x + 2, 'systolic_pressure'])
		plt.plot(range(dateS1, dateS2), dateSBP)
		plt.show()

	def callback(*args):
		if SBP.get() == 'Today':
			lblSBP.config(text="Your Systolic Blood Pressure is " + str(dataDf.at[0, 'systolic_pressure']))
		if SBP.get() == 'Yesterday':
			lblSBP.config(text="Your Systolic Blood Pressure was " + str(dataDf.at[1, 'systolic_pressure']))
		if SBP.get() == 'Custom':
			cal1.place(relx=0.15, rely=0.45)
			cal2.place(relx=0.55, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	SBP.trace("w", callback)

	cal1 = Calendar(windowSBP, selectmode="day", year=2020)
	cal2 = Calendar(windowSBP, selectmode="day", year=2020)
	buttonCalendar = Button(windowSBP, text = "Check Systolic Blood Pressure", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonSBP = Button(window, text="Systolic \nBlood Pressure", height=2, width=12,
	bg = '#E7C7FC', command=getSBP)
buttonSBP['font'] = myFont
buttonSBP.grid(column=0, row=4)

########SBP_END############


########STEPS_START############

def getSteps():
	windowSteps = Toplevel(window)
	windowSteps.geometry("700x700")
	windowSteps['background']='#B7FCF8'

	lblStepsTitle = Label(windowSteps, text="Steps", bg='#B7FCF8', font=("Arial Bold", 30))
	lblStepsTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblSteps = Label(windowSteps, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblSteps.place(relx=0.5, rely=0.4, anchor=CENTER)

	Steps = StringVar(windowSteps)
	Steps.set("Choose day")

	w = OptionMenu(windowSteps, Steps, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date1 = cal1.get_date().split("/")
		dateS1 = int(date1[1])
		date2 = cal2.get_date().split("/")
		dateS2 = int(date2[1])
		dateSteps = []
		for x in range(dateS1, dateS2):
			dateSteps.append(dataDf.at[x + 2, 'steps'])
		plt.plot(range(dateS1, dateS2), dateSteps)
		plt.show()

	def callback(*args):
		if Steps.get() == 'Today':
			lblSteps.config(text="Your step number is " + str(dataDf.at[0, 'steps']))
		if Steps.get() == 'Yesterday':
			lblSteps.config(text="Your step number was " + str(dataDf.at[1, 'steps']))
		if Steps.get() == 'Custom':
			cal1.place(relx=0.15, rely=0.45)
			cal2.place(relx=0.55, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	Steps.trace("w", callback)

	cal1 = Calendar(windowSteps, selectmode="day", year=2020)
	cal2 = Calendar(windowSteps, selectmode="day", year=2020)
	buttonCalendar = Button(windowSteps, text = "Check Steps", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonSteps = Button(window, text="Steps", height=2, width=12,
	bg = '#E7C7FC', command=getSteps)
buttonSteps['font'] = myFont
buttonSteps.grid(column=1, row=4)

########STEPS_END############


########SLEEP_START############

def getSleep():
	windowSleep = Toplevel(window)
	windowSleep.geometry("700x700")
	windowSleep['background']='#B7FCF8'

	lblSleepTitle = Label(windowSleep, text="Sleep", bg='#B7FCF8', font=("Arial Bold", 30))
	lblSleepTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblSleep = Label(windowSleep, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblSleep.place(relx=0.5, rely=0.4, anchor=CENTER)

	Sleep = StringVar(windowSleep)
	Sleep.set("Choose day")

	w = OptionMenu(windowSleep, Sleep, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date1 = cal1.get_date().split("/")
		dateS1 = int(date1[1])
		date2 = cal2.get_date().split("/")
		dateS2 = int(date2[1])
		dateSleep = []
		for x in range(dateS1, dateS2):
			dateSleep.append(dataDf.at[x + 2, 'sleep'])
		plt.plot(range(dateS1, dateS2), dateSleep)
		plt.show()

	def callback(*args):
		if Sleep.get() == 'Today':
			lblSleep.config(text="Your number of sleep hours is " + str(dataDf.at[0, 'sleep']))
		if Sleep.get() == 'Yesterday':
			lblSleep.config(text="Your number of sleep hours was " + str(dataDf.at[1, 'sleep']))
		if Sleep.get() == 'Custom':
			cal1.place(relx=0.15, rely=0.45)
			cal2.place(relx=0.55, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	Sleep.trace("w", callback)

	cal1 = Calendar(windowSleep, selectmode="day", year=2020)
	cal2 = Calendar(windowSleep, selectmode="day", year=2020)
	buttonCalendar = Button(windowSleep, text = "Check Sleep", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonSleep = Button(window, text="Sleep", height=2, width=12,
	bg = '#E7C7FC', command=getSleep)
buttonSleep['font'] = myFont
buttonSleep.grid(column=2, row=4)
########SLEEP_END############

########WEIGHT_START############

def getWeight():
	windowWeight = Toplevel(window)
	windowWeight.geometry("700x700")
	windowWeight['background']='#B7FCF8'

	lblWeightTitle = Label(windowWeight, text="Weight", bg='#B7FCF8', font=("Arial Bold", 30))
	lblWeightTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblWeight = Label(windowWeight, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblWeight.place(relx=0.5, rely=0.4, anchor=CENTER)

	Weight = StringVar(windowWeight)
	Weight.set("Choose day")

	w = OptionMenu(windowWeight, Weight, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date1 = cal1.get_date().split("/")
		dateS1 = int(date1[1])
		date2 = cal2.get_date().split("/")
		dateS2 = int(date2[1])
		dateWeight = []
		for x in range(dateS1, dateS2):
			dateWeight.append(dataDf.at[x + 2, 'weight'])
		plt.xlabel('Time')
		plt.ylabel('Weight')
		plt.title('Weight')
		plt.plot(range(dateS1, dateS2), dateWeight)
		plt.show()

	def callback(*args):
		if Weight.get() == 'Today':
			lblWeight.config(text="Your weight is " + str(dataDf.at[0, 'weight']))
		if Weight.get() == 'Yesterday':
			lblWeight.config(text="Your weight was " + str(dataDf.at[1, 'weight']))
		if Weight.get() == 'Custom':
			cal1.place(relx=0.15, rely=0.45)
			cal2.place(relx=0.55, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	Weight.trace("w", callback)

	cal1 = Calendar(windowWeight, selectmode="day", year=2020)
	cal2 = Calendar(windowWeight, selectmode="day", year=2020)
	buttonCalendar = Button(windowWeight, text = "Check Weight", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonWeight = Button(window, text="Weight", height=2, width=12,
	bg = '#E7C7FC', command=getWeight)
buttonWeight['font'] = myFont
buttonWeight.grid(column=0, row=5)

########WEIGHT_END############

########PLANS_START############

def getPlans():
	windowPlans = Toplevel(window)
	windowPlans.geometry("700x700")
	windowPlans['background']='#B7FCF8'

	lblPlansTitle = Label(windowPlans, text="Plans", bg='#B7FCF8', font=("Arial Bold", 30))
	lblPlansTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblPlans = Label(windowPlans, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblPlans.place(relx=0.5, rely=0.4, anchor=CENTER)

	lblPlansCustom = Label(windowPlans, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblPlansCustom.place(relx=0.5, rely=0.95, anchor=CENTER)

	Plans = StringVar(windowPlans)
	Plans.set("Choose day")

	w = OptionMenu(windowPlans, Plans, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date = cal.get_date().split("/")
		dateS = int(date[1]) + 2
		data = dataDf.at[dateS, 'plans']
		lblPlansCustom.config(text="Your plans are: " + data)

	def callback(*args):
		if Plans.get() == 'Today':
			lblPlans.config(text="Your plans are: " + dataDf.at[0, 'plans'])
		if Plans.get() == 'Yesterday':
			lblPlans.config(text="Your plans were: " + dataDf.at[1, 'plans'])
		if Plans.get() == 'Custom':
			cal.place(relx=0.35, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	Plans.trace("w", callback)

	cal = Calendar(windowPlans, selectmode="day", year=2020)
	buttonCalendar = Button(windowPlans, text = "Check Plans", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonPlans = Button(window, text="Plans", height=2, width=12,
	bg = '#E7C7FC', command=getPlans)
buttonPlans['font'] = myFont
buttonPlans.grid(column=1, row=5)

########PLANS_END############


########MEETINGS_START############

def getMeetings():
	windowMeetings = Toplevel(window)
	windowMeetings.geometry("700x700")
	windowMeetings['background']='#B7FCF8'

	lblMeetingsTitle = Label(windowMeetings, text="Meetings", bg='#B7FCF8', font=("Arial Bold", 30))
	lblMeetingsTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblMeetings = Label(windowMeetings, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblMeetings.place(relx=0.5, rely=0.4, anchor=CENTER)

	lblMeetingsCustom = Label(windowMeetings, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblMeetingsCustom.place(relx=0.5, rely=0.95, anchor=CENTER)

	Meetings = StringVar(windowMeetings)
	Meetings.set("Choose day")

	w = OptionMenu(windowMeetings, Meetings, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date = cal.get_date().split("/")
		dateS = int(date[1]) + 2
		data = dataDf.at[dateS, 'meetings']
		lblMeetingsCustom.config(text="Your meetings are: " + data)

	def callback(*args):
		if Meetings.get() == 'Today':
			lblMeetings.config(text="Your meetings are: " + dataDf.at[0, 'meetings'])
		if Meetings.get() == 'Yesterday':
			lblMeetings.config(text="Your meetings were: " + dataDf.at[1, 'meetings'])
		if Meetings.get() == 'Custom':
			cal.place(relx=0.35, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	Meetings.trace("w", callback)

	cal = Calendar(windowMeetings, selectmode="day", year=2020)
	buttonCalendar = Button(windowMeetings, text = "Check Meetings", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonMeetings = Button(window, text="Meetings", height=2, width=12,
	bg = '#E7C7FC', command=getMeetings)
buttonMeetings['font'] = myFont
buttonMeetings.grid(column=2, row=5)

########MEETINGS_END############


########TIME_START############

def getTime():
	windowTime = Toplevel(window)
	windowTime.geometry("700x500")
	windowTime['background']='#B7FCF8'

	currentDT = datetime.datetime.now()

	lblTime= Label(windowTime, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 12))
	lblTime.place(relx=0.25, rely=0.3, anchor=CENTER)

	lblDay= Label(windowTime, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 12))
	lblDay.place(relx=0.65, rely=0.3, anchor=CENTER)

	lblMonth= Label(windowTime, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 12))
	lblMonth.place(relx=0.25, rely=0.7, anchor=CENTER)

	lblYear= Label(windowTime, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 12))
	lblYear.place(relx=0.65, rely=0.7, anchor=CENTER)

	def getTime():
		lblTime.config(text="It's " + str(currentDT.strftime("%H:%M:%S")))

	def getDay():
		lblDay.config(text="It's " + str(currentDT.strftime("%Y/%m/%d")))

	def getMonth():
		lblMonth.config(text="It's " + datetime.datetime.now().strftime("%B"))

	def getYear():
		lblYear.config(text="It's %d" % currentDT.year)

	buttonTime = Button(windowTime, text = "Check Time", bg='#E7C7FC', command=getTime)
	buttonTime.config(height=3, width=25)
	buttonTime.place(relx=0.15, rely = 0.1)

	buttonDay = Button(windowTime, text = "Check Day", bg='#E7C7FC', command=getDay)
	buttonDay.config(height=3, width=25)
	buttonDay.place(relx=0.55, rely = 0.1)

	buttonMonth = Button(windowTime, text = "Check Month", bg='#E7C7FC', command=getMonth)
	buttonMonth.config(height=3, width=25)
	buttonMonth.place(relx=0.15, rely = 0.5)

	buttonYear = Button(windowTime, text = "Check Year", bg='#E7C7FC', command=getYear)
	buttonYear.config(height=3, width=25)
	buttonYear.place(relx=0.55, rely = 0.5)

buttonTime = Button(window, text="Time", height=2, width=12,
	bg = '#E7C7FC', command=getTime)
buttonTime['font'] = myFont
buttonTime.grid(column=0, row=6)

#######TIME_END############


########WEATHER_START############

def getWeather():
	windowWeather = Toplevel(window)
	windowWeather.geometry("700x700")
	windowWeather['background']='#B7FCF8'

	owm = pyowm.OWM("3a58957d6015c8025c341071a051adf8")
	observation = owm.weather_at_place("Bucharest,ro")
	weat = observation.get_weather()

	lblWeatherTitle = Label(windowWeather, text="Weather", bg='#B7FCF8', font=("Arial Bold", 30))
	lblWeatherTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblWeather = Label(windowWeather, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblWeather.place(relx=0.5, rely=0.4, anchor=CENTER)

	lblWeatherCustom = Label(windowWeather, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblWeatherCustom.place(relx=0.5, rely=0.95, anchor=CENTER)

	Weather = StringVar(windowWeather)
	Weather.set("Choose day")

	w = OptionMenu(windowWeather, Weather, "Today", "Tomorrow", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date = cal.get_date().split("/")
		dateS = int(date[1]) + 2
		data = dataDf.at[dateS, 'weather']
		lblWeatherCustom.config(text="The weather was " + data)

	def callback(*args):
		if Weather.get() == 'Today':
			temperature = weat.get_temperature('celsius')
			lblWeather.config(text="The weather is " + str(temperature.get('temp')) + " celsius")
		if Weather.get() == 'Tomorrow':
			tomorrow = pyowm.timeutils.tomorrow()
			temperature = weat.get_temperature('celsius')
			lblWeather.config(text="The weather will be " + str(temperature.get('temp')) + " celsius")
		if Weather.get() == 'Custom':
			cal.place(relx=0.35, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	Weather.trace("w", callback)

	cal = Calendar(windowWeather, selectmode="day", year=2020)
	buttonCalendar = Button(windowWeather, text = "Check Weather", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonWeather = Button(window, text="Weather", height=2, width=12,
	bg = '#E7C7FC', command=getWeather)
buttonWeather['font'] = myFont
buttonWeather.grid(column=1, row=6)

########WEATHER_END############


########STRESS_START############

def getStress():
	windowStress = Toplevel(window)
	windowStress.geometry("700x700")
	windowStress['background']='#B7FCF8'

	lblStressTitle = Label(windowStress, text="Stress", bg='#B7FCF8', font=("Arial Bold", 30))
	lblStressTitle.place(relx=0.5, rely=0.1, anchor=CENTER)
	
	lblStress = Label(windowStress, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblStress.place(relx=0.5, rely=0.4, anchor=CENTER)

	lblStressCustom = Label(windowStress, text="", bg='#B7FCF8', fg='BLUE', font=("Arial Bold", 20))
	lblStressCustom.place(relx=0.5, rely=0.95, anchor=CENTER)

	Stress = StringVar(windowStress)
	Stress.set("Choose day")

	w = OptionMenu(windowStress, Stress, "Yesterday", "Today", "Custom")
	w.config(width=40, height=3)
	w.config(bg = "#E7C7FC")
	w.config(font=12)
	w.config(bd=5)
	w.place(relx = 0.2, rely = 0.2)

	def customDate():
		date = cal.get_date().split("/")
		dateS = int(date[1]) + 2
		data = dataDf.at[dateS, 'stress']
		lblStressCustom.config(text="Your stress level was " + data)

	def callback(*args):
		if Stress.get() == 'Today':
			lblStress.config(text="Your stress level is " + dataDf.at[0, 'stress'])
		if Stress.get() == 'Yesterday':
			lblStress.config(text="Your stress level was " + dataDf.at[1, 'stress'])
		if Stress.get() == 'Custom':
			cal.place(relx=0.35, rely=0.45)
			buttonCalendar.place(relx=0.32, rely = 0.8)
	Stress.trace("w", callback)

	cal = Calendar(windowStress, selectmode="day", year=2020)
	buttonCalendar = Button(windowStress, text = "Check Stress", bg='#E7C7FC', command=customDate)
	buttonCalendar.config(height=3, width=30)

buttonStress = Button(window, text="Stress", height=2, width=12,
	bg = '#E7C7FC', command=getStress)
buttonStress['font'] = myFont
buttonStress.grid(column=2, row=6)

########STRESS_END############

#######CHAT_WITH_BOT_START########

def chatWithBot(textbox, chatWindow):
	textbox.insert(INSERT, "Say something: ")
	textbox.config(fg='blue')
	chatWindow.after(1000)
	r = sr.Recognizer()
	r.pause_threshold = 0.7
	r.energy_threshold = 400

	with sr.Microphone() as source:
		try:
			audio = r.listen(source,timeout=1,phrase_time_limit=5)
			message = r.recognize_google(audio)

			textbox.insert(INSERT, message + "\n")
			textbox.config(fg='black')

			textbox.insert(INSERT, "Bot says: ")
			textbox.config(fg='blue')

			r = requests.post("http://localhost:5002/webhooks/rest/webhook",
				json={"message": message})

			for i in r.json():
				bot_message = i['text']
				print(f"{bot_message}")
			
			textbox.insert(INSERT, bot_message + "\n")
			textbox.config(fg='black')

			if "say" or "tell" in message:
				myobj = gTTS(text=bot_message)
				myobj.save("welcome.mp3")
				# Playing the converted file
				subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
		except sr.UnknownValueError:
			print('Google Speech Recognition could not understand audio')
		
		except sr.RequestError as e:
			print('Could not request results from Google Speech Recognition Service')
		
		else:
			pass


def create_window():
	chatWindow = Toplevel(window)
	chatWindow.geometry("880x580")
	chatWindow['background']='#B7FCF8'

	S = Scrollbar(chatWindow)
	S.place(relx=0.985, rely=0, relheight=0.74, width=20, anchor='ne')
	T = Text(chatWindow, height=25, width=105)
	T.grid()
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	#T.insert(END, "Just a text Widget\nin two lines\n")

	buttonMic = Button(chatWindow, text="Chat", bg='#E7C7FC', command=lambda: chatWithBot(T, chatWindow))
	buttonMic.config(height=3, width=30)
	buttonMic.place(relx=0.3, rely=0.75)

#buttonChat = Button(window, text="Chat with Health Indicator Bot", command=create_window, fg='white', font='bold', height = 8, width = 44, bg='blue')
#buttonChat.grid(row=7,column=1)

chatFont = font.Font(size=30)

buttonChat = Button(window, text="Chat with \n Health Indicator Bot", height=2, width=17,
	 fg='white', bg='blue', command=create_window)
buttonChat['font'] = chatFont
buttonChat.grid(column=1, row=7)
#######CHAT_WITH_BOT_END##########

window.mainloop()

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
