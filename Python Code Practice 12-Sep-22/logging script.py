"""

Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.

 

Info : These are used to confirm that things are working as expected

 

Warning : These are used an indication that something unexpected happened, or is indicative of some problem in the near future

 

Error : This tells that due to a more serious problem, the software has not been able to perform some function

 

Critical : This tells serious error, indicating that the program itself may be unable to continue running

"""

 

# importing module

import logging

# Create and configure logger

logging.basicConfig(filename="newfile.log",

                    format='%(asctime)s %(message)s',

                    filemode='w') # By default filemode is append 'a' / 'w' is overwrite /

#In format we acan set only either levelname, message, asctime(it's date and time)

#we can set the date date format ex: datefmt='%d/%m/%y %I(12Hours)H(24 Hours):%M:%S %p(Am or pm)

# Creating an object

logger = logging.getLogger()

# Setting the threshold of logger to DEBUG

logger.setLevel(logging.DEBUG) #It will print all / Instead of DEBUG if we set "ERROR" then it will print only error and critical logs only.

# Default Level is Warning

# How to implement logging: 1 Create log file (To which file we want to store 2. Need to assign the level (either warning or debug or any)

 

# Test messages

logger.notset("Not set") # numeric value 0

logger.debug("Harmless debug Message") #numeric value 10

logger.info("Just an information") #numeric value 20

logger.warning("Its a Warning") #numeric value 30

logger.error("Did you try to divide by zero") #numeric value 40

logger.critical("Internet is down") #numeric value 50