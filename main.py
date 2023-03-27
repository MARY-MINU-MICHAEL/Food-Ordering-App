from admin_func import AdminFunctions
from user_func import *

class Main:
     def login(self,admin_or_user):
        if admin_or_user=='a':
            print('\nWelcome admin\n')
        if admin_or_user=='u':
            print('\nWelcome\n')

class admin(Main):
    def admin_execution(self,choice):
            if choice==1:
                print('.....Add food item......')
                admin_function.addfood()
            if choice==2:
                print('.....Edit food details......')
                admin_function.editfood()

            if choice==3:
                print('.....view food item......')
                admin_function.viewfood()
            if choice==4:
                print('.....Delete food item......')
                admin_function.deletefood()


class user(Main):
    def user_entry(self,reg_or_login):
        if reg_or_login=='r':
            print('\nEnter following details to register\n')
            user_function.reg()
        if reg_or_login=='l':
            print('\nWelcome user')
            user_function.login()

class user_act(user):
    def user_execution(self,user_choice):
        if user_choice==1:
          login_user_function.new_order()
        if user_choice==2:
          login_user_function.ord_his()
        if user_choice==3:
          login_user_function.update_prof()

admin_function = AdminFunctions()
user_function = Userfunctions()
login_user_function=Userfunctions()
main=Main()
log = input('Enter a if you are admin \nEnter u if you are user \n:')
main.login(log)

admin_login=admin()
user_login=user()
while log=='a' or log=='u':
    if log =='a':
        admin_choice= int(input('Enter \n1.Add food \n2.Edit food details \n3.View food details \n4.Delete food details \n:'))
        admin_login.admin_execution(admin_choice)
    if log =='u':
        user_choice=input('Enter \nr to register \nl to login \n:')
        user_login.user_entry(user_choice)
        loged_in_user=user_act()
        while user_choice=='l':      
            login_choice=int(input('Enter \n1 -To place new order \n2- To view order history \n3- To update profile \n: '))           
            loged_in_user.user_execution(login_choice)



