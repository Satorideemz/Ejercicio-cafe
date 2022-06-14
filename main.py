from logging import raiseExceptions

class Ingredient:
    count=0
    def __init__(self,elemento,cantidad,id=None,stock=None):
        self.elemento=elemento
        self.cantidad=cantidad
        Ingredient.count+=1
        self.id=Ingredient.count
        self.stock=stock
    def set_stock(self,s):
        self.stock=s    
    def use_ingredients(self):
        self.stock.disadd_stock(self)
        
    
class Stock:
    def __init__(self,stock,id=None):
        self.stock=stock
        self.id=id
    def add_stock(self,i):
        self.id=i.id
    def disadd_stock(self,i):
        if i.cantidad>self.stock:
            raise Exception("No hay suficiente stock, tiene "+str(self.stock)+" pero se requiere "+str(i.cantidad))
        self.stock=self.stock-i.cantidad

class Cafecito:
    def __init__(self,nombre,coins,ingredientes=None):
        self.nombre=nombre
        self.coins=coins
        self.ingredientes=[]
    def add_ingredients(self,a):
        self.ingredientes.append(a)
    def add_ingredients_list(self,a):
        for i in range (len(a)):
            self.ingredientes.append(a[i])        
    def show_ingredients(self):
        for i in range (len(self.ingredientes)):
            print(self.ingredientes[i].cantidad)

#entra un pedido, resta los ingredientes
    def serve_coffee(self):
        for i in range (len(self.ingredientes)):
            self.ingredientes[i].use_ingredients()


class Client:
    def __init__(self,coins,requests=None):
        self.coins=coins
        self.requests=[]
    def add_requests(self,r):
        if self.coins<r.coins:
            raise Exception("No hay suficientes monedas, tiene "+str(self.coins)+" pero se requieren "+str(r.coins))
        self.requests.append(r)
        self.coins-=r.coins
    def show_requests(self):
        for i in range (len(self.requests)):
            print(self.requests[i].nombre)            
    def insert_coins(self,c):
        self.coins=c+self.coins

