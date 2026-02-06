"""
nombre = str (input( "ingrese sus nombres:_ " ))
apellido = str (input( "ingrese sus apellidos:_" ))
id =  int (input( "ingrese su identificacion:_" ))
edad =  int (input( "ingrese su edad:_" ))
estatura = float (input( "ingrese su estatura:_ " ))
email = str (input( "ingrese su email:_ " ))

print ("su nombre es:_",nombre,"\n","su apelldio es:_",apellido,"su id es:_",id,"\n",
       "su edad es:_",edad,"\n","su estatura:_",estatura,"\n","su email:_",email)
"""
"""
import random as r
numeroAleatorio = r.randint(0,10)
print(numeroAleatorio)

numero=int(input("adivina el numero:_"))

if numeroAleatorio == numero: 
    print("adivinaste")
elif numeroAleatorio != numero:
    # el != es para decir que no es igual
    print ("perdiste")
else:
    print ("no pusiste bien el numero, vuelve a intentarlo")
"""

print("SISTEMA DE CALIFICACIONES")
print("-" * 40)

while True:
    # 1. Registrar nombre
    nombre = input("\nNombre del estudiante (o 'salir'): ")
    
    # 5. Salir del programa
    if nombre.lower() == "salir":
        print("¡Hasta luego!")
        break
    
    # 2. Solicitar calificaciones
    seguimiento = float(input("Seguimiento (70%): "))
    evaluacion = float(input("Evaluación Final (20%): "))
    autoevaluacion = float(input("Autoevaluación (10%): "))
    
    # 3. Calcular promedio
    promedio = (seguimiento * 0.70) + (evaluacion * 0.20) + (autoevaluacion * 0.10)
    
    print(f"\nPromedio de {nombre}: {promedio:.2f}")
    
    # 4. Evaluar desempeño
    if promedio < 3.0:
        print(f"❌ {nombre}, debes mejorar tu rendimiento.")
    elif promedio < 4.0:
        print(f"✅ {nombre}, buen trabajo, puedes superarte aún más.")
    else:
        print(f"🌟 Excelente, {nombre}, mantén tu esfuerzo.")
    
    # 6. Comparar con media institucional
    if round(promedio) >= 3.5:
        print("Supera la media institucional (3.5)")
    else:
        print("No supera la media institucional (3.5)")


 

