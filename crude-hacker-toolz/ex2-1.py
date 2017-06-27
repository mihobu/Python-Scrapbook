#! /usr/bin/python

# ex2-1.py -- Example using the zipfile package to extract contents of
#             a given zip file using a supplied password
#
# by Michael Burkhardt (mburkhardt@smu.edu)
# January 21, 2016

# ----------------------------------------------------------------------------
# Libraries
# ----------------------------------------------------------------------------
import zipfile

# ----------------------------------------------------------------------------
# Extract the zip file contents
# ----------------------------------------------------------------------------
zf = zipfile.ZipFile("evil.zip","r") # Open the zip file
zf.extractall(pwd="secret")
zf.close()
