lst_text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for item in lst_text:
    message = "".join(item)
    message = message.split(' ')
    message = message.pop()
    message = message.title()
    print('Привет ,', message)

