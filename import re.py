import re
mystring = " 7908 S 97th Circle, La Vista, NE 68128 "
re.search(r'\w+, [A-Z]{2}', mystring)