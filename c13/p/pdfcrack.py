import os
import PyPDF2

dic = open('dictionary.txt', 'r')
pdfReader = PyPDF2.PdfFileReader('encryptedminutes.pdf')
for word in dic.readlines():
    word = word.strip()
    if pdfReader.decrypt(word) == 1:
        print(word)
        break
    else:
        print('Word %s is error' % word)

    word = word.lower()
    if pdfReader.decrypt(word) == 1:
        print(word)
        break
    else:
        print('Word %s is error' % word)

if pdfReader.isEncrypted:
    page = pdfReader.getPage(0)
    print(page.extractText())
