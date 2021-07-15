import ply.yacc as yacc

from lexico import tokens,lexer

printList = []
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
         | mathoperation
         | creacionobjeto
         | asignarvalorobjeto
         | usarfuncionobjeto
         | usarfuncion'''
    p[0] = list(p)
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
                | bodyblock asignarvalorobjeto
                | bodyblock creacionobjeto
                | bodyblock usarfuncionobjeto
                | bodyblock usarfuncion

  '''
  p[0] = list(p)
#IF
def p_expresionif(p):
    '''expresionif : IF LPAR condicionif RPAR conllaves expresionpos
                    | IF LPAR condicionif RPAR sinllaves expresionpos
                    | IF LPAR condicionif RPAR conllaves 
                    | IF LPAR condicionif RPAR sinllaves PUNTOCOMA
                    | IF LPAR condicionif RPAR PUNTOCOMA expresionpos
                    '''
def p_expresionpos(p):
    '''expresionpos : else
                    | elseif'''
def p_elseif(p):
    ''' elseif : ELSE IF LPAR condicionif RPAR conllaves expresionpos
                | ELSE IF LPAR condicionif RPAR sinllaves  expresionpos
                | ELSE IF LPAR condicionif RPAR conllaves
                | ELSE IF LPAR condicionif RPAR sinllaves PUNTOCOMA
                | ELSE IF LPAR condicionif RPAR PUNTOCOMA expresionpos
                | ELSE IF LPAR condicionif RPAR sinllaves
                | ELSE IF LPAR condicionif RPAR PUNTOCOMA
                '''
def p_else(p):
    '''else : ELSE conllaves
            | ELSE sinllaves PUNTOCOMA
            | ELSE PUNTOCOMA '''

def p_sinLlaves(p):
    '''sinllaves : while
                | variable'''
    p[0] = list(p)

def p_conLlaves(p):
    '''conllaves : LLAVEL bodyblock LLAVER'''
    p[0] = list(p)
def p_condicionif(p):
    '''condicionif : initcondicion
                | statement'''
    p[0] = list(p)


def p_statement(p):
    '''statement : valorstatement
                | valorstatement masstatement'''
    p[0] = list(p)


def p_masestatement(p):
  '''
    masstatement : OR statement
                  | AND statement
  '''
  p[0] = list(p)


def p_valorstatement(p):
  '''
    valorstatement : comparar
                | EXCLAMACION boolean
                
                | id
                | LPAR id RPAR
                | EXCLAMACION LPAR id RPAR
                | boolean
                | numero
                | LPAR boolean RPAR
                | LPAR numero RPAR
                
  '''
  p[0] = list(p)

def p_initcondicion(p):
    '''initcondicion : varblock statement'''
    p[0] = list(p)

#CLASE
def p_claseimplementacion(p):
    ''' claseimplementacion : CLASS IDENTIFICADOR LLAVEL bloqueclase LLAVER PUNTOCOMA
                            | CLASS IDENTIFICADOR LLAVEL  LLAVER PUNTOCOMA
                            | CLASS IDENTIFICADOR LLAVEL acceso bloqueclase LLAVER PUNTOCOMA '''
    p[0] = list(p)


def p_claseacceso(p):
  '''
    acceso : PUBLIC DOBLEPUNTO
          | PRIVATE DOBLEPUNTO
          | PROTECTED DOBLEPUNTO
  '''
  p[0] = list(p)


def p_bloqueclase(p):
    ''' 
    bloqueclase : bloqueclase atributoclase
                    | atributoclase '''
    p[0] = list(p)


def p_atributoclase(p):
  ''' 
    atributoclase : definicion
                  | funcionclaseimpl
                  
  '''
  p[0] = list(p)


def p_definicion(p):
    '''definicion : numerotipo IDENTIFICADOR PUNTOCOMA
                  | STRING IDENTIFICADOR PUNTOCOMA
                  | CHAR IDENTIFICADOR PUNTOCOMA
                  | BOOL IDENTIFICADOR PUNTOCOMA '''
    p[0] = list(p)


#FUNCION
def p_funcionclaseimpl(p):
    '''
      funcionclaseimpl :  funcionimplvoid
                        | funcionimplnumero
                        | funcionimplstring
                        | funcionimplbool
    '''
    p[0] = list(p)

def p_funcionimplstring(p):
  '''
    funcionimplstring : STRING IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN concat PUNTOCOMA LLAVER
                    | CHAR IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN CHARACTER PUNTOCOMA LLAVER
                    | CHAR IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN IDENTIFICADOR PUNTOCOMA LLAVER
  '''
  p[0] = list(p)

def p_funcionimplvoid(p):
  ''' funcionimplvoid : VOID IDENTIFICADOR parametrosimpl LLAVEL bodyblock LLAVER
  '''
  p[0] = list(p)

def p_funcionimplnumero(p):
  '''
    funcionimplnumero : numerotipo IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN mathoperation PUNTOCOMA LLAVER
                      | numerotipo IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN IDENTIFICADOR PUNTOCOMA LLAVER
                      | numerotipo IDENTIFICADOR parametrosimpl PUNTOCOMA
  '''
  p[0] = list(p)

def p_funcionimplbool(p):
  '''
    funcionimplbool : BOOL IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN operacionbool PUNTOCOMA LLAVER
                      | BOOL IDENTIFICADOR parametrosimpl LLAVEL bodyblock RETURN IDENTIFICADOR PUNTOCOMA LLAVER
                      | BOOL IDENTIFICADOR parametrosimpl PUNTOCOMA
  '''
  p[0] = list(p)

def p_parametrosimpl(p):
  '''
    parametrosimpl : LPAR RPAR
                  | LPAR parametros RPAR
  '''
  p[0] = list(p)


def p_parametros(p):
  ''' parametros : tipo IDENTIFICADOR
                  | tipo IDENTIFICADOR masparametros 
  '''
  p[0] = list(p)

def p_masparametros(p):
  '''
    masparametros : COMMA parametros 
  '''
  p[0] = list(p)


def p_imprimir(p):
    '''imprimir : PRINT LPAR concat RPAR PUNTOCOMA 
                | COUT MENOR MENOR concat PUNTOCOMA
                | COUT MENOR MENOR numero PUNTOCOMA'''
    if p[1] == "printf":
        printList.append(p[3])
        print(p[3])
    else:
        printList.append(p[4])
        print(p[4])
    p[0] = list(p)

def p_while(p):
    '''while : WHILE LPAR statement RPAR LLAVEL bodyblock LLAVER'''
    p[0] = list(p)

def p_for(p):
    '''for : FOR LPAR numerotipo IDENTIFICADOR IGUAL numero PUNTOCOMA expresion PUNTOCOMA unaryexp RPAR LLAVEL bodyblock LLAVER'''
    p[0] = list(p)


def p_varblock(p):
    '''varblock : varblock variable
                | variable'''
    p[0] = list(p)

def p_struct(p):
    '''struct : STRUCT IDENTIFICADOR LLAVEL  LLAVER IDENTIFICADOR PUNTOCOMA
              | STRUCT IDENTIFICADOR LLAVEL varblock LLAVER IDENTIFICADOR PUNTOCOMA'''
    p[0] = list(p)

def p_unaryexp(p):
    '''unaryexp : IDENTIFICADOR MAS MAS 
        | IDENTIFICADOR MENOS MENOS'''    
    p[0] = list(p)

  
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
    p[0] = list(p)

def p_variableauto(p): 
  ''' 
    variableauto : AUTO id IGUAL valor PUNTOCOMA
                | AUTO id PUNTOCOMA
                
  '''
  p[0] = list(p)

def p_variablechar(p):
  ''' 
    variablechar : CHAR id IGUAL CHARACTER PUNTOCOMA
                  | CHAR id PUNTOCOMA
                  | CHAR id IGUAL IDENTIFICADOR PUNTOCOMA
  '''
  p[0] = list(p)
  
def p_variableboolean(p):
  ''' 
    variableboolean : BOOL id IGUAL operacionbool PUNTOCOMA
                  | BOOL id PUNTOCOMA
                  | BOOL id IGUAL IDENTIFICADOR PUNTOCOMA
  '''
  p[0] = list(p)

def p_variablestring(p):
  '''
    variablestring : STRING id IGUAL stringappend PUNTOCOMA
                | STRING id IGUAL concat PUNTOCOMA
                | STRING id PUNTOCOMA
  '''
  p[0] = list(p)

def p_variable_array_numero(p):
  ''' variablearraynumero : numerotipo idarray PUNTOCOMA
                    | numerotipo idarray IGUAL LLAVEL arraydatanumero LLAVER PUNTOCOMA
                    | numerotipo idarray IGUAL LLAVEL LLAVER PUNTOCOMA'''
  p[0] = list(p)  
def p_arraydata_numero(p):
  '''arraydatanumero : arraydatanumero COMMA  numero
                | numero'''
  p[0] = list(p)

def p_variable_array_char(p):
  ''' variablearraychar : CHAR idarray PUNTOCOMA
                        | CHAR idarray IGUAL LLAVEL LLAVER PUNTOCOMA
                        | CHAR idarray IGUAL LLAVEL datachar LLAVER PUNTOCOMA
                        | CHAR idarray IGUAL CADENA  PUNTOCOMA
  '''
  p[0] = list(p)

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

#OBJETOS
def p_creacionobjeto(p):
    ''' creacionobjeto : IDENTIFICADOR IDENTIFICADOR PUNTOCOMA'''
    p[0] = list(p)

def p_asignarvalores(p):
    ''' asignarvalorobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR IGUAL valor PUNTOCOMA '''
    p[0] = list(p)

def p_usarfuncionesobjeto(p):
    ''' usarfuncionobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR funcparentesis PUNTOCOMA '''
    p[0] = list(p)

#argumentos y funcion general
def p_usarfuncion(p):
  '''
    usarfuncion : IDENTIFICADOR funcparentesis PUNTOCOMA
  '''
  p[0] = list(p)

def p_funcparentesis(p):
  '''
    funcparentesis : LPAR RPAR
                  | LPAR argumentosfuncion RPAR
  '''
  p[0] = list(p)


def p_argumentosfuncion(p):
  ''' argumentosfuncion : valor
                  | valor masargumentosfuncion 
  '''
  p[0] = list(p)

def p_masargumentosfuncion(p):
  '''
    masargumentosfuncion : COMMA argumentosfuncion 
  '''
  p[0] = list(p)

#COMPARACIONES
def p_expresion_comparacion(p):
    '''expresion : valor comparador valor
                | LPAR valor comparador valor  RPAR
                | EXCLAMACION LPAR valor comparador valor  RPAR
                 '''
    p[0] = list(p)             
#Se trabaja con esto


def p_comparar(p):
    '''
    comparar : expresion
            |  mascomparaciones expresion  
            | LPAR  mascomparaciones expresion  RPAR
            | EXCLAMACION LPAR  mascomparaciones expresion  RPAR
            | LPAR  mascomparaciones RPAR
            
            
    '''
    p[0] = list(p)

def p_mascomparaciones(p):
  '''
    mascomparaciones :   comparar comparador
                      |    comparar  LPAR comparador RPAR 
                      
  '''
  p[0] = list(p)

#Operaciones


def p_mathoperation(p):
    '''mathoperation : numero operation 
        | numero
        '''
    p[0] = list(p)

def p_operation(p):
    '''operation : MAS mathoperation
        |  MENOS mathoperation
        | ASTERISCO mathoperation
        |  SLASH mathoperation'''
    p[0] = list(p)

def p_operacionboolean(p):
    ''' operacionbool : boolean comparador boolean 
                      | boolean'''
    p[0] = list(p)
#Solo tokens
def p_boolean(p):
    '''boolean : TRUE
                | FALSE'''
    p[0] = list(p)

def p_comparacion(p):
    '''comparador : IGUAL IGUAL
                | MENOR
                | MAYOR
                | MENOR IGUAL
                | MAYOR IGUAL
                | EXCLAMACION IGUAL'''
    p[0] = list(p)

def p_id(p):
  '''id : IDENTIFICADOR'''
  p[0] = p[1]

def p_id_array(p):
  ''' idarray : IDENTIFICADOR CORCHETEL ENTERO CORCHETER '''
  p[0] = list(p)

def p_numero(p):
    '''numero : ENTERO
              | FLOTANTE
              '''
    p[0] = p[1]
def p_numero_tipo(p):
    '''numerotipo : INT
              | FLOAT
              | LONG'''
    p[0] = p[1]
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
     if p:
          print("Syntax error at token", p.type)
          raise SyntaxError("Error sintactico en linea: {linea} col: {col} valor: {valor}".format(linea=p.lineno,col=p,valor=p.value))
          # Just discard the token and tell the parser it's okay.
     else:
          raise SyntaxError("Error sintactico, contenido vacio")
   #"Error sintactico en linea: {linea} col: {col} valor: {valor}".format(linea=p.lineno,col=p,valor=p.value)
   

        
    

parser = yacc.yacc()
print("test0")
test =''' !((!(1<0)<(0<2))<(0<2)); '''
parser.parse(test)
print("test1")
test1 = '''int var = 1;'''
parser.parse(test1)

test2 = '''int var[2] = {1,2};'''
parser.parse(test2)
print("test2")
test3 = '''while(1){
  int var;
  while(true){
    
  }
}'''

test3 = '''for(int x = 0;x<1;x++){
    while(true && (false) || (1<1<0<0<0<0) && variable  ){
    struct PERSONA{
        int nombre;
        int apellido;
    } persona;
    int n=1;
  }
}'''
parser.parse(test3)
print("test3")
test4 = '''string var = "hola" + "jj"; '''
parser.parse(test4)
print("test4")

test5 = '''printf("test printf"); '''
parser.parse(test5)
print("test5")
testc = '''cout << "test cout";'''
parser.parse(testc)
print("testcout")
test6 =  '''    
struct PERSONA{
        int nombre;
        int apellido;
    } persona;
 '''
parser.parse(test6)
print("test6")
test7 = '''
  int main() {
    
    return 0;
  }
'''
parser.parse(test7)
print("test7")
test8 = '''
  class myclase{};
'''
parser.parse(test8)
print("test8")
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
print("test9")
test10 = '''
  if(int var=2+2;string var1="hola";1<0){} else if (int var=2+2;string var1="hola";1<0) {} 
  else if(int var=2+2;string var1="hola";1<3);
  else if (int var=2+2;string var1="hola";1<3);
  else {int var=2+2;}




'''
parser.parse(test10)
print("test10")
test11 = '''
  int var = 1 + 1 + 4 +3 / 10 ;
'''
parser.parse(test11)
print("test11")
test12 = '''int var = n1;'''
parser.parse(test12)
print("test12")
test13 = '''bool var = true < false;'''
parser.parse(test13)
print("test13")
test14 = '''
  bool var = n1;
'''

parser.parse(test14)
print("test14")
test15 = '''
  if(int var=2+2;string var1="hola";1<0){

  }
  else{
    cout << "cout en else jeje";
  }
'''
parser.parse(test15)
print("test15")
test16 = '''
  if(int var=2+2;string var1="hola";1<0);
  else if (int var=2+2;string var1="hola";1<0) ;
  else if (int var=2+2;string var1="hola";1<0) int var=2+2 ;
  else{
    cout << "cout en else jeje";
  }
'''
parser.parse(test16)
print("test16")
test17 = '''
  int main ();
'''
parser.parse(test17)
print("test17")
test18 = '''
  OBJ obj;
'''
parser.parse(test18)
print("test18")
test19 = '''
  obj.nombre=1.2;
'''
parser.parse(test19)
print("test19")
test20 = '''
  obj.func();
'''
parser.parse(test20)
print("test20")
test21 = '''
  funkopop("string");
'''
parser.parse(test21)
print("test21")
testMain = '''
  int main(){
    cout << "Hello World";
    return 0;
    /*hola*/
  }
'''

parser.parse(testMain)
print("testMain")
parser.restart()
printList.clear()
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
    parsing = parser.parse(s)
    print(parsing)
    if parsing == None:
        return [True,printList]
    else:
        return [False,printList]



def inputLex(s):
    lexer.input(s)
    listaTokens=[]
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        listaTokens.append(tok)  
    return listaTokens
