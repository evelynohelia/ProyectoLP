from sintactico import *

def sintactico():
    ingreso = ""
    while ingreso != "exit":
        ingreso = input("C++ > ")
        parsing(ingreso)

def lexico():
    ingreso = ""
    while ingreso != "exit":
        ingreso = input("Tokens > ")
        inputLex(ingreso)


opcion  = ""

while opcion != "3":
    print('''Bienvenido a C++
1.- Sintactico & Semantico
2.- Lexico
3.- Salir
    ''')
    opcion = input("Ingresar opcion: ")
    if opcion == "1":
        sintactico()
    elif opcion =="2":
        lexico()
