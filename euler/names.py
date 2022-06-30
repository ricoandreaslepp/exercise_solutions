# sort it in alphabetical order
# calc alphabetical value
# multipy the value by its position
# what is the total score
import re
import string

total = 0
a = " " + string.ascii_uppercase

with open("names.txt") as f:
    names = f.readline()
    
def check_value(x):
    return False if ',' in x else True

def get_alpha_value(name):
    val = 0
    for ch in name:
        val += a.index(ch)
    return val

names = sorted(list(filter(check_value, re.split('"|", "', names))))[1:]

for ind, name in enumerate(names):
    total += get_alpha_value(name)*ind

print(total)
    

