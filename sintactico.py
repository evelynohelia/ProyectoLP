import ply.yacc as yacc

from lexico import tokens,lexer

def p_body(p):
    '''body :  bodyblock variable
            |  bodyblock while
            |  bodyblock expresionif
            | bodyblock claseimplementacion
            | bodyblock for
            | bodyblock funcionclaseimpl
            | bodyblock arraydeclaration
            | bodyblock creacionobjeto
            | bodyblock asignarvalorobjeto
            | bodyblock usarfuncionobjeto
            | bodyblock struct
            | bodyblock imprimir
            | bodyblock stringappend
            |'''

def p_id(p):
  '''id : IDENTIFICADOR 
  | IDENTIFICADOR CORCHETEL ENTERO CORCHETER'''

def p_tipo(p):
    '''tipo : INT 
            | FLOAT
            | LONG
            | AUTO
            | STRING
            | CHAR'''


def p_impirmir(p):
    '''imprimir : PRINT LPAR valor RPAR 
                | COUT MENOR MENOR valor
                | COUT MENOR MENOR variable'''
    if p[1] == "printf":
        print(p[3])
    else:
        print(p[4])
    

def p_bodyblock(p):
    ''' bodyblock : bodyblock variable
            |  bodyblock while
            |  bodyblock expresionif
            | bodyblock claseimplementacion
            | bodyblock for
            | bodyblock funcionclaseimpl
            | bodyblock arraydeclaration
            | bodyblock creacionobjeto
            | bodyblock asignarvalorobjeto
            | bodyblock usarfuncionobjeto
            | bodyblock struct
            | bodyblock imprimir
            | bodyblock stringappend
            |'''
def p_funcionblock(p):
    ''' funcionblock : bodyblock variable
                    |  bodyblock while
                    | bodyblock expresionif
                    | bodyblock for
                    | bodyblock imprimir
                    | RETURN statement
                    | '''
def p_operacionboolean(p):
    ''' operacionbool : boolean comparador boolean '''
def p_operacionbooleanfuera(p):
    '''operacionbooleanfuera : booleanstring
                    | booleanint'''

def p_validabooleanstring(p):
    '''booleanstring : boolean MAS CADENA
                    | boolean MENOS CADENA
                    | CADENA MAS boolean
                    | CADENA MENOS boolean
                     '''
def p_validabooleanint(p):
    '''booleanint : boolean MAS ENTERO
                    | boolean MENOS ENTERO
                    | ENTERO MAS boolean
                    | ENTERO MENOS boolean
                     '''

def p_varblock(p):
    '''varblock : varblock variable
                | '''

def p_numero_tipo(p):
    '''numerotipo : INT
              | FLOAT
              | LONG'''
def p_numero(p):
    '''numero : ENTERO
              | FLOTANTE'''
    p[0] = p[1]
def p_variable_numero(p):
    '''variable : tipo id IGUAL numero PUNTOCOMA
                | tipo id PUNTOCOMA'''


def p_variable(p):
    '''variable : AUTO id IGUAL valor PUNTOCOMA
                | AUTO id PUNTOCOMA'''
    lista = list(p)
    if len(lista) > 2:
        p[0] = p[4]


def p_variable_char(p):
    '''variable : CHAR id IGUAL CHARACTER PUNTOCOMA
                | STRING id IGUAL CADENA PUNTOCOMA
                | STRING id IGUAL stringappend PUNTOCOMA
                | STRING id IGUAL concat PUNTOCOMA
                | STRING id IGUAL booleanstring PUNTOCOMA
                | BOOL id IGUAL operacionbool PUNTOCOMA'''
    p[0] = p[4]

def p_string_append(p):
    '''stringappend : IDENTIFICADOR PUNTO APPEND LPAR stringdata RPAR'''
    p[0] = p[5]

def p_string_append_data(p):
    '''stringdata : CADENA 
                | IDENTIFICADOR'''
    p[0] = p[1]

def p_string_concat(p):
    '''concat : concat MAS CADENA
            | concat MAS IDENTIFICADOR
            | CADENA'''
    #string var = "kk" + "jj";
    if p[1] != None:
        p[0] = str(p[1]).replace('"','')
    lista = list(p)
    if len(lista) == 4:
        p[0] += str(p[3]).replace('"','')


def p_valor(p):
    '''valor : ENTERO 
            | FLOTANTE
            | CHARACTER
            | CADENA
            | TRUE
            | FALSE
            | IDENTIFICADOR'''
    p[0] = p[1]


def p_while(p):
    '''while : WHILE LPAR statement RPAR LLAVEL bodyblock LLAVER'''


def p_expresion_comparacion(p):
    '''expresion : expresion comparador expresion'''

def p_struct(p):
    '''struct : STRUCT IDENTIFICADOR LLAVEL  LLAVER IDENTIFICADOR PUNTOCOMA'''

def p_struct(p):
    '''struct : STRUCT IDENTIFICADOR LLAVEL varblock LLAVER IDENTIFICADOR PUNTOCOMA'''


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

#Evelyn Mejia 
# FOR


def p_initfor(p):
    '''initfor : tipo IDENTIFICADOR IGUAL valor'''

def p_condfor(p):
    '''condfor : IDENTIFICADOR comparador valor'''

def p_loopfor(p):
    '''loopfor : asign 
        | unaryexp'''

def p_mathasign(p):
    '''asign : IDENTIFICADOR MAS valor 
        | IDENTIFICADOR MENOS valor 
        | IDENTIFICADOR ASTERISCO valor 
        | IDENTIFICADOR SLASH valor''' 

def p_unaryexp(p):
    '''unaryexp : IDENTIFICADOR MAS MAS 
        | IDENTIFICADOR MENOS MENOS'''

def p_for(p):
    '''for : FOR LPAR initfor PUNTOCOMA condfor PUNTOCOMA loopfor RPAR LLAVEL bodyblock LLAVER'''

# ARRAY

def p_array(p):
    '''arraydeclaration : tipo id PUNTOCOMA
    | tipo id IGUAL LLAVEL arraydata LLAVER PUNTOCOMA
    | tipo id IGUAL LLAVEL LLAVER PUNTOCOMA'''



def p_arraydata(p):
    '''arraydata : arraydata COMMA  valor 
        | valor'''


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
    ''' funcionclaseimpl : tipo IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL bodyblock RETURN valor PUNTOCOMA LLAVER
                        | VOID IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL bodyblock LLAVER
                        | tipo IDENTIFICADOR LPAR parametrosimplementacion RPAR PUNTOCOMA
                        |'''
def p_parametrosimplementacion(p):
    '''parametrosimplementacion :  tipo IDENTIFICADOR masparametrosimplementacion
                                | tipo IDENTIFICADOR IGUAL valor masparametrosimplementacion
                                | tipo IDENTIFICADOR CORCHETEL CORCHETER masparametrosimplementacion
                                | tipo IDENTIFICADOR CORCHETEL CORCHETER IGUAL  masparametrosimplementacion
                                | '''
def p_parametrosfuncion(p):
    ''' parametrosfuncion : IDENTIFICADOR masparametrosfuncion
                            | valor masparametrosfuncion
                            |'''
def p_masparametrosimplementacion(p):
    '''masparametrosimplementacion :  COMMA parametrosimplementacion
                                    | '''
def p_masparametrosfuncion(p):
    ''' masparametrosfuncion : COMMA parametrosfuncion
                            | '''
def p_creacionobjeto(p):
    ''' creacionobjeto : IDENTIFICADOR IDENTIFICADOR PUNTOCOMA'''
def p_asignarvalores(p):
    ''' asignarvalorobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR IGUAL valor PUNTOCOMA '''
def p_usarfuncionesobjeto(p):
    ''' usarfuncionobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR LPAR parametrosfuncion RPAR PUNTOCOMA '''

#errors
def p_error(p):
    print("syntax error")
parser = yacc.yacc()
test = '''
    void main(){
       while(1){
          int var;
       }     
       for(int x = 0 ; x < 5 ; x++){
           auto s =  "hola";
       }
    }
'''
parser.parse(test)

test2 =  '''
    struct PERSONA{
        int nombre;
    } persona;
'''

parser.parse(test2)


test3 = "int var = 1;"

parser.parse(test3)

test4 =  '''
    class objeto1{int valor; int valor2;int funcs(int val){return 0;}}
'''
parser.parse(test4)

test5 = '''
    int func(){
        return 0;
    }
'''
parser.parse(test5)
test6 = '''
    obj1.funce(2);
'''
parser.parse(test6)

test7 = '''
    class objeto1{int funcs(int val=1){return 0;} void funcs2(){ int val=2;} void funcs3(){ int val=2; obj1.func(); }}
'''
parser.parse(test7)
test8 = '''
    bool valor=true<false; bool val=true<false;
'''
parser.parse(test8)
test9 = '''
    int findElement(int arr[], int n, int key);
'''
parser.parse(test9)


def parsing(s):
    parser.parse(s)


def inputLex(s):
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)  