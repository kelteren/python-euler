'''Largest Palindrome Product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#solved

def isPalindrome(num):
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
larges_palindrome = 0

for x in range(999,99,-1):
	for y in range(999,99,-1):
		product = x*y
		if (isPalindrome(x*y) and product > larges_palindrome):
			larges_palindrome = product
			palY = y
			palX = x
			
print("Largest palindrome is " + str(larges_palindrome) + " and consists of " + str(palX) + " and " + str(palY) )

#solved
