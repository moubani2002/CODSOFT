#codsoft task - 3:
#Password generator

import random
def generate_password():

    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2',
               '3', '4', '5', '6', '7', '8', '9', '0', '!' ,'@', '#', '$', '%', '&']
    
    length = int(input("Enter the length of the password: "))

    new_password =" "

    for x in range(length):
        new_password = new_password+random.choice(keys)

    print("Your password is: ", new_password)

generate_password()


