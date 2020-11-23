import re

pattern = re.compile('^[1234]+$')
str = '2134'
if re.search(pattern,str):
    print("valid String")
else:
    print("Invalid String")
