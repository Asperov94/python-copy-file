import hashlib
from shutil import copyfile
from os import path


def hashsum(file):
    '''читает файл частями, возвращает хеш сумму'''
    with open(file, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    print(file_hash.hexdigest())
    return file_hash.hexdigest()



#+vars
path_old =''
path_new =''
#-vars

if __name__ == '__main__':
    if path.isfile(path_old) and path.isfile(path_new):
        if hashsum(path_old) != hashsum(path_new):
            copyfile(path_old, path_new)   
    else:
        copyfile(path_old, path_new)





