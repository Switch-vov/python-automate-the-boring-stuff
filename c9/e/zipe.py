import zipfile
import os

exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(spamInfo)
exampleZip.extractall()
exampleZip.extract('spam.txt')


exampleZip.close()
