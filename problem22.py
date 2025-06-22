# problem22.py

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53 , is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

# solved poorly


alfabet = 'abcdefghijklmnopqrstuvwxyz'

def name_value(name: str) -> int:
    # Calculate alphabetical value (A=1, B=2, ..., Z=26)
    return sum(ord(char) - ord('A') + 1 for char in name)


def score(name:str, name_list:[str]) -> int:
	score = 0

	# loop through name, find first factor
	name = name.lower()
	for char in name:					# loop through each character in the name
		factor_1 = 0 					# sets factor to 0
		for count in alfabet: 			# loop though the alphabet, increments the counter and checks  
			factor_1 += 1  				# for equality with current character
			if count == char:
				score += factor_1
				break

	# factor_1 = name_value(name)

	# loop through namelist, find second factor
	name_counter = 0
	for word in name_list:
		name_counter += 1
		if word.lower() == name:
			score = score * name_counter
	return score

# TODO create a function that uses a direct value assignment
def name_value():
	pass 	# use direct function for calculating name value

with open('0022_names.txt') as f:
	content = f.read()

# sanitizing the name liste
names = content.strip().strip(',').split(',')
names = [name.strip('"') for name in names]
names.sort()

# testing with the testvector 'Colin', known to yield '49714'
# print(score('COLIN', names))

total_score_of_all_names = 0


# TODO replace with a list comprehension and 
for name in names:
	total_score_of_all_names += score(name, names)

print(total_score_of_all_names)

# solved poorly