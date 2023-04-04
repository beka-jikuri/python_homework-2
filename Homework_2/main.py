 # task N1


     # 1.1

Phone = 'Samsung'

print("Is Phone == 'Samsung'? I think it's true")
print(Phone == 'Samsung')
print("\nIs Phone == 'iPhone'? I think it's false")
print(Phone == 'iPhone')



    # 1.2

text = "Good Evening"
x = text.lower()

print('\n',x)




#     # 1.3

number = 1000

print('\n',"true:", number>800)
print('\n',"false:", number>1200)
print('\n',"true:", number==1000)
print('\n',"false:", number!=1000)


print("\n")
# --------------------------------------------------------------------------------------------------------------------------------------

print("\n")

#  task N2

    # 2.1

alien_color = 'Green'

if alien_color == 'Green':
    print("you've just earned 5 points!")



    #2.2 
alien_color = 'Blue'

if alien_color == 'Green':
    print("you've just earned 5 points!")
else: print("you've just earned 10 points!")    





    #2.3

alien_color = 'Red'

if alien_color == 'Green':
    print("you've just earned 5 points!")
elif alien_color == 'Yellow':
    print("you've just earned 10 points!")
elif alien_color == 'Red':  
    print("you've just earned 15 points!")  



print("\n")
print("\n")

    # 2.3

age = 1

if 2>age:
    print("Person is a baby!")
elif 2<=age<4:
    print("Person is a toddler!")
elif 4<=age<13:
    print("Person is a kid!")
elif 13<=age<20:
    print("Person is a teenager!")
elif 20<=age<65:
    print("Person is an adult!")
elif 65<=age:
    print("Person is an elder!")



print("\n")
print("\n")

    # 2.4


fruits = ['Apple', 'Grape', 'Jack Fruit', 'Pineapple', 'Peach', 'Dragon Fruit', 'Mango','Banana']
favorite_fruits = ['Apple','Banana','Peach']

for fruit in fruits:
    if fruit in favorite_fruits :
        print(f"{fruit}:you really like it! ")
    else: print(f"{fruit}:It's just a fruit!")    

print("\n")
print("\n")

# --------------------------------------------------------------------------------------------------------------------------------------
# Task #3

    # 3.1

Usernames = ['Jordan', 'Nicole', 'admin', 'Nick', 'Beka']

for username in Usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else: 
        print(f"Hello {username}, thank you for logging in again.")
                


print("\n")
print("\n")



    # 3.2   --------- see "hello_admin.py"

    # 3.3

current_users = ['Jordan', 'Nicole', 'admin', 'Nick', 'Beka']
new_users = ['Nicole', 'Jack', 'Nomi', 'Gwen', 'Nick']


for name in new_users:
    if name in current_users:
        print(f"{name} is already taken.please, choose another one!")
    else:
        print(f"{name} is available, you can take it.")


print("\n")
print("\n")

    # 3.4

Number_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numb in Number_List:
    if numb == 1:
        print(f"{numb}st")
    elif numb == 2:
        print(f"{numb}nd")
    elif numb == 3:
        print(f"{numb}rd")
    else:
        print(f"{numb}th")            





print("\n")
print("\n")



# --------------------------------------------------------------------------------------------------------------------------------------

# task N4

product = [['Paulaner',11], ['Hoegaarden',10], ['primator',9], ['HB',12], ['Augustiner',13]]



for beer in product:
    print (beer[0], beer[1])