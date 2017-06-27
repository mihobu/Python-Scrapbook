#! /usr/bin/python

# ex2-3.py -- Run a dictionary attack against a zip file.
# 
# Michael Burkhardt
# January 21, 2016

# ----------------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------------
import zipfile
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
#f = open("HW1-dictionary.txt","r") # short test dictionary
f = open("words","r") # /usr/share/dict/words from MacOS
dict = f.readlines()
f.close()
print "There are %d words in the dictionary." % len(dict)

# ----------------------------------------------------------------------------
# Open the zip file
# ----------------------------------------------------------------------------
zf = zipfile.ZipFile("evil.zip","r")

# ----------------------------------------------------------------------------
# Run the attack
# ----------------------------------------------------------------------------
cracked = False
crackedPW = ""
attempt = 0
err_runtime = 0
err_other = 0
for word in dict:
  word = word.strip()
  attempt = attempt + 1
  anim(attempt)
  #print "Attempt %d, pwd=%s" % (attempt,word)
  try:
    zf.extractall(pwd=word)
    cracked = True
    crackedPW = word
    break
  except RuntimeError:
    # Occasionally, the check_byte matches even when the password is incorrect.
    # In this case, a RuntimeError exception is thrown. Because of this, I'll
    # simply ignore these exceptions when/if they happen.
    nop = True
    err_runtime = err_runtime + 1
  except BaseException as error:
    # Some other error occurred. Take note quietly and move on.
    #print('An exception occurred: {}'.format(error))
    #print "Unexpected error:", sys.exc_info()[1]
    err_other = err_other + 1
zf.close()
print "\n"

# ----------------------------------------------------------------------------
# Report errors
# ----------------------------------------------------------------------------
if err_runtime > 0:
  print "I ignored %d runtime errors" % err_runtime
if err_other > 0:
  print "I ignored %d unknown errors" % err_other

# ----------------------------------------------------------------------------
# Report results
# ----------------------------------------------------------------------------
if cracked:
  print "The password is: %s" % crackedPW
  print "It took %d attempts." % attempt
else:
  print "Could not crack the password after %d attempts :-(" % attempt

