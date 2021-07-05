# 1 palindrome
'''def palindrome(string):
    var=""
    for i in string:
        var=i+var
    if var==string:
        return f'{string} is a palindrome'
    else:
        return f'{string} is not a palindrome'


arg=input('ENTER ANY WORD')
print(palindrome(arg))'''

# 2 Max
import random

'''def Max(list):
    M=max(list)
    return f"{M} is maximum"


A,B,C=int(input('Enter any number')),int(input('Enter any number')),int(input('Enter any number'))
L=[]
L.append(A), L.append(B), L.append(C)
print(Max(L))'''

# 4 min
'''def Min(list):
    M=min(list)
    return f"{M} is minimum"


A,B,C=int(input('Enter any number')),int(input('Enter any number')),int(input('Enter any number'))
L=[]
L.append(A), L.append(B), L.append(C)
print(Min(L))'''

# 3 sum
'''def Sum(list):
    S=sum(list)
    return f"{S} is the sum of these numbers"


A,B,C=int(input('Enter any number')),int(input('Enter any number')),int(input('Enter any number'))
L=[]
L.append(A), L.append(B), L.append(C)
print(Sum(L))'''

# 5 check for empty list
'''def empty(list):
    el=[]
    if list==el:
        return 'EMPTY!!'
    else:
        return "NOT EMPTY!!"


L=[]
L2=[1,3,4,3]
print(empty(L))
print(empty(L2))'''

# 6 random element from list
'''def rand(list):
    E=random.choice(list)
    return E

L=[2,4,6,4,7,5,8,9,6,8,6,5,7,5,3,7,5,4]
print(rand(L))'''

# 7 copy list
'''def copy(list):
    L=[]
    for i in list:
        L.append(i)
    return f'LIST COPIED:{L}'

LIST=[2,4,6,4,7,5,8,9,6,8,6,5,7,5,3,7,5,4]
print(copy(LIST))'''

# 8 second largest list
'''def Max2(list):
    List=list
    M=max(List)
    list.remove(M)
    M2=max(List)
    return f"{M2} is the second largest"


A,B,C=int(input('Enter any number')),int(input('Enter any number')),int(input('Enter any number'))
L=[]
L.append(A), L.append(B), L.append(C)
print(Max2(L))'''

# 9 print list-3rd element
'''def listred(list):
    for i in list:
        if list.index(i)==2:
            list.remove(i)
            break
    return list


L=[2,3,5,6,8,9,15]
print(listred(L))'''

# 10 count odd and even
'''def oddevencounter(list):
    odd=0
    even=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return f'{odd} odd numbers {even} even numbers'

a=int(input('How many numbers do you want to work with?'))
L=[]
for i in range(a):
    N=int(input('enter a number'))
    L.append(N)
print(oddevencounter(L))'''







