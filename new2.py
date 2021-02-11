import os
from glob import glob

#получаем имя файлов в указанной директории
path = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/New folder'
for root,dirs,files in os.walk(path):
     targetFilesArray = (files)
     # print(targetFilesArray)

# функция для поиска конкретного файла в целевой директории и поддиректториях,
# возвращает список, содержащий путь и имя файла
def findFiles (fileName,path):
    files =[]
    for dir,_,_ in os.walk(path):
        files.extend(glob(os.path.join(dir, fileName)))
    return files

#для каждого файла из указанной выполняем фукнцию поиска
for x in targetFilesArray:
    path = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/Old folder tree'
    a = findFiles (x,path)
# перебор элементов списка
    i = 0
    while i < len(a):
        targetFile = (a[i])
        print (targetFile)
        i += 1
    # print (a)