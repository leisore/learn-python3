#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## list
print('list:')
arr1 = [1,2,4,50,10]
print(arr1)

print(arr1[0])
print(len(arr1))
print(arr1[len(arr1)-1])

arr1.insert(1,90)
print(arr1)

arr1.pop()
print(arr1)

arr1.pop(4)
print(arr1)

arr1.append(100)
print(arr1)


## set
print('\nset:')
set1 = set([1,2,3,3,4,55,55])
print(set1)
#print(set1[0]) # unsupport
set1.add(100)
print(set1)
print(set1)
set1.add(200)
print(set1)
set1.remove(4)
print(set1)


## tuple
print('\ntuple:')
tuple1=(1,2,3,4)
print(tuple1)
print(len(tuple1))
#tuple1.append(10)

tuple2=(1,2,(3,4))
print(tuple2)
print(tuple2[2][0])


## dic
dic1={"k1": 'tom', 'key2': 'foo'}
print(dic1)
print(dic1["key2"])

dic2={"k1": 'tom', 'key2': 100, 'k3': dic1}
print(dic2)

print('k1' in dic2)
print('k1' in dic2.get('k3'))

dic2.pop('key2')
print(dic2)

print(dic2.get('k4'))
print(dic2.get('k4', -1))


