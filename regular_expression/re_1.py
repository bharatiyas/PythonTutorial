# We need to import the built-in module re

import re

in_string = "abcd"
pattern = "e"

print(re.match(pattern, in_string))		# In this case match will return None because there is no match.

pattern = "a"
print(re.match(pattern, in_string))		# In this case match will return a Match object with where the match was found

if re.match(pattern, in_string):
	print("Match found")
else:
	print("Match not found")

in_string = "bcda"
if re.match(pattern, in_string):
	print("Match found")
else:
	print("Match not found")		# Match is not found because 'a' is at the end of the in_string

# re.match() looks for the match at the begining of the match. When we want to pattern matching to happen throughout the
# whole string we use re.search()

in_string = "bcda"
if re.search(pattern, in_string):
	print("Match found by search()")
else:
	print("Match not found by search()")


# Meta Characters - Special set of chars which create a pattern which should be matched. They are used to create complex
# patterns which can be matched to a string.


# * - Makes sure that a particular character preceding it is present >= 0 times.
# In the following example it will look for 'a' at the start, 'b' to be present 0 or more times, 'c' at the end
pattern = r"ab*c"		# Make it a raw string because we have '*'
in_string = "abbcd"
re.match(pattern, in_string)

# + - Makes sure that a particular character preceding it is present at least once ( > 0)
# In the following example it will look for 'a' at the start, 'b' to be present 1 or more times, 'c' at the end
pattern = r"ab+c"

# {x} where x is an integer - Makes sure that a particular character preceding it is present EXACTLY x number of times
# In the following example it will look for 'a' at the start, 'b' to be present exactly 3 times, 'c' at the end
pattern = r"ab{3}c"

# {x,} where x is an integer - Makes sure that a particular character preceding it is present MINIMUM x number of times
# In the following example it will look for 'a' at the start, 'b' to be present >=3 times, 'c' at the end
pattern = r"ab{3,}c"

# . = Wildcard - Means that . can take place of any other character
# In the following example we can have any character (single) between 'a' and 'b'
pattern = r"a.b"


# . = Optional - Means that a particular character preceding it is optional, i.e. it may or may not be present
# In the following example '-' character between 'a' and 'b' is optional.
pattern = r"a-?b"


# ^ - Means that pattern must be present at the beginning of the string
# In the following example, "91" must be present at the beginning of the string
pattern = r"^91"


# [] - Character classes - Used when you want to match a set of characters instead of a single charcter.
#  Usage - Mention each character inside [] or you can specify a range. There is a OR relation between chars.

pattern = r"[Pp]ython"			# If you want to match Python or python
pattern = r"[a-z]ython"			# If you want to match aython or bython..... or zython
pattern = r"[A-Za-z]"		# If you want to match ABCD....Z or abcd.....z
pattern = r"[0-9]"			# If you want to match 920393 or any number series


# re.findAll() - Enables to check for all the occurrences of a pattern in a string. It returns a list of all the matches
string = "the sun is shining, there were birds are cherping and then we went out to play."
pattern = r"the"

list_of_matches = re.findall(pattern, string)
# list_of_matches = ['the', 'the', 'the']
print(len(list_of_matches))


# Example finding vowels in a word
string = "reimbursement"
pattern = r"[aeiou]"
print(re.findall(pattern, string))


# \d = any digits - Shorthand for matching any digits in a string
string = "I have 3 apples and 4 bananas"
pattern = r"\d"
print(re.findall(pattern, string))


# \D = any non-digits - Shorthand for matching any non-digits in a string. OPPOSITE of \d
string = "I have 3 apples and 4 bananas!!"
pattern = r"\D"
print(re.findall(pattern, string))		# This will include white spaces and other special chars


# \w = any alpha-numeric character - Shorthand for matching any alpha-numeric in a string.
string = "I sat @ the table and ate 3 apples and 4 bananas!!"
pattern = r"\w"
print(re.findall(pattern, string))		# This will NOT match white space, @ and ! in this example


# \W = any non-alpha-numeric character - Shorthand for matching any non-alpha-numeric in a string.
string = "I sat @ the table and ate 3 apples and 4 bananas!!"
pattern = r"\W"
print(re.findall(pattern, string))		# This will match white space, @ and ! in this example


# \s = any whitespace character - Shorthand for matching any whitespace character in a string.
string = "I sat @ the table \t and ate 3 apples and 4 bananas \n. I came back home!!"
pattern = r"\s"
print(re.findall(pattern, string))


# \S = any non-whitespace character - Shorthand for matching any non-whitespace character in a string.
string = "I sat @ the table \t and ate 3 apples and 4 bananas \n. I came back home!!"
pattern = r"\S"
print(re.findall(pattern, string))

pattern = r"\S+"		# Get all the words in a regular expression
