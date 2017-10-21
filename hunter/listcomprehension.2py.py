#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      14cse013
#
# Created:     21/10/2017
# Copyright:   (c) 14cse013 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print S;
print V;
print M
