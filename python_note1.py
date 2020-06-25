#!/usr/bin/env python
# coding: utf-8

# In[8]:


nest=[1,2,3,[4,5,['target','source']]]


# In[9]:


nest[3][2][1]


# In[6]:


d={'name': 'SHivam', 'Class': '12th', 'School': 'PPS'}


# In[7]:


print(d)


# In[8]:


d['name']


# In[ ]:


d['name']+ d['Class']


# In[10]:


seq=['a','b','c']


# In[17]:


for item in seq:
    i=2
    while i<=4:
        
        print(item)
        
        i=i+1


# In[18]:


for item in seq[0:4]:
    i=2
    while i<=4:
      
        i=i+1

        print(item)


# In[45]:


count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break


# In[22]:


data=[1,2,3]
for item in data[:-1]:
    print(item)


# 

# In[80]:


a = [1, 2, 3, 4, 5]
for x in reversed(a):
    print(x)


# In[33]:


a = [1, 2, 3, 4, 5]
for x in a[::-1]:
    print(x)


# In[6]:


seq=['a','b','c']
i=0

while i<=4:
    for item in seq:
        print(item)
    i=i+1
        


# In[15]:


seq=['a','b','c']
arg=[1,3,5]
for item in seq:
    for source in arg:
        print(item)
        print(source)


# In[47]:


m=[0,1,2,3,4]
i=0
while i<=4:
    
    for n in m:
        
        result=n*n
        print(result)
        
        i=i+1
        print(i)


# In[11]:


m=[0,1,2,3,4]

for n in m:
    result=n*n
    print(result)


# In[1]:


def add_num(a,b):
    return(a+b)
add_num(2,3)


# In[46]:


def add_numbers(x,y,z=1):
    print(x)
    print(y)
    print(z)
    
    
    if z==None:
        print(add_numbers(1,2))
        return x*y


    else:
        
        return x*y*z
    
    
    
    
    
add_numbers(1,2,3)
    
 


# In[110]:


def add_numbers(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers(1, 2, flag=True))


# In[116]:


add_numbers(1,2)


# In[1]:


num=int(input("show the multiplication table of"))
for i in range(1,11):
 print(num,'X',i,'=',num*i)


# In[36]:


num=int(input("Show the multiplication table of"))
def table(n):
    for i in range(1,11):
    
        print(n,'x',i, '=',n*i)

n=15
table(num)



# In[48]:


x=(1,'a',2,'b')
type(x)


# In[49]:


x=[1,2,'a','b']
type(x)


# In[50]:


x.append(3.3)


# In[51]:


x


# In[52]:


x[3]='c'


# In[53]:


x


# In[54]:


for item in x:
    print(item)


# In[55]:


i=0
while(i!=len(x)):
    print(x[i])
    i=i+1


# In[56]:


[1,2]+[3,4]


# In[57]:


[1]*3


# In[58]:


1 in[1,2,3]


# In[59]:


0 in[1,2,3]


# In[60]:


x='This is a string'


# In[61]:


x


# In[64]:


print(x[0])
print(x[0:1])
print(x[0:2])
print(x[0:])


# In[72]:


x[-2]
x[-4:-2]


# In[73]:


x[:3]


# In[80]:


firstname="Shivam"
lastname="Bhat"
print(firstname + ' ' + lastname)
print(firstname*3 + ' ' + lastname*3)
print('name' in firstname)


# In[92]:


firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0] # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1] # [-1] selects the last element of the list
print(firstname)
print(lastname)


# In[122]:


firstname = 'Monkey.D Roronoa Hawkeye Toshiro'.split(' ')[0:4]
lastname='Luffy Zoro Mihawk Hitsugaya'.split(' ')[0:4]
print(firstname)
print(lastname)


# In[116]:


'shivam' + str(2)


# In[133]:


firstname = 'Monkey.D Roronoa Hawkeye Toshiro'.split(' ')[0][:9]
lastname='Luffy Zoro Mihawk Hitsugaya'.split(' ')[0][:6] 
print(firstname)
print(lastname)


# In[166]:


x={'shivamBhat':'shivambhat.sb@gmail.com',
   'Mayagomes':' mayaworld.mw@gmail.com '}


# In[167]:


x


# In[168]:


x['shivamBhat']


# In[170]:


for name in x:
    print(name)


# In[174]:


for email  in x.values():
    print(email)


# In[175]:


for name, email in x.items():
    print(name)
    print(email)


# In[186]:


x=("Shivam","Bhat","shivambhat.sb@gmail.com")
y=("Gary" ,"Kirsten","gkafrica@gmail.com")
fname,lname,email=x
gname,hname,gmail=y
print(x + y)


# In[177]:


x


# In[178]:


fname


# In[179]:


lname


# In[180]:


email


# In[188]:


print("Hello" + "world")


# In[191]:


greeting="Hello"
name=input("please enter the name")
print(greeting + ' ' + name)


# In[22]:


splitstring='this\nstring \nhas been split\nover several times.'
print(splitstring)
tabbedstring="1\t2\t3\t4"
print(tabbedstring)
print('the pet owner" shop\' \'said \'t \'n ', ' \n ,he is ' 'resting ".')
print("the pet  shop owner said\"\n\t,'no'....no he is resting\".")
print("""the pey shop ownder said "no 'n'o.... \'the 'is resting".""")


# In[24]:


print("C:\\Users\\shivbhat\\Desktop")


# In[25]:


print(r"C:\Users\shivbhat\Desktop")


# In[76]:


greeting="hello"
name=input("enter the name here")
print(greeting+name)
print(greeting+ ' ' +name)
print(type(greeting))
print(type(name))


# In[74]:


table=int(input("enter mul table"))
def mul(n):
    for i in range(1,11):
        
        print(n, 'x', i, '=' ,n*i)
          
        
n=10
mul(table)
    


# In[80]:


a=12
b=3
#(a//b) #integer division ,rounded  down to minus infinity
for i in range(1,a//b):
    
    print(i)


# In[84]:


Lion='asiatic lion'
print(Lion[:])


# In[131]:


parrot="Norwegian Blue"
parrot[3:5]
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print(parrot[-11])
print(parrot[0:6])
print(parrot[:])
print(parrot[-11:-1])
print(parrot[-4:])


# In[17]:


number="9,332;345:231;111;661,523"
seperators=number[1::4]
print(seperators)
values="".join(char if char not in seperators else " " for char in number).split
print([int(val)for val in values])
    


# In[99]:


text = 'geeks for geeks'
  
# Splits at space 
print(text.split())


# In[90]:


text = 'geeks for geeks'
  
# Splits at space 
print(text.split()) 
  
word = 'geeks, for, geeks'
  
#using Split method


# In[13]:


letters="abcdefghijklmnopqrstuvwxyz"
backwards=letters[25::-1]
print(backwards)

#slicingbackwards


# In[22]:


letters="abcdefghijklmnopqrstuvwxyz"

letters[16:13:-1]
letters[4::-1]
letters[25:17:-1]
letters[:-9:-1]
#slicing backwards


# In[12]:


string1= "He"
string2=" is probably"
string3="roaming"
string4="in the woods"
print(string1 + ' ' + string2 + ' ' + string3 + ' ' + string4)
print("hello  " *   (5 + 4 ))
print("hello  "  * 5 +"4")
#concatenating Strings


# In[65]:


Today="monday"
print("mon" in Today)
print("day" in Today)
print("thurs" in Today)
print("don" in Today)

#Finding substring in String


# In[76]:


#string replacement fields

age=24
print("My age is {0} years".format(26))

print("There are {0} days in {1},{2},{3},{4},{5},{6},{7} ".format(31,"\njan","\nMar","\nMay","\nJuly","\nAug","\nOct","\nDec"))

print("jan:{0}, feb:{2}, Mar:{0}, Apr:{1} ,May:{0}, June:{1}, July:{0}, Aug:{0}, Sept:{1}, Oct:{0}, Nov:{1}, Dec:{0}".format(31,30,28))


# In[3]:


for i in range(1,13):
    print("No. is {0:2},squared is {1:3},cubed is {2:3} ".format(i,i**2,i**3))


# In[5]:


for i in range(1,13):
    print("No. is {0:<2},squared is {1:<3},cubed is {2:<3} ".format(i,i**2,i**3))


# In[9]:


print("pi is approx equal to : {0:12}".format(22/7))
print("pi is approx equal to : {0:<12f}".format(22/7))
print("pi is approx equal to : {0:12.50f}".format(22/7))
print("pi is approx equal to : {0:<42.50f}".format(22/7))
print("pi is approx equal to : {0:<78.50f}".format(22/7))


# In[74]:


age=26
name=input("Enter your name \n")
print( 'I'' ' 'am' +' ' + name + '' + f" and my age is {age}years old")
print(type(age))
print(f" pi is approximately  equal to{22/7:12.50f}")


# In[76]:


pi=22/7

print(f"pi is approx  equal to {pi:12.50f}")


# In[79]:


"spam" + "eggs" + "beans"
"spam\neggs\nbeans"


# In[83]:


first_name = "John"
last_name = "Cleese"
age = 78
 
print(first_name + last_name + str(age))


# In[86]:


quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
 
Total = total + tax
 
print(total)


# In[87]:


days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])


# In[118]:


word = 'geeks:for:geeks'
  
# Splitting at ':' 
print(word.split(':',4)) 


# In[15]:


word = 'geeks, for, geeks,' 'pawan'
  
# maxsplit: 0 
print(word.split(' , ',0)) 
  
# maxsplit: 4 
print(word.split(', ', 4)) 
  
# maxsplit: 1 
print(word.split(', ', 1)) 


# In[7]:


name=input("please enter your name")
age=int(input("How old are you {}".format(name)))
print(age)

if age<=18:
    print("come back in {} years".format(18-age))
elif age==1000:
    print("You are ancient")
else:
    print("you are eligible to vote")
            


# In[ ]:


#guess game
answer=5
guess=int(input("please guess the  number:"))
if guess!=answer:
    if guess<answer:
        print("guess a little higher")
        guess=int(input("please guess the  number:"))
    if guess<5:
        print("Guess again")
    else:
        print("guess a little lower")
        
    guess=int(input("please guess the  number:"))
    if guess==answer:
        print("correct answer")
    else:
        print("incorrect answer")
        


# In[22]:


#guess game part 2:
answer=5
guess=int(input("please guess the  number:"))
if guess==answer:
    print("you got it first time")
else:
        
    if guess<answer:
        print("guess a little higher")
        guess=int(input("please guess the  number:"))
    if guess<5:
        print("Guess again")
    else:
        print("guess a little lower")
        
    guess=int(input("please guess the  number:"))
    if guess==answer:
        print("correct answer")
    else:
        print("incorrect answer")


# In[35]:


age=int(input("how old are you"))
if age>=16 and age<=65:
    print("Have a good day at work")
else:
    print("enjoy free time")
    print("o_o" *12)


# In[39]:


age=int(input("how old are you"))
if age>=16 or age>=65:
    
   print("Have a good day at work")
else:
    print("enjoy free time")
    print("o_o" *12)
    


# In[44]:


day="wednesday"
temperature=28
raining=not True
if day =="saturday" and temperature>27 or not  raining:
    
    print("I will go to swim")
else:
    print("I will sleep")


# In[11]:


if 0:
    print("True")
else:
    print("False")
    
name=input("enter the name")
if name!= "":
    
    print("name is {}".format(name))
else:
    print("A man with no name")


# In[ ]:


letter = input("enter any random letter/word here?")
print(letter.casefold())
if "vlad" in letter.casefold():
    print("Nothing here")


# In[1]:


name=input("\t enter your name")
age=int(input("\tenter your age"))
if age>=18  and age<=31:
    print("\tyou can go for holiday")
else:
    print("sorry not allowed")


# In[11]:


number="9,223;372:036 854,775;807."
seperators=''
for char in  number:
    if  not char.isnumeric():
        seperators=seperators+char
print(seperators)
    


# In[12]:


quote=" Hello guys, I am a new bie and its fun to code"
for letter in quote:
    
     if letter not in quote.casefold():
            print(letter)
       


# In[14]:


for i in range(1,20):
    print("number is {},squared is {},cubed is {}".format(i,i**2,i**3))


# In[25]:


for i in range(1,100,5):
    print(i)


# In[26]:


for i in range(100 , 1 ,-5):
    print(i)


# In[50]:


for i in range(0,10):
    for j in range(2,3):
        print("{0} X {1} = {2}".format(j,i,j*i))
print("--------------------------------------")


# In[46]:


def pyramid(n):
    for i  in range(0,n):
        for j in range(0,i+1):
            
            print("*",end="")
        #print(end="\n")
        print("\r")
        
n=5
pyramid(n)
        


# In[2]:


shopping_list=["apple","eggs","wheat","spam","rice"]
for i in shopping_list:
    if i=="eggs":
        continue
    print( " buy " +   i )


# In[10]:


shopping_list=["apple","eggs","spam","wheat","sugar"]
item_to_be_found="spam"
found_at=None

for index in range(len(shopping_list)):
    if shopping_list[index]==item_to_be_found:
        found_at=index
        break
print("the item is found at {} position  and value is {}".format( found_at, shopping_list[index]))


# In[43]:


shopping_list=["bar","wheat","rice","Barley"]
item_to_be_found="Chocolate"
found_at=None
if item_to_be_found in shopping_list:
    found_at=shopping_list.index(item_to_be_found)

if  found_at is not None:
                   
    print("item is found at {}".format(found_at ))
    print("item is  {}".format(item_to_be_found))
else:
    print("{} not found".format(item_to_be_found))
            
               


# In[39]:


ch = "geeksforgeeks"
  
# initializing argument string  
ch1 = "geeks"
  
# using index() to find position of "geeks" 
# starting from 2nd index  
# prints 8 
pos = ch.index(ch1,2) 
  
print ("The first position of geeks after 2nd index : ",end="") 
print (pos) 


# In[47]:


i=0
while i<10:
    print("the value of i is : {}".format(i))
    i+=1
    


# In[28]:


game_exit=["north","south","east","west"]
direction=input("enter the right direction for levelling up the game")
while direction not in game_exit:
    if direction.casefold()=="exit":
        print("game over")
        break
    
    direction=input("enter the right direction for levelling up the game")
    

else:
    
    print("You have cleared this game level")
    


# In[7]:


for i in range(0, 100, 7):
    if i > 0 and i %11 == 0:
        print(i)

        break


# In[19]:


for i in range(21):
    if i > 0 and i %3 != 0 and i %5 != 0:
        print(i)


# In[27]:


for i in range(21):
    if i > 0 and i %3==0 or  i %5==0:
        continue
        print(i)
    else:
        print(i)


# In[ ]:


#Guess game using random

import random
highest=11
answer=random.randint(1,highest)
print(answer)
print("enter the number bewteen 1 and {}".format(highest))
guess=int(input())
if guess==answer:
    print("you got it for the first time")
else:
    if guess<answer:
        print("Guess the number a little higher?")
        guess=int(input("Guess again"))

        
    if guess<answer:
        print("Guess again?")
    else:
        print("guess a little lower")
guess=int(input("enter the number "))
if guess==answer:
    print("you are finally correct")
else:
    print("I give up!")
    


# In[ ]:


#guess game using while Loop
import random
highest=11
answer=random.randint(1,highest)
print(answer)
print("enter the number bewteen 1 and {}".format(highest))
guess=int(input())
while guess!=answer:
    guess=int(input())
    
    
    if guess==answer:
        print("you got it for the first time")
        break
    else:
        if guess<answer:
            print("Guess the number a little higher?")
            guess=int(input("Guess again"))

        
        if guess<answer:
            print("Guess again?")
        guess=int(input("press 0 for exit"))
            
        if guess==0:
            break
        else:
            print("guess a little lower")
            break
            
#guess=int(input("enter the number "))
#if guess==answer:
    #print("you are finally correct")
#else:
   # print("I give up!")
    


# In[25]:


#hi lo game
low=1
high=1000
print("enter the numbers btw  {} and {}".format(low,high))
input("Enter the guess")
guesses=1
while True:
    print("enter the guesses between {} an  {}".format(low,high))
    guess=low+(high-low)//2
    high_low=input("Try to guess the number.It is either high(h),low(l) or correct(c)"
                  "my guess is {}".format(guess))
    if high_low=="h":
        #guess is low,guess for higher no.
        
        low=guess+1
    elif high_low=="l":
        #guess is high , guess for little lower no.
        high=guess-1
    elif high_low=="c":
        #guess is correct
        print("you answer is correct and I got in {} guesses".format(guesses))
        break
    else:
        print("enter either h,l or c")
    guesses=guesses+1
else:
    print("you have thought of no. {}".format(low))
    print("you got in {} no. of guesses".format(guesses))
        
        
    
    


# In[10]:


#augmented assignement
greeting="good"
greeting+= " morning "
print(greeting)

greeting*=5
print(greeting)


# In[8]:


number = 5
multiplier = 8
answer = 0
for i in range(multiplier):
    answer+=number

 
print(answer)


# In[22]:


list=[23,45,1,19,0,-6]
list.sort()
print("smallest number is {}".format(list[0]))
print("smallest number is {}".format(min(list)))


# In[ ]:


option=input("select the options from the list")
list=["learn java","learn digital maketing","learn python","learn AI","learn cooking"]


# In[ ]:


print("1:Learn java")
print("2:learn digital maketing")
print("3:learn python")
print("4:learn AI")
print("5:learn cooking")
print("Select the interest from given options below:\n1.{} \n2.{}\n3.{}\n4.{}\n5.{}".format(a,b,c,d,e))

choice=int(input("Select from below "))
while choice!=0:
    if choice=="1":
        print("Learn java")
        break
    elif choice=="2":
        print("learn digital maketing")
        break
    elif choice=="3":
        print("learn python")
        break
    elif choice=="4":
        print("learn AI")
        break
    elif choice=="5":
        
        print("learn cooking")
        break
else:
    print("out")
        
        
    


# In[1]:


print("choose your option for  below:")
print("1:\t learn python")
print("2:\t learn java")
print("3:\t learn sql")
print("4:\t learn cooking")


while True:
    choice=input()
    if choice=="0":
        break
    elif choice in"12345":
        print("you choose in {}".format(choice))
    else:
        break


# In[9]:


value = 8
answer = 0
 
for x in range(1, 13):
    answer = value * x
print("{0} times {1} is {2}".format(x, value, answer))


# In[12]:


asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]
 
for asteroid in asteroids:
    if asteroid == 9617:
        print("Grahamchapman")
    elif asteroid == 9618:
        print("Johncleese")
    elif asteroid == 9619:
        print("Terrygilliam")
        break
    elif asteroid == 9620:
        print("Ericidle")
    elif asteroid == 9621:
        print("Michaelpalin")
    else:
        print("Terryjones")
else:
    print("MontyPython")


# In[2]:


choice = None
 
while choice != '0':
    choice = input("Please enter your choice.  Press enter to quit")
    if choice == '':
        
        break
        
 
        print("You have selected {}".format(choice))
    
else:
    print("Thank you for playing, please call back soon.")


# In[49]:


a=int(input("enter first no:"))
b=int(input("enter second no."))
print(a+b)
print(a-b)
print(a*b)


# In[81]:


# Python program to check leap year or not 
def checkYear(year): 
    
    year=int(input("please enter the year"))
    
    
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                    return True
            else: 
                return False
        else: 
            return True
    else: 
        return False

# Driver Code 
year = 2000
if(checkYear(year)): 
	print("Leap Year") 
else: 
	print("Not a Leap Year") 
	
# This code is contributed by Chinmoy Lenka 

    

             
       


# In[86]:


def checkyear(year):
        year=int(input("please enter the year"))
        if (year % 4)== 0:
            print("leap year")
            return True
        else:
            print("not")
            return False
checkyear(year)

    


# In[87]:


def is_leap(year):
    year = int(input())


    if (year % 4)== 0:
        print("leap year")
        return True
    else:
        print("not a leap year")
        return False



is_leap(year)
    


# In[93]:


def is_leap(year):
    leap = False
    if (year % 4)== 0:
        return True
    else:

        return leap
    year = int(input())
is_leap(year)
year = int(input())
print(is_leap(year))


# In[94]:



string = """    geeks for geeks    """ 
 
# prints the string without stripping 
print(string)  
 
# prints the string by removing leading and trailing whitespaces 
print(string.strip())    
 
# prints the string by removing geeks 
print(string.strip(' geeks')) 


# In[114]:


n = int(input().strip())
if n%2!=0:
    print("Weird")    
elif n%2 == 0 and 2 <= n <= 5:
    print ("Not Weird")
elif n%2 == 0 and 6 <= n <= 20:
    print ("Weird")
else:
    print("Not Weird")


# In[124]:


n=int(input())
for i in range(1,n+1):
    print(i,end='')


# In[125]:


sum = 0
for i in range(1, 11): 
    sum = sum + i 
print("Sum of first 10 natural number :", sum) 


# In[ ]:




