"""
Calculates the total of all name scores from a list of names.

The script reads a list of names from a file, sorts them alphabetically,
calculates each name's alphabetical value, multiplies it by its position
in the list, and sums all resulting scores.

Attributes:
    names (TYPE): Alphabetically sorted list of names from the input file.
    total_score_of_all_names (int): Sum of all calculated name scores.
"""
# problem22.py

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53 , is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?

# solved and optimized

def name_score(name: str) -> int:
    """
    Calculates the alphabetical value of a given name.

    Each letter is assigned a value corresponding to its position in the alphabet
    (A=1, B=2, ..., Z=26), and the total score is the sum of these values.
    
    Args:
        name (str): The uppercase name string that shall be used for calculating the worth of the characters in the name.
    
    Returns:
        int: Calculated worth of the characters in the name string
    """
    # Calculate alphabetical value (A=1, B=2, ..., Z=26)
    return sum(ord(char.upper()) - ord('A') + 1 for char in name)

with open('0022_names.txt') as file:
	names = file.read()

# sanitizing the name list and sorting
names = names.strip().split(',')
names = [name.strip('"') for name in names]
names.sort()

total_score_of_all_names = 0

for index, name in enumerate(names):
	total_score_of_all_names += (index + 1) * name_score(name)

	# testing with the testvector 'Colin', known to yield '49714'
	# print(score('COLIN', names))

	# if(name == 'COLIN'):
	# 	print('found',index,name)
	# 	nv:str = name_score(str(name))
	# 	print(f'Score = {index+1} * {nv} = {(index+1)*nv} ')

print(total_score_of_all_names)

# solved and optimized