import sys
import hashlib

def get_file_md5(fname):
    m = hashlib.md5()   #创建md5对象
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)  #更新md5对象

    return m.hexdigest()    #返回md5对象



if __name__ == '__main__':
    file_name = "F:\download\SecureLink-2.10.0-rc.3-1076-1650-win-x64.exe"
    file_md5 = get_file_md5(file_name)
    print(file_md5)