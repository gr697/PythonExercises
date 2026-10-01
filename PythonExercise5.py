import math
'''
Write a function(s) to implement the Sieve of Eratosthenes algorithm 

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  

This algorithm is used to find all the prime numbers less than or equal to a given integer \verb+n+.  

You should write 2 functions.  One function should implement the Sieve of Eratosthenes algorithm using a list stored as a global variable.  The second function should print whether the given integer is prime or not prime by using the generated list from the first function
'''

def createList(n):
    A = [True]*(n+1)

    for i in range(2,int(math.sqrt(n))+1):
        if A[i]:
            for j in range(i*i, n+1, i):     #range(start,stop,step)
                A[j] = False
    for i in range(2,n+1):
        if A[i]:
            print(i)
