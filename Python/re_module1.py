import  re

txt = "The rain in Spain"
print('**************** search() ******************')
x = re.search('^Th.*Spain$', txt)
print(x) # Return Match object if matches otherwise None
# <_sre.SRE_Match object at 0x00557E58>

print('**************** findall() ******************')
x = re.findall("ai", txt)
print(x) # Returns a list containg all matches otherwise []
# ['ai', 'ai']

print('**************** split() ******************')
x = re.split("\s", txt) # Split at each white-space character:
print(x)
# ['The', 'rain', 'in', 'Spain']

# You can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s", txt, 2) 
print(x)
# ['The', 'rain', 'in Spain']

print('**************** sub() ******************')
x = re.sub("\s", "9", txt) # Replace white space character with 9
print(x)
# The9rain9in9Spain

# You can control the number of replacements by specifying the count parameter
x = re.sub("\s", "9", txt, 2)
print(x)
# The9rain9in Spain

# re.search() checks for a match anywhere in the string 
x = re.search('ai', txt)
print(x)
# <_sre.SRE_Match object at 0x002CCA68>

print('**************** match() ******************')
# re.match() checks for a match only at the beginning of the string
x = re.match('ai', txt)
print(x)
# None

print('**************** finditer() ******************')
x = re.finditer('ai', txt)
print(x)
for i in x:
    print('i: ', i.span())
# In MULTILINE mode: match() only matches at the beginning of the string
#                    search() with a regular expression beginning with '^' will match at
#                    the beginning of each line.
x = re.match('X', 'A\nB\nX', re.MULTILINE)  # No match
y = re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match
print(x, y)
# (None, <_sre.SRE_Match object at 0x002CCA68>)
