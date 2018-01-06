import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 123-456-7890')
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 123-456-7890')
print('Phone number found: ' + mo.group(1))
print('Phone number found: ' + mo.group(2))
print('Phone number found: ' + mo.group(0))
print('Phone number found: ' + str(mo.groups()))

mo = phoneNumRegex.findall('My number is 123-456-7890')
print('Phone number found: ' + str(mo))

numberRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
mo = numberRegex.search('1231,234')
print(str(mo.group() ))
