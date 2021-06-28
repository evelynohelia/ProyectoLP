import ply.yacc as yacc

from main import tokens

def p_body(p):
    '''body : variable'''

def p_variable(p):
    '''variable : tipo IDENTIFICADOR IGUAL valor PUNTOCOMA'''

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
            | STRING'''


def p_error(p):
    print('Syntax error')

parser = yacc.yacc()

while True:
    try:
        s = input('C++ > ')
    except EOFError:
        break
    parser.parse(s)