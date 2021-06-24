#1
'''def max():
    A,B,C=int(input('Give a number')),int(input('Give another number')),int(input('Give a number'))
    if A>B and A>C:
        print(f'{A} is the greatst')
    elif B>A and B>C:
        print(f'{B} is the greatest')
    else:
        print(f'{C} is the greatest')


max()'''

#2
'''def month(nu):
    if nu > 12:
        print('Please give a number between 1 and 12')
    elif nu == 1:
        print("JANUARY")
    elif nu == 2:
        print("FEBRUARY")
    elif nu == 3:
        print("MARCH")
    elif nu == 4:
        print("APRIL")
    elif nu == 5:
        print("MAY")
    elif nu == 6:
        print("JUNE")
    elif nu == 7:
        print("JULY")
    elif nu == 8:
        print("AUGUST")
    elif nu == 9:
        print("SEPTEMBER")
    elif nu == 10:
        print("OCTOBER")
    elif nu == 11:
        print("NOVEMBER")
    else:
        print('DECEMBER')


A=int(input('ENTER A NUMBER'))
month(A)'''

#3
'''def nag(name,age):
    print('name=',name)
    print('age=',age)


N=input('WHAT IS YOUR NAME')
A=int(input('WHAT IS YOUR AGE'))
nag(N,A)'''

#4
'''def min():
    A,B,C=int(input('Give a number')),int(input('Give another number')),int(input('Give a number'))
    if A<B and A<C:
        print(f'{A} is the smallest')
    elif B<A and B<C:
        print(f'{B} is the smallest')
    else:
        print(f'{C} is the smallest')


min()'''

#5
def fizz_buzz(a):
    if a % 3 == 0 and a % 5 == 0:
        print('FizzBuzz')
    elif a%5==0:
        print('Buzz')
    elif a%3==0:
        print('Fizz')
    else:
        print(a)


N=int(input('ENTER THE NUMBER TO BE CHECKED'))
fizz_buzz(N)