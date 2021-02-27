print('SPECIAL OLYMPIC GAMES')
count = int(input('Input count of members: '))
i = count
members = []
while i > 0:
    name = input('Who position on this?: {}'.format(i))
    members.append(name)
    i-=1

# кто участвовоал в олимпиаде?
print('Special Olympic games members: ', sorted(members))

# Записали людей с конца?

members.reverse()
# Выделим первые три места

result = members[:3]

result = 'Winners is: {}! Congreatulations!'.format(result)

print(result)