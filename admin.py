class Admin:
    def __init__(self,FoodID,Name,Quantity,Price,Discount,Stock):
        self.FoodID=FoodID
        self.Name=Name
        self.Quantity=Quantity
        self.Price=Price
        self.Discount=Discount
        self.Stock=Stock

    def set_FoodID(self,FoodID):
        self.FoodID = FoodID

    def get_FoodID(self):
        return self.FoodID
    
    def set_Name(self,Name):
        self.Name = Name

    def get_Name(self):
        return self.Name
    
    def set_Quantity(self,Quantity):
        self.Quantity = Quantity

    def get_Quantity(self):
        return self.Quantity
    
    def set_Price(self,Price):
        self.Price = Price

    def get_Price(self):
        return self.Price
    
    def set_Discount(self,Discount):
        self.Discount = Discount

    def get_Discount(self):
        return self.Discount
    
    def set_Stock(self,Stock):
        self.Stock = Stock

    def get_Stock(self):
        return self.Stock
    
    def __str__(self):
        return f' FoodID:{self.FoodID} \n Name:{self.Name} \n Quantity:{self.Quantity} \n Price:{self.Price} \n Discount:{self.Discount} \n Stock: {self.Stock}  '
    
    