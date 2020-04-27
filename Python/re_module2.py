import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())  # position (start- and end-position) of the first match occurrence

x = re.search(r"\bS\w+", txt)
print(x.string) # Print the string passed into the function

x = re.search(r"\bS\w+", txt)
print(x.group()) # Print the part of the string where there was a match.

# Output:
# ------
# (12, 17)
# The rain in Spain
# Spain

# using re.compile() and saving the resulting regular expression object
# for reuse is more efficient when the expression will be used several times
# in a single program
com = re.compile('ai')
x = com.search(txt)
print(x)
x = com.match(txt)
print(x)