#! /home/mhb/anaconda2/bin/python

# cracker2.py -- Read some ciphertext and attempt to crack it.
#
# by Michael Burkhardt (mburkhardt@smu.edu)
# February 13, 2016

# ----------------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------------

import sys
import re

# ----------------------------------------------------------------------------
# FUNCTION to decode ciphertext: decode(k,t)
# where k is the key and t is the ciphertext.
# Returns: decoded string
# ----------------------------------------------------------------------------
def decode(k,t):
  shift_ltr = k
  shift_dig = shift_ltr % 9 + 1

  # ----------------------------------------------------------------------------
  # Decode the plaintext
  # ----------------------------------------------------------------------------
  decoded_text = ""
  for c in t:
    # handle replacement for capital (English) letters
    if re.search("[A-Z]",c):
      c = ((ord(c) - shift_ltr - 65) % 26) + 65
    elif re.search("[a-z]",c):
      c = ((ord(c) - shift_ltr - 97) % 26) + 97
    elif re.search("[0-9]",c):
      c = ((ord(c) - shift_dig - 48) % 10) + 48
    else:
      # do not shift other characters
      c = ord(c)

    decoded_text = decoded_text + chr(c)
  
  return decoded_text

# -----------------------------------------------------------------------------
# Load the TOP 100 English words, in encrypted form, into a dictionary.
# -----------------------------------------------------------------------------

keymatch = {} # empty dictionary
dupes = 0
with open('top100crypt.txt','r') as f:
  for line in f:
    (encword,key) = line.split()
    #print "word: %s, key: %s" % (encword,key)
    if keymatch.get(encword) == None:
      keymatch[encword] = int(key)
    else:
      dupes = dupes + 1
 
# print summary
print "There are %d words in the dictionary." % len(keymatch)
print "discarded %d dupes" % dupes

# ----------------------------------------------------------------------------
# Prompt for ciphertext
# ----------------------------------------------------------------------------

ciphertext = raw_input("Enter ciphertext to decrypt: ")
ciphertext_lc = ciphertext.lower() # make an all-lowercase copy

# ----------------------------------------------------------------------------
# Initialize the keycounts array, in which we'll track counts of keys that
# correspond to matches found in the ciphertext for the 100 most common
# English words.
# ----------------------------------------------------------------------------

keycounts = [0] * 26

# ----------------------------------------------------------------------------
# For each word in the ciphertext, look at the list of encrypted common words.
# Count the number of times each key matches.
# ----------------------------------------------------------------------------

for word in ciphertext_lc.split():
  k = keymatch.get(word)
  if k != None:
    #print "Found a match: %s" % word
    keycounts[k] = keycounts[k] + 1

mx = max(keycounts)
key = keycounts.index(mx)

if mx == 0:
  print "I am stuck, so will proceed with brute force attack."
  for key in range(1,26):
    print "[key=%2d] %s" % (key,decode(key,ciphertext))
else:
  print "I found %d matching words with key %d." % (mx,key)
  print "Therefore, I'm concluding that the correct decryption key is %d." % key
  print "The decoded phrase is: %s" % decode(key,ciphertext)

