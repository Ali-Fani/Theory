import re

string = input()

pattern = "\+98\-*[0-9]{3}\-*[0-9]{3}\-*[0-9]{4}"


result = re.match(pattern, string)

if result:
    print('Accept')
else:
    print('Reject')
