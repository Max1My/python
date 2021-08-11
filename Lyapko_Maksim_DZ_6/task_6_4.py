def save_file(n):
    with open('users_hobby.txt','w',encoding='utf-8') as f:
      f.writelines(n)
users_site = []
users = []
hobby = []
with open('users.csv','r',encoding='utf-8') as f:
    line = f.readlines()
    for i in line:
        i = i.strip()
        users.append(i)
with open('hobby.csv','r',encoding='utf-8') as f:
    line = f.readlines()
    for i in line:
        i = i.strip()
        hobby.append(i)
for i in range(len(users)):
    line = users[i] + ' : ' + hobby[i] +'\n'
    users_site.append(line)
    save_file(users_site)
print(users_site)