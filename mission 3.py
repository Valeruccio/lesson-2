my_list_1 = [2, 2, 5, 12, 8, 2, 12]
result = []
for n in my_list_1:
 if my_list_1.count(n) == 1:
     result.append(n)
print(result)