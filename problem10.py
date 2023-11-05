"""Summation of Primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

# solved

limit = 2000000
sumPrimes = 0

def isPrime(num):
    if num <= 1:
        return False
    
    if num ==2 :
        return True

    if num % 2 == 0:
    	return False
    
    for i in range(3, int(num**0.5) + 1,2):
        if num % i == 0:
            return False
    return True


for number in range(limit):
	if isPrime(number):
		sumPrimes += number

print(sumPrimes)

# solved
