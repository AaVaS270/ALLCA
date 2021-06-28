# 1 Sum 1 to 10 while loop
'''i=0
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print(sum)'''

# 2 swap
'''a=10
b=20
c=b
b=a
a=c
print(a,b)'''

# 3 take a number and check if prime
'''def prime(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                print(f'{a} is not prime')
                break
        else:
                print(f'{a} is prime')
    else:
        print(f'{a} is neither prime nor composite')


prime(4)'''

# 4 print text n times
'''for i in range(10):
    print(i,'Hello World')'''

# 5
'''x=5
x+=3
print(x)'''

# 6
'''def mul(list):
    p=1
    for i in list:
        p=p*i
    print(p)


li=[1,10,4,5,9]
mul(li)'''

# 7
'''def add(list):
    p=0
    for i in list:
        p=p+i
    print(p)


li=[1,10,4,5,9]
add(li)'''

# 8 prime
p=int(input('Give the number to check'))
if p>1:
        for i in range(2,p):
            if p%i==0:
                print(f'{p} is not prime')
                break
        else:
                print(f'{p} is prime')



