def save_file(n):
    with open(dir_save_f,'w',encoding='utf-8') as f:
      f.writelines(n)
users_site = []
users = []
hobby = []
dir_user = input('Введите имя файла пользователей: ')
dir_hobby = input('Введите путь к файлу хобби: ')
dir_save_f = input('Введите имя для файла сохранения: ')
with open(dir_user,'r',encoding='utf-8') as f:
    line = f.readlines()
    for i in line:
        i = i.strip()
        users.append(i)
with open(dir_hobby,'r',encoding='utf-8') as f:
    line = f.readlines()
    for i in line:
        i = i.strip()
        hobby.append(i)
for i in range(len(users)):
    line = users[i] + ' : ' + hobby[i] +'\n'
    users_site.append(line)
    save_file(users_site)
print(users_site)
