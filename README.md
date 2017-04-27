SUS - A quick and dirty usability scale calculator
==================================================

Overview of SUS
===============

The [System Usability Scale](https://en.wikipedia.org/wiki/System_usability_scale) is 10 question test where participants are asked to score the following 10 items with one of five responses that range from Strongly Agree to Strongly disagree:

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

Usage
=====

Takes the answers to SUS questions 1 to 10 as a position number from 1-5 on the command like and outputs the SUS Score.
The numbers range from 1 - Strongly Disagree to 5 - Strongly Agree.

    Usage:
    ./SUS.py 4152514231
	
    yields - SUS Score: 85

    # The answer to Q3 is:  5 - Strongly Agree
    # The answer to Q10 is: 1 - Strongly Disagree 
