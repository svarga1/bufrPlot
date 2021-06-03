#Program to plot Radiosonde bufr file

#Modules
import ncepbufr
import numpy as np
import matplotlib.pyplot as plt

#Open the file
bufr = ncepbufr.open("FILENAME") 
bufr.advance()
bufr.advance()
bufr.advance() #Has to advance three times: load subset fails if less than three, and causes a crash if it advances more than three times. 5 times also works
#Update: it no longer crashes if it advances more than three times. Might have been caused by advancing after loading
bufr.load_subset()

#Variables
dryBulb=bufr.read_subset('TMDB').squeeze()-273.15 #Converts from K to C
pressure=bufr.read_subset('PRLC').squeeze()/100 #Converts from Pa to hPa

#Location and Date
lon=bufr.read_subset('CLON')[0][0]
lat=bufr.read_subset('CLAT')[0][0]
date=bufr.msg_date

bufr.close() #Closes the file

print(np.shape(dryBulb))
print(np.shape(pressure))
print(lon)
print(lat)

#Histograms to test DQ and make sure I can see plots

#fig = plt.figure() 
#plt.hist(dryBulb)
#plt.title('Dry Bulb Temperature')
#plt.savefig('dryBulb.png')

#fig = plt.figure()
#plt.hist(pressure)
#plt.title('Pressure')
#plt.savefig('pressure.png')


#Plot Pressure vs. DBT

fig=plt.figure()
plt.scatter(dryBulb,pressure)
plt.title('Dry Bulb Temperature from Station X')
plt.xlabel('Dry Bulb Temperature (C' + u'\N{degree sign}' + ')')
plt.ylabel('Pressure (hPa)')
plt.savefig('sounding.png')
