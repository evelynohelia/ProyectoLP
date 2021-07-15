from tkinter import Entry, Tk,Text,Button,END,re
from sintactico import *
import sys


def sintactico(ingreso):
        return parsing(ingreso)

def lexico(ingreso):
        return inputLex(ingreso)


class Interfaz:
    def __init__(self, ventana):
        #titulo de la ventana 
        self.ventana=ventana
        self.ventana.title("C++ Analyzer")
        self.ventana.geometry("700x400")
        self.ventana['bg'] = '#49A'


        #Pantalla de entrada
        self.pantalla=Text(ventana, width=60, height=8, background="white", foreground="black", font=("Helvetica",12))

        #setea la pantalla en la ventana
        self.pantalla.grid(row=0, column=1, rowspan=3, columnspan=3,  padx=5, pady=5)
        
        botonLexico = Button(ventana, text='Léxico', width=9, height=1, font=("Helvetica",15), command = self.analizarLexico)      
        botonSemantico = Button(ventana, text='Semántica', width=9, height=1, font=("Helvetica",15), command = self.analizarSemantico)
        botonSintaxis = Button(ventana, text='Sintaxis', width=9, height=1, font=("Helvetica",15) , command = self.analizarSintaxis)

        botones=[botonLexico, botonSintaxis, botonSemantico]
        contador=0

        for fila in range(0,3):
            for columna in range(0,1):
                botones[contador].grid(row=fila,column=columna)
                contador+=1

        self.consola=Text(ventana, state="disabled", width=75, height=12, background="black", foreground="white", font=("Helvetica",12))
        self.consola.grid(row=3, column=0, rowspan=3, columnspan=3,  padx=5, pady=5)

        
        return

    def analizarLexico(self, escribir=True):
        self.limpiarPantalla()
        inp = self.pantalla.get(1.0, "end-1c")
        tokenlexico = lexico(inp)
        for i in tokenlexico:
            self.mostrarEnPantalla(i)
            self.mostrarEnPantalla('\n')

    def analizarSintaxis(self, escribir=True):
        self.limpiarPantalla()
        inp = self.pantalla.get(1.0, "end-1c")
        tokensintaxis = sintactico(inp)
        self.mostrarEnPantalla(tokensintaxis)   


    def analizarSemantico(self, escribir=True):
        self.limpiarPantalla()
        inp = self.pantalla.get(1.0, "end-1c")
        tokensintaxis = sintactico(inp)
        self.mostrarEnPantalla(tokensintaxis)    

    def limpiarPantalla(self):
        self.consola.configure(state="normal")
        self.consola.delete("1.0", END)
        self.consola.configure(state="disabled")
        return
    

    def mostrarEnPantalla(self, valor):
        self.consola.configure(state="normal")
        self.consola.insert(END, valor)
        self.consola.configure(state="disabled")
        return


ventana_principal=Tk()
analyzer=Interfaz(ventana_principal)
ventana_principal.mainloop()