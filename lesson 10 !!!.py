from pip._internal.operations.install.wheel import _raise_for_invalid_entrypoint

friend = {
    'name': 'Max',
    'age' : 23,
    'has_car' : True
}

for key in friend:
    print(key)
    print(friend[key])

print("000000000000000000000000000000")

for val in friend.values():
    print((val))

print("000000000000000000000000000000")

for item in friend.items():
    print(item)

print("000000000000000000000000000000")

for key, val in friend.items():
    print(key)
    print(val)