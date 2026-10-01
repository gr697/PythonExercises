import math
'''
Question 1:

Write a function(s) that converts an octal number, represented as a string into its decimal value.
'''

def octalToDecimal(oct):
  thou = oct // 1000
  hund = (oct - thou) // 100
  ten = (oct - (thou*100) - (hund*100))// 10
  digit = (oct - (thou*100) - (hund*100) - (ten*10))
  print(ten)
  print(digit)
  return (thou * pow(8,3) + (hund*pow(8,2)) + (ten*pow(8,1)) + (digit*pow(8,0)))

'''
Question 2: 

Write a function(s) that prints out a tree shape (see below). The function should take two arguments: a tree width and a trunk height. For example, the arguments 9 and 4 will print out a tree of width 9 and trunk length 4, as shown below:

    *
   ***
  *****
 *******
*********
   ***
   ***
   ***
   ***

You can assume that the width of the tree will be odd and hence every line will have an odd number of asterisks. The trunk will always have a width of three asterisks.
'''

def printTree(width,trunk):
  print("    *")
  print("   ***")
  print("  *****")
  print("   ***")
  print("   ***")


