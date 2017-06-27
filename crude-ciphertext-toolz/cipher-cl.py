#! /home/mhb/anaconda2/bin/python

# cipher-cl.py -- Command line version of the cipher.py
#                 useful for batch-encoding many short (e.g. one-word) messages
#
# Usage: cipher-cl.py <ciphertext> <key>
#
# by Michael Burkhardt (mburkhardt@smu.edu)
# February 13, 2016

# ----------------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------------

import sys
import re

# ----------------------------------------------------------------------------
# get inputs from command line - no error checking :-(
# ----------------------------------------------------------------------------
plaintext = sys.argv[1]
shift_s   = sys.argv[2]

# ----------------------------------------------------------------------------
# Check for empty plaintext string and replace with something useful. 
# ----------------------------------------------------------------------------
if plaintext == "":
  #plaintext = "Warning! You have 76,543 unread messages in your INBOX."
  plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
  #print "Empty plaintext string, using default:\n%s" % plaintext

# ----------------------------------------------------------------------------
# Convert shift input to int; if failure pick arbitrary default
# ----------------------------------------------------------------------------
try:
  shift_ltr = int(shift_s)
except ValueError:
  print "ERROR: Invalid input for shift value"
  sys.exit(0)

# ----------------------------------------------------------------------------
# Validate the shift value provided by the user
# ----------------------------------------------------------------------------
if shift_ltr < 1 or shift_ltr > 25:
  print "ERROR: Shift value must be in the range 0 to 25."
  sys.exit(0)

# ----------------------------------------------------------------------------
# Shift value for digits must be in the range 1 to 9 (inclusive)
# if shift_ltr > 9, then compute a special value.
# ----------------------------------------------------------------------------
shift_dig = shift_ltr % 9 + 1  # force to value between 1 and 9 (inclusive)
#if shift_ltr > 9:
  #print "Shift value for digits: %d" % shift_dig

# ----------------------------------------------------------------------------
# Encode the plaintext
# ----------------------------------------------------------------------------
encoded_text = ""
for c in plaintext:
  # handle replacement for capital (English) letters
  if re.search("[A-Z]",c):
    c = ((ord(c) + shift_ltr - 65) % 26) + 65
  elif re.search("[a-z]",c):
    c = ((ord(c) + shift_ltr - 97) % 26) + 97
  elif re.search("[0-9]",c):
    c = ((ord(c) + shift_dig - 48) % 10) + 48
  else:
    # do not shift other characters
    c = ord(c)

  encoded_text = encoded_text + chr(c)

print "%s\t%d" % (encoded_text,shift_ltr)
