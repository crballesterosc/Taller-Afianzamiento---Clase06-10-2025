
print("\n")
print("Bienvenido amis ejercicios - Autor: Cristian Ballesteros")
a = 1
while(a <= 10):
    a += 1
    print("\n")
    opcion = int(input("Digite el numero del problema que desea revisar: "))


    def Problema1():
        print(f"Problema {opcion}")
        num1 = int(input("Ingrese un numero: "))
        if (num1 < 0):
            print(f"El numero ingresado es {num1} es invalido, por favor ingrese un numero entero positivo")
        else:
            numt = num1**2
            print(f"El cuadrado del numero {num1} es: {numt}")


    def Problema2():
        print(f"Problema {opcion}")
        num = int(input("Ingrese un numero: "))
        while(num != 1):
            if(num % 2 == 0):
                num = int(num/2)
            elif(num % 2 == 1):
                num = int((3*num)+1) 
            print(num, end= " ")


    def Problema3():
        print(f"Problema {opcion}")
        poblA = 25 
        poblB = 18.9 
        crecA = 0.02
        crecB = 0.03 
        año = 2022 

        while (poblB <= poblA):
            poblA += (poblA*crecA) 
            poblB += (poblB*crecB) 
            año += 1

        print(f"En el año {año}, la poblacion B superara la poblacion A")


    def Problema4():
        print(f"Problema {opcion}")
        print("Listado de numeros del 1 al 100 con su cuadrado")
        for a in range(1, 101):
            b = a**2
            print(f"El cuadrado del {a} es: {b}")


    def Problema5():
        print(f"Problema {opcion}")
        print("Listado de numeros impares del 1 al 999")
        for i in range (1,1000):
            if(i % 2 != 0):
                print(i)

        print("Listado de numeros pares del 1 al 1000")
        for i in range (1,1001):
            if(i % 2 == 0):
                print(i)


    def Problema6():
        print(f"Problema {opcion}")
        val1 = int(input("Ingrese un numero desde donde empiece el listado: "))
        
        for i in range(val1, 0, -1): 
            if(i % 2 == 0):
                print(i, end=" ")


    def Problema7():
        print(f"Problema {opcion}")
        print()
            

    def Problema8():
        print(f"Problema {opcion}")
        num = int(input("Ingrese el numero que desea que 2 sea elevado: "))
        numf = (2**num)
        print(f"2 elevado a la {num} es igual a: {numf}")


    def Problema9():
        print(f"Problema {opcion}")
        numn = int(input("Digite un numero natural: "))
        numR = int(input("Digite un numero real: "))

        numF = numR**numn

        print(f"{numR} elevado a la {numn} es igual a: {numF}")


    def Problema10():
        print(f"Problema {opcion}")
        for a in range(1, 10):  
            print(f"Tabla de multiplicar del {a}")
            for b in range(1, 11):  
                print(f"{a} x {b} = {a * b}")
        print()  



    if(opcion == 1):
        Problema1()
    elif(opcion == 2):
        Problema2()
    elif(opcion == 3):
        Problema3()
    elif(opcion == 4):
        Problema4()
    elif(opcion == 5):
        Problema5()
    elif(opcion == 6):
        Problema6()
    elif(opcion == 7):
        Problema7()
    elif(opcion == 8):
        Problema8()
    elif(opcion == 9):
        Problema9()
    elif(opcion == 10):
        Problema10()
    else:
        print("Opcion no valida")









