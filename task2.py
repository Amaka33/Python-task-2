import string
import random


def user_details():
    fname= input('What is your first name? ')
    lname= input('What is your last name? ')
    email= input('Input email address: ')
    details= [fname, lname, email]
    return details

def random_password(details):
    characters = string.ascii_letters
    lngth = 5
    ran_passw = ''.join(random.choice(characters) for i in range (lngth))
    
    pword = str(details[0][0:2] + details[1][-2:] + ran_passw)
    
    return pword

store = []
continuation = True

while continuation:
    
    details = user_details()
    pword = random_password(details)
    print (f'Your generated password is {pword}')
    
    user_confirmation = input('Do you like the generated password?[yes/no] ')
    confirmation = True
    while confirmation:
        if user_confirmation == 'yes':
            details.append(pword)
            store.append(details)
            confirmation = False
        
        else:
            user_pword = str(input('Please input your desired password[characters must be >7]: '))
                        
            pword_lngth = True                
            while pword_lngth:
                if len(user_pword) >=7:
                    print('Your password is saved')
                    details.append(user_pword)
                    store.append(details)
                    pword_lngth = False
                    confirmation = False                               
                else:
                   user_pword = input('Please characters must be >7, input valid password: ')
                   
                   
                                                 
    new_user = str(input('Are you the last user?[yes/no] '))
    if new_user == 'yes':
        continuation = False
        for details in store:
            print()
            print(f'Name: {details[0]} {details[1]}')
            print(f'Email address: {details[2]}')
            print(f'Password: {details[-1]}')
            print()
            
        
    else:
        continuation = True
                
            