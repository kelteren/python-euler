"""Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Attributes:
    found (bool): Description
    i (int): Description
"""

# solved


def testDivisibility(divident, divisors):
    """Summary

    Args:
        divident (int): number to be tested whether is divisible by all numbers in divisors
        divisors (int): upper bound for list of divisors 

    Returns:
        boolean: returns whether divident is divisible by all divisors
    """
    for i in range(1, divisors+1):
        if divident % i != 0:
            return False
    return True


i = 1
found = False

while found != True:
    if testDivisibility(i, 20):
        print(i)
        found = True
        break
    i += 1

# solved
