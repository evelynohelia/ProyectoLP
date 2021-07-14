import ply.yacc as yacc

from lexico import tokens,lexer

def p_body(p):
    '''
    body : comparar PUNTOCOMA
         | variable
         | imprimir
         | while
         | for
         | struct
         | claseimplementacion
         | funcionclaseimpl
         | expresionif
         | mathoperation'''
#Gramaticas
def p_empty(p):
  '''empty : '''
  pass

def p_bodyblock(p):
  ''' bodyblock : empty
      bodyblock : bodyblock while
                | bodyblock variable
                | bodyblock for
                | bodyblock struct
                | bodyblock imprimir
                | bodyblock expresionif
                | bodyblock mathoperation
                | bodyblock operacionbool

  '''
#IF
def p_expresionif(p):
    '''expresionif : IF LPAR condicionif RPAR conllaves expresionpos
                    | IF LPAR condicionif RPAR sinllaves expresionpos
                    | IF LPAR condicionif RPAR conllaves 
                    | IF LPAR condicionif RPAR sinllaves PUNTOCOMA
                    '''
def p_expresionpos(p):
    '''expresionpos : else
                    | elseif'''
def p_elseif(p):
    ''' elseif : ELSE IF LPAR condicionif RPAR conllaves else
                | ELSE IF LPAR condicionif RPAR sinllaves PUNTOCOMA else 
                | ELSE IF LPAR condicionif RPAR conllaves 
                | ELSE IF LPAR condicionif RPAR sinllaves PUNTOCOMA'''
def p_else(p):
    '''else : ELSE conllaves
            | ELSE sinllaves PUNTOCOMA'''

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

#CLASE
def p_claseimplementacion(p):
    ''' claseimplementacion : CLASS IDENTIFICADOR LLAVEL bloqueclase LLAVER PUNTOCOMA
                            | CLASS IDENTIFICADOR LLAVEL  LLAVER PUNTOCOMA
                            | CLASS IDENTIFICADOR LLAVEL acceso bloqueclase LLAVER PUNTOCOMA '''
def p_claseacceso(p):
  '''
    acceso : PUBLIC DOBLEPUNTO
          | PRIVATE DOBLEPUNTO
          | PROTECTED DOBLEPUNTO
  '''
def p_bloqueclase(p):
    ''' 
    bloqueclase : bloqueclase atributoclase
                    | atributoclase '''
def p_atributoclase(p):
  ''' 
    atributoclase : definicion
                  | funcionclaseimpl
                  
  '''

def p_definicion(p):
    '''definicion : numerotipo IDENTIFICADOR PUNTOCOMA
                  | STRING IDENTIFICADOR PUNTOCOMA
                  | CHAR IDENTIFICADOR PUNTOCOMA
                  | BOOL IDENTIFICADOR PUNTOCOMA '''
#FUNCION
def p_funcionclaseimpl(p):
    '''
      funcionclaseimpl :  funcionimplvoid
                        | funcionimplnumero
                        | funcionimplstring
                        | funcionimplbool
    '''

def p_funcionimplstring(p):
  '''
    funcionimplstring : STRING IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN concat PUNTOCOMA LLAVER
                    | CHAR IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN CHARACTER PUNTOCOMA LLAVER
                    | CHAR IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN IDENTIFICADOR PUNTOCOMA LLAVER
  '''

def p_funcionimplvoid(p):
  ''' funcionimplvoid : VOID IDENTIFICADOR parametrosimpl LLAVEL bodyblock LLAVER
  '''
def p_funcionimplnumero(p):
  '''
    funcionimplnumero : numerotipo IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN numero PUNTOCOMA LLAVER 
                      | numerotipo IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN IDENTIFICADOR PUNTOCOMA LLAVER
                      | numerotipo IDENTIFICADOR parametrosimpl PUNTOCOMA
  '''
def p_funcionimplbool(p):
  '''
    funcionimplbool : BOOL IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN boolean PUNTOCOMA LLAVER 
                      | BOOL IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN IDENTIFICADOR PUNTOCOMA LLAVER
                      | BOOL IDENTIFICADOR parametrosimpl PUNTOCOMA
  '''
def p_parametrosimpl(p):
  '''
    parametrosimpl : LPAR RPAR
                  | LPAR parametros RPAR
  '''

def p_parametros(p):
  ''' parametros : tipo IDENTIFICADOR
                  | tipo IDENTIFICADOR masparametros 
  '''
def p_masparametros(p):
  '''
    masparametros : COMMA parametros 
  '''

def p_imprimir(p):
    '''imprimir : PRINT LPAR concat RPAR PUNTOCOMA 
                | COUT MENOR MENOR concat PUNTOCOMA'''
    if p[1] == "printf":
        print(p[3])
    else:
        print(p[4])

def p_while(p):
    '''while : WHILE LPAR statement RPAR LLAVEL bodyblock LLAVER'''

def p_for(p):
    '''for : FOR LPAR numerotipo IDENTIFICADOR IGUAL numero PUNTOCOMA expresion PUNTOCOMA unaryexp RPAR LLAVEL bodyblock LLAVER'''

def p_varblock(p):
    '''varblock : varblock variable
                | variable'''
def p_struct(p):
    '''struct : STRUCT IDENTIFICADOR LLAVEL  LLAVER IDENTIFICADOR PUNTOCOMA
              | STRUCT IDENTIFICADOR LLAVEL varblock LLAVER IDENTIFICADOR PUNTOCOMA'''

def p_unaryexp(p):
    '''unaryexp : IDENTIFICADOR MAS MAS 
        | IDENTIFICADOR MENOS MENOS'''    
    
def p_statement(p):
    '''statement : expresion
                | EXCLAMACION boolean
                | EXCLAMACION LPAR expresion RPAR
                | EXCLAMACION IDENTIFICADOR
                | boolean
                | numero'''
  
def p_variable(p):
    '''variable : variableauto 
                | variablenumero
                | variablechar
                | variablestring
                | variablearraynumero
                | variablearraychar
                | variableboolean
                 '''
    p[0] = p[1]


#VARIABLESTIPO
def p_variablenumero(p):
    ''' variablenumero : numerotipo id IGUAL mathoperation PUNTOCOMA
                        | numerotipo id PUNTOCOMA
                        | numerotipo id IGUAL IDENTIFICADOR PUNTOCOMA'''
def p_variableauto(p): 
  ''' 
    variableauto : AUTO id IGUAL valor PUNTOCOMA
                | AUTO id PUNTOCOMA
                
  '''
def p_variablechar(p):
  ''' 
    variablechar : CHAR id IGUAL CHARACTER PUNTOCOMA
                  | CHAR id PUNTOCOMA
                  | CHAR id IGUAL IDENTIFICADOR PUNTOCOMA
  '''
def p_variableboolean(p):
  ''' 
    variableboolean : BOOL id IGUAL operacionbool PUNTOCOMA
                  | BOOL id PUNTOCOMA
                  | BOOL id IGUAL IDENTIFICADOR PUNTOCOMA
  '''
def p_variablestring(p):
  '''
    variablestring : STRING id IGUAL stringappend PUNTOCOMA
                | STRING id IGUAL concat PUNTOCOMA
                | STRING id PUNTOCOMA
  '''
def p_variable_array_numero(p):
  ''' variablearraynumero : numerotipo idarray PUNTOCOMA
                    | numerotipo idarray IGUAL LLAVEL arraydatanumero LLAVER PUNTOCOMA
                    | numerotipo idarray IGUAL LLAVEL LLAVER PUNTOCOMA'''

def p_arraydata_numero(p):
  '''arraydatanumero : arraydatanumero COMMA  numero
                | numero'''

def p_variable_array_char(p):
  ''' variablearraychar : CHAR idarray PUNTOCOMA
                        | CHAR idarray IGUAL LLAVEL LLAVER PUNTOCOMA
                        | CHAR idarray IGUAL LLAVEL datachar LLAVER PUNTOCOMA
                        | CHAR idarray IGUAL CADENA  PUNTOCOMA
  '''
def p_arraydata_char(p):
  ''' datachar : CHARACTER
                | datachar COMMA CHARACTER
  
  '''
  lista = list(p)
  if len(lista) > 2:
    p[0] = p[4]
#CONCAT Y APPEND
def p_string_append(p):
    '''stringappend : IDENTIFICADOR PUNTO APPEND LPAR stringdata RPAR'''
    p[0] = p[5]
def p_string_concat(p):
    '''concat : stringdata MAS concat
              | stringdata'''
    #string var = "kk" + "jj";
    if p[1] != None:
        p[0] = str(p[1]).replace('"','')
    lista = list(p)
    if len(lista) == 4:
        p[0] += str(p[3]).replace('"','')

#COMPARACIONES
def p_expresion_comparacion(p):
    '''expresion : valor comparador valor
                | LPAR valor comparador valor  RPAR '''
#Se trabaja con esto
def p_comparar(p):
    '''
    comparar : expresion
            | expresion comparador comparar
    '''

#Operaciones


def p_mathoperation(p):
    '''mathoperation : numero operation 
        | numero
        '''

def p_operation(p):
    '''operation : MAS mathoperation
        |  MENOS mathoperation
        | ASTERISCO mathoperation
        |  SLASH mathoperation'''

def p_operacionboolean(p):
    ''' operacionbool : boolean comparador boolean 
                      | boolean'''

#Solo tokens
def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''
def p_comparacion(p):
    '''comparador : IGUAL IGUAL
                | MENOR
                | MAYOR
                | MENOR IGUAL
                | MAYOR IGUAL
                | EXCLAMACION IGUAL'''
def p_id(p):
  '''id : IDENTIFICADOR'''

def p_id_array(p):
  ''' idarray : IDENTIFICADOR CORCHETEL ENTERO CORCHETER '''

def p_numero(p):
    '''numero : ENTERO
              | FLOTANTE
              '''
    p[0] = p[1]
def p_numero_tipo(p):
    '''numerotipo : INT
              | FLOAT
              | LONG'''
def p_string_append_data(p):
    '''stringdata : CADENA
                | IDENTIFICADOR'''
    p[0] = p[1]
def p_tipo(p):
    '''tipo : numerotipo
            | STRING
            | CHAR'''

def p_valor(p):
    '''valor : numero
            | CHARACTER
            | boolean
            | stringdata'''
    p[0] = p[1]


#errors
def p_error(p):
    print("syntax error")
parser = yacc.yacc()
test =''' 1<1<0<0<0<0; '''
parser.parse(test)

test1 = '''int var = 1;'''
parser.parse(test1)

test2 = '''int var[2] = {1,2};'''
parser.parse(test2)

test3 = '''while(1){
  int var;
  while(true){
    
  }
}'''

test3 = '''for(int x = 0;x<1;x++){
    while(true){
    struct PERSONA{
        int nombre;
        int apellido;
    } persona;
    int n=1;
  }
}'''
parser.parse(test3)

test4 = '''string var = "hola" + "jj"; '''
parser.parse(test4)


test5 = '''printf("test printf"); '''
parser.parse(test5)

testc = '''cout << "test cout";'''
parser.parse(testc)

test6 =  '''    
struct PERSONA{
        int nombre;
        int apellido;
    } persona;
 '''
parser.parse(test6)

test7 = '''
  int main() {
    
    return 0;
  }
'''
parser.parse(test7)
test8 = '''
  class myclase{};
'''
parser.parse(test8)
test9 = '''
  class myclase{
    public:
      int hola;
      char funct(string h,int numero){
        return 'a';
      }
  };
'''
parser.parse(test9)
test10 = '''
  if(1<0){

  }
  else{
    cout << "cout en else jeje";
  }
'''
parser.parse(test10)
test11 = '''
  int var = 1 + 1 + 4 +3 / 10 ;
'''
parser.parse(test11)

test12 = '''int var = n1;'''
parser.parse(test12)

test13 = '''bool var = true < false;'''
parser.parse(test13)

test14 = '''
  bool var = n1;
'''
parser.parse(test14)

test17 = '''
  int main ();
'''
parser.parse(test17)


testMain = '''
  int main(){
    cout << "Hello World";
    return 0;
  }
'''

parser.parse(testMain)


#     void main(){
#        while(1){
#           int var;
#        }
#        for(int x = 0 ; x < 5 ; x++){
#            auto s =  "hola";
#        }
#     }
# '''
# parser.parse(test)
#

#
#
# test3 = "int var = 1;"
#
# parser.parse(test3)
#
# test4 =  '''
#     class objeto1{int valor; int valor2;int funcs(int val){return 0;}}
# '''
# parser.parse(test4)
#
# test5 = '''
#     int func(){
#         return 0;
#     }
# '''
# parser.parse(test5)


def parsing(s):
    parser.parse(s)


def inputLex(s):
    lexer.input(s)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)  