import os

def make_dir(n):
    dir_path = os.path.join(main_dir,n)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

main_dir = 'my_project'
second_dir = ['settings', 'mainapp', 'adminapp','authapp']

for i in range(len(second_dir)):
    make_dir(second_dir[i])

