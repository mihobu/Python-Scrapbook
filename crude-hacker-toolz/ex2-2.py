#! /usr/bin/python

# ex2-2.py -- Prompt user to enter a password, then use the zipfile package
#             to extract contents of a zip file using that password.
#             In the process, catch any thrown exceptions."""
#
# by Michael Burkhardt (mburkhardt@smu.edu)
# January 21, 2016

# ----------------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------------
import zipfile
import sys

# ----------------------------------------------------------------------------
# Interactively prompt user for a password
# ----------------------------------------------------------------------------
word = raw_input("Please enter a password: ")

# ----------------------------------------------------------------------------
# Extract the zip file contents, with exception handling
# ----------------------------------------------------------------------------
zf = zipfile.ZipFile("evil.zip","r")
try:
  zf.extractall(pwd=word)
except BaseException as error:
  # Catch any kind of exception (not normally advisable)
  print('An exception occurred: {}'.format(error))
zf.close()
