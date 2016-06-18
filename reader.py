
# Author: Joseph Mammo
# Analysis: O(n) ~ has the potential to be improved to O(ln(n))!
# Current features: - Take in row csv file and hourly and monthly plot the occupied and unoccupied data of the a specific location

#Import the required libraries
import csv 
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import scipy

#read in the CSV and store it in a huge array
f = open('MetOneAll.csv')
csv_f = csv.reader(f)

#print rows from the read csv - tester
#for row in csv_f:
    #  print row[0]

csv_srf =[] #Surface IH Office Data
csv_trs = [] # Transition W_D data
csv_crn = [] # LL Cavern NE Corner data
csv_ecntrm = [] # E Count Room NW Corner data
csv_ewall = [] # E Count Room W Wall data
csv_ecntrmm = [] # E Count Room data
csv_dvs = [] # Common Corridor Refrig data
csv_dvs_srt = [] # organized Common Corridor Refrig data -- weekdays from 8 to 5

#Parameter - location data -> array
for row in csv_f:
    if(row[2] == "Surface IH Office"):
        csv_srf.append(row)
    if(row[2] == "Transition W_D"):
        csv_trs.append(row)
    if(row[2] == "LL Cavern NE Corner"):
        csv_crn.append(row)
    if(row[2] == "E Count Room NW Corner"):
        csv_ecntrm.append(row)
    if(row[2] == "Common Corridor Refrig"):
        csv_dvs.append(row)
    if(row[2] == "E Count Room W Wall"):
        csv_ewall.append(row)
    if(row[2] == "E Count Room"):
        csv_ecntrmm.append(row)
#plt.plot(csv_dvs)



# -- START ANALYSIS CODE -- #

loc_data_occ = []
loc_data_uocc = []
loc_data = []
info = '1 = Davis Campus Common Corridor; 2 = LL Cavern NE Corner; 3 = Surface IH Office; 4 = Transition W_D; 5 = E Count Room NW Corner; 6 = E Count Room W Wall; 7 = E Count Room'
print(info)
loc_num = int(input("Enter a number from 1 - 7: ")) # 1 = csv_dvs, 2 = csv_crn, 3 = csv_srf, 4 = csv_trs, 5 = csv_ecntrm, 6 = csv_ewall, 7 = csv_ecntrmm
loc_name = ""

if(loc_num == 1):
    for row in csv_dvs:
        loc_data.append(row)
    loc_name = "Common Corridor Refrig"
elif(loc_num == 2):
    for row in csv_crn:
        loc_data.append(row)
    loc_name = "LL Cavern NE Corner"
elif(loc_num == 3):
    for row in csv_srf:
        loc_data.append(row)
    loc_name = "Surface IH Office"
elif(loc_num == 4):
    for row in csv_trs:
        loc_data.append(row)
    loc_name = "Transition W_D"
elif(loc_num == 5):
    for row in csv_ecntrm:
        loc_data.append(row)
    loc_name = "E Count Room NW Corner"
elif(loc_num == 6):
    for row in csv_ewall:
        loc_data.append(row)
    loc_name = "E Count Room W Wall"
elif(loc_num == 7):
    for row in csv_ecntrmm:
        loc_data.append(row)
    loc_name = "E Count Room"
    
#Occupied - unoccupied splitter
for row in loc_data:
    # print row[0]
    date_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M')
    #print(date_object.weekday()) #only 0 - 4 are needed
    h = (date_object - date_object.replace(hour=0,minute=0,second=0)).seconds / 3600.
    w = date_object.isocalendar()[1]
    d = date_object.isocalendar()[2]
    if((date_object.weekday() == 5 or date_object.weekday() == 6 and ((w/2 == 2) and d == 0) and ((w/2 != 2) and d == 4)) and (h >=8 and h < 18)):
       loc_data_uocc.append(row)
    else:
       loc_data_occ.append(row)         
    
#unoccupied
x_val = []
y_val = []

for row in loc_data_uocc:
    #print(row)
    x_val.append(datetime.strptime(row[0], '%m/%d/%Y %H:%M'))
    y_val.append(row[1])
    
#plt.plot(x_val, y_val)
#plt.show()


#occupied
x_val = []
y_val = []

for row in loc_data_occ:
    #print(row)
    x_val.append(datetime.strptime(row[0], '%m/%d/%Y %H:%M'))
    y_val.append(row[1])
    
#plt.plot(x_val, y_val)
#plt.show()

# END Occupied - unoccupied splitter

#Hourly Plotter
inpt = int(input("Hourly plotter: Enter 1 for occupied and 2 for unoccupied: ")) # 1 = occupied and 2 = unoccupied
time_grapher = []

if(inpt == 1):
    for row in loc_data_occ:
        time_grapher.append(row)
    title = "Occupied Data"
elif(inpt == 2):
    for row in loc_data_uocc:
        time_grapher.append(row) 
    title = "Unoccupied Data"       
           
e = []
n = []
t = []
el = []
twl = []
o = []
tw = []
th = []
fo = []
fi = []


time_nor = [8,9,10,11,12,13,14,15,16,17]
time_avg = [] 

for row in time_grapher:
    #print(row)
    date_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M')
    #print(date_object.weekday()) #only 0 - 4 are needed
    h = (date_object - date_object.replace(hour=0,minute=0,second=0)).seconds / 3600.
    if (h == 8):
        e.append(int(row[1]))
    elif (h == 9):
        n.append(int(row[1]))
    elif (h == 10):
        t.append(int(row[1]))        
    elif (h == 11):
        el.append(int(row[1]))
    elif (h == 12):
        twl.append(int(row[1]))
    elif (h == 13):
        o.append(int(row[1]))
    elif (h == 14):
        tw.append(int(row[1]))
    elif (h == 15):
        th.append(int(row[1]))
    elif (h == 16):
        fo.append(int(row[1]))
    elif (h == 17):
        fi.append(int(row[1]))
        
#if val == nan, enter 0! -- fix        
time_avg.append(np.mean(e))
time_avg.append(np.mean(n))
time_avg.append(np.mean(t))
time_avg.append(np.mean(el))
time_avg.append(np.mean(twl))
time_avg.append(np.mean(o))
time_avg.append(np.mean(tw))
time_avg.append(np.mean(th))
time_avg.append(np.mean(fo))
time_avg.append(np.mean(fi))

#for row in time_avg:
   # print(row)
   
plt.plot(time_nor,time_avg)
plt.title(title + " data for " + loc_name + " | avg:" + str(np.mean(time_avg)) + " per.5 micro meter/ft^3")
plt.ylabel('Particle Count per.5 micro meter/ft^3')
plt.xlabel('Time in hours')
#plt.legend(" | avg:" + str(np.mean(time_avg)) + " per.5 micro meter/ft^3")
patch = mpatches.Patch(color='blue', label='avg:' + str(np.mean(time_avg)) + ' per.5 micro meter/ft^3')
plt.legend(handles=[patch])
plt.show()


# Monthly Plotter
inptt = int(input("Monthly plot: enter 1 for occupied and 2 for unoccupied: "))
monthly_grapher = []

month_nor = [1,2,3,4,5,6,7,8,9,10,11,12]
month_avg = []

jan = []
feb = []
mar = []
apr = []
may = []
jun = []
jul = []
aug = []
sep = []
octt = []
nov = []
dec = []

if(inptt == 1):
    for row in loc_data_occ:
        monthly_grapher.append(row)
        mon_title = "Occupied Data"
elif(inptt == 2):
    for row in loc_data_uocc:
        monthly_grapher.append(row)
        mon_title = "Unoccupied Data"
        
for row in monthly_grapher:
    month_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M')
    m = month_object.month
    if(m == 1):
        jan.append(int(row[1]))
    elif(m == 2):
        feb.append(int(row[1]))
    elif(m == 3):
        mar.append(int(row[1]))
    elif(m == 4):
        apr.append(int(row[1]))
    elif(m == 5):
        may.append(int(row[1]))
    elif(m == 6):
        jun.append(int(row[1]))
    elif(m == 7):
        jul.append(int(row[1]))
    elif(m == 8):
        aug.append(int(row[1]))
    elif(m == 9):
        sep.append(int(row[1]))
    elif(m == 10):
        octt.append(int(row[1]))
    elif(m == 11):
        nov.append(int(row[1]))
    elif(m == 12):
        dec.append(int(row[1]))
        
month_avg.append(np.mean(jan))
month_avg.append(np.mean(feb))
month_avg.append(np.mean(mar))
month_avg.append(np.mean(apr))
month_avg.append(np.mean(may))
month_avg.append(np.mean(jun))
month_avg.append(np.mean(jul))
month_avg.append(np.mean(aug))
month_avg.append(np.mean(sep))
month_avg.append(np.mean(octt))
month_avg.append(np.mean(nov))
month_avg.append(np.mean(dec))

plt.plot(month_nor,month_avg)
plt.title(title + " data for " + loc_name + " | avg:" + str(np.mean(month_avg)) + " per.5 micro meter/ft^3")
plt.ylabel('Particle Count per.5 micro meter/ft^3')
plt.xlabel('Months')
patch = mpatches.Patch(color='blue', label='avg:' + str(np.mean(month_avg)) + ' per.5 micro meter/ft^3')
plt.legend(handles=[patch])
plt.show()
# -- END ANALYSIS CODE -- #