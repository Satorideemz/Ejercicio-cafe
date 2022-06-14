from hashlib import shake_128
import unittest
from parameterized import parameterized
from main import Cafecito
from main import Ingredient
from main import Stock
from main import Client


class TestApp(unittest.TestCase):

    @parameterized.expand([
        ('Coffee','50',{'elemento': 'Coffee', 'cantidad': '50', 'id': 6, 'stock': None}),
        ('Milk','60',{'elemento': 'Milk', 'cantidad': '60', 'id': 7, 'stock': None})
    ])
    def test_atributos_ingredient(self,elemento,cantidad, atributos):
        object = Ingredient(elemento, cantidad)
        self.assertDictEqual(object.__dict__, atributos)

    @parameterized.expand([
        ('Coffee solo','2',{'nombre': 'Coffee solo', 'coins': '2', 'ingredientes': []}),
        ('Coffee with milk','3',{'nombre': 'Coffee with milk', 'coins': '3', 'ingredientes': []})

    ])

    def test_atributos_cafecito(self,nombre,coins,atributos):
        object = Cafecito(nombre,coins)
        self.assertDictEqual(object.__dict__, atributos)

    @parameterized.expand([
        ('Sugar','25',{'elemento': 'Sugar', 'cantidad': '25', 'id': 4, 'stock': None})   
    ])

    def test_add_stock(self,elemento,cantidad,atributos):
        object = Ingredient(elemento, cantidad)
        s1=Stock(300)
        s1.add_stock(object)
        self.assertDictEqual(s1.__dict__,{'stock': 300,'id':5})
    def test_set_stock(self):
        s1=Stock(200)
        i1=Ingredient("Chocolate",20)
        i1.set_stock(s1)
        self.assertDictEqual(i1.__dict__,{'elemento': 'Chocolate', 'cantidad': 20, 'id': 14, 'stock': s1})
    def test_disadd_stock(self):
        s1=Stock(300,5)
        i1=Ingredient("Chocolate",30,5,s1)
        s1.disadd_stock(i1)
        self.assertDictEqual(s1.__dict__,{'stock': 270,'id':5})
    def test_disadd_stock_fail(self):
        s1=Stock(40,6)
        i1=Ingredient("Chocolate",50,6,s1)
        with self.assertRaises(Exception):
            s1.disadd_stock(i1) 
        self.assertDictEqual(s1.__dict__,{'stock': 40,'id':6})
    def test_add_ingredients(self):
        c1=Cafecito("Capuchino",4)
        i1=Ingredient("Sugar",30)
        i2=Ingredient("Milk",100)
        i3=Ingredient("Coffee",60)
        i4=Ingredient("Water",160)
        c1.add_ingredients(i1)
        c1.add_ingredients(i2)
        c1.add_ingredients(i3)
        c1.add_ingredients(i4)
        self.assertDictEqual(c1.__dict__,{'nombre':'Capuchino','coins':4,'ingredientes':[i1,i2,i3,i4]})
    def test_insert_coin(self):
        cl1=Client(0)
        cl1.insert_coins(10)
        self.assertDictEqual(cl1.__dict__,{'coins':10,'requests': []})
    def test_add_request(self):
        c1=Cafecito("Capuchino",2)
        c2=Cafecito("Late",3)
        cl1=Client(5)
        cl1.add_requests(c1)
        cl1.add_requests(c2)
        self.assertDictEqual(cl1.__dict__,{'coins':0,'requests': [c1,c2]})    
    def test_serve_coffee(self):
        s1=Stock(300,1)
        s2=Stock(300,2)
        s3=Stock(300,3)
        s4=Stock(300,4)
        i1=Ingredient("Sugar",30,1,s1)
        i2=Ingredient("Milk",100,2,s2)
        i3=Ingredient("Coffee",60,3,s3)
        i4=Ingredient("Water",160,4,s4)
        c1=Cafecito("Capuchino",4)
        c1.add_ingredients(i1)
        c1.add_ingredients(i2)
        c1.add_ingredients(i3)
        c1.add_ingredients(i4)
        c1.serve_coffee()
        self.assertDictEqual(s1.__dict__,{'stock': 270,'id':1})
        self.assertDictEqual(s2.__dict__,{'stock': 200,'id':2})
        self.assertDictEqual(s3.__dict__,{'stock': 240,'id':3})
        self.assertDictEqual(s4.__dict__,{'stock': 140,'id':4})

if __name__ == '__main__':
    unittest.main()