import ply.yacc as yacc

from main import tokens

def p_body(p):
    '''body : variable
            | while
            | expresionif
            | imprimir 
            |'''

def p_impirmir(p):
    '''imprimir : PRINT LPAR valor RPAR'''
    print(p[3])

def p_bodyblock(p):
    ''' bodyblock : bodyblock variable
                    |  bodyblock while
                    | expresionif
                    | '''
def p_varblock(p):
    '''varblock : varblock variable
                | '''
def p_variable(p):
    '''variable : AUTO IDENTIFICADOR IGUAL valor PUNTOCOMA
                | AUTO IDENTIFICADOR PUNTOCOMA'''

def p_variable_numero(p):
    '''variable : numerotipo IDENTIFICADOR IGUAL numero PUNTOCOMA
                | numerotipo IDENTIFICADOR PUNTOCOMA'''

def p_variable_char(p):
    '''variable : CHAR IDENTIFICADOR IGUAL CHARACTER PUNTOCOMA'''

def p_numero_tipo(p):
    '''numerotipo : INT
              | FLOAT
              | LONG'''

def p_numero(p):
    '''numero : ENTERO
              | FLOTANTE'''

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
            | FALSE
            | IDENTIFICADOR'''
    p[0] = p[1]


def p_while(p):
    '''while : WHILE LPAR statement RPAR LLAVEL bodyblock LLAVER'''


def p_expresion_comparacion(p):
    '''expresion : expresion comparador expresion'''



#Ricardo Villacis IF

def p_expresionif(p):
    '''expresionif : IF LPAR condicionif RPAR conllaves expresionpos
                    | IF LPAR condicionif RPAR sinllaves expresionpos
                    '''
def p_expresionpos(p):
    '''expresionpos : else
                    | elseif
                    | '''
def p_elseif(p):
    ''' elseif : ELSE IF LPAR condicionif RPAR conllaves else
                | ELSE IF LPAR condicionif RPAR sinllaves else
                | '''
def p_else(p):
    '''else : ELSE conllaves
            | ELSE sinllaves'''
def p_sinLlaves(p):
    '''sinllaves : while
                | variable'''
def p_conLlaves(p):
    '''conllaves : LLAVEL bodyblock LLAVER'''
def p_condicionif(p):
    '''condicionif : initcondicion
                | statement'''

def p_initcondicion(p):
    '''initcondicion : varblock statement'''
def p_statement(p):
    '''statement : expresion
                | EXCLAMACION boolean
                | EXCLAMACION LPAR expresion RPAR
                | EXCLAMACION IDENTIFICADOR'''
def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''

def p_expresion(p):
    '''expresion : valor'''

def p_comparacion(p):
    '''comparador : IGUAL IGUAL
                | MENOR
                | MAYOR
                | MENOR IGUAL
                | MAYOR IGUAL
                | EXCLAMACION IGUAL'''


#errors
def p_error(p):
    print('Syntax error')

parser = yacc.yacc()
test = '''
    while(1){
        auto var = "hola mundo";
        while(true != false){
            auto hola;
        }
    }
'''
parser.parse(test)
while True:
    try:
        s = input('C++ > ')
    except EOFError:
        break
    parser.parse(s)