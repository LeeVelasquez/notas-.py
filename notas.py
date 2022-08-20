# Add to this file for the sample app lab
n1 = float(input('ingrese la primera nota: '))
n2 = float(input('ingrese la segunda nota: '))
n3 = float(input('ingrese la tercera nota: '))
n4 = float(input('ingrese la cuarta nota: '))
nombre = input(' ingrese nombre ')
codigo = input(' ingrese codigo ')

numero1 = n1*0.15
numero2 = n2*0.2
numero3 = n3*0.25
numero4 = n4*0.4

promedio = numero1+numero2+numero3+numero4



if (promedio>=17):
    print(promedio)
    print("El alunmo "+ nombre +" con el codigo "+ codigo +" su estado es muy bien")
elif(promedio>=14 and promedio<17):
     print(promedio)
     print(" El alunmo "+ nombre +" con el codigo "+ codigo +" su estado es regular sigue estudiando  ")
else:
    print(promedio)
    print(" El alunmo "+ nombre +" con el codigo "+ codigo +" su estado es malo  ")
