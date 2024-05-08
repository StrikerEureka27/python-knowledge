str = 'This is a test'

print(str[2])
print(str[-2])

res1 = str.index('a')
res2 = str.index('i', 4)
res3 = str.index('i', 2, 5)
res4 = str.rindex('i')

print(res1)
print(res2)
print(res3)
print(res4)

# Fragment

alphabet = 'ABCDEFGHIJKLMNOPQRSTWXYZ'

frg = alphabet[2:10]
print(frg)

frg2 = alphabet[2:10:2]
print(frg2)

frg3 = alphabet[::3]
print(frg3)

frg4 = alphabet[::-1]
print(frg4)

# String methods

# Upper and split
chain = 'This is the Pablo text'
resChainUpper = chain.upper()
resChainSplit = chain.split()
print(resChainUpper)
print(resChainSplit)

# Join
a = "Hello,"
b = " Learn Python "
c = " is "
d = " Awsome " 

resJoin = ''.join([a,b,c,d])
str = resJoin.replace('Python', 'Java')
print(str)

# String properties

# Multiplication
str2 = 'Hello'
print(str2*5)

# multilines
str3 = """
This is a multiline
text for a example
text
"""
print(str3)

print('text' in str3)
print('text' not in str3)

# List 
# Ordered sequence of objects
my_list = ['a', 'b', 'c', 'd']
my_list_2 = [1, 'b', 'c', ['h']]
print(type(my_list))

listLength = len(my_list)
res = my_list[0:4]

print(res)
print(len(my_list))

print(my_list + my_list_2)

my_list.append('new element')
deleted  = my_list.pop(len(my_list)-1)

print(f'Deleted element: {deleted}')
print(f'my_list {my_list}')

sortedList = [2, 4, 1, 100, 24]
sortedList2 = ['a','j', 'e','h', 'b']

sortedList.sort() # void
sortedList2.sort()

print(sortedList)
print(sortedList2)

sortedList.reverse()
print(sortedList)

# Dictionary

my_dic = {
    'k1': 'value 1',
    'k2': 'value 2',
    'k3': 'value 3',
}

client = {
    'name': 'Pablo', 
    'age': 25,
    'weigth': 80
}

res = my_dic['k2']
res = client['age']

print(res)

dic2 = {
    'c1': ['a', 'b', 'c'], 
    'c2': ['d', 'e', 'f']
}

print(dic2['c2'][1].upper())

# Adding new 

dic2[3] = 'c3'
print(dic2)

dic2['c3'] = 'hello'
#print(dic2.keys())
#print(dic2.values())
#print(dic2.items())


mi_dict = {"valores_1":{"v1":3,"v2":6},
           "puntos":{"points1":9,"points2":[10,300,15]}}

print(mi_dict['puntos']['points2'][1])

# Tuple

my_pet_tuple = ('cat','dog','fish','cat')
my_num_tuple = (10,20,30)
print(len(my_pet_tuple))
print(my_num_tuple + my_pet_tuple)



lis = list(my_num_tuple)
print(type(lis))
print(my_pet_tuple.count('cat'))

# Sets

my_set_one = {1, 2, 2, 3, 4, 5} 
my_set_two = set({ 1,2, 3,3,3,3 ,4, 5, (1, 2, 3) })

print(my_set_one)
print(my_set_two)
my_set_one.add(100)
my_set_one.remove(3)

print(my_set_one.union(my_set_two))

# Booleans

my_flag = True

print(my_flag)

print(5>10)
print( 5 == 5 )




