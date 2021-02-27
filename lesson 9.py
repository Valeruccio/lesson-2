friend = {'name': 'Max','age' : 23}
print(friend, type(friend))

print(friend['age'])

friend['has_car'] = True

print(friend)

friend['has_car'] = False
print(friend)

del friend['age']
print(friend)

friend['gay'] = True
print(friend)

if 'age' in friend:
    print('есть возраст')

if 'gay' in friend:
    print('пидор')

