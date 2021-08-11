def gen_num(n):
    for i in range(n):
        yield i
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
gen = gen_num(len(src))
for i in range(len(src)):
    num = src[next(gen)]
    if src.count(num) == 1:
        result.append(num)
print(result)