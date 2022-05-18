# Nombre: Jhostyn Javier Gavilanez Suarez
# Fecha: 17/05/2022

# Tema: Ejercicios en Python, resolucion de 5 problemas propuesto en el pdf:  https://drive.google.com/file/d/18UNwvd5maRooL812SWhIWjCIX15i-OwA/view
# Resolucion del ejercicio 2
print("************   Bienvenidos al Ejercicio 2  ********** ")
print("Tema: Ingresar un valor en libras y transformarlo a kilos y gramos ")
# Datos para la transformacion de libras a kilos y gramos
valorMasaKilos = 2.2046  # Numero de transformacion de kilos
valorMasaGramos = 453.592  # Numero de tranformacion de gramos

# Datos de ingreso de usuario
numLibras = float(input("Ingrese un valor en libras ->> "))
print()  # para dejar un espacio en blanco
# formula de la transformacion de libras a kilos
transformacionLibrasKilos = numLibras/valorMasaKilos
# formula de la transformacion de libras a gramos
transformacionLibrasGramos = numLibras * valorMasaGramos
print("\n La transformación obtenida de las " +
      str(numLibras)+" libras, son las siguientes: \n ")
print("Transformacion de libras a Kilos ->> ",
      transformacionLibrasKilos)  # resultados de libras a kilos
print("Transformacion de libras a Gramos ->> ",
      transformacionLibrasGramos)  # resultado de libras a gramos

