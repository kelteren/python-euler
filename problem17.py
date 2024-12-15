'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
(three hundred and forty-two) contains letters and (one hundred and fifteen) contains letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

# unsolved


# defining functions

def num_letters(word:str):   # useless function
	return len(word)

def num_to_letter(num):
	match num:
		case 1:
			return "one":
		case 2:
			return "two":
		case 3:
			return "three":
		case 4:
			return "four":
		case 5:
			return "five":
		case 6:
			return "six":
		case 7:
			return "seven":
		case 8:
			return "eight":
		case 9:
			return "nine":
		case 10:
			return "ten":
		case 11:
			return "eleven":
		case 12:
			return "twelve":
		case 13:
			return "thirteen":
		case 14:
			return "fourteen":
		case 15:
			return "fifteen":
		case 16:
			return "sixteen":
		case 17:
			return "seventeen":
		case 18:
			return "eighteen":
		case 19:
			return "nineteen":
		case 20:
			return "twenty":
		case 30:
			return "thirty":
		case 40:
			return "fourty":
		case 50:
			return "fifty":
		case 60:
			return "sixty":
		case 70:
			return "seventy":
		case 80:
			return "eighty":
		case 90:
			return "ninety":

def num2words(num):
	# return number as written out in words
	pass

# testing functions
# print(num_letters('five three one'))


# solving the case
letters = 0

for number in range(1,1000 + 1):
	# do something with number
	letters += number
	pass

print(letters)

# unsolved