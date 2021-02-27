empty_list = []

friends = ['Max', 'Leo', 'Kate']

print(type(friends))

print('Второй друг: ', friends[1])
print('Первый друг с конца: ', friends[-1])
friends.append('Ron')
print(friends)
print(len(friends[0:4]))
friends.pop()
print(friends)
del friends[2]
print(friends)
friends.remove('Leo')
print(friends)
print(len(friends))