#! /home/mhb/anaconda2/bin/python

# Borrows some code from http://goo.gl/hSH1UN

import socket,struct

def makeMask(n):
    "return a mask of n bits as a long integer"
    return (2L<<n-1) - 1

def dottedQuadToNum(ip):
    "convert decimal dotted quad string to long integer"
    return struct.unpack('L',socket.inet_aton(ip))[0]

def networkMask(ip,bits):
    "Convert a network address to a long integer" 
    return dottedQuadToNum(ip) & makeMask(bits)

def addressInNetwork(ip,net):
   "Is an address in a network"
   return ip & net == net

ipaddrstr = "192.168.192.0"
address = dottedQuadToNum(ipaddrstr)
networka = networkMask("10.0.0.0",24)
networkb = networkMask("192.168.0.0",24)

print (address,networka,networkb)

print "\nIs %s in network %s?" % (address,networka)
print addressInNetwork(address,networka)

print "\nIs %s in network %s?" % (address,networkb)
print addressInNetwork(address,networkb)
