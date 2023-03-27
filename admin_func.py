from admin import Admin

import random

class AdminFunctions:
    foodlist = []
    def addfood(self):
        # ID = int(random.randint(0,100))
        # FoodID=print(f'Food ID : {ID}')
    
        FoodID=int(input('Enter ID: '))
        # ID=int(random.randin
        # t(0,100))
        # FoodID=print(f'Food ID : {ID}')
        Name = input('Enter name of the dish: ')
        Quantity = input('Enter the quantity of Dish: ')
        Price = float(input('Enter the price of the dish: '))
        Discount = input('Enter discount for the dish:  ')
        Stock = input('Enter the amount of food left in stock: ')
        food_obj=Admin(FoodID,Name,Quantity,Price,Discount,Stock)
        self.foodlist.append(food_obj) 
        print("Food item Successfully Added!")
    
    def editfood(self):
        food_ID= int(input('Enter the food ID to edit: '))
        for food in self.foodlist:
            if food_ID == food.get_FoodID():
                print(food,'\n')
                # Edit_opt=int(input('Enter \n1.Edit name \n2.Edit quantity \n3.Edit price \n4.Edit discount \n5.Stock \n:'))
                # def addfood(self): 
                # ID = random.randint(0,100)
                # FoodID=print(f'Food ID : {ID}')
                
                self.foodlist.remove(food)
                
                FoodID=food_ID
                # ID=int(random.randin
                # t(0,100))
                # FoodID=print(f'Food ID : {ID}')
                Name = input('Enter edited name of the dish: ')
                Quantity = input('Enter edited quantity of Dish: ')
                Price = float(input('Enter edited price of the dish: '))
                Discount = input('Enter edited discount for the dish:  ')
                Stock = input('Enter edited amount of food left in stock: ')
                food_obj=Admin(FoodID,Name,Quantity,Price,Discount,Stock)
                # food_obj.Name=eName
                # food_obj.Quantity=eQuantity
                # food_obj.Price=ePrice
                # food_obj.Discount=eDiscount
                # food_obj.eStock=eStock
                self.foodlist.append(food_obj) 
                print("Food item edited Successfully!")
                break

    def deletefood(self):
        
        food_ID = int(input('Enter the food ID to delete: '))
        for food in self.foodlist:
            if food_ID == food.get_FoodID():
                    self.foodlist.remove(food)
                
                
                 
                    

                


                

    def viewfood(self):
        for i in self.foodlist:
            print(i)
    
    


                


