import math
'''
Question 0:

Complete the recursive function below which performs multiplication of two  numbers without using the inbuilt * sign
'''

def multiply(number, by):
 if by == 0:
  return 0
 else:
  return number + multiply(number,by-1)



'''
Question 1: 
 
 Complete the function below which takes in an integer input between zero and one hundred (0 ≤ n ≤ 100) and prints out the number expressed in English text, with spaces and no dashes (–), e.g. for the number “33”, we would expect to see “thirty three”. Hint: you may want to create additional functions to help.
 
 Call this function from the main to test your program.
'''

def numberToText(value):
  if value <= 10:
    result = digit(value)
  if value <=12:
    result = bespokeNumbers(value)
  if value <20:
    result = firstPart(value%10) + "teen"
  if value <=99:
    result = firstPart(value//10) + "ty" + digit(value%10)
  if value == 100:
    result = "one hundred"
  return result

def firstPart(value):
 if value == 2:
    return "Twen"
 if value == 3:
   return "Thir"
 if value == 4:
    return "For"
 if value == 5:
     return "Fif"
 if value == 6:
    return "Six"
 if value == 7:
    return "Seven"
 if value == 8:
    return "Eigh"
 if value == 9:
    return "Nine"

def bespokeNumbers(value):
  if value == 11:
    return "eleven"
  if value == 12:
    return "twelve"



def digit(value):
  if value <= 0:
    return "zero"
  if value == 1:
    return "one"
  if value == 2:
    return "two"
  if value == 3:
    return "three"
  if value == 4:
    return "four"
  if value == 5:
    return "five"
  if value == 6:
    return "six"
  if value == 7:
    return "seven"
  if value == 8:
    return "eight"
  if value == 9:
    return "nine"
  if value == 10:
    return "ten"
  else:
    return -1




'''
Question 2: 
 
 Complete the function below that calculates, and returns, the distance between two points.
 
 Call this function from the main to test your program. Hint: may wish to use the following print statement in your main function, or similar: 

 printf("%1.2f\n", calculateDistance(0, 0, 4, 3));
'''

def calculateDistance(x1, y1, x2, y2):
 xNew = (x2-x1)
 yNew = (y2-y1)
 result = math.pow(xNew,2)+ math.pow(yNew,2)
 result = math.sqrt(result)
 return result;


''' 
Question 3: 
 
 Complete the function below that is given an integer, n, where 1 ≤ n ≤ 9999 and prints whether it is even, odd, or/and prime.  The output should be whole sentences for example, 

 1 is odd and not prime.
 2 is even and prime.
 3 is odd and prime.
 4 is even and not prime.
 5 is odd and prime
 
 Call this function from the main to test your program.
'''

def printOddEvenAndOrPrime(n):
  print(str(n) + " is " + checkEven(n) + " and " + checkPrime(n))
  
def checkEven(n):
  remainder = n%2
  if remainder == 0:
    return "even"
  return "odd"

def checkPrime(n):
  if n < 2:
    return "not prime"
  for i in range(2,n):
    result = n%i
    if result == 0:
      return "not prime"
  return "prime"
 

  