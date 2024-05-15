import re

# . (dot) any char
# \w word char
# \s whitespace
# + 1 or more
# * 0 or more
string = "called piiig"
pat = re.compile("iig")
result = pat.search(string)
print(result)

string = "called piiig"
pat = re.compile("xiig")
result = pat.search(string)
print(result)

pat = re.compile("called")
result = pat.match(string)
print(result)


pat = re.compile("ig")
result = pat.search(string)
print(result.group())

pat = re.compile("...ed")
result = pat.search(string)
print(result.group())

pat = re.compile("x...g")
result = pat.search(string)
#print(result.group())

string = "called piiig much better: xyzg"
pat = re.compile("...g")
result = pat.search(string)
print(result.group())


pat = re.compile("...g")
result = pat.findall()
print(result)

pat = re.compile("c\.l")
result = pat.search(string)
print(result.group())

string = 'blah :cat blah blah'
pat = re.compile(":\w\w\w")
result = pat.search(string)
print(result.group())

string = 'blah :catxxx blah blah'
pat = re.compile(":\w\w\w")
result = pat.search(string)
print(result.group())

string = "blah :cat blah blah"
pat = re.compile(":\w\w\w")
result = pat.search(string)
print(result)

string = "blah :catxxx blah blah"
pat = re.compile(":\w\w\w")
result = pat.search(string)
print(result)

string = "blah :123 blah blah blah"
pat = re.compile(":\d\d\d")
result = pat.search(string)
print(result.group())

string = "1 2 3"
pat = re.compile("\d\s\d\s\d")
result = pat.search(string)
print(result.group())

string = "1       2       3      "
pat = re.compile("\d\s+\d\s+\d")
result = pat.search(string)
print(result.group())

