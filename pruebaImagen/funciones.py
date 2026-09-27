name = input("Enter your name: ")
#aixo es una funcio que no retorna res

def print_hi(name):
    print("Hi, " + name + "!")

print_hi(name)


#aquesta funcio retorna un valor
def suma(a, b):
    return a + b

#inicia el programa
if __name__ == '__main__':
    print_hi(name)
    result = suma(5, 3)
    print("The sum of 5 and 3 is: " + str(result))
    print(suma(10, 20))

    