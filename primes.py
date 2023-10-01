"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(number):
    if number<2:
        return False
    elif number==2 or number==3 or number==5 or number==7:
        return True
    else:
        if number%2 !=0 and number%3 !=0 and number%5 !=0 and number%7 !=0 :
            return True

def primes(number_of_primes):
    list = []

    if number_of_primes<1:
        raise ValueError("The number can't be lower than 1")
    
    i=0
    while len(list) < number_of_primes:
        if isPrime(i):
            list.append(i)
        i += 1
        
    return list
          
