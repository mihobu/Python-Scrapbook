#! /home/mhb/anaconda2/bin/python

# This is a test script.
# Load the TOP 100 English words, in encrypted form, into a dictionary.

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
