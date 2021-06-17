#1
'''A=float(input('enter a number'))
B=float(input('enter another number'))
S=A+B
print(S)'''

#2
import cmath
import math

'''N=int(input('Give the value of n'))
sum=(N*(N+1))/2
print(f'Sum of first {N} numbers={sum}')'''

#3
'''N=int(input('How many minutes have passed since midnight?'))
hours=N//60
min=N%60
print(f'{hours}hours {min}minutes')'''

#4
N=int(input('Enter a number to check'))
if N!=1:
    for i in range(2,N):
        if (N%i)==0:
            print(f'{N} is a composite number')
            break
    else:
        print(f'{N} is a prime number')
else:
    print(f'{N} is neither prime nor composite')

#5
'''sec=int(input('enter time in seconds'))
hr=sec//3600
min=sec//60
secs=sec-(min*60)
print(f'{hr}hours {min}minutes {secs}seconds')'''

#6
'''nu=int(input('Give a number'))
if nu>7:
    print('Please give a number betweem 1 and 7')
elif nu==1:
    print("SUNDAY")
elif nu==2:
    print("MONDAY")
elif nu==3:
    print("TUESDAY")
elif nu==4:
    print("WEDNESDAY")
elif nu==5:
    print("THURSDAY")
elif nu==6:
    print("FRIDAY")
else:
    print('SATURDAY!!')'''

#7
'''A=100
S=math.sqrt(A)
print(S)'''

#9
'''l=[6,5,3,8,4,3,5,4,11]
s=0
for i in l:
    s=s+i
print(f'sum={s}')'''

#10
'''rec={"Mark":90,"Harry":87,"Aavas":32,"Nathan":76,"Marcus":92,"Paul":88,"Laam":100}
Nam=input('Enter the name of the student(first letter capital)')
if Nam in rec:
    print(rec.get(Nam))
elif Nam not in rec:
    print('Invalid entry')'''

#8
'''Var1='A'
Var2='B'
Var1,Var2=Var2,Var1
print(Var1,Var2)'''