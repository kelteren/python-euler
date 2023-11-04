'''
The prime factors of 13195 are 5, 7,13 and 29.

What is the largest prime factor of the number 600851475143?
'''

number = 600851475143

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

def primefactors(n):
	# loop from or towards n and check if disible with prime numbers 
	# return list of prime factors, as iterable?

primefactors(number) 