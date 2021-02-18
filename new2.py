import os
from glob import glob
import shutil
#получаем имя всех файлов в указанной директории - эти файлы надо будет записать поверх старых
path = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/New folder'
for root,dirs,files in os.walk(path):
     targetFilesArray = files
     # array1 =[]
     # for i in targetFilesArray:
     #     array2 = array1.append(os.path.join(root,i))


     print(targetFilesArray)
     # print (array1)

# функция для поиска конкретного файла в целевой директории и поддиректториях,
# возвращает список, содержащий путь и имя файла
def findFiles (fileName,path):
    files =[]
    for dir,_,_ in os.walk(path):
        files.extend(glob(os.path.join(dir, fileName)))
    return files

#для каждого файла выполняем фукнцию поиска
for x in targetFilesArray:
    path = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/Old folder tree'
    a = findFiles (x,path)
    # print(a)

# делаем из списков сорса и таргета экземпляры файлов
    i = 0
    while i < len(a):
        targetFile = (a[i])
        print (targetFile)
        i += 1

    # i = 0
    # while i < len(array1):
    #     sourceFile = (array1[i])
    #     print (sourceFile)
    #     i += 1


# перезаписываем дубликаты
# pathToFile = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/New folder/'
# for root,dir,files in os.walk(pathToFile):
#     files1=files
#     for file in files1:
#         sourceArray = []
#         for i in file:
            array2 = sourceArray.append(os.path.join(root,i))
            rewright = shutil.copyfile(array2,targetFile)
            print (rewright)