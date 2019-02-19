import os
import shutil
from pathlib import Path
home = str(Path.home())
home
path = home + '\\Desktop\\'
path
os.chdir(path)
if not os.path.exists(path+'All_files'):
    print('creating folder....\n')
    os.mkdir(path+'All_files')
else:
    print('..All_files folder already exist..\nHence skipping')
    

if not os.path.exists(path+'All_folders'):
    print('creating folder....\n')
    os.mkdir(path+'All_folders')
else:
    print('..All_folders already exist..\nHence skipping')

print(path)

listdir = os.listdir()

for va in listdir:
    if os.path.isfile(path+va):
        if not "All_files" in va and not "Desktop_Cleaner.py" in va:
            print(va + ' its a file hence moving to Allfiles\n')
            src = path+va
            dst = path+'All_files'
            if not os.path.isfile(dst+'\\'+va):
                 shutil.move(src,dst)
            else:
                print('file already exists in '+dst)
                print('\nHence removing '+va+" from Desktop..")
                os.remove(path+va)
    elif os.path.isdir(path+va):
        if va != "All_folders" and va != "All_files":
            src = path+va
            dst=path+'All_folders'
            print('\n'+va + ' is a directory\n Hence moving to All_folders')
            if not os.path.isdir(dst+'\\'+va):
                 shutil.move(src,dst)
            else:
                print('\n'+va+' already exists in '+dst)
                print('Hence removing '+va+" from Desktop..")
                shutil.rmtree(path+va)
    else:
        print(va+' unrecognisable\n')
input()

