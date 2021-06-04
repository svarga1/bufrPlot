#Program that checks the number of Profiles 

#Modules
import ncepbufr
import numpy as np

FILENAME='/work/noaa/stmp/svarga/gdas.t00z.adpupa.tm00.bufr_d'

#Load Bufr file and move to the first message

bufr=ncepbufr.open(FILENAME)

bufr.advance() #This should be put in a loop to generalize it for other files
bufr.advance()



numSubsets=np.array(1) #Array that counts the number of subsets
counter=1 #Starts at 1 to include the first message
dataLen=np.array(1) # Array that counts the # of data points per subset
#Using a while loop will call bufr.advance again, skipping the first message. Fix this in future
while bufr.advance() == 0: #bufr.advance steps through the messages and returns a 0 when succesful. It returns 1 at the end of the file.
	numSubsets=np.append(numSubsets,bufr.subsets)  #append the number of subsets in the current message to the arrayi
	while bufr.load_subset()==0: #Loop through every subset
		try:
			dataLen=np.append(dataLen, len(bufr.read_subset('PRLC').squeeze()))
		except:
			pass
	counter+=1
print('There are {} messages'.format(counter)) #Counter will be the number of profiles in the bufr file. 
print('The mean number of subsets is {}'.format(np.mean(numSubsets)))
np.savetxt('numSubsets.txt',numSubsets, fmt='%d')
np.savetxt('numData.txt',dataLen, fmt='%d')

#Should probably include an auto-timeout since it's running on the login node
#What happens if we call load subset before advancing? Does it crash or return 1
