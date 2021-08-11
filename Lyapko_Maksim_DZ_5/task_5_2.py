def odd_nums(n):
    return(odd_num for odd_num in range(1,n,2))
gen = odd_nums(15)
for i in range(15):
    print(next(gen))