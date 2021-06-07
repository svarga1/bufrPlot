#Program to plot Radiosonde bufr file
##Change FILEPATH and OUTPUTPATH before running


#Most of the commands are identical to the jupiter notebook example from ncepbufr


#Modules
import ncepbufr
import numpy as np
import matplotlib.pyplot as plt


FILEPATH='/work/noaa/stmp/svarga/gdas.t00z.adpupa.tm00.bufr_d' 
OUTPUTPATH='.'


#Open the file
bufr = ncepbufr.open(FILEPATH) 
bufr.advance()
bufr.advance()


bufr.advance() #Has to advance three times to start for the test file; Calling load_subset before this returns -1. 
bufr.load_subset()


#Variables
dryBulb=bufr.read_subset('TMDB').squeeze()-273.15 #Converts from K to C
pressure=bufr.read_subset('PRLC').squeeze()/100 #Converts from Pa to hPa
dppt=bufr.read_subset('TMDP').squeeze()-273.15

#Location and Date
lon=bufr.read_subset('CLON')[0][0]
lat=bufr.read_subset('CLAT')[0][0]
date=bufr.msg_date

bufr.close() #Closes the file.

#Shape and Missing Data check- Needs updated
print(np.shape(dryBulb))
print(np.count_nonzero(np.isnan(dryBulb)))
print(np.shape(pressure))
print(np.count_nonzero(np.isnan(dryBulb)))
print(np.shape(dppt))
print(np.count_nonzero(np.isnan(dryBulb)))
print(lon)
print(lat)


#Plot Pressure vs. DBT

fig=plt.figure()
plt.scatter(dryBulb,pressure,color='red', label='Dry Bulb') #Plots dry bulb
plt.scatter(dppt,pressure,color='green', label='Dew Point') #plots dew point temperature
plt.title('Radiosonde Profile at lat {:.2f}, lon: {:.2f} \n Time: {}'.format(lat,lon,date)) #Adds title to plot
plt.xlabel('Temperature (C' + u'\N{degree sign}' + ')') #Adds x and y labels
plt.ylabel('Pressure (hPa)')
ax=plt.gca()
ax.set_ylim(ax.get_ylim()[::-1]) #Inverts the y-axis
plt.legend() #Adds legend
plt.savefig(OUTPUTPATH+'/sounding.png') #saves the plot
