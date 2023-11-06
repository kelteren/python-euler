"""Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# solved

def testDivisibility(divident, divisors):
	for i in range(1,divisors+1):
		if divident % i != 0:
			return False
	return True

i = 1
found = False

while found != True:
	if testDivisibility(i,20):
		print(i)
		found = True
		break
	i += 1

# solved
