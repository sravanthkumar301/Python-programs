#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str="#python#@iot#"
for char in str:
    if char.isalphabet():
       print(char)


# In[ ]:


#range of 1,10

for number in range(1,10):
    print(number)


# In[ ]:


f=open(r"C:\Users\srava\Desktop\sravan.txt","r")
print(f.read())
f.close()


# In[ ]:


f=open(r"C:\Users\srava\Desktop\sravan.txt","w")
print(f.write("vishnu \n "))
f.close()


# In[ ]:


f=open(r"C:\Users\srava\Desktop\sravan.txt","r")
print(f.read())
f.close()


# In[ ]:


f=open(r"C:\Users\srava\Desktop\sravan.txt","a")
print(f.write("vardhan \n"))
f.close()


# In[ ]:


f=open(r"C:\Users\srava\Desktop\sravan.txt","wb")
import pickle
a = [1,2,3]
pickle.dump(a,f)
f.close()


# In[ ]:


f=open(r"C:\Users\srava\Desktop\sravan.txt","rb")
import pickle
a = pickle.load(f)
print(a)
f.close()


# In[ ]:


dict={"name":"sravan","age":21,"native":"nellore"}
print(len(dict))


# In[ ]:


dict={"name":"sravan","age":21,"native":"nellore"}
index(sravan)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#printing of even numbers
for number in range(1,20):
    if(number%2==0):
        print(number)
 


# In[ ]:


#sum 1,100
a=0
for i in range(1,100):
    a=a+i
print(a)


# In[ ]:


names = ["sravan", "vikas", "venkatesh", "mahendra", "vishnu"]

for name in names:
    print(name)


# In[ ]:


name="sravan"
for name in name:
    print(name)


# In[ ]:


a=1
for i in range(1,100):
     a=a*i
        print(a)


# In[ ]:


units=int(input("enter your units"))
if units <= 100:
        total_bill = units * 10
elif 100>units<= 200:
    total_bill = (100 * 10) + ((units- 100) * 15)
elif 200>units <= 300:
    total_bill = 100 * 10 + 100 * 15 + (units - 200) * 20
else:
    total_bill = 100 * 10 + 100 * 15 + 100 * 20 + (units - 300) * 25
    
print(total_bill)
    


# In[ ]:


#first 10 even numbers
for i in range(1,11):
  if i%2==0:
    print(i)


# In[ ]:


#first 10 odd numbers
for i in range(1,11):
  if i%2!=0:
    print(i)


# In[ ]:


#first 10 natural numbers
for i in range(1,11):
    print(i)


# In[ ]:


#first 10 whole number
for i in range(0,11):
    print(i)


# In[ ]:


#write a programme to print first 10 integers and their squares using while loop 1 1, 2 4, 3 9 and so on
for i in range(1,11):
    a=i*i
    print(i,a)


# In[ ]:


#wru=ite a loop statement to print the following series 10,20,30,40......300
for i in range(10,301,10):
    print(i)
    


# In[ ]:


#wru=ite a loop statement to print the following series 105,98,91,....7.
for i in range(105,6,-7):
    print(i)


# In[ ]:


#write aprogramme to print 10 natural num in reverse order
#i=11
#while i>=2:
#   i-=1
 #  print(i)
i=11
while i>=2:
    i-=1
    print(i)


# In[ ]:




#write a programme to print sum of first 10 natural num
sum=0
for i in range(1,11):
    sum=sum+i
    print(sum)
    
# In[ ]:


#write a programme to print sum of first 10 even  num
sum=0
for i in range(1,20):
    if i%2==0:
        sum=sum+i
        print(sum)


# In[ ]:


#write a programme to print table of a number given by user 
a=int(input('enter the number'))
for i in range


# In[ ]:


#write a programme to print all even number that fall b/w two numbers 
#(exclusive both numbers )entered from the user using while loop
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Even numbers between", start, "and", end)
print("-----------------------")

if start % 2 != 0:  # If start number is odd, increment it by 1
    start += 1

while start < end:
    print(start)
    start += 2  # Increment by 2 to get the next even number


# In[ ]:


number = int(input("Enter a number: "))

print("Table of", number)
print("  ")

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)


# In[ ]:


#write a programme to check whether a number is prime or not using while
number = int(input("Enter a number: "))

is_prime = True
divisor = 2

while divisor < number:
    if number % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime and number > 1:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# In[ ]:


#Write a program to find the sum of the digits of a number accepted from the user.
n=int(input("enter the number"))
s=0
st=str(n)
for i in st:
    s=s+int(i)
    print(s)


# In[ ]:


#Write a program to find the product of the digits of a number accepted from the user.
n=int(input("enter the number"))
s=1
st=str(n)
for i in st:
    s=s*int(i)
    print(s)


# In[ ]:


#Write a program to reverse the number accepted from user using while loop.
num=int(input("enter the num"))
sum=0
while num!=0:
    n1=num%10
    sum=sum*10+n1
    num//=10
print(str(sum))
    


# In[ ]:


#Write a program to reverse the number accepted from user using while loop.
num=int(input("enter the num"))
sum=0
while num!=0:
    n1=num%10
    sum=sum*10+n1
    num//=10
print(sum)
print(type(sum))    


# In[ ]:


#1. Write a Python program to find the maximum of two numbers using the greater than operator.
a=int(input("enter the first number"))
b=int(input("enter the second number"))
if(a>b):
    print("a is greater than b")
else:
    print("b is greater than c")


# In[ ]:


#2. Write a program to check if a given number is even or odd using the modulo operator.
num=int(input("enter the num"))
if(num%2==0):
    print("the num is even")
else:
    print("the num is even")


# In[ ]:


#Write a program to check if a given year is a leap year or not using logical operators.
year=int(input("enter the year"))
if(year%400==0):
    print("the year is leap")
else:
    print("not a leap year")


# In[ ]:


year=int(input("enter the year"))
if(year%4==0 and year%100!=0):
    print("the year is leap")
else:
    print("not a leap year")


# In[ ]:


# year=1999
# if year%4==0:
#     if year%100==0 and year%400==0:
#     print('Leapyear')   
# else:
#     print('Not Leapyear')

y=1700
if y%4==0:
    if y%100!=0:
        print("leap year")
    else:
        if y%400==0:
            print("Leap year")
        else:
            print('Not leap year')
else:
    print('Not a Leap year')


# In[ ]:


#Write a program to check if a given character is a vowel or a consonant using if-elif-else statements.
vowels="AEIOU"
char=(input("enter the char"))
if(char in vowels):
    print(f"{char} is vowel")
else:
    print("it is consonent")


# 

# In[ ]:


#Write a program to calculate the total cost of purchasing a quantity of a particular item,
#considering a discount based on the quantity purchased.
amount=int(input("enter the amount"))
if(amount>=2000):
    discount=(amount/100*5)
    total=(amount-discount)
    print(total)
else:
    print("discount is not available")


# In[ ]:


# Write a program to determine if a triangle is equilateral, isosceles, or scalene based on the lengths of its sides.
a=int(input("enter first side"))
b=int(input("enter third side"))
c=int(input("enter third side"))
if((1/2*(a*b)):
   print("triangle is isoseles")


# In[ ]:


var="sravan"
print(var.capitalize())


# In[ ]:


var="sRAVAN"
print(var.capitalize())


# In[ ]:


var="sravansravan"

print(var.lstrip())


# In[ ]:


var="sravan is agood boy"

print(var.split())


# In[ ]:


var="sravan kumar"
print(var.replace("sravan kumar","anil kumar"))


# In[ ]:


var="sravan*is*agood*boy"

print(var.split('*'))


# In[ ]:


#Write a Python program to find the maximum of two numbers using the greater than operator.
a=10
b=20
if a<b:
           print(a is greater)
   else:
       print((b is greater))


# In[ ]:


#Write a function that takes a string as input and returns `True` if it is a palindrome (reads the same forwards and backwards), and `False` otherwise.



# In[ ]:


help(str)


# In[ ]:


#capitalize()	Converts the first character to upper case
v="sRaVaN"
print(v.capitalize())


# In[ ]:


#casefold() Converts string into lower case
v="sraVanth kumar Is good Boy"
print(v.casefold())


# In[ ]:


#accesing
#positive indexing
#sravan
#012345
str="sravan"
str[0]
str[1]
str[2]
str[3]
str[4]
str[5]


# In[ ]:


#negative indexing
#-6-5-4-3-2-1
# s r a v a n
var="sravan"
var[-1]
var[-2]


# In[ ]:


#slicing
#[start:end:step]
var="my name is sravan"
var[1:16:2]

#length(str)
var=("sravan")  # it gives length of the passed value
len(var)
# In[ ]:


str="sravan"
print(str[0:1])
print(str[0:])
print(str[:1])
print(str[ ::-1])
print(str[:])
print(str[::-1])



# In[ ]:


str="123"
rev=str[ ::-1]
if (str==rev):
    print('palindrome')
else:
    print('not palindrome')


# In[ ]:


str="sravan"
i=0
len_str=len(str)
while i<len_str:
    print(str[i])
    i+=1


# In[ ]:


n=int(input("enter value"))
for i in range(1,n+1):
    print("*"*i)


# In[ ]:


n=int(input("enter value"))
for i in range(1,n+1):
     print("* "*i)
        


# In[ ]:


str="#python#@iot#"
for i in str:
    if i.isalpha():
        print(i)


# In[ ]:


password=input("enter password")
upper_count=0
lower_count=0
special_count=0
digit_count=0
for i in password:
    if i.uppercase:
        upper_count+=1
    elif i is lower_count:
        lower_count+=1
    elif i is digit_count:
        digit_count+=1
    else:
        special_count+=1
if len(password)>=8 and  upper_count>=2 and lower_count>=1 and speacial_count>=1 and digit_count>=2:
    print("password is valid")
else:
    print("invalid password")
    


# In[ ]:


import string
help(string)


# In[ ]:


import string
alpha=string.ascii_lowercase
print(alpha)


# In[ ]:


dir(str)


# In[ ]:


list1=[1,2,3,4]
print(list1[3])


# In[ ]:


list=("sravakumar")
list[0:2]


# In[ ]:


list=["vikas","sravan"]
list.append("sulliga")
print(list)


# In[ ]:


list=["vikas","sravan"]
list.extend("")
print(list)


# In[ ]:


list=[1,2,3,4,5,10,[10,11,12,[1,2,3]]]
print([list[3],list[6][1],list[6][3][1]])


# In[ ]:


list=[1,2,3,4,5,6]
list.remove(1)


# In[ ]:


list=[1,2,3,4]
del list[2]
print(list)


# In[ ]:


list = ["sravan", "vikas", "vishnu"]
list.remove("vishnu")
print(list)


# In[ ]:


list = [1,2,3,4]
list.remove(1)
print(list)


# In[ ]:


list=[1,1,1,2,3,4]
list1=list.count(1)
print(list1)


# In[ ]:


list1=[1,2,3,4,5,2,1]
list2=list1.count(10)
print(list2)


# In[ ]:


var=[1,2,3,4,5,2,3,1]
var1=var.index(5)
print(var1)


# In[ ]:


var=[1,2,3,4,5,2,3,1]
var1=var.index(5)
print(var1)


# In[ ]:


list=[1,2,3,4,5,6]
list.reverse()
print(list)


# In[ ]:


str1='python'
print(str1)
str2=str1[::-1]
print(str2)
print(str1)


# In[ ]:


list1=[1,2,3,4,5]
print(list1)
list2=list1[::-1]
print(list2)
print(list1)


# In[ ]:


list1=[16,3,7,9,10]
list1.sort(reverse=true)
print(list1)


# In[ ]:


list=[1,-5,10]
list.sort()
print(list)

n=max(list)
print(n)

n=min(list)
print(n)


# In[ ]:


var="AXBZYC"
print(max(var))
print(min(var))


# In[ ]:


#sum of squares
number=[2,3,4,5,6,7,8]
sum=0
for num in number:
    sum=sum+num**2
    print(sum)


# In[ ]:


num=int(input("enter the num"))
count=1
print("multiplication table of",num)
while count<=10:
    ans=num*count
    print (num, 'x', count, '=', ans)    
    count+=1


# In[ ]:


a=5
def fun():
    a=10+a
    b=20
    print(a,b,globals()["a"])
    
fun()


# In[ ]:


def is_harshad_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0
def find_harshad_numbers(start, end):
    harshad_numbers = []
    for num in range(start, end+1):
        if is_harshad_number(num):
            harshad_numbers.append(num)
    return harshad_numbers
start_num = 1
end_num = 100

harshad_nums = find_harshad_numbers(start_num, end_num)
print("Harshad numbers between", start_num, "and", end_num, "are:", harshad_nums)


# In[ ]:


n=int(input("enter the number"))
if n<0:
    n=-n
    square=n*n
while(n>0):
    if (n%10!=square%10):
        print("{} is automorphile".forma


# In[ ]:


dict1={"name":"sravankumar","age":20}
print(dict1)


# In[ ]:


#nested dictionary
dict={"name":{1,2,3,4}}
print(dict)


# In[ ]:


#sravan=key 1is keyvalue[kumar and 301 is list]
dic={"sravan":{1:["kumar",301]}}
print(dic["sravan"][1][0])


# In[ ]:


dic={"sravan":{1:["kumar",301]}}
print(dic["sravan"])


# In[ ]:


dic={"sravan":{1:["kumar",301]}}
print(dic["sravan"][1][1])


# In[ ]:


#get().method
dic={"name":"sravan","age":21,"district":"nellore"}
print(dic.get("name"))
print(dic.get("age"))
print(dic.get("district"))


# In[ ]:


#values().method+writes key values as a list 
dic={"name":"sravan","age":21,"district":"nellore"}
x=dic.values()
print(x)


# In[ ]:


#key().method=writtens keys and adds the key 
dic={"name":"sravan","age":21,"district":"nellore"}
dic2=dic["btech","yeruru","sravan"]="mechanical"
x=dic.keys()
print(x)
print(type(dic2))


# In[ ]:


#update()=
dict={1:2,2:4,4:16}
dict1={}
dict.update()


# In[ ]:


#map() 
s=[1,2,3,4,5]
add=list(map(lambda x:x**2,s))
print(add)


# In[ ]:


#map() 
s=[1,2,3,4,5]
mul=list(map(lambda x:x*2,s))
print(mul)


# In[ ]:


#zip
list1=[1,2,3,4,5]
list2=["sravan","vikas","vishnu","venkatesh","nani"]
result=zip(list1,list2)
print(list(result))


# In[ ]:


#filter()
list1=[1,2,3,4,5]
x=filter(lambda x:x>=1,list1)
print(list(x))


# In[ ]:


#ennumerate()
names=["sravan","vikas","vishnu"]
for i,name in enumerate(names):
    print(i,name)


# In[ ]:


#binary()
print(bin(16))


# In[ ]:


list=[1,2,3]
for i in list:
    print((bin(i)))


# In[ ]:


#min
list=[1,2,3,4,5]
max(list)


# In[ ]:


#max
list=[1,2,3,4,5]
min(list)


# In[ ]:


#reduce()
import functools


# In[ ]:


#mjin()
list=[1,2,3,4,5]
print(min(list))


# In[ ]:


a=[1,2,3,4]

length=len(a)
print(length)


# In[ ]:


a=1.25
b=2
print(round((a*b)))


# In[ ]:


a=1.423
print(round(a,3))


# In[ ]:


seq=[1,0,4,3]
print(seq.reverse())


# In[ ]:


#bin
x=3
y=bin(x)
print(y)


# In[ ]:


#char
a=103
print(chr(a))


# In[ ]:


#reduce
from functools import reduce
a=[1,2,3,4,5]
b=reduce(lambda x,y:x+y,a)
print(b)

print("*************************")

def product(x,y):
    return x*y

b=reduce(product,[1,2,3,4,5])
print(b)


# In[ ]:


#accumulate()
#from package_name import module_name  (how to import packages from modules)
#from library_name.package_name import module_name
#syntax: itertools.accumulate(iterable,function)

from itertools import accumulate

a=[1,2,3,4]
   
print(list(accumulate(a,lambda x,y:x+y)))


# In[ ]:


#filters()
a=[-1,-2,-3,1,2,3]
result=list(filter(lambda x:x>=0,a))
print(result)


# In[ ]:


var=open(r'‪C:\Users\srava\Desktop\lopps2.txt','r')


# In[ ]:


var = open(r'‪C:\Users\srava\Desktop\lopps2.txt')


# In[ ]:


var = open(r'‪C:\Users\srava\Desktop\iot.txt','w')


# In[ ]:


#syntax
#dict={key:value,key:value}
a={"name":"sravan","age":21,20:"yeruru"}
a.get(20)


# In[ ]:


#values()
d={1:2,2:4,3:6}
b=d.values()
print(b)


# In[ ]:


#key()
a={'name':'sravan','age':21,'village':'yeruru'}
x=a.keys()
print(x)


# In[ ]:


#items()
a={'name':'sravan','age':21,'village':'yeruru'}
x=a.items()
print(x)


# In[ ]:


#update()
a={'name':'sravan','age':21,'village':'yeruru'}
a.update({'colour':'white'})
print(a)


# In[ ]:


class demo:
    a='python'
    a1='iot'
obj=demo()
print(obj)

print('*********************')

class demo:
    a='python'
    a1='iot'
obj=demo()
print(demo.a)#calling function-name or class name
print(demo.a1)
print(type(obj))# calling from object
print(obj.a)
print(obj.a1)


# In[ ]:


class Mahindra:
    def suresh(friend):
        friend.venkatesh='sravanth '
        friend.vikas='Four Twenty'
        #return(friend.venkatesh+friend.vikas)
    def vishnu(friend):
        print(friend.venkatesh+friend.vikas)
        
obj=Mahindra()
obj.suresh()
obj.vishnu()


# In[ ]:


class Mahindra:
    def suresh(friend):
        friend.venkatesh='Hostel Roommates '
        friend.vikas='Friends'
        return(friend.venkatesh+friend.vikas)
    def vishnu(friend):
        friend.v='4'
        friend.vi='20'
        return(friend.v+friend.vi)
        
obj=Mahindra()
Noor=obj.suresh()
Mahesh=obj.vishnu()
print(Noor)
print(Mahesh)


# In[ ]:


class Demo:
    '''hello world'''
    attr1='vikas'
    att2='loves women'

    def method(self):
        print(obj.__dict__)
        self.a=10
        self.b=20
        print(self.a+self.b)
        print(obj.__dict__)
    
    
    def method2(self):
        print(obj.__dict__)
        try:
            print(self.a+self.b)
        except Exception as e:
            print(e)

obj=Demo()
obj.method()

print(obj.__dict__)
obj.method2()

print(obj.__dict__)


# In[ ]:


class Dog:

    attr1 = "mammal"

# Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()


# In[ ]:


class Demo:
    '''hello world'''
    attr1='vikas'
    att2='loves women'

    def method(self):
        print(obj.__dict__)
        self.a=10
        self.b=20
        print(self.a+self.b)
        print(obj.__dict__)
    
    
    def method2(self):
        print(obj.__dict__)
        try:
            print(self.a+self.b)
        except Exception as e:
            print(e)

obj=Demo()
#obj.method()

print(obj.__dict__)
obj.method2()

print(obj.__dict__)


# In[ ]:


#string palindrome
x="malayalam"
y=x[::-1]
if x==y:
    print("{} is palindrom".format(x))
else:
    print("{} is not a palindrome".format(x))


# In[ ]:


#number palindrome
n=int(input("enter number"))
temp=n
rev=0
while n>=1:
    rem=n%10
    rev=((rev*10)+rem)
    n=n//10
if(temp==rev):
    print("{} is palindrome".format(temp))
else:
    print("{} is not a palindrome".format(temp))


# In[ ]:


#nested if statement
x=50
if x>10:
    print("above ten")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 20")
else:
    print("none")


# In[ ]:


#while loop
i=0
while i<6:
    print(i)
    i+=1


# In[ ]:


#while loop
i=1
while i<6:
    print(i)
    i+=1


# In[ ]:


#for loop
names=["sravan","vikas","vishnu"]
for x in names:
    print(x)


# In[ ]:


for x in "sravan":
    print(x)


# In[ ]:


#break statemennames=["sravan","vikas","vishnu"]
names=["sravan","vikas","vishnu"]
for x in names:
    print(x)
    if x=="vikas":
        break


# In[ ]:


#continue statement
names=["sravan","vikas","vishnu"]
for x in names:
   
    if x=="vikas":
        continue
    print(x)


# In[ ]:


#else in for loop:
for x in range(6):
    print(x)
else:
    print("finished!")


# In[ ]:


#break in for loop:
for i in range(5):
    print(i)
    if i==2:
        break
    
        
print('finished')
        
    


# In[ ]:


i=1
while i<6:
    if i==3:
        break
    print(i)
    i+=1
    


# In[ ]:


#bank
class Bank:
    Bank_name="CANARA"
    ifsc_code="CNRB100"
    
    def __init__(self,account_name,account_number,amount):
        self.a=account_name
        self.b=account_number
        self.c=amount
        
obj=Bank("sravan","12345","2456")
print(obj.a)
obj.__dict


# In[ ]:


#college
class College:
    College_name="SVR"
    College_address="Ayyalur"
    
    def __init__(self,branch_name,Roll_num,student_rank):
        self.a=branch_name
        self.b=Roll_num
        self.c=student_rank
obj=College("mech","19R1A0301","first rank")
print(obj.a)
obj.__dict__


# In[ ]:


class Person:
    
    def __init__(self,name,sex,age,profession):
        self.name=name
        self.sex=sex
        self.age=age
        self.profession=profession
        print(self.name,self.age)
    def show(self):
        print(self.name,self.sex,self.age,self.profession)
        
employee=Person('sravanth','male','21','software developer')
employee.__init__
employee.show()
employee.__dict__


# In[ ]:


class Car:
    company="Tata"
    def design (self,model,colour,seating):
        self.m=model
        self.c=colour
        self.s=seating
        print(self.company)
        print(self.m)
        
    def show(self):
        print(self.c,self.s)
        
menu=Car()
menu.design("thor","black","7")
menu.show()
menu.__dict__


        
    
    


# In[ ]:


class Demo:
    def __init__(self,a):
        self.a=a
        
obj1=Demo(2)
print(obj1.__dict__)
obj2=Demo(4)
print(obj2.__dict__)
obj1+obj2


# In[ ]:


v="python"

x=(v*2)


print(x)


# In[ ]:


class Int:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a

obj1=Int(2)
print(obj1.__dict__)
obj2=Int(4)
print(obj2.__dict__)
obj1+obj2
Int.__add__(obj1,obj2)
    
    
        


# In[ ]:


a="thatiparthi"
b="vikas"
v=a+b
print(v)
x=a*b
print(x)#strings canot be multiply


# In[ ]:


class Int:
    def __init__(self,a):
        self.a=a
    def __truediv__(self,other):
        return self.a/other.a

obj1=Int(2)
print(obj1.__dict__)
obj2=Int(4)
print(obj2.__dict__)
obj1/obj2
Int.__truediv__(obj1,obj2)
    


# In[2]:


#Single-level inheritance
class Animals:
    'Animals are lion,dog,rabit,....'
    def __init__(self,eat,speak):
        self.e=eat
        self.s=speak
        print('I can ',self.e)
        print('i can ',self.s)
    def display(self,bath):
        self.b=bath
        print("i cant do",self.b)
        
class Dog(Animals):
    def __init__(self,name,behave,bath,eat,speak):
        
        self.n=name
        self.be=behave
        
        print("i am ",self.n)
        
        print("i have ", self.be)
        super().__init__(eat,speak)
        #super().__init__(speak)
        #super().__init__(bath)
        self.display(bath)
        
lab=Dog('vikas','mental','bath','bite','bow')

        
    
    


# ## 

# In[17]:


l=[5,7,10,11,1]
start=0
end=len(l)
while start<end:
    l[start],l[end-1]=l[end-1],l[start]
    start+=1
    end-=1
print(l)


# In[1]:


l=[5,7,10,11,111,-23] 
max_num = l[0]
min_num=l[4]
for i in l:
    if max_num < i:
        max_num=i
    if min_num>i:
        min_num=i
print(min_num)
print(max_num)


# In[5]:




