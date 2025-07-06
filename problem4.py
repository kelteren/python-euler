'''Largest Palindrome Product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Attributes:
    largest_palindrome (int): The largest palindrome found
    palX (int): First factor of palindrome 
    palY (int): Second factor of palindrome
'''

# solved


def isPalindrome(num):
    """Checks whether a number num is a palindrome

    Args:
        num (INT): parameter to be checked if is a palindrome

    Returns:
        Boolean: TRUE if if num is palindrome. False if number is not palindrome
    """
    original_num = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    if reverse == original_num:
        return True
    else:
        return False


palY = 0
palX = 0
largest_palindrome = 0

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        product = x*y
        if (isPalindrome(x*y) and product > largest_palindrome):
            largest_palindrome = product
            palY = y
            palX = x

print("Largest palindrome is " + str(largest_palindrome) +
      " and consists of " + str(palX) + " and " + str(palY))

# solved
