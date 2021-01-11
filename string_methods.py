# capitalize

txt = 'hello, welcome to my world'
print(txt.capitalize())

#Note:- Strings are immutable.

# center(length, character) - character is optional

txt = " hello "
print(txt.center(10,'g')) # exactly one character should be given 

#count()

txt = 'hello, welcome to my world'
print(txt.count('w'))

# count method will return number as a  output

# endswith()
txt = 'hello, welcome to my world'
print(txt.endswith('d', 5)) # txt.endswith(value, start, end)-start & end both are optional

#find()

txt = 'hello, welcome to my world'
print(txt.find('welcome'))


