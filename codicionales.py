#Declaramos una varaible
from pyparsing import And


calificacion = input ("Introduce tu calificacion de la AZ -900?")

calificacion = int(calificacion)
#Preguntamos si la calificacion es menor a 700
if calificacion < 700 :  
    print("Vees por no estudiar")
elif calificacion == 700 :
    print("PANZAZO")
elif calificacion > 1000 :
    print("Minetes")
else: #Si no se cumple el if anterior, pasa a else
    print("Felicidades")

#Verificado de mayoria de edad 
edad = input("INTRODUCE TU EDAD")
edad = int(edad)

if edad >= 18 and edad <=100:
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abues te fio")
elif edad < 0 : 
    print("Ni que viajaras en el tiempo")
else:
    print("No puedes llevarte esos cigarros")

#En Python no existe Switch Case
