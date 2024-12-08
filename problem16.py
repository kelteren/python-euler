'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number  2^1000?
'''

# solved

def tverrsum(num):
	if(num < 10):
		return num
	else:
		# return tverrsum(num/10) + (num % 10)
		return num % 10 + tverrsum(num // 10)

def eksponert(base,eksponent):
	produkt = 1 
	for i in range(1,eksponent+1):
		produkt = produkt * base
	return produkt

base = 2
exp  = 1000

print(tverrsum(eksponert(base,exp)))

# solved
