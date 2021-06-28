import ply.yacc as yacc

from main import tokens

def p_body(p):
    '''body : variable
            | while
            |'''

def p_variable(p):
    '''variable : tipo IDENTIFICADOR IGUAL valor PUNTOCOMA
                | tipo IDENTIFICADOR PUNTOCOMA'''

def p_tipo(p):
    '''tipo : INT 
            | FLOAT
            | LONG
            | AUTO
            | CHAR
            | VOID'''

def p_valor(p):
    '''valor : ENTERO 
            | FLOTANTE
            | CHARACTER
            | STRING
            | TRUE
            | FALSE'''


def p_while(p):
    '''while : WHILE LPAR expresion RPAR LLAVEL body LLAVER'''


def p_expresion_comparacion(p):
    '''expresion : expresion MAYOR expresion                
                | expresion MAYOR IGUAL expresion
                | expresion MENOR expresion
                | expresion MENOR IGUAL expresion
                | expresion IGUAL IGUAL expresion
                | expresion EXCLAMACION IGUAL expresion'''

def p_expresion(p):
    '''expresion : valor'''


#errors
def p_error(p):
    print('Syntax error')

parser = yacc.yacc()

while True:
    try:
        s = input('C++ > ')
    except EOFError:
        break
    parser.parse(s)