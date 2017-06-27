#!/usr/bin/python

# ex3.py -- Run a port scan against a single IP address.
#
# Michael Burkhardt (mburkhardt@smu.edu)
# January 25, 2016

# ----------------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------------
import socket
import subprocess
import sys
from datetime import datetime

# ----------------------------------------------------------------------------
# Identify the victim(s)
# ----------------------------------------------------------------------------
dest_ipaddr = raw_input("Enter IPv4 address: ")
#dest_mask = raw_input("Mask: ")

# TO DO:
# 1. validate the input
# 2. prompt for a subnet mask and run the scan against all matching addresses

# ----------------------------------------------------------------------------
# Scan "privileged" ports
# ----------------------------------------------------------------------------
print "Scanning address: %s" % dest_ipaddr

for port in range(1,1023):  
  try:
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpresult = sock.connect_ex((remoteServerIP, port))
    tcpsock.close()
    if tcpresult == 0:
      print "Port %d \t Open".format(port)

  except socket.error:
    # "socket-related errors"
    print "Couldn't connect to server"
    sys.exit()

  except KeyboardInterrupt:
    # CTRL-C
    sys.exit()

  except socket.gaierror:
    # Some kind of "get address" error (shouldn't need for IP addresses)
    continue


# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total
