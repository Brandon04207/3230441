"""
naranja= int(input("cuantos kilos de naranja hay:_"))
mango= int(input("cuantos kilos de mango hay:_"))

kiloNaranja=naranja*3000
kilomango=mango*1300


if (naranja ==50 and mango==50):
    {
        print ("las naranjas valen:_",kiloNaranja*0.05,),
        print ("las los mangos valen:_",kilomango*0.04,),
        print("el total a pagar es:_",(kiloNaranja*0.05)+(kilomango*0.04))
    }
elif (naranja==50 and mango==100):
    {
        print ("las naranjas valen:_",kiloNaranja*0.05,),
        print ("las los mangos valen:_",kilomango*0.06,),
        print("el total a pagar es:_",(kiloNaranja*0.05)+(kilomango*0.06))
    }
else:
    {
      print("naranja es",kiloNaranja),
      print("mango es",kilomango),  
      print("el total a pagar es:_",kiloNaranja+kilomango)  
    }
    """
    #----------------------------------------------------------------
dineroApuesta= int(input("cuanto dinero quieres apostar:_"))        
import random as r
n1 = r.randint(0,4)
n2 = r.randint(0,4)
n3 = r.randint(0,4)

print(n1)
print(n2)
print(n3)
if n1==n2 and n1==n3 :
    {
        print("ganaste:_",(dineroApuesta*3))
    }
elif n1 == n2 or n1 == n3 or n2 == n3:
    {
        print("ganaste:_",(dineroApuesta*1.5))
    }
else:
    {
        print("no gano nada")
    }