''' Копируем файл если не совпадает хеш сумма'''
import hashlib
from shutil import copyfile
from os import path


def hashsum(file):
    '''читает файл частями, возвращает хеш сумму'''
    with open(file, "rb") as fread:
        file_hash = hashlib.md5()
        while chunk := fread.read(8192):
            file_hash.update(chunk)
    print(file_hash.hexdigest())
    return file_hash.hexdigest()



#+vars
PATH_OLD =''
PATH_NEW =''
#-vars

if __name__ == '__main__':
    if path.isfile(PATH_OLD) and path.isfile(PATH_NEW):
        if hashsum(PATH_OLD) != hashsum(PATH_NEW):
            copyfile(PATH_OLD, PATH_NEW)
    else:
        copyfile(PATH_OLD, PATH_NEW)
