import ply.lex as lex

tokens = ('IDENTIFICADOR',)

#TOKENS
t_IDENTIFICADOR= r'\w+'

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

data = "Test\nHola"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)