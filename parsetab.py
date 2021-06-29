
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASTERISCO AUTO BACKSLASH BOOL CHAR CHARACTER CIRCUNFLEJO CLASS COMADOBLE COMASIMPLE COMENTARIO COMMA CORCHETEL CORCHETER DOBLEPUNTO ELSE ENTERO EXCLAMACION FALSE FLOAT FLOTANTE FOR IDENTIFICADOR IF IGUAL INT INTERROGACION LLAVEL LLAVER LONG LPAR MAS MAYOR MENOR MENOS NEW NULLPOINTER NUMERAL PIPE PORCENTAJE PRINT PRIVATE PROTECTED PUBLIC PUNTERO PUNTO PUNTOCOMA RETURN RPAR SLASH STATIC STRING STRUCT THEN TRUE VIRGUILA VOID WHILEbody : variable\n            | while\n            | expresionif\n            | claseimplementacion\n            | funcionclaseimpl\n            | creacionobjeto\n            | asignarvalorobjeto\n            | usarfuncionobjeto\n            | struct\n            |imprimir : PRINT LPAR valor RPAR bodyblock : bodyblock variable\n                    |  bodyblock while\n                    | bodyblock expresionif\n                    |  funcionblock : bodyblock variable\n                    |  bodyblock while\n                    | bodyblock expresionif\n                    | RETURN statement\n                    | varblock : varblock variable\n                | variable : AUTO IDENTIFICADOR IGUAL valor PUNTOCOMA\n                | AUTO IDENTIFICADOR PUNTOCOMAvariable : numerotipo IDENTIFICADOR IGUAL numero PUNTOCOMA\n                | numerotipo IDENTIFICADOR PUNTOCOMAvariable : CHAR IDENTIFICADOR IGUAL CHARACTER PUNTOCOMAnumerotipo : INT\n              | FLOAT\n              | LONGnumero : ENTERO\n              | FLOTANTEtipo : INT \n            | FLOAT\n            | LONG\n            | AUTO\n            | CHAR\n            | VOIDvalor : ENTERO \n            | FLOTANTE\n            | CHARACTER\n            | STRING\n            | TRUE\n            | FALSE\n            | IDENTIFICADORwhile : WHILE LPAR statement RPAR LLAVEL bodyblock LLAVERexpresion : expresion comparador expresionstruct : STRUCT IDENTIFICADOR LLAVEL varblock LLAVER IDENTIFICADOR PUNTOCOMAexpresionif : IF LPAR condicionif RPAR conllaves expresionpos\n                    | IF LPAR condicionif RPAR sinllaves expresionpos\n                    expresionpos : else\n                    | elseif\n                    |  elseif : ELSE IF LPAR condicionif RPAR conllaves else\n                | ELSE IF LPAR condicionif RPAR sinllaves else\n                | else : ELSE conllaves\n            | ELSE sinllavessinllaves : while\n                | variableconllaves : LLAVEL bodyblock LLAVERcondicionif : initcondicion\n                | statementinitcondicion : varblock statementstatement : expresion\n                | EXCLAMACION boolean\n                | EXCLAMACION LPAR expresion RPAR\n                | EXCLAMACION IDENTIFICADORboolean : TRUE\n                | FALSEexpresion : valorcomparador : IGUAL IGUAL\n                | MENOR\n                | MAYOR\n                | MENOR IGUAL\n                | MAYOR IGUAL\n                | EXCLAMACION IGUALinitfor : tipo IDENTIFICADOR IGUAL valor initfor : IDENTIFICADOR comparador valor loopfor : asign \n                | unaryexp asign :  IDENTIFICADOR MAS valor\n                | IDENTIFICADOR MENOS valor \n                | IDENTIFICADOR ASTERISCO valor\n                | IDENTIFICADOR SLASH valorunaryexp : IDENTIFICADOR MAS MAS\n                | IDENTIFICADOR MENOS MENOS for : FOR LPAR initfor PUNTOCOMA initfor PUNTOCOMA loopfor RPAR LLAVEL bodyblock LLAVERarray_declaration : tipo IDENTIFICADOR CORCHETEL ENTERO CORCHETER PUNTOCOMA claseimplementacion : CLASS IDENTIFICADOR LLAVEL bloqueclase LLAVER bloqueclase : bloqueclase definicion\n                    |  bloqueclase funcionclaseimpl\n                    | definicion : tipo IDENTIFICADOR PUNTOCOMA\n                    |  funcionclaseimpl : tipo IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL funcionblock LLAVER\n                        | VOID IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL bodyblock LLAVER\n                        |parametrosimplementacion :  tipo IDENTIFICADOR masparametrosimplementacion\n                                |  parametrosfuncion : IDENTIFICADOR masparametrosfuncion\n                            | masparametrosimplementacion :  COMMA parametrosimplementacion\n                                    |  masparametrosfuncion : COMMA parametrosfuncion\n                            |  creacionobjeto : IDENTIFICADOR IDENTIFICADOR PUNTOCOMA asignarvalorobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR IGUAL valor\n                            | LPAR expresion RPAR\n                            | LPAR statement RPAR\n                            | EXCLAMACION  LPAR statement RPAR usarfuncionobjeto : IDENTIFICADOR PUNTO IDENTIFICADOR LPAR parametrosfuncion RPAR PUNTOCOMA '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,36,37,38,39,40,41,42,50,51,54,58,64,111,113,114,117,118,121,122,124,125,126,138,139,140,142,151,152,156,157,159,166,168,173,179,180,],[-10,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-45,-39,-40,-41,-42,-43,-44,-24,-107,-26,-109,-110,-111,-23,-108,-25,-27,-53,-53,-59,-60,-90,-49,-51,-52,-50,-112,-46,-57,-58,-61,-48,-96,-97,-54,-55,]),'AUTO':([0,43,50,54,73,74,75,76,78,93,95,101,112,113,117,118,119,121,122,123,124,125,127,128,137,138,139,140,141,142,143,146,147,148,152,153,154,155,156,157,159,160,163,165,167,168,169,170,171,173,175,178,179,180,],[11,-22,-24,-26,96,-93,107,107,-22,96,-21,107,96,-23,-25,-27,-15,-53,-53,-15,-59,-60,-91,-92,96,-49,-51,-52,96,-50,96,107,-15,-15,-46,-12,-13,-14,-57,-58,-61,-94,96,96,-22,-96,-12,-13,-14,-97,96,96,-54,-55,]),'CHAR':([0,43,50,54,73,74,75,76,78,93,95,101,112,113,117,118,119,121,122,123,124,125,127,128,137,138,139,140,141,142,143,146,147,148,152,153,154,155,156,157,159,160,163,165,167,168,169,170,171,173,175,178,179,180,],[14,-22,-24,-26,97,-93,108,108,-22,97,-21,108,97,-23,-25,-27,-15,-53,-53,-15,-59,-60,-91,-92,97,-49,-51,-52,97,-50,97,108,-15,-15,-46,-12,-13,-14,-57,-58,-61,-94,97,97,-22,-96,-12,-13,-14,-97,97,97,-54,-55,]),'WHILE':([0,50,54,93,113,117,118,119,121,122,123,124,125,137,138,139,140,141,142,143,147,148,152,153,154,155,156,157,159,163,165,169,170,171,175,178,179,180,],[15,-24,-26,15,-23,-25,-27,-15,-53,-53,-15,-59,-60,15,-49,-51,-52,15,-50,15,-15,-15,-46,-12,-13,-14,-57,-58,-61,15,15,-12,-13,-14,15,15,-54,-55,]),'IF':([0,50,54,113,117,118,119,121,122,123,124,125,137,138,139,140,141,142,143,147,148,152,153,154,155,156,157,159,163,165,169,170,171,179,180,],[17,-24,-26,-23,-25,-27,-15,-53,-53,-15,-59,-60,17,-49,-51,-52,158,-50,17,-15,-15,-46,-12,-13,-14,-57,-58,-61,17,17,-12,-13,-14,-54,-55,]),'CLASS':([0,],[18,]),'VOID':([0,74,75,76,101,127,128,146,160,168,173,],[20,-93,109,109,20,-91,-92,109,-94,-96,-97,]),'IDENTIFICADOR':([0,11,12,13,14,16,18,19,20,22,23,24,25,28,31,35,43,47,49,50,54,59,61,62,66,73,80,81,88,89,90,91,95,96,97,98,99,100,102,104,105,106,107,108,109,113,117,118,129,133,135,164,167,],[12,26,27,29,30,36,44,45,46,48,-28,-29,-30,52,36,67,36,36,36,-24,-26,36,-73,-74,36,36,36,115,-72,-75,-76,-77,-21,26,30,-28,-29,-30,130,-33,-34,-35,-36,-37,-38,-23,-25,-27,144,149,115,36,36,]),'LPAR':([0,15,17,21,35,45,46,52,144,158,],[16,31,43,47,66,75,76,81,75,167,]),'EXCLAMACION':([0,16,31,32,34,36,37,38,39,40,41,42,43,47,50,54,57,73,87,92,95,113,117,118,164,167,],[21,35,35,63,-71,-45,-39,-40,-41,-42,-43,-44,35,35,-24,-26,63,35,63,63,-21,-23,-25,-27,35,35,]),'STRUCT':([0,],[22,]),'INT':([0,43,50,54,73,74,75,76,78,93,95,101,112,113,117,118,119,121,122,123,124,125,127,128,137,138,139,140,141,142,143,146,147,148,152,153,154,155,156,157,159,160,163,165,167,168,169,170,171,173,175,178,179,180,],[23,-22,-24,-26,98,-93,104,104,-22,98,-21,104,98,-23,-25,-27,-15,-53,-53,-15,-59,-60,-91,-92,98,-49,-51,-52,98,-50,98,104,-15,-15,-46,-12,-13,-14,-57,-58,-61,-94,98,98,-22,-96,-12,-13,-14,-97,98,98,-54,-55,]),'FLOAT':([0,43,50,54,73,74,75,76,78,93,95,101,112,113,117,118,119,121,122,123,124,125,127,128,137,138,139,140,141,142,143,146,147,148,152,153,154,155,156,157,159,160,163,165,167,168,169,170,171,173,175,178,179,180,],[24,-22,-24,-26,99,-93,105,105,-22,99,-21,105,99,-23,-25,-27,-15,-53,-53,-15,-59,-60,-91,-92,99,-49,-51,-52,99,-50,99,105,-15,-15,-46,-12,-13,-14,-57,-58,-61,-94,99,99,-22,-96,-12,-13,-14,-97,99,99,-54,-55,]),'LONG':([0,43,50,54,73,74,75,76,78,93,95,101,112,113,117,118,119,121,122,123,124,125,127,128,137,138,139,140,141,142,143,146,147,148,152,153,154,155,156,157,159,160,163,165,167,168,169,170,171,173,175,178,179,180,],[25,-22,-24,-26,100,-93,106,106,-22,100,-21,106,100,-23,-25,-27,-15,-53,-53,-15,-59,-60,-91,-92,100,-49,-51,-52,100,-50,100,106,-15,-15,-46,-12,-13,-14,-57,-58,-61,-94,100,100,-22,-96,-12,-13,-14,-97,100,100,-54,-55,]),'PUNTO':([12,],[28,]),'ENTERO':([16,31,43,47,49,50,53,54,59,61,62,66,73,80,88,89,90,91,95,113,117,118,164,167,],[37,37,37,37,37,-24,83,-26,37,-73,-74,37,37,37,-72,-75,-76,-77,-21,-23,-25,-27,37,37,]),'FLOTANTE':([16,31,43,47,49,50,53,54,59,61,62,66,73,80,88,89,90,91,95,113,117,118,164,167,],[38,38,38,38,38,-24,84,-26,38,-73,-74,38,38,38,-72,-75,-76,-77,-21,-23,-25,-27,38,38,]),'CHARACTER':([16,31,43,47,49,50,54,55,59,61,62,66,73,80,88,89,90,91,95,113,117,118,164,167,],[39,39,39,39,39,-24,-26,85,39,-73,-74,39,39,39,-72,-75,-76,-77,-21,-23,-25,-27,39,39,]),'STRING':([16,31,43,47,49,50,54,59,61,62,66,73,80,88,89,90,91,95,113,117,118,164,167,],[40,40,40,40,40,-24,-26,40,-73,-74,40,40,40,-72,-75,-76,-77,-21,-23,-25,-27,40,40,]),'TRUE':([16,31,35,43,47,49,50,54,59,61,62,66,73,80,88,89,90,91,95,113,117,118,164,167,],[41,41,68,41,41,41,-24,-26,41,-73,-74,41,41,41,-72,-75,-76,-77,-21,-23,-25,-27,41,41,]),'FALSE':([16,31,35,43,47,49,50,54,59,61,62,66,73,80,88,89,90,91,95,113,117,118,164,167,],[42,42,69,42,42,42,-24,-26,42,-73,-74,42,42,42,-72,-75,-76,-77,-21,-23,-25,-27,42,42,]),'IGUAL':([26,29,30,32,34,36,37,38,39,40,41,42,52,57,60,61,62,63,87,92,],[49,53,55,60,-71,-45,-39,-40,-41,-42,-43,-44,80,60,88,89,90,91,60,60,]),'PUNTOCOMA':([26,27,29,36,37,38,39,40,41,42,79,82,83,84,85,136,144,149,],[50,51,54,-45,-39,-40,-41,-42,-43,-44,113,117,-31,-32,118,151,160,166,]),'RPAR':([32,33,34,36,37,38,39,40,41,42,56,57,65,67,68,69,70,71,72,75,76,77,81,87,92,94,103,110,115,116,120,130,134,135,145,146,150,161,174,],[58,64,-71,-45,-39,-40,-41,-42,-43,-44,86,-65,-66,-68,-69,-70,93,-62,-63,-100,-100,111,-102,-47,120,-64,131,132,-106,136,-67,-104,-101,-102,-99,-100,-105,-103,175,]),'MENOR':([32,34,36,37,38,39,40,41,42,57,87,92,],[61,-71,-45,-39,-40,-41,-42,-43,-44,61,61,61,]),'MAYOR':([32,34,36,37,38,39,40,41,42,57,87,92,],[62,-71,-45,-39,-40,-41,-42,-43,-44,62,62,62,]),'LLAVER':([34,36,37,38,39,40,41,42,50,54,57,65,67,68,69,74,78,87,95,101,112,113,117,118,119,120,121,122,123,124,125,127,128,137,138,139,140,142,143,147,148,152,153,154,155,156,157,159,160,162,165,168,169,170,171,172,173,179,180,],[-71,-45,-39,-40,-41,-42,-43,-44,-24,-26,-65,-66,-68,-69,-70,-93,-22,-47,-21,126,133,-23,-25,-27,-15,-67,-53,-53,-15,-59,-60,-91,-92,152,-49,-51,-52,-50,159,-20,-15,-46,-12,-13,-14,-57,-58,-61,-94,168,173,-96,-16,-17,-18,-19,-97,-54,-55,]),'LLAVEL':([44,48,86,93,131,132,141,175,178,],[74,78,119,123,147,148,123,123,123,]),'ELSE':([50,54,113,117,118,121,122,124,125,152,159,176,177,],[-24,-26,-23,-25,-27,141,141,-59,-60,-46,-61,178,178,]),'COMMA':([115,130,],[135,146,]),'RETURN':([147,],[164,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,],[1,]),'variable':([0,73,93,112,137,141,143,163,165,175,178,],[2,95,125,95,153,125,153,169,153,125,125,]),'while':([0,93,137,141,143,163,165,175,178,],[3,124,154,124,154,170,154,124,124,]),'expresionif':([0,137,143,163,165,],[4,155,155,171,155,]),'claseimplementacion':([0,],[5,]),'funcionclaseimpl':([0,101,],[6,128,]),'creacionobjeto':([0,],[7,]),'asignarvalorobjeto':([0,],[8,]),'usarfuncionobjeto':([0,],[9,]),'struct':([0,],[10,]),'numerotipo':([0,73,93,112,137,141,143,163,165,175,178,],[13,13,13,13,13,13,13,13,13,13,13,]),'tipo':([0,75,76,101,146,],[19,102,102,129,102,]),'expresion':([16,31,43,47,59,66,73,164,167,],[32,57,57,57,87,92,57,57,57,]),'statement':([16,31,43,47,73,164,167,],[33,56,72,77,94,172,72,]),'valor':([16,31,43,47,49,59,66,73,80,164,167,],[34,34,34,34,79,34,34,34,114,34,34,]),'comparador':([32,57,87,92,],[59,59,59,59,]),'boolean':([35,],[65,]),'condicionif':([43,167,],[70,174,]),'initcondicion':([43,167,],[71,71,]),'varblock':([43,78,167,],[73,112,73,]),'numero':([53,],[82,]),'bloqueclase':([74,],[101,]),'parametrosimplementacion':([75,76,146,],[103,110,161,]),'parametrosfuncion':([81,135,],[116,150,]),'conllaves':([93,141,175,178,],[121,156,176,156,]),'sinllaves':([93,141,175,178,],[122,157,177,157,]),'definicion':([101,],[127,]),'masparametrosfuncion':([115,],[134,]),'bodyblock':([119,123,147,148,],[137,143,163,165,]),'expresionpos':([121,122,],[138,142,]),'else':([121,122,176,177,],[139,139,179,180,]),'elseif':([121,122,],[140,140,]),'masparametrosimplementacion':([130,],[145,]),'funcionblock':([147,],[162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> variable','body',1,'p_body','sintactico.py',6),
  ('body -> while','body',1,'p_body','sintactico.py',7),
  ('body -> expresionif','body',1,'p_body','sintactico.py',8),
  ('body -> claseimplementacion','body',1,'p_body','sintactico.py',9),
  ('body -> funcionclaseimpl','body',1,'p_body','sintactico.py',10),
  ('body -> creacionobjeto','body',1,'p_body','sintactico.py',11),
  ('body -> asignarvalorobjeto','body',1,'p_body','sintactico.py',12),
  ('body -> usarfuncionobjeto','body',1,'p_body','sintactico.py',13),
  ('body -> struct','body',1,'p_body','sintactico.py',14),
  ('body -> <empty>','body',0,'p_body','sintactico.py',15),
  ('imprimir -> PRINT LPAR valor RPAR','imprimir',4,'p_impirmir','sintactico.py',18),
  ('bodyblock -> bodyblock variable','bodyblock',2,'p_bodyblock','sintactico.py',22),
  ('bodyblock -> bodyblock while','bodyblock',2,'p_bodyblock','sintactico.py',23),
  ('bodyblock -> bodyblock expresionif','bodyblock',2,'p_bodyblock','sintactico.py',24),
  ('bodyblock -> <empty>','bodyblock',0,'p_bodyblock','sintactico.py',25),
  ('funcionblock -> bodyblock variable','funcionblock',2,'p_funcionblock','sintactico.py',27),
  ('funcionblock -> bodyblock while','funcionblock',2,'p_funcionblock','sintactico.py',28),
  ('funcionblock -> bodyblock expresionif','funcionblock',2,'p_funcionblock','sintactico.py',29),
  ('funcionblock -> RETURN statement','funcionblock',2,'p_funcionblock','sintactico.py',30),
  ('funcionblock -> <empty>','funcionblock',0,'p_funcionblock','sintactico.py',31),
  ('varblock -> varblock variable','varblock',2,'p_varblock','sintactico.py',34),
  ('varblock -> <empty>','varblock',0,'p_varblock','sintactico.py',35),
  ('variable -> AUTO IDENTIFICADOR IGUAL valor PUNTOCOMA','variable',5,'p_variable','sintactico.py',37),
  ('variable -> AUTO IDENTIFICADOR PUNTOCOMA','variable',3,'p_variable','sintactico.py',38),
  ('variable -> numerotipo IDENTIFICADOR IGUAL numero PUNTOCOMA','variable',5,'p_variable_numero','sintactico.py',41),
  ('variable -> numerotipo IDENTIFICADOR PUNTOCOMA','variable',3,'p_variable_numero','sintactico.py',42),
  ('variable -> CHAR IDENTIFICADOR IGUAL CHARACTER PUNTOCOMA','variable',5,'p_variable_char','sintactico.py',45),
  ('numerotipo -> INT','numerotipo',1,'p_numero_tipo','sintactico.py',48),
  ('numerotipo -> FLOAT','numerotipo',1,'p_numero_tipo','sintactico.py',49),
  ('numerotipo -> LONG','numerotipo',1,'p_numero_tipo','sintactico.py',50),
  ('numero -> ENTERO','numero',1,'p_numero','sintactico.py',53),
  ('numero -> FLOTANTE','numero',1,'p_numero','sintactico.py',54),
  ('tipo -> INT','tipo',1,'p_tipo','sintactico.py',57),
  ('tipo -> FLOAT','tipo',1,'p_tipo','sintactico.py',58),
  ('tipo -> LONG','tipo',1,'p_tipo','sintactico.py',59),
  ('tipo -> AUTO','tipo',1,'p_tipo','sintactico.py',60),
  ('tipo -> CHAR','tipo',1,'p_tipo','sintactico.py',61),
  ('tipo -> VOID','tipo',1,'p_tipo','sintactico.py',62),
  ('valor -> ENTERO','valor',1,'p_valor','sintactico.py',65),
  ('valor -> FLOTANTE','valor',1,'p_valor','sintactico.py',66),
  ('valor -> CHARACTER','valor',1,'p_valor','sintactico.py',67),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',68),
  ('valor -> TRUE','valor',1,'p_valor','sintactico.py',69),
  ('valor -> FALSE','valor',1,'p_valor','sintactico.py',70),
  ('valor -> IDENTIFICADOR','valor',1,'p_valor','sintactico.py',71),
  ('while -> WHILE LPAR statement RPAR LLAVEL bodyblock LLAVER','while',7,'p_while','sintactico.py',76),
  ('expresion -> expresion comparador expresion','expresion',3,'p_expresion_comparacion','sintactico.py',80),
  ('struct -> STRUCT IDENTIFICADOR LLAVEL varblock LLAVER IDENTIFICADOR PUNTOCOMA','struct',7,'p_struct','sintactico.py',86),
  ('expresionif -> IF LPAR condicionif RPAR conllaves expresionpos','expresionif',6,'p_expresionif','sintactico.py',92),
  ('expresionif -> IF LPAR condicionif RPAR sinllaves expresionpos','expresionif',6,'p_expresionif','sintactico.py',93),
  ('expresionpos -> else','expresionpos',1,'p_expresionpos','sintactico.py',96),
  ('expresionpos -> elseif','expresionpos',1,'p_expresionpos','sintactico.py',97),
  ('expresionpos -> <empty>','expresionpos',0,'p_expresionpos','sintactico.py',98),
  ('elseif -> ELSE IF LPAR condicionif RPAR conllaves else','elseif',7,'p_elseif','sintactico.py',100),
  ('elseif -> ELSE IF LPAR condicionif RPAR sinllaves else','elseif',7,'p_elseif','sintactico.py',101),
  ('elseif -> <empty>','elseif',0,'p_elseif','sintactico.py',102),
  ('else -> ELSE conllaves','else',2,'p_else','sintactico.py',104),
  ('else -> ELSE sinllaves','else',2,'p_else','sintactico.py',105),
  ('sinllaves -> while','sinllaves',1,'p_sinLlaves','sintactico.py',107),
  ('sinllaves -> variable','sinllaves',1,'p_sinLlaves','sintactico.py',108),
  ('conllaves -> LLAVEL bodyblock LLAVER','conllaves',3,'p_conLlaves','sintactico.py',110),
  ('condicionif -> initcondicion','condicionif',1,'p_condicionif','sintactico.py',112),
  ('condicionif -> statement','condicionif',1,'p_condicionif','sintactico.py',113),
  ('initcondicion -> varblock statement','initcondicion',2,'p_initcondicion','sintactico.py',116),
  ('statement -> expresion','statement',1,'p_statement','sintactico.py',119),
  ('statement -> EXCLAMACION boolean','statement',2,'p_statement','sintactico.py',120),
  ('statement -> EXCLAMACION LPAR expresion RPAR','statement',4,'p_statement','sintactico.py',121),
  ('statement -> EXCLAMACION IDENTIFICADOR','statement',2,'p_statement','sintactico.py',122),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintactico.py',124),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintactico.py',125),
  ('expresion -> valor','expresion',1,'p_expresion','sintactico.py',128),
  ('comparador -> IGUAL IGUAL','comparador',2,'p_comparacion','sintactico.py',131),
  ('comparador -> MENOR','comparador',1,'p_comparacion','sintactico.py',132),
  ('comparador -> MAYOR','comparador',1,'p_comparacion','sintactico.py',133),
  ('comparador -> MENOR IGUAL','comparador',2,'p_comparacion','sintactico.py',134),
  ('comparador -> MAYOR IGUAL','comparador',2,'p_comparacion','sintactico.py',135),
  ('comparador -> EXCLAMACION IGUAL','comparador',2,'p_comparacion','sintactico.py',136),
  ('initfor -> tipo IDENTIFICADOR IGUAL valor','initfor',4,'p_initfor','sintactico.py',143),
  ('initfor -> IDENTIFICADOR comparador valor','initfor',3,'p_condfor','sintactico.py',146),
  ('loopfor -> asign','loopfor',1,'p_loopfor','sintactico.py',150),
  ('loopfor -> unaryexp','loopfor',1,'p_loopfor','sintactico.py',151),
  ('asign -> IDENTIFICADOR MAS valor','asign',3,'p_mathasign','sintactico.py',154),
  ('asign -> IDENTIFICADOR MENOS valor','asign',3,'p_mathasign','sintactico.py',155),
  ('asign -> IDENTIFICADOR ASTERISCO valor','asign',3,'p_mathasign','sintactico.py',156),
  ('asign -> IDENTIFICADOR SLASH valor','asign',3,'p_mathasign','sintactico.py',157),
  ('unaryexp -> IDENTIFICADOR MAS MAS','unaryexp',3,'p_unaryexp','sintactico.py',160),
  ('unaryexp -> IDENTIFICADOR MENOS MENOS','unaryexp',3,'p_unaryexp','sintactico.py',161),
  ('for -> FOR LPAR initfor PUNTOCOMA initfor PUNTOCOMA loopfor RPAR LLAVEL bodyblock LLAVER','for',11,'p_for','sintactico.py',164),
  ('array_declaration -> tipo IDENTIFICADOR CORCHETEL ENTERO CORCHETER PUNTOCOMA','array_declaration',6,'p_array','sintactico.py',169),
  ('claseimplementacion -> CLASS IDENTIFICADOR LLAVEL bloqueclase LLAVER','claseimplementacion',5,'p_claseimplementacion','sintactico.py',173),
  ('bloqueclase -> bloqueclase definicion','bloqueclase',2,'p_bloqueclase','sintactico.py',175),
  ('bloqueclase -> bloqueclase funcionclaseimpl','bloqueclase',2,'p_bloqueclase','sintactico.py',176),
  ('bloqueclase -> <empty>','bloqueclase',0,'p_bloqueclase','sintactico.py',177),
  ('definicion -> tipo IDENTIFICADOR PUNTOCOMA','definicion',3,'p_definicion','sintactico.py',179),
  ('definicion -> <empty>','definicion',0,'p_definicion','sintactico.py',180),
  ('funcionclaseimpl -> tipo IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL funcionblock LLAVER','funcionclaseimpl',8,'p_funcionclaseimpl','sintactico.py',183),
  ('funcionclaseimpl -> VOID IDENTIFICADOR LPAR parametrosimplementacion RPAR LLAVEL bodyblock LLAVER','funcionclaseimpl',8,'p_funcionclaseimpl','sintactico.py',184),
  ('funcionclaseimpl -> <empty>','funcionclaseimpl',0,'p_funcionclaseimpl','sintactico.py',185),
  ('parametrosimplementacion -> tipo IDENTIFICADOR masparametrosimplementacion','parametrosimplementacion',3,'p_parametrosimplementacion','sintactico.py',187),
  ('parametrosimplementacion -> <empty>','parametrosimplementacion',0,'p_parametrosimplementacion','sintactico.py',188),
  ('parametrosfuncion -> IDENTIFICADOR masparametrosfuncion','parametrosfuncion',2,'p_parametrosfuncion','sintactico.py',190),
  ('parametrosfuncion -> <empty>','parametrosfuncion',0,'p_parametrosfuncion','sintactico.py',191),
  ('masparametrosimplementacion -> COMMA parametrosimplementacion','masparametrosimplementacion',2,'p_masparametrosimplementacion','sintactico.py',193),
  ('masparametrosimplementacion -> <empty>','masparametrosimplementacion',0,'p_masparametrosimplementacion','sintactico.py',194),
  ('masparametrosfuncion -> COMMA parametrosfuncion','masparametrosfuncion',2,'p_masparametrosfuncion','sintactico.py',196),
  ('masparametrosfuncion -> <empty>','masparametrosfuncion',0,'p_masparametrosfuncion','sintactico.py',197),
  ('creacionobjeto -> IDENTIFICADOR IDENTIFICADOR PUNTOCOMA','creacionobjeto',3,'p_creacionobjeto','sintactico.py',199),
  ('asignarvalorobjeto -> IDENTIFICADOR PUNTO IDENTIFICADOR IGUAL valor','asignarvalorobjeto',5,'p_asignarvalores','sintactico.py',201),
  ('asignarvalorobjeto -> LPAR expresion RPAR','asignarvalorobjeto',3,'p_asignarvalores','sintactico.py',202),
  ('asignarvalorobjeto -> LPAR statement RPAR','asignarvalorobjeto',3,'p_asignarvalores','sintactico.py',203),
  ('asignarvalorobjeto -> EXCLAMACION LPAR statement RPAR','asignarvalorobjeto',4,'p_asignarvalores','sintactico.py',204),
  ('usarfuncionobjeto -> IDENTIFICADOR PUNTO IDENTIFICADOR LPAR parametrosfuncion RPAR PUNTOCOMA','usarfuncionobjeto',7,'p_usarfuncionesobjeto','sintactico.py',206),
]
