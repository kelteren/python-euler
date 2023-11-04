"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

limit = 1000000000 # adding limit just for avoiding endless loops, hopefully a solution is within limit

def testDivisibility(divident: int, divisors:int):
	for i in range(divisors+1):
		if divident % i != 0:
			return False
	return True

for i in range(10+1):
	print(i)