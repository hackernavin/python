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

st=raw_input("enter the number")
n=int(input("enter the string"))

def Exploder(string,n):
 print(string*n)
def Myfun(string,exploder,n):
    exploder(string,n)

 Myfun(st,exploder,n)