from user import User

import re
class Userfunctions:
    userlist=[]
    def reg(self):
        name=input('Enter fullname: ')

        phno_in=input('Enter 10 digit phone number: ')  
        def validate_phno_in(phno_in):
            pattern = re.compile(r'^\d{10}$')
            return bool(pattern.match(phno_in))
        if validate_phno_in(phno_in):
            phno=phno_in

        else:
            print(f"{phno_in} is an invalid phone number")
            phno_in=input('Enter correct phone number:')
            phno=phno_in
        
         
        email_in=input('Enter email id:')
        def validate_email_in(email_in):
            pattern = re.compile(r'\w+[@][a-z]+[.]com$')
            return bool(pattern.match(email_in))
        
        if validate_email_in(email_in):
            email=email_in  
                        
        else:
            print(f"{email_in} is an invalid email id")
            mail=input('Enter correct email id:') 
            email=mail      
        
        addr=input('Enter address: ')
        pw=input('Enter password: ')
        userobj=User(name,phno,email,addr,pw)
        self.userlist.append(userobj)
        print('\nLogin to continue\n')

    def login(self):
        print('\nEnter email id and pass word to log in\n')
        email_in=input('Enter email id: ')
        pw_in=input('Enter password: ')
        for user in self.userlist:           
            dict=user.__dict__           
            if dict['email'] == email_in and dict['pw']==pw_in:
                print('\nWelcome user\n')
                print(user)
            else:
                print('Enter correct deatils')
                email_in=input('Enter email id: ')
                pw_in=input('Enter password: ')
    dish_list=[]    
    def new_order(self):
        
        print('\nEnter\n \n1- Tandoori Chicken (4 pieces) [INR 240] \n2- Vegan Burger (1 Piece) [INR 320] \n3- Truffle Cake (500gm) [INR 900] \n ')
        dish=input('Enter the food ids to order: ')
        print('***Ordered dishes***')
        d={1:'Tandoori Chicken (4 pieces) [INR 240]',2:'Vegan Burger (1 Piece) [INR 320]',3:'Truffle Cake (500gm) [INR 900]'}
                      
        for i in dish:
            if i!=',':
                for j in i:
                    k=d[int(j)]
                    print(k)
                    self.dish_list.append(k)
        #print(dish_list)
        dish_choice=int(input('\nEnter\n\n1- For new orders \n0- Otherwise \n: '))
        if dish_choice==1:
            print('\nEnter \n1- Tandoori Chicken (4 pieces) [INR 240] \n2- Vegan Burger (1 Piece) [INR 320] \n3- Truffle Cake (500gm) [INR 900] \n: ')
            dish=input('Enter the food ids to order: ')
            d={1:'Tandoori Chicken (4 pieces) [INR 240]',2:'Vegan Burger (1 Piece) [INR 320]',3:'Truffle Cake (500gm) [INR 900]'}
            for i in dish:
                if i!=',':
                    for j in i:
                        k=d[int(j)]
                        self.dish_list.append(k)  
            dish_choice=int(input('\nEnter\n1- For new orders \n0- Otherwise \n: '))             
            placed_order=int(input('Enter 1 to place the order \n:'))
            if placed_order==1:
                for dish in self.dish_list:
                    print(dish)
                print('Order placed successfully!!')
                
        else :        
            pass
        
    def ord_his(self):
        print('***Order history***')
        for dish in self.dish_list:
                print(dish)
    
    def update_prof(self):
        print('\nEnter email id and pass word to update your profile in\n')
        email_in=input('Enter email id: ')
        pw_in=input('Enter password: ')
        for user in self.userlist:           
            dict=user.__dict__           
            if dict['email'] == email_in and dict['pw']==pw_in:
                print('\nWelcome user\n')
                print(user)
                del(user)
            else:
                print('Enter correct deatils')
                email_in=input('Enter email id: ')
                pw_in=input('Enter password: ')

        
        name=input('\nEnter updated fullname: ')

        phno_in=input('Enter updated 10 digit phone number: ')  
        def validate_phno_in(phno_in):
            pattern = re.compile(r'^\d{10}$')
            return bool(pattern.match(phno_in))
        if validate_phno_in(phno_in):
            phno=phno_in

        else:
            print(f"{phno_in} is an invalid phone number")
            phno_in=input('Enter correct phone number:')
            phno=phno_in
         
        email_in=input('Enter updated email id:')
        def validate_email_in(email_in):
            pattern = re.compile(r'\w+[@][a-z]+[.]com$')
            return bool(pattern.match(email_in))
        
        if validate_email_in(email_in):
            email=email_in  
                        
        else:
            print(f"{email_in} is an invalid email id")
            mail=input('Enter correct email id:') 
            email=mail      
        
        addr=input('Enter updated address: ')
        pw=input('Enter updated password: ')
        userobj=User(name,phno,email,addr,pw)
        self.userlist.append(userobj)
        print('Profile updated successfully')
        print(user)


    
        
    
    


       
