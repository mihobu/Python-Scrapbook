#! /usr/bin/python

import crypt
import random

saltstr = "./abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
salt = saltstr[random.randint(1,len(saltstr))] + saltstr[random.randint(1,len(saltstr))]

passwd = raw_input('Password: ')
cryptedpass = crypt.crypt(passwd,salt)
print "Hash: %s" % cryptedpass
