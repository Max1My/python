list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
result2 = []
for index in range(1, len(list)):
    if list[index - 1] < list[index]:
        result2.append(list[index])
print(result2)