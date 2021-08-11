import pickle

users_site = {}
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
    users_site[users[i]] = hobby[i]
if len(hobby) < len(users):
    users_site = None
    print(users_site)
if len(hobby) > len(users):
  f.close(1)
with open('users_site.pickle','wb') as f:
    pickle.dump(users_site,f)