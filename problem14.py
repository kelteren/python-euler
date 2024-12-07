"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2    (n is even)
n -> 3n+1   (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13-> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# solved

def next(n):
    if(n % 2 == 0):
        return round(n/2)
    else:
        return round(3*n + 1)

stop        = 1_000_000
# stop        = 1_000
maxChain    = 0
maxTerm     = 0

for i in range(2, stop+1):
    num = i
    chain_length=1

    while(num != 1):
        # print(f'{num} -> ',end='')
        num = next(num)
        chain_length += 1
    
    if (chain_length+1) > maxChain:
        maxChain = chain_length + 1
        maxTerm = i

print(f"Chain is {maxChain} items long for item {maxTerm}")

# solved
