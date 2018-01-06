import os
import shelve
import pprint

print(os.path.join('abc', 'bca', 'cda'))
print(os.getcwd())
os.makedirs('1/2/3/4/5', exist_ok=True)
print(os.path.getsize('osexample.py'))
print(os.listdir('./'))

shelfFile = shelve.open('mydata')
cats = ['Z', 'A', 'B']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

print(pprint.pformat(cats))