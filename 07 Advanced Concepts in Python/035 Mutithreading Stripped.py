from xml.dom.minidom import parse
import xml.dom.minidom
import smtplib
import time
import _thread



# Define a function for the thread
def print_time(threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % (threadName, time.ctime(time.time())))


# Two threads will be created
try:
   _thread.start_new_thread(print_time, ("Thread-1", 2, ))
   _thread.start_new_thread(print_time, ("Thread-2", 4, ))
except:
   print("We have a problem Houston. We were unable to start threads.")

while 1:
   pass
