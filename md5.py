import hashlib

md5 = 'eca00607b2bdf09ccbdbcfb89de65d4f'
sum = 30*(30+1)/2
print(hashlib.md5('hash'.encode('utf-8')).hexdigest())

text = '''
Hello world to md5
'''

list = text.split()

for word in list:
    hash = hashlib.md5(word.encode('utf-8')).hexdigest()
    if hash == md5 or hash[0:5] == md5[0:5]:
        print(hash)
        print(word)

