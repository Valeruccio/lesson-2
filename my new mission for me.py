a = [1,3,4,5,2,3,5,6,7,8,96,23,1,2,3,4,5,6,]

result = []

for n in a:
    if a.count(n) == 1:
        result.append(n)
print(result)