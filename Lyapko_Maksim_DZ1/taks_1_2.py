def numbers(value):
    res = 0
    while value != 0:
        res += value % 10
        value //= 10

    return res

arr = [i**3 for i in range (1,1001, 2)]

res1 = sum(filter(lambda num: numbers(num) % 7 == 0, arr))
res2 = sum(filter(lambda num: numbers(num + 17) % 7 == 0, arr))

print(res1)
print(res2)