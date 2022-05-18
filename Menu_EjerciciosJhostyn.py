# Nombre: Jhostyn Javier Gavilanez Suarez
# Fecha: 17/05/2022

# Tema: Ejercicios en Python, resolucion de 5 problemas propuesto en el pdf:  https://drive.google.com/file/d/18UNwvd5maRooL812SWhIWjCIX15i-OwA/view

#En este caso, tambien he realizado un menu para nuestros ejercicios, en caso sea de utilizarse.

piNumero = 3.1415   # Variable global numero Pi

# Menu de Opciones acerca de los 5 ejercicios en python
while(True):
    print("*****************************************************")
    print("Bienvenidos al Menú de Ejercicio Python - Jhostyn Gavilánez")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Salir")
    print("*****************************************************")
    # Aqui se llama la opcion del menu
    opcionMenu = int(input("Elije una Opcion -> "))
    print("---------------------------------------------------")
    # Aqui se declara el If/else para verificar la opcion del menu

    if opcionMenu == 1:  # En este apartado va el ejercicio 1
        print("************   Bienvenidos al Ejercicio 1  ********** ")
        print("Tema: Ingresar el radio de un círculo del usuario y calcule el área ")
        print()
        # Ingreso de usuario un numero entero
        radioCirculo = int(input("Ingrese el radio del Circulo ->> "))
        # Formula del area del circulo
        areaCirculo = piNumero * (radioCirculo*radioCirculo)
        print()
        print("El área del Circulo con radio "+str(radioCirculo) +
              ", es igual a =>> ", areaCirculo)  # Resultado ejercicio 1
        print()

    elif opcionMenu == 2:  # En este apartado va el ejercicio 2
        print("************   Bienvenidos al Ejercicio 2  ********** ")
        print("Tema: Ingresar un valor en libras y transformarlo a kilos y gramos ")
        # Datos para la transformacion de libras a kilos y gramos
        valorMasaKilos= 2.2046 #Numero de transformacion de kilos
        valorMasaGramos= 453.592 #Numero de tranformacion de gramos 
        
        numLibras = float(input("Ingrese un valor en libras ->> "))# Datos de ingreso de usuario
        print() # para dejar un espacio en blanco 
        transformacionLibrasKilos = numLibras/valorMasaKilos # formula de la transformacion de libras a kilos
        transformacionLibrasGramos= numLibras * valorMasaGramos  # formula de la transformacion de libras a gramos
        print("\n La transformación obtenida de las "+str(numLibras)+" libras, son las siguientes: \n ")
        print("Transformacion de libras a Kilos ->> ", transformacionLibrasKilos) #resultados de libras a kilos
        print("Transformacion de libras a Gramos ->> ", transformacionLibrasGramos) #resultado de libras a gramos
        print()
        
    elif opcionMenu == 3: # En este apartado va el ejercicio 3
        print("************   Bienvenidos al Ejercicio 3  ********** ")
        print("Tema: Preguntar al usuario su nombre y lo salude con su nombre \n")
        
        nombreUsuario= input("\n ¿ Cómo se llama Estimad@ ? ->>") # Preguntamos al usuario su nombre mediante input
        print("\n ¡Hola "+nombreUsuario+", me alegro de conocerte ! ") # Respuesta: Saludamos al Usuario 

    elif opcionMenu == 4: # En este apartado va el ejercicio 4
        print("************   Bienvenidos al Ejercicio 4  ********** ")
        print("Tema: Ingresar dos números y realizar todas las operaciones aritméticas \n")

        # Ejercicio 4: Ingresar dos numeros y realizar todas las operaciones aritmeticas.
        num1Ejercicio4 = int(input("Ingrese el numero 1 ->> ")) # Ingreso del numero 1
        num2Ejercicio4 = int(input("Ingrese el numero 2 ->> ")) # Ingreso del numero 2
        #num1 = 10; num2 = 5 - pruebas 
        print(" ***********  Operadores aritméticos - Resolución ********** ")
        print("La suma del numero " +str(num1Ejercicio4)+" y el número "+str(num2Ejercicio4)+", es en total ->>" , num1Ejercicio4+num2Ejercicio4)  # 15
        print("La resta del numero " +str(num1Ejercicio4)+" y el número "+str(num2Ejercicio4)+", es en total ->>", num1Ejercicio4-num2Ejercicio4)  # 5
        print("La multiplicación del numero " +str(num1Ejercicio4)+" y el número "+str(num2Ejercicio4)+", es en total ->>", num1Ejercicio4*num2Ejercicio4)  # 50
        print("La división del numero " +str(num1Ejercicio4)+" y el número "+str(num2Ejercicio4)+", es en total ->>", num1Ejercicio4/num2Ejercicio4)  # 2.0
        print("El módulo del numero " +str(num1Ejercicio4)+" y el número "+str(num2Ejercicio4)+", es en total ->>", num1Ejercicio4 % num2Ejercicio4)  # 0
        print("El exponente del numero " +str(num1Ejercicio4)+" y el número "+str(num2Ejercicio4)+", es en total ->>", num1Ejercicio4**num2Ejercicio4)  # 100000
        print("El cociente del numero " +str(num1Ejercicio4)+" y el número "+str(num2Ejercicio4)+", es en total ->>", num1Ejercicio4//num2Ejercicio4)  # 2
        
    elif opcionMenu == 5: # En este apartado va el ejercicio 5
        print("************   Bienvenidos al Ejercicio 5 ********** ")
        print("Tema: Volumen de la esfera \n")

        radioEsfera= int(input("Ingrese el radio de la esfera -->> ")) # el usuario debe ingresar datos
        #formula del volumen de la esfera
        volumenEsfera= (4*piNumero*(radioEsfera*radioEsfera*radioEsfera))/3
        # Aqui presentamos en consola el resultado del volumen de la esfera 
        print("El Volumen de la esfera con radio "+str(radioEsfera)+", es igual a -->> ", volumenEsfera)

    elif opcionMenu == 6:
        print("Saliste de la Aplicación, chao !!!")
        break
    else:
        print("Error, ingresaste una opción no válida")
print("Gracias por visualizar nuestro menu de ejercicios Python ")


