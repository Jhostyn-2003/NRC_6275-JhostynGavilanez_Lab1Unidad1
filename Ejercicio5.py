# Nombre: Jhostyn Javier Gavilanez Suarez
# Fecha: 17/05/2022

# Tema: Ejercicios en Python, resolucion de 5 problemas propuesto en el pdf:  https://drive.google.com/file/d/18UNwvd5maRooL812SWhIWjCIX15i-OwA/view

piNumero = 3.1415   # Variable  numero Pi

print("************   Bienvenidos al Ejercicio 5 ********** ")
print("Tema: Volumen de la esfera \n")

# el usuario debe ingresar datos
radioEsfera = int(input("Ingrese el radio de la esfera -->> "))
# formula del volumen de la esfera
volumenEsfera = (4*piNumero*(radioEsfera*radioEsfera*radioEsfera))/3
# Aqui presentamos en consola el resultado del volumen de la esfera
print("El Volumen de la esfera con radio " +
      str(radioEsfera)+", es igual a -->> ", volumenEsfera)
