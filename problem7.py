"""10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

# solved

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

i = 0
count = 0
NotFound = True

while NotFound:
    i = i + 1
    if isPrime(i):
        count = count + 1

    if count == 10001:
        print(count)
        print(i)
        NotFound = False

# solved

