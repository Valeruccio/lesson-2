friend = 'Sasha Alex'

first_letter = friend[2:4]
print('First letter', first_letter, friend[:4], friend[2:])
print(len(friend))
print(friend.find('lex'))
print(friend.split())

friends = 'Sasha;Alex'
print(friends.split(';'))

number = '45443'
print(number.isdigit())

print(friend.upper())

print(friend.lower())


name = 'Govnyuk'
age = 30

hello_str = 'Привет, %s конченный тебе %d лет'%(name,age)
print(hello_str)

hello_str = 'Привет, {} конченный тебе {} лет'.format(name ,age)
print(hello_str)