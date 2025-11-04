#import random,
#alias = as 
import random as r
#el alias de random es r

numero= r.randint (0,100)


if numero > 0:
    if numero %2== 0:
        print (numero)
        numero += 10
        print (f"el {numero} es positivo par mas diez")
    else: 
        print(f"el {numero} no es par")
else:
    numero *= -1
print ("el numero es ahora:",numero )

