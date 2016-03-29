import re


s = "112abc-32u1-abcssssu1"
print re.findall("(abc[^u]*)",s,re.S)
print re.search('(abc.*u)',s,re.S).group()
print re.match("abc",s,re.S)