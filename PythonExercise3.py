
''' 
 Write a function which returns true if a number is divisible by 3 and  false if it is not.  Hint: use the modulo (%) operator.

 Modify your code so that your function now returns true if a number is divisible by 3 or 5 and false if it is not.
'''

def mod(number, by):
  if number%by == 0:
    return "true"
  else:
    return "false"