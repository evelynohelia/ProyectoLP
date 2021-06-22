import ply.lex as lex

tokens = ['IDENTIFICADOR','ENTERO','FLOTANTE','CHARACTER','STRING','COMENTARIO','PUNTERO'] 
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
    'print': 'PRINT',

}
tokens = tokens + list(reserved.values())

#TOKENS
t_PUNTERO = r'\*[a-zA-Z_][A-Za-z0-9_]*'
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value,'IDENTIFICADOR') 
    return t
t_CHARACTER = r'\'[a-zA-z]\''
t_STRING = r'\"[a-zA-z0-9\s]*\"'

def t_FLOTANTE(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_ENTERO(t):
    r'[0-9]+'
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

data = "*hola identificador1 _identificador2 2.5 786 /*comentario*/ true false \"Esto es una prueba\" int \'c\'"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)