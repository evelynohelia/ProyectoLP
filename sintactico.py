import ply.yacc as yacc

from main import tokens

def p_body(p):
    '''body : variable
            | while
            | expresionif
            | claseimplementacion
            | funcionclaseimpl
            | creacionobjeto
            | asignarvalorobjeto
            | usarfuncionobjeto
            |'''
def p_bodyblock(p):
    ''' bodyblock : bodyblock variable
                    |  bodyblock while
                    | bodyblock expresionif
                    | '''
def p_funcionblock(p):
    ''' funcionblock : bodyblock variable
                    |  bodyblock while
                    | bodyblock expresionif
                    | RETURN statement
                    | '''

def p_varblock(p):
    '''varblock : varblock variable
                | '''
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
            | FALSE
            | IDENTIFICADOR'''


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


#Ricardo Villacis Clase
def p_claseimplementacion(p):
    ''' claseimplementacion : CLASS IDENTIFICADOR LLAVEL bloqueclase LLAVER'''
def p_bloqueclase(p):
    ''' bloqueclase : bloqueclase definicion
                    |  bloqueclase funcionclaseimpl
                    | '''
def p_definicion(p):
    '''definicion : tipo IDENTIFICADOR PUNTOCOMA
                    | '''
def p_funcionclaseimpl(p):
    ''' funcionclaseimpl : tipo IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL funcionblock LLAVER
                        | VOID IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL bodyblock LLAVER
                        |'''
def p_parametrosimplementacion(p):
    '''parametrosimplementacion :  tipo IDENTIFICADOR masparametrosimplementacion
                                | '''
def p_parametrosfuncion(p):
    ''' parametrosfuncion : IDENTIFICADOR masparametrosfuncion
                            | '''
def p_masparametrosimplementacion(p):
    '''masparametrosimplementacion :  COMMA parametrosimplementacion
                                    | '''
def p_masparametrosfuncion(p):
    ''' masparametrosfuncion : COMMA parametrosfuncion
                            | '''
def p_creacionobjeto(p):
    ''' creacionobjeto : IDENTIFICADOR IDENTIFICADOR PUNTOCOMA'''
def p_asignarvalores(p):
    ''' asignarvalorobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR IGUAL valor
                            | LPAR expresion RPAR
                            | LPAR statement RPAR
                            | EXCLAMACION  LPAR statement RPAR'''
def p_usarfuncionesobjeto(p):
    ''' usarfuncionobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR LPAR parametrosfuncion RPAR PUNTOCOMA '''
#errors
def p_error(p):
    print('Syntax error')

parser = yacc.yacc()
test= ''' hola.ric();'''
parser.parse(test)

while True:
    try:
        s = input('C++ > ')
    except EOFError:
        break
    parser.parse(s)