# print('hello world')

# x,y,z=10, 'nilly', '15'
# print(x,y,z)

# text = input("Type some code: ")
# print(text)


#possible
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

#impossible
# 2myvar = "John"
# my-var = "John"
# my var = "John"


# x=10
# y=10.5
# z=5+5j

# print(type(x), type(y), type(z))
#print(str(z))

film="the cost of ticket is {1} dollar {0} of"
# f="the cost of ticket is 25 dollar of"
# teachers ='''kgjskjhjkhjfhjkg
# kjghjfghfjghfj
# kjfghjfghjghjgh'''
# x='jsdfhjdsfh'

# print(film[1:5])
# print(film[:5])
# print(film[5:])
print(film[::2])
# print(film[-5:-2])
# print(film.upper())
# print(film.lower())
# print(film.find('of'))
print(film.strip())
# print(film.replace('25', '30'))
# print(film.replace("25", "45").replace("is","are")) #for multiple replacement
# print(film.split('is'))
# print(film.count('of'))
# print(film.format(30,'kjdkj')) #format
# print(f+' lkfdgjfkgj' +' ' +x)

x=20
y=10.5
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x**y)
# print(x%y)
# print(x//y) #floor division

# print((x>=y) or (y==x))
# print((x>=y) and (y<x))
# x+=3
# x-=1
# x/=5
# x*=2
# print(x^2)

# Python Collections (Arrays)
#There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members


#List
# list1=[1,2,'dkjjdkh',1, True, False, 45]
# list2=list(('jdfhjd', 2,5))
# list3=[True, False, 5, 'djfhdj']
# print(type(list1),type(list2))
# print(len(list1), len(list2)) #lenght
# print(list2[-2])
# print(list1[3])
# print(list1[:2])
# print(list1[4:])
# print(list1[1:5])
# print(list1[-4:-1])

#changing list items
# list1[2]=5
# list3[0:2]='Mira',5,0
# print(list1, list3)

#adding to list
# list1.append('mira')
# list2.extend(list1)
# list3.insert(0,'jhghg')

# #remove from list
# list1.remove('mira')
# del list2[0]
# list3.pop(0)
# list3.clear()
# print(list1, list2, list3)

# list2.sort(key=str.lower)
# print(list2)

#tuples
# tuple1=('mdmsfh',5,'mdsfndmf',True, False, True, 25, 35)
# tuple2=tuple((True, False, False, True))
# tuple3=('5,25,85,95,54,34,46,74')
# print(len(tuple1))
# print(tuple1[1:5])

#update tuples
# list1=list(tuple1)
# # list1.append
# print(type(list1))

#Unpack Tuples
# (mira, aynur, *m) = tuple1
# print(mira)
# print(aynur)
# print(*m)

# x=tuple1.count(25)
# y=tuple1.index(1)
# print(x,y)

#set: Set items are unchangeable, but you can remove items and add new items.
# set1={'narmin','ali', 'kenan', 'murad', 'aydan', True, False}
# set2=set((5,3,75,1,0,'sdjkdd','djdfdjfd'))
# print(len(set1),set2)
# print(type(set2))

#access to the set
# for x in set2:
#      print(x)

#sets can not be changed, but you can add and remove
# set2.add('kenan')
# print(set2.union(set1))
# x=set1.update(set2) #Insert the items from set
# print(x)
# print(set2.intersection(set1)) #Return a set that contains the items that exist in both set
# print(set2.intersection_update(set1)) #Remove the items that is not present in both 

# print(set2.remove('kenan'))
# print(set1.clear())
# print(set2.pop())
# del set2

# z=set2.copy()
# print(z)

#dictionaries
# dict1={'name':'BMW', 'model':'msdhd', 'year':2022}
# dict2=dict(name='Mercedes', model='kjdhdj', year=2022)
# dict3={'name':'BMW', 'model':'msdhd', 'color':['red','black','white'], 'year':2022}
# dict4={
#      'car1':{
#           'name':'BMW',
#           'year':2021
#      },
#      'car2':{
#           'name':'Audi',
#           'year':2022
#      }
# }
# print(len(dict1))
# print(dict4['car1']['name'])
# # access dictionary items
# print(dict1['model'])
# print(dict3['color'][0]) 
# print(dict2.get('model'))
# print(dict2.keys()) #for keys
# print(dict2.values()) #for values
# print(dict2.items()) #taking for all items

#modify dict
# dict2['name']='Audi'

#adding
# dict2['color']=['green','yellow']
# dict2.update({'years':2021})
# print(dict2)

#deleting
# dict2.pop('name')
# dict2.popitem() #remove the last item
# del dict1['color']
# dict2.clear()
# print(dict2)

# a=[10,2,4,8,11]
# n=a.pop(4)
# if n>len(a):
#      print(a.pop(0))

# a.remove(10)
# a.insert(0,25)
# print(a)

# print(min(5,95,3,45))

#if statement
b=[True, False, 'audi', 2019]
a='The costs of these shoues are the 25 and 30 dollars'
# # print(len(a))
# if (len(a)>=10 & len(a[:7]))>10:
#      print('hello world')
# elif a.count('a')>=25 or b.count('a')<=10:
#      print('hello mars')
# else:
#      print('Aynur is intelligent')

#loops
x=10
y=5
# while x>0 and y>1:
#      print(a,b)
#      a-=1
#      b-=2

# for x in b:
#      print(x)
#      if x==20:
#           print('hello world')
#      else:
#           print('get out')
import math
# for x in range(4,10):
#      print(x)
#      if x>5:
#           print(math.pow(x,2))
#      else:
#           print(math.log(x))
      
#      A= "The costs of these shoes are 25 and 30 dollars."
# print(A.replace("25", "45").replace("30","100"))
# print(A.count('o'))

import math
import datetime

x=[5,25,69,86]
# print(min(x))
# print(max(x))
# print(abs(-25))
# print(pow(5,3))
# print(math.sqrt(65))
# print(math.log(85))
# print(math.exp(2)) #(ex)
# print(math.ceil(4.4))
# print(math.floor(4.6))

# x=datetime.datetime.now().weekday()
# y=datetime.datetime.today()
# print(y)

# if x>5:
#      print('Today is not workday')
# else:
#      print('working day')

# if len(x)>=min(x):
#      print('it is okay')
# elif math.sqrt(2)<=max(x):
#      print('md')
# else:
#      print('you need revise again')

y=15
# while y<=20:
#      print(y)
#      y+=1

# while y>=len(x): 
#      y-=3
#      if y==9:
#           continue
#      print('this is true')
# else:
#      print(y)

#for
# for x1 in range(2,6,2):
#      print(x1)
# else:
#      print('finished')

# for x2 in range(6):
#   if x2 == 3: break
#   print(x2)
# else:
#   print("Finally finished!")

# def fisrtfunc(x,y,z):
#      print (math.pow(x,y)+math.log(z))
# fisrtfunc(5,3,25)

# def mira(x,y):
#      print(x+' '+y[2])
# mira('Mira',('17','19','1994'))

# def my_function(x):
#   return 5 * x
# print(my_function(3))

# x1=['Mira', 'Aynur', 'Nurlan',25, False]

# import datetime
# currentday=datetime.datetime.now().weekday()
# if currentday>=5:
#      print('today is not working day')
# else:
#      print('today is working day')

#the sum of 100
# total =0
# for z in range(1,101):
#      total=total+z
# print(total)

# def summ():
#      total=0
#      for i in range(1,101):
#           total=total+i
#      return total
# print(summ())

#print() prints a value to the screen. That value is not accessible to or used by the rest of the code. return returns a value from a function back to the code that called it, 
# allowing that value to be used later on. This will print the number 4 to the screen, and that's it.


# hasil ve ya faktorial
# def pro_10():
#     product = 1
#     for i in range(1, 11):
#         product = product * i
#     return product

# print(pro_10())

# fac=1
# for x in range(1,6):
#      fac*=x
# print(fac)

# def fact(n):
#      fac=1
#      for x in range(1,n+1):
#           fac*=x
#      return fac
# print(fact(5))

#exam bilet
# A= {5, 14, 12, 7, 42, 14, 24, 22}
# B= {2, 47, 34, 5, 11, 22}
# C= A.intersection(B)
# if len(C)>len(B):
#      print(max(C))
# else:
#      pro=1
#      for i in C:
#           pro=pro*i
#      print(pro)

#exam bilet1 sual 3
list1= [27, 15, 1, 5, 2, 14, 19, 22, 31]
# d=min(C)
# B=max(C)
# if d>len(C):
#      print(math.pow(d,2))
# else:
#      print(math.pow(len(C),2))
# list1.sort(reverse=True)
# print(list1)




