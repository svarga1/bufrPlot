#Program that checks the number of Profiles 

#Modules
import ncepbufr


FILENAME='/work/noaa/stmp/svarga/gdas.t00z.adpupa.tm00.bufr_d'

#Load Bufr file and move to the first message

bufr=ncepbufr.open(FILENAME)

bufr.advance() #This should be put in a loop to generalize it for other files
bufr.advance()
bufr.advance()


counter=1 #Starts at 1 to include the first message

while bufr.advance() == 0: #bufr.advance steps through the messages and returns a 0 when succesful. It returns 1 at the end of the file.
	counter +=1
print(counter) #Counter will be the number of profiles in the bufr file. 


#Should probably include an auto-timeout since it's running on the login node
#What happens if we call load subset before advancing? Does it crash or return 1
