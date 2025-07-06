'''Largest Prime Factor
The prime factors of 13195 are 5, 7,13 and 29.

What is the largest prime factor of the number 600851475143?
'''

# solved

number = 600851475143

# def isPrime(num):
#     if num <= 1:
#         return False
    
#     if num ==2 :
#         return True

#     if num % 2 == 0:
#     	return False
    
#     for i in range(3, int(num**0.5) + 1,2):
#         if num % i == 0:
#             return False
#     return True

def primefactors(n):
	# loop from or towards n and check if divisible with prime numbers 
	# return list of prime factors, as iterable?
    i = 2
    while i**2 < n:
        while n % i == 0:
            n = n / i
        i += 1
    return int(n)

print(primefactors(number)) 

# solved
