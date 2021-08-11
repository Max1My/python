import os
import random

def make_dirs(n):
   dir_path = os.path.join(main_dir, n,third_dir)
   if not os.path.exists(dir_path):
      os.makedirs(dir_path)

def create_files_py(files):
   for i in range(len(second_dir)):
      dir_path = os.path.join(main_dir,second_dir[i])
      f_content = bytes(random.randint(0, 255)
                        for _ in range(random.randrange(10 ** 5)))
      with open(os.path.join(dir_path, f'{files}.py'), 'wb') as f:
          f.write(f_content)

def create_file_html(files):
   for i in range(len(html_files)):
      dir_path = os.path.join(main_dir,second_dir[i],third_dir)
      f_content = bytes(random.randint(0, 255)
                        for _ in range(random.randrange(10 ** 5)))
      with open(os.path.join(dir_path, f'{files}.html'), 'wb') as f:
          f.write(f_content)

def create_settings_files(files):
    for i in range(len(settings_files)):
        dir_path = os.path.join(main_dir, settings_dir)
        f_content = bytes(random.randint(0, 255)
                          for _ in range(random.randrange(10 ** 5)))
        with open(os.path.join(dir_path, f'{files}.py'), 'wb') as f:
            f.write(f_content)
main_dir = 'my_project'
settings_dir = 'settings'
second_dir = ['mainapp','authapp']
third_dir = 'templates'
py_files = ['__init__',"models",'views']
html_files = ['index','base']
settings_files = ['__init__','dev','prod']


if not os.path.exists(main_dir):
   os.mkdir(main_dir)

dir_path = os.path.join(main_dir, settings_dir)
if not os.path.exists(dir_path):
   os.makedirs(dir_path)

for i in range(len(second_dir)):
   make_dirs(second_dir[i])

for l in range(len(py_files)):
   create_files_py(py_files[l])

for i in range(len(html_files)):
   create_file_html(html_files[i])

for i in range(len(settings_files)):
   create_settings_files(settings_files[i])