import ply.lex as lex

tokens = ['IDENTIFICADOR','ENTERO','FLOTANTE','CHARACTER','CADENA','COMENTARIO','PUNTERO','EXCLAMACION','PORCENTAJE','CIRCUNFLEJO','AND','ASTERISCO','MENOS','MAS','IGUAL','LLAVEL','LLAVER','PIPE','VIRGUILA',
         'CORCHETEL','CORCHETER','BACKSLASH','PUNTOCOMA','COMASIMPLE','DOBLEPUNTO','COMADOBLE','MENOR','MAYOR','INTERROGACION','COMMA','PUNTO','SLASH','NUMERAL','LPAR','RPAR']

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for': 'FOR',
    'int': 'INT',
    'float': 'FLOAT',
    'long': 'LONG',
    'char': 'CHAR',
    'string' : 'STRING',
    'void': 'VOID',
    'public': 'PUBLIC',
    'private':'PRIVATE',
    'protected':'PROTECTED',
    'static' :'STATIC',
    'struct': 'STRUCT',
    'true': 'TRUE',
    'false': 'FALSE', 
    'nullptr' : 'NULLPOINTER',
    'auto' :'AUTO',
    'bool' : 'BOOL',
    'new' : 'NEW',
    'class': 'CLASS',
    'return': 'RETURN',
    'printf' : 'PRINT',
    'cout':'COUT',
    'append' : 'APPEND',
    'findElement' : 'FINDELEMENT'
}

tokens = tokens + list(reserved.values())

#TOKENS
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value,'IDENTIFICADOR') 
    return t

t_LPAR = r'\('
t_RPAR = r'\)'
t_EXCLAMACION = r'!'
t_PORCENTAJE = r'%'
t_CIRCUNFLEJO = r'\^'
t_AND = r'&'
t_ASTERISCO = r'\*'
t_MENOS = r'\-'
t_MAS = r'\+'
t_IGUAL = r'='
t_LLAVEL = r'\{'
t_LLAVER = r'\}'
t_PIPE = r'\|'
t_VIRGUILA = r'~'
t_PUNTERO = r'\*[a-zA-Z_][A-Za-z0-9_]*'
t_CORCHETER = r'\]'
t_CORCHETEL = r'\['
t_BACKSLASH = r'\\'
t_PUNTOCOMA = r';'
t_COMASIMPLE= r'\''
t_DOBLEPUNTO = r':'
t_COMADOBLE = r'\"'
t_MENOR = r'<'
t_MAYOR = r'>'
t_INTERROGACION = r'\?'
t_COMMA = r','
t_PUNTO = r'\.'
t_SLASH = r'/'
t_NUMERAL = r'\#'


t_CHARACTER = r'\'[a-zA-z]\''
t_CADENA = r'\"[a-zA-z0-9\s]*\"'

def t_FLOTANTE(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t
def t_ENTERO(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t

def t_COMENTARIO(t):
    r'(//.*|/\*.*\*/)'
    pass

#IGNORE
t_ignore = " \t"
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#BUILDER
lexer = lex.lex()
