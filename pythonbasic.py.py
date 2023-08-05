#!/usr/bin/env python
# coding: utf-8

# In[1]:


#string methods
#concatunation=combining more than two variables using(+) operator
str1=('sravan')
str2=("vikas")
str3=("vishnu")
str4=(str1+" "+str2+" "+str3)
print(str4)


# In[2]:


str1="1,2,3,4,"
str2="5,6,7,8"
str3=str1+str2
print(str3)


# In[3]:


str1="hello"
str2="sravan"
print(str1+" "+str2)


# In[4]:


#repetition=repeting of word with a short space of words.
str1="sravan"
print((str1+" ")*4)


# In[5]:


#capetalize=convert first character to upper case in a string.
str1="sravAN"
print(str1.capitalize())


# In[6]:


#count_method=writtens number of times a specified value occurs in astring.
var="sravankumar"
print(var.count('r'))


# In[7]:


var = list([1,2,3])
var


# In[8]:


#find_method=written the  first position of the value .
var="sravansravan"
print(var.find("s"))


# In[9]:


#rfind_method
var="sravan sravan"
print(var.rfind("s"))


# In[10]:


#index=writtens first position
var="sravan sravan"
print(var.index("s"))


# In[11]:


#index=writtens first position
var="sravan sravan"
print(var.index("z"))


# In[ ]:


#rindex_method
var="sravan ravan"
print(var.rindex("r"))


# In[ ]:


#rindex_method
var="sravan ravan"
print(var.rindex("k"))


# In[ ]:


#rindex_method
var="1,2,3,4"
print(var.rindex(","))


# In[ ]:


#uppercase=writtens the uppercase for the string
str=("sravn kumar")
print(str.upper())


# In[ ]:


#uppercase=writtens the uppercase for the string
str=("srAvn Kumar")
print(str.upper())


# In[ ]:


#lowercase=writtens the lowercase for the string
str=("SravaN kuMaR")
print(str.lower())


# In[ ]:


#swapcase_method=it converts upper case to lower case and lowercase to uppercase.
var="sRaVaN"
print(var.swapcase())


# In[ ]:


#tittle
var="sraVan"
var1=var.ti+++++++++++tle()
print(var1)


# In[ ]:


#Write a Python program to print the length of a string.
str="sravan"
len(str)


# In[ ]:


#2. Write a Python program to concatenate two strings.
str1="sravan"
str2="kumar "
str3="chevuru"
str4=(str1+str2+str3)
print(str4)


# In[ ]:


#3. Write a Python program to convert a string to uppercase.
str="sravan"
print(str.upper())


# In[ ]:


#4. Write a Python program to convert a string to lowercase.
str="SRAVAN"
print(str.lower())


# In[ ]:


#5. Write a Python program to check if a string starts with a specific prefix.
str1="sravan"
prefix="s"
print(str1.startswith(prefix))


# In[ ]:


#6. Write a Python program to check if a string ends with a specific suffix.
str1="sravan"
suffix="van"
print(str1.endswith(suffix))


# In[ ]:


#7. Write a Python program to find the index of a specific character in a string.
str="sravan"
str.index("s")


# In[ ]:


#8. Write a Python program to count the occurrences of a specific character in a string.
str="sravankumar"
str.count("r")


# In[ ]:


#9. Write a Python program to replace all occurrences of a specific character in a string with another character.
str1="sravan"
str1.replace("sravan","kumar")


# In[ ]:


#10. Write a Python program to split a string into a list of words.
str="sravan"
str.split(" ")


# In[ ]:


#Write a Python program that takes a user input and prints the length of the input string.
input1=input("enter the input")
len(input1)


# In[ ]:


#Write a Python program that takes a user input and prints the input string in uppercase.
var=input("enter the input")
print(var.upper())


# In[ ]:


#Write a Python program that takes a user input and checks if it contains only numeric characters.
var="123"
var.isdigit()


# In[ ]:


#Write a Python program that takes a user input and counts the number of vowels (a, e, i, o, u) in the input string.
var=input("enter the input ")
vowels=("a,e,i,o,u")
count=0
for vowel in var:
    if vowel in vowels:
        count+=1
print(count)


# In[12]:


#Write a Python program that takes a user input and checks if it is a palindrome (reads the same forwards and backwards).
var1=input("enter the input")
var2=var1[::-1]
if var1==var2:
    print("it is palindrome")
else:
    print("not a palindrome")


# In[5]:


#Write a Python program that takes a user input and prints the reversed version of the input string
var1=input("enter the input ")
var2=var1[::-1]
print(var2)


# In[7]:


#Write a Python program that takes a user input of a sentence and capitalizes the first letter of each word.
var=input("enter the input")
print(var.capitalize())


# In[19]:


#Write a Python program that takes a user input of a sentence and capitalizes the first letter of each word.
var1="sravan is a good boy"
var2=var1.split(" ")
print(var2)
for u in range(len(var2)):
    print(var2[u].capitalize())


# In[21]:


#Write a Python program that takes a user input of a sentence and capitalizes the first letter of each word.
var = 'jaya prasad'
print(var.title())


# In[7]:


help(str)


# In[8]:


#Write a Python program that takes a user input and checks if it is a valid email address (contains "@" and ".").
var=input("enter your mail ")
if "@" in var and "." in var:
    print("valid")
else:
    print("invalid")


# In[ ]:


#Write a Python program that takes a user input and replaces all occurrences of a specific character with another character.
var=input("  ")
var2=var.replace(var,"kumar")
print(var2)


# In[ ]:


#Write a Python program that takes a user input and checks if it is a valid password 
# (contains at least one uppercase letter, one lowercase letter, and one digit).
password=input("eneter password ")
upper_count=0
lower_count=0
digit_count=0
for i in password:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
    elif i.isdigit():
        digit_count+=1
if(upper_count>=1 and lower_count>=1 and digit_count>=1):
    print("valid password")
else:
    print("invalid")
    


# In[3]:


#1. Write a Python program that takes a list of numbers as input and prints the sum of all the numbers
list=[1,2,3,4,5,6]
print(sum(list))


# In[9]:


#2. Write a Python program that takes a list of strings as input and prints the concatenation of all the strings.
a="sravan"
b="vikas"
c=a+b
print(c)


# In[11]:


var=[1,6,3]
var.sort()
print(var)
var[2]


# In[12]:


import string
help(str)


# In[ ]:


#armstrong number
n=int(input("enter number"))
t=n%10
n=n//10
sum=0
while n!=0:
    rem=n//10
    n=n//10
    sum=sum+rem**3
if n==sum:
    print("armstrong")
else:
    print("not a armstrong")


# In[ ]:


# Python program to check if the number is an Armstrong number or not


num = int(input("Enter a number: ")) # take input from the user
sum = 0                              #initialize sum
temp = num                          
while temp > 0:
   rem = temp % 10
   sum = sum+rem ** 3       # find the sum of the cube of each digit
   temp //= 10
if num == sum:                        # display the result
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[ ]:


#fibonacci
n=0
n=1
num=int(input("enter range"))

