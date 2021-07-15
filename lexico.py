import ply.lex as lex

tokens = ['IDENTIFICADOR','ENTERO','FLOTANTE','CHARACTER','CADENA','EXCLAMACION','AND','ASTERISCO','MENOS','MAS','IGUAL','LLAVEL','LLAVER','OR','CORCHETEL','CORCHETER','PUNTOCOMA','DOBLEPUNTO','MENOR','MAYOR','COMMA','PUNTO','SLASH','LPAR','RPAR']

reserved = {
    'if' : 'IF',
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
    'struct': 'STRUCT',
    'true': 'TRUE',
    'false': 'FALSE', 
    'auto' :'AUTO',
    'bool' : 'BOOL',
    'class': 'CLASS',
    'return': 'RETURN',
    'printf' : 'PRINT',
    'cout':'COUT',
    'append' : 'APPEND',
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
t_AND = r'&&'
t_ASTERISCO = r'\*'
t_MENOS = r'\-'
t_MAS = r'\+'
t_IGUAL = r'='
t_LLAVEL = r'\{'
t_LLAVER = r'\}'
t_OR = r'\|\|'
t_CORCHETER = r'\]'
t_CORCHETEL = r'\['
t_PUNTOCOMA = r';'
t_DOBLEPUNTO = r':'
t_MENOR = r'<'
t_MAYOR = r'>'
t_COMMA = r','
t_PUNTO = r'\.'
t_SLASH = r'/'


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
    print("Token Ilegal en la linea: {linea} token: {t}".format(t=t,linea=t.lineno))
    t.lexer.skip(1)
    raise Exception("Token Ilegal en la linea: {linea} token: {t}".format(t=t,linea=t.lineno))

#BUILDER
lexer = lex.lex()

