import os

#получаем имя файлов в указанной директории
path = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/New folder'
for root,dirs,files in os.walk(path):
     targetFilesArray = (files)
     print(targetFilesArray)

#перебор элементов списка
i = 0
while i < len (targetFilesArray):
   targetFile =  (targetFilesArray[i])
   # print (targetFile)
   i += 1

#функция ищем все совпадения по имени файла в указанной директории, записываем в список checkResults
def findMatch (pathToInitial, pathToTarget):
    checkResult = []

    for root, dirs, files in os.walk(pathToInitial):        #получает список файлов в исходной папке для сравнения
        fileName = (files)

    for root, dirs, files in os.walk(pathToTarget):
        targetFiles = files                                 #получает список файлов в таргетной папке
        for i in targetFiles:                               #перебирает файлы из таргетной папки и сравнивает их с исходными
            if i in fileName:
                checkResult.append(os.path.join(root, i))   #записывает в список найденные совпадения

    x = len(checkResult)                                    #выводит сообщение, функция возвращает пустой список
    if x == 0:
        checkResult = "совпадений нет"

    return checkResult


path1 = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/New folder'
path2 = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/Old folder tree/Old folder2'
a = findMatch(path1,path2)
print (a)
