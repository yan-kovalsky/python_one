import os

path = 'C:/Users/kamaev/Desktop/OTHER/Python/testing/New folder'
for root,dirs,files in os.walk(path):
     print('вложенные файлы',files)

