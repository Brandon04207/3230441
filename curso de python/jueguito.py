import random as r

dinero = int (input("ingrese una cantidad de dinero:_"))

n1= r.randint(0,4)
n2= r.randint(0,4)
n3= r.randint(0,4)

print ("los numeros son:_",n1,n2,n3)

if n1==n2 and n1==n3:
    print ( "usted gano", dinero * 3)
    
elif n1 == n2 or n1 == n3 or n2 == n3:
    print ( "usted gano", dinero * 1.5)

else:
    print ( "no gano nada")