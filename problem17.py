'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
(three hundred and forty-two) contains letters and (one hundred and fifteen) contains letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

# unsolved


# defining functions

def num_to_letter(num):
	match num:
		case 0:
			return "zero"
		case 1:
			return "one"
		case 2:
			return "two"
		case 3:
			return "three"
		case 4:
			return "four"
		case 5:
			return "five"
		case 6:
			return "six"
		case 7:
			return "seven"
		case 8:
			return "eight"
		case 9:
			return "nine"
		case 10:
			return "ten"
		case 11:
			return "eleven"
		case 12:
			return "twelve"
		case 13:
			return "thirteen"
		case 14:
			return "fourteen"
		case 15:
			return "fifteen"
		case 16:
			return "sixteen"
		case 17:
			return "seventeen"
		case 18:
			return "eighteen"
		case 19:
			return "nineteen"
		case 20:
			return "twenty"
		case 30:
			return "thirty"
		case 40:
			return "fourty"
		case 50:
			return "fifty"
		case 60:
			return "sixty"
		case 70:
			return "seventy"
		case 80:
			return "eighty"
		case 90:
			return "ninety"

def num_letters(word:str):   # useless function
	return len(word)

def num2words(num):
	# return number as written out in words
	enere = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tiere = [None,None,'twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

	if 0 <= num <= 9:
		return enere[num]
	elif 10 <= num <= 19:
		return enere[num]
	elif 20 <= num <= 90 and num % 10 == 0:
		return tiere[num//10]
	elif 20 <= num <= 100:
		return tiere[num//10] + enere[num % 10]
	else:
		pass

for i in range(0,67):
	print(num2words(i))

# solving the case
letters = 0
upper_limit = 1000

for number in range(1 , upper_limit + 1):

	# do something with number to determine amount of letters

	letters += number
	pass

# print(letters)

# unsolved