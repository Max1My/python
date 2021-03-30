percents = ['процент','процента','процентов']
numbers = int(input('Введите число от 0 до 20: '))
if(numbers==0):
    print(str(numbers)+ ' ' + percents[2])
if(numbers==1):
    print(str(numbers)+ ' ' + percents[0])
if(5>numbers>1):
    print(str(numbers)+ ' ' + percents[1])
if(21>numbers>4):
    print(str(numbers)+ ' ' + percents[2])
print(percents)

