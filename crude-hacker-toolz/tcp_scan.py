#! /home/mhb/anaconda2/bin/python
from __future__ import print_function

# tcp_scan.py - A crude TCP port scanner
#
# by Michael Burkhardt (mburkhardt@smu.edu)
# February 7, 2016

# *****************************************************************************
# Usage statement
# *****************************************************************************
usage = """
------------------------------------------------------------------------------
tcp_scan.py - A crude TCP port scanner

Usage: tcp_scan.py [Options] <ipspec>

Where <ipspec> may be a single IP address (e.g. 192.168.1.1)
or an IP network and net mask (e.g. 192.168.1.0/24)

Options:
-s, --start-port N      start of range to scan
-e, --end-port N        end of range to scan
-f, --force             force scan when IP range contains >256 hosts
-r, --randomize         randomize the port order and time interval (1-5 sec)

This program checks all specified ports on all hosts in the specified range to
see whether a TCP service is running. Results are displayed at the end. The
order of port checking and interval between connection attempts can be
randomized. By default, interval is 2 seconds. When port range is not
specified, only select common ports (FTP, SSH, Telnet, SMTP, IMAP, HTTP,
and HTTPS) are scanned.
------------------------------------------------------------------------------
"""

# *****************************************************************************
# Import some libraries
# *****************************************************************************

from netaddr import *
import socket
import sys
import time
import getopt
import numpy as np

# *****************************************************************************
# Process command-line arguments
# *****************************************************************************

argv = sys.argv[1:]

try:
  opts, args = getopt.getopt(argv,"s:e:hf",['start-port','end-port','help','force'])
except getopt.GetoptError:
  print(usage)
  sys.exit()

# *****************************************************************************
# Process the command line options and configure the scan.
# *****************************************************************************

start_port =    -1 # the default starting port (start of well known ports)
end_port   =    -1 # the default starting port (end of well known ports)
force      = False # don't force when >256 hosts
randomize  = False # don't randomize

for opt, arg in opts:
  if opt in ('-h', '--help'):
    print(usage)
    sys.exit()
  elif opt in ('-s', '--start-port'):
    start_port = int(arg)
  elif opt in ('-e', '--end-port'):
    end_port = int(arg)
  elif opt in ('-f', '--force'):
    force = True
  elif opt in ('-r', '--randomize'):
    randomize = True

# *****************************************************************************
# There should be exactly one argument (remaining). If not,
# display usage and exit.
# *****************************************************************************

if len(args) != 1:
  print(usage)
  sys.exit()

# *****************************************************************************
# Configure the target host range
# *****************************************************************************

ipn  = IPNetwork(args[0])
ip_list = list(ipn)

print("Scanning network %s (%d hosts)..." % (str(ipn),len(ip_list)))

if len(ip_list) > 256 and not force:
  print("Scanning more than 256 hosts not allowed. (-f to force)")
  sys.exit()

# *****************************************************************************
# Configure the port range (same for all target hosts)
# *****************************************************************************

if start_port != -1 and end_port != -1:
  print("Scanning port range: %d to %d" % (start_port,end_port))
  port_list = range(start_port,end_port+1)
else:
  port_list = [21, 22, 23, 25, 80, 143, 443]
  print("Scanning common ports: %s" % str(port_list))

# *****************************************************************************

family = socket.AF_INET
interval = 2

print("\n\0337")
for ip in ip_list:
  if randomize:
    np.random.shuffle(port_list)
    interval = np.random.randint(1,6)
  host = str(ip)
  # Use VT escape codes to keep the output pretty
  print("\0338\033[KScanning host %s..." % host,end="")
  sys.stdout.flush()
  found_ports = []
  for port in port_list:
    sockaddr = (host,port)
    socktype = socket.SOCK_STREAM
    s = None

    # create a socket
    try:
      s = socket.socket(family, socktype)
    except socket.error as msg :
      # quietly ignore the error
      # print " * ERROR creating socket:", msg
      s = None
      continue

    # connect to the socket
    try:
      # print "\n\nTrying %s:%d (%d)" % (sockaddr[0],sockaddr[1],socktype)
      s.settimeout(0.2)
      s.connect(sockaddr)
      s.shutdown(socket.SHUT_RDWR)
      # print " + Connected to %s:%d (%s)" % (host,port,socktype)
      found_ports.append(port)
    except socket.error as msg:
      # quietly ignore the error
      # print " * ERROR connecting:", msg
      s.close()
      s = None
      continue

    time.sleep(interval) # take a little nap between checks

  if len(found_ports) > 0:
    found_ports.sort()
    print("Found %s" % str(found_ports))
    print("\0337")

print("\n\nScan complete.")
