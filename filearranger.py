import os
import shutil
user_directory = input("Enter the Folder path")
os.chdir(user_directory)
for i in os.listdir():
    if '.' in i:
        if not os.path.exists(i.split('.')[1]):
            os.mkdir(i.split('.')[1])
        shutil.move(i,i.split('.')[1])

