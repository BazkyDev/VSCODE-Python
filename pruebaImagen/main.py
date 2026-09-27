print("Hello, World!")

#CON # SE COMENTA

'''
ASI PUEDES HACER UN COMENTARIO MULTILINEA
DERER

'''


nom = "john"
print(nom+" is learning Python.")

#PONEMOS INPUT PARA QUE EL USUARIO PUEDA INTRODUCIR SU NOMBRE
nom = input("Enter your name: ")
print("Hello, " + nom + "! Welcome to Python programming.")


#PONEMOS INT PARA QUE EL INPUT SEA UN NUMERO ENTERO
edat = int(input("Enter your age: "))
print("You are " + str(edat) + " years old.")
if edat >= 18:
    print("You are an adult.")

#ponemos FLOAT PARA QUE EL INPUT SEA UN NUMERO DECIMAL
medida = float(input("Enter your height in meters: "))
print("Your height is " + str(medida) + " meters.")

#crear lista
llista =[1,2,3,4,5]
#acceder a un elemento de la lista
print("The first element of the list is: " + str(llista[0]))
#modificar un elemento de la lista
llista[0] = 10
#afegir un elemento a la lista
llista.append(6)
#insertar un elemento en una posición específica
llista.insert(2, 15)
#eliminar un elemento de la lista
llista.remove(4)
#eliminar un elemento de la lista por valor

#existe un elemento en la lista
if 3 in llista:
    print("3 is in the list.")

#ordenado la lista
llista.sort()

#recorrer la lista con un bucle for
for element in llista:
    print(element)

#para saber cual es el ultimo elemento de la lista
print("The last element of the list is: " + str(llista[-1]))

#per esborrar per element de la llista per index
del llista[1]

#con remove puedes eliminar un elemento por valor 
llista.remove(15)
print("The list after removing 15 is: " + str(llista))

#insertar un elemento en una posición específica
llista.insert(1, "jordi")
print("The list after inserting 'jordi' at index 1 is: " + str(llista))

#para saber el tipo de dato de una variable
print("The type of the variable 'llista' is: " + str(type(llista)))


#condicionales
if edat < 18:
    print("You are a minor.")
elif edat >= 18 and edat < 65:
    print("You are an adult.")


#bucle for
for i in range(1, 11): #iterate from 1 to 10
    print(i)

#bucle for para printar los elementos de la lista
for i in range(0, len(llista)): #iterate from 0 to 9
    print(llista[i])


#bucle while
i = 1
while i <= 10:
    print(i)
    i += 1


#funciones
def saludar(name):    
    print("Hello, " + name + "!")

saludar("Alice")
saludar("Bob")



#funciones con return
def sumar(a, b):
    return a + b 

#return quelcom
resultat = sumar(5, 3)
print("The sum of 5 and 3 is: " + str(resultat))


#retorna es impar
def es_impar(num):
    if num % 2 != 0:
        return True
    else:
        return False


print("Is 5 odd? " + str(es_impar(5)))
print("Is 6 odd? " + str(es_impar(6)))









