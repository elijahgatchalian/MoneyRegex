# Eli Gatchalian
# April 22, 2016
# CPSC 3400 - P3
# Version 1 - Python 3.5.1

# This program reads in a file full of prices. Using regular expression, the
# program fills three files (bucks.txt, sale.txt, misc.txt) with valid prices.
# Valid prices for bucks.txt are in the form of $x where x is any digit that 
# does not begin with zero. Valid prices for sale.txt are in the form $x.99
# where x must meet the same criteria in bucks.txt. Valid prices for misc.txt 
# are in the form $x.bc where x must meet the same criteria as previous files
# and b and c are single digits that cannot be nine at the same time.
# Example Command Line: python3 MoneyRegex.py testFile.txt

import re
import sys
import itertools

bucks = open("bucks.txt", "w")
sale = open("sale.txt", "w")
misc = open("misc.txt", "w")
print("Outputting to...\n bucks.txt\n sale.txt\n misc.txt")

user_file = open(sys.argv[1],"r")
all_prices = []
for money in user_file:
    all_prices.append(money)

# Bucks
bucks_pattern = re.compile(r"""    \$[1-9][0-9]*$         | # By itself
                                    \$[1-9][0-9]*\s       | # White space after buck
                                    \$[1-9][0-9]*\n$      | # New line after buck
                                    \$[1-9][0-9]*\.\s    | # Buck followed by period and whitespace
                                    \$[1-9][0-9]*\.\n      # Buck followed by period and new line
                                    """,re.VERBOSE)
valid_bucks = []
bucks.write("a) bucks.txt: all prices in the form $x:\n")
for n in all_prices:
    valid_bucks.append(re.findall(bucks_pattern,n))
valid_bucks = list(itertools.chain.from_iterable(valid_bucks))
for price in valid_bucks:
    price = price.replace('.','')
    bucks.write(str(price) + '\n')

# Sale
sale_pattern = re.compile(r"""    \$[1-9][0-9]*\.[9]{2} # Find valid buck with .99
                            """,re.VERBOSE)
valid_sale = []
sale.write("b) sale.txt, all prices in the form $x.99:\n")
for n in all_prices:
    valid_sale.append(re.findall(sale_pattern, n))
valid_sale = list(itertools.chain.from_iterable(valid_sale))
for price in valid_sale:
    sale.write(str(price) + '\n')

# Misc
misc_pattern = re.compile(r"""    \$[1-9][0-9]*\.[0-8][0-9]     | # Prevents .99
                                    \$[1-9][0-9]*\.[0-9][0-8]     # Prevents .99
                            """,re.VERBOSE)
valid_misc = []
misc.write("c) misc.txt all other prices:\n")
for m in all_prices:
    valid_misc.append(re.findall(misc_pattern, m))
valid_misc = list(itertools.chain.from_iterable(valid_misc))
for price in valid_misc:
    misc.write(str(price) + '\n')
