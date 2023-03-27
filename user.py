class User:
    def __init__(self,name,phno,email,addr,pw):
        self.name=name
        self.phno=phno
        self.email=email
        self.addr=addr
        self.pw=pw

    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    
    def set_phno(self,phno):
        self.phno=phno
    def get_phno(self):
        return self.phno
    
    def set_email(self,email):
        self.email=email
    def get_email(self):
        return self.email
    
    def set_addr(self,addr):
        self.addr=addr
    def get_addr(self):
        return self.addr
    
    def set_pw(self,pw):
        self.pw=pw
    def get_pw(self):
        return self.pw
    
    def __str__(self):
        return f' Name:{self.name} \n Phone number:{self.phno} \n Email_id:{self.email} \n Address:{self.addr} \n Password:{self.pw} '
    