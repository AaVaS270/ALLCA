#1
'''a=int(input('enter a number'))
b=int(input('enter another number'))
if a==b:
    print('1')
elif a>b:
    print("2")
else:
    print('3')'''

#2
'''a=int(input('number:'))
b=int(input('number:'))
c=int(input('number:'))
d=int(input('number:'))
if a==b and c==d:
        print('HELLO')'''

#3
'''a=int(input('number:'))
b=int(input('number:'))
c=int(input('number:'))
d=int(input('number:'))
if a==b or c==d:
        print('HELLO')'''

#4
'''x=float(input('enter a number'))
if x>0:
    print('TRUE')
elif x<0:
    print('FALSE')
else:
    print(0)'''

#5
'''x=int(input('enter a number'))
if x%2==0:
    print('EVEN')
else:
    print('ODD')'''

#8
'''fn=input('FIRST NAME:')
ln=input('LAST NAME')
C=ln+fn
print(C)'''

#9
'''n=input(' NAME:')
age=input('AGE')
add=input('ADDRESS:')
print(n)
print(age)
print(add)'''

#10
'''rad = float(input('enter the radius(in cm)'))
rad2 = rad ** 2
Area = 3.14 * rad2
Per = 2 * 3.14 * rad
print(f'Area={Area}cm^2 and Perimeter={Per}cm')'''

#11
'''wei=float(input('What is your weight?(in kg)'))
hei=float(input('How tall are you?(in m)'))
BMI=wei/(hei**2)
print(f'Your body mass index is {BMI}')'''

#12
stu1=int(input('Students in class A='))
cha1=stu1//2
if stu1%2!=0:
    cha1=cha1+1
print(f'{cha1} chairs are required')
stu2=int(input('Students in class B='))
cha2=stu2//2
if stu2%2!=0:
    cha2=cha2+1
print(f'{cha2} chairs are required')
stu3=int(input('Students in class C='))
cha3=stu3//2
if stu3%2!=0:
    cha3=cha3+1
print(f'{cha3} chairs are required')

