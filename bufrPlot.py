#Program to plot Radiosonde bufr file
##Change FILEPATH and OUTPUTPATH before running

#Modules
import ncepbufr
import numpy as np
import matplotlib.pyplot as plt


FILEPATH='' 
OUTPUTPATH=''


#Open the file
bufr = ncepbufr.open(FILEPATH) 
bufr.advance()
bufr.advance()
bufr.advance() #Has to advance three times to start; Calling load_subset before this returns -1. Can use advance n times after to cycle through the different observations. Need to check if the bufr object is iterable, i.e. can it be used to loop through all the observations in the set/ how to know when it has no new data? 
#bufr.advance()
#bufr.advance()
bufr.load_subset()

#Variables
dryBulb=bufr.read_subset('TMDB').squeeze()-273.15 #Converts from K to C
pressure=bufr.read_subset('PRLC').squeeze()/100 #Converts from Pa to hPa
dppt=bufr.read_subset('TMDP').squeeze()-273.15
#Location and Date
lon=bufr.read_subset('CLON')[0][0]
lat=bufr.read_subset('CLAT')[0][0]
date=bufr.msg_date

bufr.close() #Closes the file-- look through documentation to find the method to unload a subset without closing a file, so we can iterate through the file.

print(np.shape(dryBulb))
print(np.count_nonzero(np.isnan(dryBulb)))
print(np.shape(pressure))
print(np.count_nonzero(np.isnan(dryBulb)))
print(np.shape(dppt))
print(np.count_nonzero(np.isnan(dryBulb)))
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
plt.scatter(dryBulb,pressure,color='red', label='Dry Bulb') #Scatter plot works fine, but the line plot doesn't. Possibly na data or caused by readings on the way up and down?
plt.scatter(dppt,pressure,color='green', label='Dew Point')
plt.title('Radiosonde Profile at lat {:.2f}, lon: {:.2f} \n Time: {}'.format(lat,lon,date))
plt.xlabel('Temperature (C' + u'\N{degree sign}' + ')')
plt.ylabel('Pressure (hPa)')
ax=plt.gca()
ax.set_ylim(ax.get_ylim()[::-1]) #Inverts the y-axis
plt.legend()
plt.savefig(OUTPUTPATH+'/sounding.png')
