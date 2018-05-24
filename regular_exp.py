import re
`Findall method:`
s = 'Hello world, this is a test!'
result = re.findall(r'\w+',s)
=> ['Hello', 'world,', 'this', 'is', 'a', 'test!']

`sub string method:`
print(re.sub( r'\S+' , 'WORD', s))
=>  WORD WORD WORD WORD WORD WORD

