friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

if 'Max' in friends:
    print('I know him!')

if 'M' in friend_name:
    print(True)

i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i+=1

print('000000')

for friend in friends:
    print(friend)

print('000000')

for x in friend_name:
    print(x)

for a in roles:
    print(a)