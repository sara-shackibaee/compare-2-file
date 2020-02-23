


import wget
import tarfile
import hashlib
url = 'address tar file in site for download'
filename = wget.download(url)
my_tar1 = tarfile.open('tar file')
my_tar1.extractall() 
my_tar1.close()
md5file1 = hashlib.md5(open("file1 extracte shodeh for hash", 'rb').read()).hexdigest()
print(md5file1)
my_tar2 = tarfile.open('filepath2')
my_tar2.extractall() 
my_tar2.close()
md5file2 = hashlib.md5(open("file2 extracte shodeh for hash", 'rb').read()).hexdigest()

if(md5file1 == md5file2):
    print("file not change")
else:
    print("file change")