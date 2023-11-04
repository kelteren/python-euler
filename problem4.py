'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# solution goes here

def isPalindrome(num:int):
	# check if num * num yields a palindrome, return true if palindrome or false otherwise
	pass


for i in range(999,0,-1):
	if isPalindrome(i):
		print(i)
		break