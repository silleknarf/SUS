#!/usr/bin/python

#
# SUS - A quick and dirty usability scale
# Takes the answers to SUS questions 1 to 10 as a position number from 1-5
# on the command like and oututs the SUS Score 
#
# 	Usage:
# 	./SUS.py 4152514231
#			
# 	yields - 85
#		
# The answer to Q1 is:  5 - Strongly Agree
# The answer to Q10 is: 1 - Strongly Disagree 
#

import sys
number = sys.argv[1]

total = 0
# Get the position numbers and digits of the input
for position, digit in enumerate([int(d) for d in number]):
	# If the position number is 1,3,5,7,9
	if position % 2 == 0:
		# Subtract one from the input and add it to the running total
		total += (int(digit) - 1)
	# If the position number is 2,4,6,8,10
	else:
		# Add 5 - input to the running total
		total += (5 -  int(digit))

# To get a score out of 100
total *= 2.5
print total
