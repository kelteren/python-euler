'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
(three hundred and forty-two) contains letters and (one hundred and fifteen) contains letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

# solved

import math

def num2words(num:int) -> str:
	# return number as written out in words
	enere = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tiere = [None,None,'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

	if 0 <= num <= 9:
		return enere[num]
	elif 10 <= num <= 19:
		return enere[num]
	elif 20 <= num <= 90 and num % 10 == 0:
		return tiere[num // 10]
	elif 20 <= num < 100:
		return tiere[num // 10] + '-' + enere[num % 10]
	elif 100 <= num <= 900 and num % 100 == 0:
		return enere[num // 100] + ' hundred '
	elif 100 < num < 1000:
		return enere[num // 100] + ' hundred and ' + num2words(num % 100)
	elif 1000 < num < math.inf:
		pass 
	elif num == 1000: 
		return 'one thousand'
	else:
		raise ValueError('ugyldig inngangsfaktor')

letters = 0
upper_limit = 1000

for number in range(1 , upper_limit + 1):
	word = num2words(number)
	letters += len(word.replace(" ","").replace("-",""))

	# prints number, words, trimmed words and length to terminal
	print(number, end = ' - ')
	print(word, end = ' - ')
	print(word.replace(" ","").replace("-",""), end = ' - ')
	print(len(word.replace(" ","").replace("-","")))

print(letters)

# solved