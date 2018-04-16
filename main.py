from tkinter import *

#Functions / Logic
def periodCalc(days):
    period = 365 / days
    periodEnt.delete(0, END)
    periodEnt.insert(END,period)

def roiPerPeriod(contracts, premium):
    shares = contracts * 100
    roiperperiod = shares * premium
    roiPeriodEnt1.delete(0, END)
    roiPeriodEnt1.insert(END, roiperperiod)

def roiPerPercent(contracts, strikeprice, roiPerperiod):
    shares = contracts * 100
    totalinvestment = (shares * strikeprice)
    investmentEnt.delete(0, END)
    investmentEnt.insert(END, totalinvestment)
    roiperpercent = (roiPerperiod / totalinvestment) * 100
    roiPeriodEnt2.delete(0, END)
    roiPeriodEnt2.insert(END, roiperpercent)

def roiPerYearNoMargin(period, roiperperiodpercent):
    roiperyear = (period * roiperperiodpercent)
    noMarginEnt.delete(0, END)
    noMarginEnt.insert(END, roiperyear)

def roiPerYearYesMargin(roiNoMargin):
    roi = roiNoMargin * 3
    yesMarginEnt.delete(0, END)
    yesMarginEnt.insert(END, roi)

def roiPerYear(period, roiPerperiod):
    roi = period * roiPerperiod
    roiYearEnt.delete(0, END)
    roiYearEnt.insert(END, roi)

#Refreshes input and runs functions
def calculate():
    strike = float(strikeEnt.get())
    totalinvestment = float(investmentEnt.get())
    days = float(daysEnt.get())
    premium = float(premiumEnt.get())
    noMargin = float(noMarginEnt.get())
    yesMargin = float(yesMarginEnt.get())
    contracts = float(contractsEnt.get())
    period = float(periodEnt.get())
    roiperperioddollar = float(roiPeriodEnt1.get())
    roiperperiodpercent = float(roiPeriodEnt2.get())
    roiyear = float(roiYearEnt.get())

    periodCalc(days)
    roiPerPeriod(contracts, premium)
    roiperperioddollar = float(roiPeriodEnt1.get())
    roiPerPercent(contracts, strike, roiperperioddollar)
    roiperperiodpercent = float(roiPeriodEnt2.get())
    period = float(periodEnt.get())
    roiPerYearNoMargin(period, roiperperiodpercent)
    noMargin = float(noMarginEnt.get())
    roiperperioddollar = float(roiPeriodEnt1.get())
    roiPerYearYesMargin(noMargin)
    roiPerYear(period, roiperperioddollar)

#GUI

#Start window
window = Tk()
window.title('Options ROI Calculator')
window.configure(background = "white")
window.resizable(False, False)

#Creating Top Beggining label
Label(window, text = "Options ROI Calculator", bg = "white", fg = "black", font = "none 19 bold").grid(row = 0, column = 0, sticky = N)

#Strike price
Label(window, text = "Strike Price", bg = "white", fg = "black", font = "none 12").grid(row = 1, column = 0, sticky = N)
strikeEnt = Entry(window, width  = 20, bg = "white")
strikeEnt.grid(row=2, column = 0, sticky = N)
strikeEnt.insert(END, '0')

#Premium
Label(window, text = "Premium", bg = "white", fg = "black", font = "none 12").grid(row = 3, column = 0, sticky = N)
premiumEnt = Entry(window, width  = 20, bg = "white")
premiumEnt.grid(row=4, column = 0, sticky = N)
premiumEnt.insert(END, '0')

#Days
Label(window, text = "Days", bg = "white", fg = "black", font = "none 12").grid(row = 5, column = 0, sticky = N)
daysEnt = Entry(window, width  = 20, bg = "white")
daysEnt.grid(row=6, column = 0, sticky = N)
daysEnt.insert(END, '0')

#ROI without Margin yearly
Label(window, text = "ROI yearly without margin", bg = "white", fg = "black", font = "none 12").grid(row = 7, column = 0, sticky = N)
noMarginEnt = Entry(window, width  = 20, bg = "white")
noMarginEnt.grid(row=8, column = 0, sticky = N)
noMarginEnt.insert(END, '0')

#ROI with Margin yearly
Label(window, text = "ROI yearly with margin", bg = "white", fg = "black", font = "none 12").grid(row = 9, column = 0, sticky = N)
yesMarginEnt = Entry(window, width  = 20, bg = "white")
yesMarginEnt.grid(row=10, column = 0, sticky = N)
yesMarginEnt.insert(END, '0')

#Calculate button
Label(window, text = "", bg = "white", fg = "black", font = "none 12").grid(row = 11, column = 0, sticky = N)
Button(window, text = "Calculate", width = 8, command = calculate).grid(row = 12, column = 0, sticky = N)
Label(window, text = "", bg = "white", fg = "black", font = "none 12").grid(row = 13, column = 0, sticky = N)

#Contracts
Label(window, text = "Contracts", bg = "white", fg = "black", font = "none 12").grid(row = 14, column = 0, sticky = N)
contractsEnt = Entry(window, width  = 20, bg = "white")
contractsEnt.grid(row=15, column = 0, sticky = N)
contractsEnt.insert(END, '1')

#Total Investment
Label(window, text = "Total Investment", bg = "white", fg = "black", font = "none 12").grid(row = 16, column = 0, sticky = N)
investmentEnt = Entry(window, width  = 20, bg = "white")
investmentEnt.grid(row=17, column = 0, sticky = N)
investmentEnt.insert(END, '0')

#Period
Label(window, text = "Period", bg = "white", fg = "black", font = "none 12").grid(row = 18, column = 0, sticky = N)
periodEnt = Entry(window, width  = 20, bg = "white")
periodEnt.grid(row=19, column = 0, sticky = N)
periodEnt.insert(END, '0')

#ROI / Period ($)
Label(window, text = "ROI / Period ($)", bg = "white", fg = "black", font = "none 12").grid(row = 20, column = 0, sticky = N)
roiPeriodEnt1 = Entry(window, width  = 20, bg = "white")
roiPeriodEnt1.grid(row=21, column = 0, sticky = N)
roiPeriodEnt1.insert(END, '0')

#ROI / Period (%)
Label(window, text = "ROI / Period (%)", bg = "white", fg = "black", font = "none 12").grid(row = 22, column = 0, sticky = N)
roiPeriodEnt2 = Entry(window, width  = 20, bg = "white")
roiPeriodEnt2.grid(row=23, column = 0, sticky = N)
roiPeriodEnt2.insert(END, '0')

#ROI / Year ($)
Label(window, text = "ROI / Year ($)", bg = "white", fg = "black", font = "none 12").grid(row = 24, column = 0, sticky = N)
roiYearEnt = Entry(window, width  = 20, bg = "white")
roiYearEnt.grid(row=25, column = 0, sticky = N)
roiYearEnt.insert(END, '0')

#Exit function
def close_window():
    window.destroy()
    exit()

#Exit button
Label(window, text = "", bg = "white", fg = "black", font = "none 12").grid(row = 26, column = 0, sticky = N)
Button(window, text = "Exit", width = 14, command = close_window).grid(row = 27, column = 0, sticky = N)
Label(window, text = "", bg = "white", fg = "black", font = "none 12").grid(row = 28, column = 0, sticky = N)


#Run Tkinter window
window.mainloop()