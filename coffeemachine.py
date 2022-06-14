
from main import Cafecito
from main import Ingredient
from main import Stock
from main import Client

#cargo los ingredientes iniciales que tendra
i1= Ingredient("Coffee",50,1,Stock(1000,1))
i2= Ingredient("Double coffee",100,2,Stock(1000,2))
i3= Ingredient("Sugar",10,3,Stock(1000,3))
i4=Ingredient("Milk",50,4,Stock(1000,4))
i5=Ingredient("Chocolate",25,5,Stock(1000,5))
i6=Ingredient("Tea",40,6,Stock(1000,6))
i7=Ingredient("Water",200,7,Stock(1000,7))

#cargo los tipos de cafe iniciales
c1=Cafecito("Coffee solo",2)
c1.add_ingredients_list([i1,i3,i7])

c2=Cafecito("Double coffee",2)
c2.add_ingredients_list([i2,i3,i7])

c3=Cafecito("Coffee with milk",2)
c3.add_ingredients_list([i1,i3,i4,i7])

c4=Cafecito("Double coffee with milk",3)
c4.add_ingredients_list([i2,i3,i4,i7])

c5=Cafecito("Coffee with chocolate",2)
c5.add_ingredients_list([i1,i3,i5,i7])

c6=Cafecito("Capuchino",3)
c6.add_ingredients_list([i1,i3,i4,i4,i7])

c7=Cafecito("Tea",1)
c7.add_ingredients_list([i6,i7])

#main
def pedir_cafe():
    l1=[]
    print("Lista de cafes disponibles:")
    for i in range (7):
        l1.append(eval("c"+str(i+1)))
        print(l1[i].nombre)
    b=str(input("Ingrese el cafe que va a querer:"))
    c=int(input("Si desea mas de uno, escriba la cantidad que desea, de lo contrario escriba uno:"))
    while c>=1:
        for i in range(len(l1)):
            if b==l1[i].nombre:
                print("Cafe: "+l1[i].nombre+" seleccionado")
                cl1.add_requests(l1[i])
                l1[i].serve_coffee()
                print("Cafe hecho exitosamente")
                c=c-1
    d=str(input("Desea otro cafe?(y/n)"))
    if d=="y":
        pedir_cafe()    
a=0
while a<1:
    a = int(input("Ingrese las monedas:"))
cl1=Client(a)
pedir_cafe()


