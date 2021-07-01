# 1 reverse a string
'''def reverse(a):
    rev=""
    for i in a:
        rev=i+rev
    return rev

A=input('Enter any text')
print('Reverse:',reverse(A))'''

# 2 unique elements of a list
'''def unique(list):
    li=[]
    for i in list:
        if list.count(i)==1:
            li.append(i)
    return li


L=[2,4,5,5,6,7,4,5,4,7]
print(unique(L))'''

# 3 even numbers from a list
'''def even(list):
    li=[]
    for i in list:
        if i%2==0:
            li.append(i)
    return li


L=[2,4,5,5,6,7,4,5,4,7]
print(even(L))'''

# 4 factorial
'''def factorial(N):
    F=1
    for i in range(1,N+1):
        F=F*i
    return F

n=int(input('Give a number to check its factorial'))
print(factorial(n))'''

# 5 even indixed elements of a list
'''def eveind(list):
    L=[]
    for i in list:
        if list.index(i)%2==0:
            L.append(i)
    return L


L=[2,4,5,5,6,7,4,5,4,7]
print('AT EVEN INDICES:',eveind(L))'''

# 6 odd indexed elements of a list
'''def oddind(list):
    L=[]
    for i in list:
        if list.index(i)%2!=0:
            L.append(i)
    return L


L=[2,4,5,5,6,7,4,5,4,7]
print('AT ODD INDICES:',oddind(L))'''

# 7 number of characters
'''S=input('Give a string')
print('Number of characters=',len(S))'''