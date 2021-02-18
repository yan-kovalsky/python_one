import os
from glob import glob
import shutil
#получаем имя всех файлов в указанной директории - эти файлы надо будет записать поверх старых
path = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/New folder'
for root,dirs,files in os.walk(path):
     targetFilesArray = files
     array1 =[]
     for i in targetFilesArray:
         array1.append(os.path.join(root,i))


     # print(targetFilesArray)
print (array1)

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
    if len(a) > 1:
        print('Для файла', x, 'в целевой директории найдены несколько совпадений!:',a)
    else:
       final = a
       print(final)

# делаем из списков экземпляры файлов
    i = 0
    while i < len(array1):
        sourceFile = (array1[i])
        # print (sourceFile)
        i += 1

    i = 0
    while i < len(final):
        targetFile = (final[i])
        # print (targetFile)
        i += 1

 # перезаписываем дубликаты
rewright = shutil.copyfile(sourceFile,targetFile)
print (rewright)