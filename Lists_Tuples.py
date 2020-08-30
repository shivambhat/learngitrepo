#!/usr/bin/env python
# coding: utf-8

# In[2]:


Feline_species=["Panther","lion","Tiger","leopard","Puma","Cougar","Cheetah"]
Feline_species.append("snow leopard")
for i in  Feline_species:
    print("Animal is {}".format(i))
      


# In[8]:


even=[2,4,6,8]
odd=[1,3,5,7]
numbers=even+odd
ordered_numbers=sorted(numbers)
print(ordered_numbers)

if ordered_numbers==numbers:
    print("numbers in order")
else:
    print("numbers in disarray")
    


# In[6]:


list1=[]
list2=list() #constructor is being called without any parameters
print("the list 1 is {} ".format(list1))
print("the list 2 is {} ".format(list2))
if list1==list2:
    print("match")
else:
    
    print("match not found  ")
    
    
print(list("match"))



# In[2]:


even=[2,4,6,8]
another_even=list(even) #constructor is being called with  parameter as even.
another_even.sort(reverse=True)
print(even)
print(another_even)

if even== another_even:
    print("match")
else:
    print("no match found")


# In[28]:


even=[2,4,6,8,10]
odd=[1,3,5,7,9]
numbers=[odd,even]
for i in numbers:
    print(i)
    for j in i:
        print(j)


# In[29]:


menu=[]
menu.append(["eggs","spam","bacon"])
menu.append(["eggs","sausage","bacon"])
menu.append(["eggs","spam"])
menu.append(["eggs","bacon","spam"])
menu.append(["eggs","bacon","sausage","spam"])
menu.append(["spam","eggs","sausage","bacon"])
menu.append(["spam","sausage","eggs","bacon"])
menu.append(["spam","eggs","sausage","spam"])
for meal in menu:
    if not "spam" in meal:
        print(meal)
        for ingredients in meal:
            print(ingredients)
       


# In[65]:


menu=[]
menu.append(["eggs","spam","bacon"])
menu.append(["eggs","sausage","bacon"])
menu.append(["eggs","spam"])
menu.append(["eggs","bacon","spam"])
menu.append(["eggs","bacon","sausage","spam"])
menu.append(["spam","eggs","sausage","bacon"])
menu.append(["spam","sausage","eggs","bacon"])
menu.append(["spam","eggs","sausage","spam"])


i=0
for meal in menu[i]:
    
    
    if  meal[i] in "spam":
        
        
        continue
        
            
    print("\n")    
    print("meal" +  meal)
    for ingredients in meal:
        print( ingredients,end=" ")
       


# In[190]:


list=[2,3,6,6,5]
list.sort(reverse=True)
print(list)
i=int(input("enter the valuse of list"))
if list[i]==max(list):
    print("winner")
elif list[i]==max(list)-1:
    print(list[i])
    print("runner up")
else:
    print("you  are too far behind")


# In[184]:


list=[2,3,6,6,5]
print(max(list)-1)


# In[104]:


list=['apple','mango','orange','banana','pears']
my_iterator=iter(list)
n=list.len()
for i in range(n):
    
    print(next(my_iterator))
    
    
 
print("\n")    
for i in list:
    print(i)


# In[115]:


list=['apple','mango','orange','banana','pears']
my_iterator=iter(list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


# In[6]:


my_list=list(range(10))
print(my_list)

even=list(range(0,100,2))
odd=list(range(0,100,1))
print("\n")

print(even)
print("\n")
print(odd)


# In[3]:


string="12345566577454858uirohsojfslfjslt34tl"
print(string.index('5'))
print(string[16])


# In[19]:


Decimals=range(1,150,2)
print(Decimals)
print(Decimals[23])
print(Decimals.index(23))
print(list(Decimals))


# In[128]:


sevens=range(0,100,7)
x=int(input("enter the value less than 30? "))
if x in sevens:
    
    print("{} is divisble by 7".format(x))


# In[7]:


sevens=range(0,100,7)

print(list(sevens))


# In[130]:


y=range(0,50,5)
for i in y[::-1]:
    print(i)
    print("\n")
    


# In[131]:


y=range(50,0,-5)
for i in y:
    
    print(i)


# In[162]:


decimals=range(0,50)
my_range=decimals[0:50:5]
for i in my_range:
    print('X'* 20 )
print("\n")
print("-x-x-x-x-x-x-x-x-x-x--x-x-x-x-x-x--x-x-x-x-x--x-x--x-x--x-x--x-x--x-x--x-x-x--x-x-x-x--x-x-x--x--x-x--x-x-x-x--x-x-x--x")
print("\n")

    
    
for i in range(0,50,5):
    print('X' * 20)
    
    
print(my_range==i)
    
    


# In[176]:


o=range(0,30,2)
print(o)

p=o[::5]
for i in p:
    print(i)


# In[40]:


r=range(0,20)
print( list(r[::-1]))


  


# In[47]:


decimals=range(0,100)
my_range=decimals[3:40:3]
print(my_range)
print(list(my_range))
for i in my_range:
    print(i)
print(my_range==range(3,40,3))


# In[8]:


#objects are immutable not  variables
t=("name","address","age")
print(t)
t=t[0],"Addresses",t[2]
print(t)


# In[2]:


a,b=12,13
a,b=b,a
print(a,b)


# In[3]:


#unpacking of tuple
x,y,z=t
print(x,y,z)


# In[22]:


even = range(0, 20, 2)
 
for number in even[::-1]:
    print(number, end=', ')
    


# In[31]:


current_choice="_"

computer_parts=[] #empty list
while current_choice!='0':
    if current_choice in "1234567":
        if current_choice== "1":
            computer_parts.append("Modem")
            
            print("adding {}".format(current_choice))
        elif current_choice=="2":
            computer_parts.append("CPU")
            
            print("adding {}".format(current_choice))
        elif current_choice=="3":
            computer_parts.append("Printer")
            
            print("adding {}".format(current_choice))
        elif current_choice=="4":
            computer_parts.append("Keyboard")
            
            print("adding {}".format(current_choice))
        elif current_choice=="5":
            
            computer_parts.append("Harddisk")

            print("adding {}".format(current_choice))
            
        elif current_choice=="6":
             computer_parts.append("Mouse")
             print("adding {}".format(current_choice))
            
        elif current_choice=="7":
             computer_parts.append("HDMI Cable")
             print("adding {}".format(current_choice))
                
    else:
        print("Add options from list below:")
        print("1:Modem")
        print("2:CPU")
        print("3:Printer")
        print("4:Keyboard")
        print("5:Harddisk")
        print("6:Mouse")
        print("7:Mouse")
        print("0:Finish")
        
    current_choice=input()
    
print(computer_parts)
            


# In[6]:


current_choice="_"
computer_parts=[]
available_parts=["Modem","CPU","Printer","Keyboard","Harddisk","Mouse","HDMI Cable"]

while current_choice!='0':
    if current_choice in"1234567":
        if current_choice=="1":
            computer_parts.append("Modem")
            
            print("adding {}".format(current_choice))

        elif current_choice=="2":
            computer_parts.append("CPU")
            print("adding {}".format(current_choice))

        elif current_choice=="3":
            computer_parts.append("Printer")
            print("adding {}".format(current_choice))

        elif current_choice=="4":
            computer_parts.append("Keyboard")
            print("adding {}".format(current_choice))

        elif current_choice=="5":
            computer_parts.append("Harddisk")
            print("adding {}".format(current_choice))

        elif current_choice=="6":
            computer_parts.append("Mouse")
            print("adding {}".format(current_choice))

        elif current_choice=="7":
            computer_parts.append("HDMI Cable")
            print("adding {}".format(current_choice))

    else:
        print("From List of items below:")
            
        for parts in available_parts:
            
                
                
            print("{0}:{1}".format(available_parts.index(parts)+1,parts))
            
                      
    current_choice = input()
                      
print(computer_parts)
                  
                         


# In[11]:


current_choice="_"
computer_parts=[]
available_parts=["Modem","CPU","Printer","Keyboard","Harddisk","Mouse","HDMI Cable"]

while current_choice!='0':
    if current_choice in"1234567":
        if current_choice=="1":
            computer_parts.append("Modem")
            
            print("adding {}".format(current_choice))

        elif current_choice=="2":
            computer_parts.append("CPU")
            print("adding {}".format(current_choice))

        elif current_choice=="3":
            computer_parts.append("Printer")
            print("adding {}".format(current_choice))

        elif current_choice=="4":
            computer_parts.append("Keyboard")
            print("adding {}".format(current_choice))

        elif current_choice=="5":
            computer_parts.append("Harddisk")
            print("adding {}".format(current_choice))

        elif current_choice=="6":
            computer_parts.append("Mouse")
            print("adding {}".format(current_choice))

        elif current_choice=="7":
            computer_parts.append("HDMI Cable")
            print("adding {}".format(current_choice))

    else:
        print("From List of items below:")
        
            
        for number,parts in enumerate(available_parts):
            
        
            
                
                
            print("{0}:{1}".format(number+1,parts))
            
                      
    current_choice = input()
                      
print(computer_parts)
                  
                         


# In[5]:


#refactoringthecode
current_choice="_"
computer_parts=[]
available_parts=["Modem","CPU","Printer","Keyboard","Harddisk","Mouse","HDMI Cable"]


valid_choices=[]

for i in range(1,len(available_parts)+1):
    
    valid_choices.append(str(i))
print(valid_choices)
    
    
    
    

while current_choice!='0':
    if current_choice in valid_choices:
        index=int(current_choice)-1
        choice=available_parts[index]
        computer_parts.append(choice)
        
        
        print("adding {}".format(current_choice))
            
            

        
    else:
        print("From List of items below:")
        
            
        for number,parts in enumerate(available_parts):
            
        
            print("{0}:{1}".format(number+1,parts))
            
                      
    current_choice = input()
                      
print(computer_parts)
                  
                         


# In[6]:


data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = [Flower for Flower in data  if "Flower" in Flower]
shrubs = [Shrub for Shrub in data  if "Shrub" in Shrub]
print(flowers)
print(shrubs)


# In[6]:


#RemovingitemsformList
current_choice="_"
computer_parts=[]
available_parts=["Modem","CPU","Printer","Keyboard","Harddisk","Mouse","HDMI Cable"]


valid_choices=[]

for i in range(1,len(available_parts)+1):
    
    valid_choices.append(str(i))
print(valid_choices)
    
while current_choice!='0':
    if current_choice in valid_choices:
        index=int(current_choice)-1
        choice=available_parts[index]
        if choice in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(choice)
        else:
            print("Adding {}".format(current_choice))
            
            computer_parts.append(choice)
        print("your list now contains {}".format(computer_parts))

            
    else:
        print("From List of items below:")
        
            
        for number,parts in enumerate(available_parts):
            
        
            print("{0}:{1}".format(number+1,parts))
            
                      
    current_choice = input()
                      
print(computer_parts)
                  
                         


# In[10]:


even=[2,4,6,8]
odd=[1,3,5,7]
even.extend(odd)
print(even)
another_even=even
print(another_even)

even.sort(reverse=True)
print(even)
print(another_even)


# In[1]:


pangram="the quick brown fox jumps over lazy dog"
letters=sorted(pangram)
print(letters)

numbers=[1,2,4,7,9,11,1,5]
m=sorted(numbers)
print(m)

numbers.sort()
print(numbers)


# In[2]:



#caseinsensitivesorting
car_names=["eon","maruti","Hyundai","Honda","Tata","fiat"]
car_names.sort(key=str.casefold)

print(car_names)


# In[12]:


#Diffwaysofcreatingalist
even=[2,4,6,8]
odd=[1,3,5,7]
numbers=even+odd
print(numbers)
numbers.sort()
print(numbers)
Sorted_numbers=sorted(numbers)
more_numbers=numbers.copy()
print(more_numbers)
print(Sorted_numbers)
print(numbers is Sorted_numbers)
print(numbers == Sorted_numbers)

more_numbers=numbers[:]
print(more_numbers)


more_numbers=list(numbers)
print(more_numbers)


# In[15]:


computer_parts=["modem","cpu","monitor","mouse","keyboard","trackball"]
computer_parts[3:]=["printer","scanner","gpu"]
print(computer_parts)


# In[16]:


#deletingitemsfromlist
Data=[12,1,3,100,140,240,178,102,200,210,236]
max_range=200
min_range=100
for index,value in enumerate(Data):
    
    if value<100 or value>200:
        del Data[index]
        
print(Data)


# In[40]:


#Removingthelowvalues

Data=[12,1,3,100,140,240,178,102,200,210,236]
max_range=200
min_range=100
stop=0
for index,value in enumerate(Data):
    print(index)
    print(value)
    if value>=min_range:
        stop=index
        break
        
        
print(stop)#debugging
    
del Data[:stop]

print(Data)
#print(stop)

        


# In[28]:


#Removingthehighvalues

Data=[12,1,3,100,140,240,178,102,200,210,236]
max_range=200
min_range=100
start=0
for index,value in enumerate(Data):
    
    print(index)
    print(value)
    if value<=min_range:
        stop=index
    continue
        
        
print(stop)#debugging
    
del Data[:stop]

print(Data)
#print(stop)

        


# In[3]:


#removing High values
Data=[100,140,240,178,102,200,210,236]
max_range=200
min_range=100
start=0
for index in range(len(Data)-1,-1,-1):
    print(index)
    if Data[index]<=max_range:
        start=index+1
        break
        
print(start)
del Data[start:]
print(Data)
        


# In[11]:


#removing hgh & low end values
data=[104,101,4,5,308,103,107,100,306,102,108]
min_valid=100
max_valid=200
for index in range(len(data)-1,-1,-1):
    print(index)
    if data[index]<min_valid or data[index]>max_valid:
        print(data,index)
        del data[index]
print(data)


# In[3]:


data=[104,101,4,5,308,103,107,100,306,102,108]
min_valid=100
max_valid=200
top_index=len(data)-1
for index,value in enumerate(reversed(data)):
    if data[index]<min_valid or data[index]>max_valid:
        
        
        print(top_index-index,data)
        del data[top_index-index]
        print(data[8])

   
        


print(data)
        
        
        


# In[8]:


#Nested List
even=[2,4,6,8]
odd=[1,3,5,7]
numbers=[even,odd]
print(numbers)

for numbers_list in numbers:
    print(numbers_list)
    for num in numbers_list:
        print(num)


# In[7]:


menu=[
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"],
]


for meal in menu:
    
    if "spam" not in meal:
        
        print(meal)
        
        for item in meal:
            
            print(item)
    else:
        print("{0} has a spam score of {1}".format(meal,meal.count("spam")))
        
    
    
    


# In[42]:


#NospamChallange
menu=[
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"],
]
print(len(menu))
for meal in menu :
    for index in range(len(meal)-1,-1,-1):
        print(index)
        if meal[index]=="spam":
            del meal[index]
            
    print(meal)
    
   


# In[20]:


#Second Approach
menu=[
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"],
]

for meal in menu:
    for item in meal:
        if item!="spam":
            print(item)
            print("\n")
    print(",".join(meal),end=",")


# In[6]:


flowers=["Sunflower","Tulip","Iris","Dahlia","Rose"]

   
print("->".join(flowers))
    


# In[4]:


#Tuples
metallica="Ride the lightning","Metallica","1984"
print(metallica)
metallica2=list(metallica)
print(metallica2)
metallica2[0]="master of puppets"
print(metallica2)


# In[6]:


#unpacking the Tuple
data_tuple=1,2,4
x,y,z=data_tuple
print(x)
print(y)
print(z)


# In[11]:


#More Unpacking
for t in enumerate("abcdefghi"):
    index,character=t
    print(index,character)


# In[18]:


table=("cofee table",200,100,75,34.50)
print(table[1]* table[2])
name,length,width,height,price=table
print("area is" , length * width)


# In[21]:


#More UnPacking
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for album in albums:
    name,artist,year=album
    
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
    
    
    
for name,artist,year in albums:
    
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
    


# In[22]:


for name,artist,year in albums:
    
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
    


# In[70]:


albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for album,name,year,song in albums:
    
        
    print("album:{}, name:{},year:{},song:{}".format(album,name,year,song))
    print()
    album=albums[3]
    print(album)
    songs=album[3]
    print(songs)
    song=songs[2]
    print(song)
    songes=song[1]
    


# In[66]:


print(song)
print(songs)
print(album)

mayhem=albums[3][3][2][1]
print(mayhem)


# In[71]:


print(song)
print(songes)


# In[76]:


albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
 
print(albums[1])
print()
print(albums[1][3])
print()

print(albums[1][3][5])
print()

print(albums[1][3][5][1])

print(albums[2])
print()
print(albums[2][2])


# In[78]:


print(albums[2])
print()
print(albums[2][2])



# In[20]:


values="23,2,45,66,77,90,13,3"
print(values)
type(values)

values_list=values.split(",")

print(values_list)
for index in range(len(values_list)):
    
    values_list[index]=int( values_list[index])
    
    
    
print( values_list,end="\n")


# In[22]:


empty=[]
for value in values_list:
    empty.append(int(value))
print(empty)
    


# In[2]:


albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]


# In[5]:


while True:
    print("Please use your album(invalid chioce exists):")
    for index,(title,artist,year,songs) in enumerate(albums):
        print("{}:{},{},{},{}".format(index+1,title,artist,year,songs))
    break


# In[8]:


for index,value in enumerate(albums):
    
    title,artist,year,songs=value
    
    
    print(index+1,title,artist,year,songs)


# In[5]:


#Simple JukeBox
SONGS_LIST_INDEX=3 #constant
SONGS_TITLE_INDEX=1 #constant
while True:
    print("Please use your album(invalid chioce exists):")
    for index,(title,artist,year,songs) in enumerate(albums):
        print("{}:{}".format(index+1,title))
    
    choice=int(input())
    if 1<=choice<=len(albums):
        songs_list=albums[choice-1][SONGS_LIST_INDEX]
    else:
        break
    print(albums[choice-1])
    print(songs_list)
    print()
    
    print("choose your song")
    for index,(track,song) in enumerate(songs_list):
        print("{}:{}".format(index+1,song))
    
    song_choice=int(input())
    if 1<=song_choice<=len(songs_list):
        title=songs_list[song_choice-1][SONGS_TITLE_INDEX]
    else:
        
        
       for index,(track,song) in enumerate(songs_list):
        
        print("{}:{}".format(index+1,song))
        
        break
        
        
        
    print("playing..... {}".format(title))
    print( '=' * 40)


# In[ ]:




