"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # Your code here
    x = 0
    o = 0

    for i in range(0, len(txt)):
        if txt[i] == 'x' or txt[i] == 'X':
            x += 1
        elif txt[i] == 'o' or txt[i] == 'O':
            o += 1

    print(f"x = {x} o = {o}")
    if x == o:
        return True
    elif x > o or o > x:
        return False

print(XO("oOxXm"))
    
        
