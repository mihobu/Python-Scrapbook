#! /home/mhb/anaconda2/bin/python

# *****************************************************************************
# This is a very short script that shows how to deal with command line
# arguments in Python. Based on a found example: http://goo.gl/6gWBEP
# 01 Feb 2016 - Michael Burkhardt
# *****************************************************************************


import sys, getopt


# *****************************************************************************
# A funtion called "main"
# *****************************************************************************

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   print 'There are %d arguments.' % len(args)
   print 'Stringified: %s' % str(args)

   if not inputfile:
     print "Error: input file not specified."
   else:
     print 'Input file: %s' % inputfile

   if not outputfile:
     print "Error: output file not specified."
   else:
     print 'Output file: %s' % outputfile


# *****************************************************************************
# The real main line
# *****************************************************************************

if __name__ == "__main__":
   main(sys.argv[1:])
