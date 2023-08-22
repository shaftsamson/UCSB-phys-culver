#!/usr/bin/env python3

#
# server.py - Serve data from a TCP socket
#
# 17May17  Added call to socket.shutdown()
# 10May16  Everett Lipman
#
USAGE="""
usage: server.py port [file]

       Serve data from specified port.
       Default message is sent if no file is specified.
"""
N_ARGUMENTS = (1,2)

import sys
import os
import socket
import time



###############################################################################

def usage(message = ''):
   sys.stdout = sys.stderr
   if message != '':
      print()
      print(message)
   print(USAGE)

   sys.exit(1)
###############################################################################

def check_arguments():
   """Check command line arguments for proper usage.
   """
   global nargs, progname
   nargs = len(sys.argv) - 1
   progname = os.path.basename(sys.argv[0])
   flag = True
   if nargs != 0 and N_ARGUMENTS[-1] == '*':
      flag = False
   else:
      for i in N_ARGUMENTS:
         if nargs == i:
            flag = False
   if flag:
      usage()
   return(nargs)
###############################################################################

def bind_port(prt):
   """Create socket and bind to port prt.
   """

   host = ''  # bind to all available interfaces
 
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse port
   s.bind((host, prt))
   s.listen(1)
    
   return(s)
###############################################################################

if __name__ == '__main__':
   port=55553  
   seconds = time.time()
   local_time = time.ctime(seconds)
   local_time=local_time.encode('utf-8')

   

   thesocket = bind_port(port)

   while True:
      connection, peer = thesocket.accept()
      print()
      print('Sending data to %s...' % repr(peer), end='')
      connection.sendall(local_time) 
      print('Done.\n')
      connection.shutdown(socket.SHUT_RDWR)
      connection.close()


#Here we send the time to a terminal in my computer, since I dont have an rpi. 
#We do so by finding the date using the time package and turning seconds into the date, 
#then we turn that data into a byte like object and send it with connection.sendall(local_time)



