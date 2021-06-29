
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASTERISCO AUTO BACKSLASH BOOL CHAR CHARACTER CIRCUNFLEJO CLASS COMADOBLE COMASIMPLE COMENTARIO COMMA CORCHETEL CORCHETER DOBLEPUNTO ELSE ENTERO EXCLAMACION FALSE FLOAT FLOTANTE FOR IDENTIFICADOR IF IGUAL INT INTERROGACION LLAVEL LLAVER LONG LPAR MAS MAYOR MENOR MENOS NEW NULLPOINTER NUMERAL PIPE PORCENTAJE PRIVATE PROTECTED PUBLIC PUNTERO PUNTO PUNTOCOMA RETURN RPAR SLASH STATIC STRING STRUCT THEN TRUE VIRGUILA VOID WHILEbody : variable\n            | while\n            | expresionif\n            | claseimplementacion\n            | bodyblock : bodyblock variable\n                    |  bodyblock while\n                    | expresionif\n                    | varblock : varblock variable\n                | variable : tipo IDENTIFICADOR IGUAL valor PUNTOCOMA\n                | tipo IDENTIFICADOR PUNTOCOMAtipo : INT \n            | FLOAT\n            | LONG\n            | AUTO\n            | CHAR\n            | VOIDvalor : ENTERO \n            | FLOTANTE\n            | CHARACTER\n            | STRING\n            | TRUE\n            | FALSE\n            | IDENTIFICADORwhile : WHILE LPAR statement RPAR LLAVEL bodyblock LLAVERexpresion : expresion comparador expresionexpresionif : IF LPAR condicionif RPAR conllaves expresionpos\n                    | IF LPAR condicionif RPAR sinllaves expresionpos\n                    expresionpos : else\n                    | elseif\n                    |  elseif : ELSE IF LPAR condicionif RPAR conllaves else\n                | ELSE IF LPAR condicionif RPAR sinllaves else\n                | else : ELSE conllaves\n            | ELSE sinllavessinllaves : while\n                | variableconllaves : LLAVEL bodyblock LLAVERcondicionif : initcondicion\n                | statementinitcondicion : varblock statementstatement : expresion\n                | EXCLAMACION boolean\n                | EXCLAMACION LPAR expresion RPAR\n                | EXCLAMACION IDENTIFICADORboolean : TRUE\n                | FALSEexpresion : valorcomparador : IGUAL IGUAL\n                | MENOR\n                | MAYOR\n                | MENOR IGUAL\n                | MAYOR IGUAL\n                | EXCLAMACION IGUAL claseimplementacion : CLASS IDENTIFICADOR LLAVEL bloqueclase LLAVER bloqueclase : definicion definicion\n                    | definicion : tipo IDENTIFICADOR PUNTOCOMA\n                    | '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,21,56,64,65,67,68,69,75,76,77,79,82,85,86,88,95,96,],[-5,0,-1,-2,-3,-4,-13,-12,-33,-33,-39,-40,-58,-29,-31,-32,-30,-27,-37,-38,-41,-34,-35,]),'WHILE':([0,21,50,56,57,64,65,66,67,68,72,73,75,76,77,78,79,80,82,83,84,85,86,88,91,94,95,96,],[7,-13,7,-12,-9,-33,-33,-9,-39,-40,7,-8,-29,-31,-32,7,-30,7,-27,-6,-7,-37,-38,-41,7,7,-34,-35,]),'IF':([0,57,66,78,],[8,8,8,87,]),'CLASS':([0,],[9,]),'INT':([0,18,21,36,37,50,52,54,56,57,64,65,66,67,68,72,73,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,94,95,96,],[10,-11,-13,10,10,10,-10,10,-12,-9,-33,-33,-9,-39,-40,10,-8,-29,-31,-32,10,-30,10,-61,-27,-6,-7,-37,-38,-41,-11,10,10,-34,-35,]),'FLOAT':([0,18,21,36,37,50,52,54,56,57,64,65,66,67,68,72,73,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,94,95,96,],[11,-11,-13,11,11,11,-10,11,-12,-9,-33,-33,-9,-39,-40,11,-8,-29,-31,-32,11,-30,11,-61,-27,-6,-7,-37,-38,-41,-11,11,11,-34,-35,]),'LONG':([0,18,21,36,37,50,52,54,56,57,64,65,66,67,68,72,73,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,94,95,96,],[12,-11,-13,12,12,12,-10,12,-12,-9,-33,-33,-9,-39,-40,12,-8,-29,-31,-32,12,-30,12,-61,-27,-6,-7,-37,-38,-41,-11,12,12,-34,-35,]),'AUTO':([0,18,21,36,37,50,52,54,56,57,64,65,66,67,68,72,73,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,94,95,96,],[13,-11,-13,13,13,13,-10,13,-12,-9,-33,-33,-9,-39,-40,13,-8,-29,-31,-32,13,-30,13,-61,-27,-6,-7,-37,-38,-41,-11,13,13,-34,-35,]),'CHAR':([0,18,21,36,37,50,52,54,56,57,64,65,66,67,68,72,73,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,94,95,96,],[14,-11,-13,14,14,14,-10,14,-12,-9,-33,-33,-9,-39,-40,14,-8,-29,-31,-32,14,-30,14,-61,-27,-6,-7,-37,-38,-41,-11,14,14,-34,-35,]),'VOID':([0,18,21,36,37,50,52,54,56,57,64,65,66,67,68,72,73,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,94,95,96,],[15,-11,-13,15,15,15,-10,15,-12,-9,-33,-33,-9,-39,-40,15,-8,-29,-31,-32,15,-30,15,-61,-27,-6,-7,-37,-38,-41,-11,15,15,-34,-35,]),'IDENTIFICADOR':([6,9,10,11,12,13,14,15,17,18,20,21,24,36,40,42,43,46,52,55,56,59,60,61,62,89,],[16,19,-14,-15,-16,-17,-18,-19,25,25,25,-13,47,25,25,-53,-54,25,-10,71,-12,-52,-55,-56,-57,25,]),'LPAR':([7,8,24,87,],[17,18,46,89,]),'IGUAL':([16,23,25,26,27,28,29,30,31,32,41,42,43,44,58,63,],[20,41,-26,-51,-20,-21,-22,-23,-24,-25,59,60,61,62,41,41,]),'PUNTOCOMA':([16,25,27,28,29,30,31,32,38,71,],[21,-26,-20,-21,-22,-23,-24,-25,56,81,]),'EXCLAMACION':([17,18,21,23,25,26,27,28,29,30,31,32,36,52,56,58,63,89,],[24,24,-13,44,-26,-51,-20,-21,-22,-23,-24,-25,24,-10,-12,44,44,24,]),'ENTERO':([17,18,20,21,36,40,42,43,46,52,56,59,60,61,62,89,],[27,27,27,-13,27,27,-53,-54,27,-10,-12,-52,-55,-56,-57,27,]),'FLOTANTE':([17,18,20,21,36,40,42,43,46,52,56,59,60,61,62,89,],[28,28,28,-13,28,28,-53,-54,28,-10,-12,-52,-55,-56,-57,28,]),'CHARACTER':([17,18,20,21,36,40,42,43,46,52,56,59,60,61,62,89,],[29,29,29,-13,29,29,-53,-54,29,-10,-12,-52,-55,-56,-57,29,]),'STRING':([17,18,20,21,36,40,42,43,46,52,56,59,60,61,62,89,],[30,30,30,-13,30,30,-53,-54,30,-10,-12,-52,-55,-56,-57,30,]),'TRUE':([17,18,20,21,24,36,40,42,43,46,52,56,59,60,61,62,89,],[31,31,31,-13,48,31,31,-53,-54,31,-10,-12,-52,-55,-56,-57,31,]),'FALSE':([17,18,20,21,24,36,40,42,43,46,52,56,59,60,61,62,89,],[32,32,32,-13,49,32,32,-53,-54,32,-10,-12,-52,-55,-56,-57,32,]),'LLAVEL':([19,39,50,78,91,94,],[37,57,66,66,66,66,]),'ELSE':([21,56,64,65,67,68,82,88,92,93,],[-13,-12,78,78,-39,-40,-27,-41,94,94,]),'LLAVER':([21,37,53,54,56,57,64,65,66,67,68,70,72,73,75,76,77,79,80,81,82,83,84,85,86,88,95,96,],[-13,-60,69,-62,-12,-9,-33,-33,-9,-39,-40,-59,82,-8,-29,-31,-32,-30,88,-61,-27,-6,-7,-37,-38,-41,-34,-35,]),'RPAR':([22,23,25,26,27,28,29,30,31,32,33,34,35,45,47,48,49,51,58,63,74,90,],[39,-45,-26,-51,-20,-21,-22,-23,-24,-25,50,-42,-43,-46,-48,-49,-50,-44,-28,74,-47,91,]),'MENOR':([23,25,26,27,28,29,30,31,32,58,63,],[42,-26,-51,-20,-21,-22,-23,-24,-25,42,42,]),'MAYOR':([23,25,26,27,28,29,30,31,32,58,63,],[43,-26,-51,-20,-21,-22,-23,-24,-25,43,43,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,],[1,]),'variable':([0,36,50,72,78,80,91,94,],[2,52,68,83,68,83,68,68,]),'while':([0,50,72,78,80,91,94,],[3,67,84,67,84,67,67,]),'expresionif':([0,57,66,],[4,73,73,]),'claseimplementacion':([0,],[5,]),'tipo':([0,36,37,50,54,72,78,80,91,94,],[6,6,55,6,55,6,6,6,6,6,]),'statement':([17,18,36,89,],[22,35,51,35,]),'expresion':([17,18,36,40,46,89,],[23,23,23,58,63,23,]),'valor':([17,18,20,36,40,46,89,],[26,26,38,26,26,26,26,]),'condicionif':([18,89,],[33,90,]),'initcondicion':([18,89,],[34,34,]),'varblock':([18,89,],[36,36,]),'comparador':([23,58,63,],[40,40,40,]),'boolean':([24,],[45,]),'bloqueclase':([37,],[53,]),'definicion':([37,54,],[54,70,]),'conllaves':([50,78,91,94,],[64,85,92,85,]),'sinllaves':([50,78,91,94,],[65,86,93,86,]),'bodyblock':([57,66,],[72,80,]),'expresionpos':([64,65,],[75,79,]),'else':([64,65,92,93,],[76,76,95,96,]),'elseif':([64,65,],[77,77,]),}

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
  ('body -> <empty>','body',0,'p_body','sintactico.py',10),
  ('bodyblock -> bodyblock variable','bodyblock',2,'p_bodyblock','sintactico.py',12),
  ('bodyblock -> bodyblock while','bodyblock',2,'p_bodyblock','sintactico.py',13),
  ('bodyblock -> expresionif','bodyblock',1,'p_bodyblock','sintactico.py',14),
  ('bodyblock -> <empty>','bodyblock',0,'p_bodyblock','sintactico.py',15),
  ('varblock -> varblock variable','varblock',2,'p_varblock','sintactico.py',17),
  ('varblock -> <empty>','varblock',0,'p_varblock','sintactico.py',18),
  ('variable -> tipo IDENTIFICADOR IGUAL valor PUNTOCOMA','variable',5,'p_variable','sintactico.py',20),
  ('variable -> tipo IDENTIFICADOR PUNTOCOMA','variable',3,'p_variable','sintactico.py',21),
  ('tipo -> INT','tipo',1,'p_tipo','sintactico.py',24),
  ('tipo -> FLOAT','tipo',1,'p_tipo','sintactico.py',25),
  ('tipo -> LONG','tipo',1,'p_tipo','sintactico.py',26),
  ('tipo -> AUTO','tipo',1,'p_tipo','sintactico.py',27),
  ('tipo -> CHAR','tipo',1,'p_tipo','sintactico.py',28),
  ('tipo -> VOID','tipo',1,'p_tipo','sintactico.py',29),
  ('valor -> ENTERO','valor',1,'p_valor','sintactico.py',32),
  ('valor -> FLOTANTE','valor',1,'p_valor','sintactico.py',33),
  ('valor -> CHARACTER','valor',1,'p_valor','sintactico.py',34),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',35),
  ('valor -> TRUE','valor',1,'p_valor','sintactico.py',36),
  ('valor -> FALSE','valor',1,'p_valor','sintactico.py',37),
  ('valor -> IDENTIFICADOR','valor',1,'p_valor','sintactico.py',38),
  ('while -> WHILE LPAR statement RPAR LLAVEL bodyblock LLAVER','while',7,'p_while','sintactico.py',42),
  ('expresion -> expresion comparador expresion','expresion',3,'p_expresion_comparacion','sintactico.py',46),
  ('expresionif -> IF LPAR condicionif RPAR conllaves expresionpos','expresionif',6,'p_expresionif','sintactico.py',53),
  ('expresionif -> IF LPAR condicionif RPAR sinllaves expresionpos','expresionif',6,'p_expresionif','sintactico.py',54),
  ('expresionpos -> else','expresionpos',1,'p_expresionpos','sintactico.py',57),
  ('expresionpos -> elseif','expresionpos',1,'p_expresionpos','sintactico.py',58),
  ('expresionpos -> <empty>','expresionpos',0,'p_expresionpos','sintactico.py',59),
  ('elseif -> ELSE IF LPAR condicionif RPAR conllaves else','elseif',7,'p_elseif','sintactico.py',61),
  ('elseif -> ELSE IF LPAR condicionif RPAR sinllaves else','elseif',7,'p_elseif','sintactico.py',62),
  ('elseif -> <empty>','elseif',0,'p_elseif','sintactico.py',63),
  ('else -> ELSE conllaves','else',2,'p_else','sintactico.py',65),
  ('else -> ELSE sinllaves','else',2,'p_else','sintactico.py',66),
  ('sinllaves -> while','sinllaves',1,'p_sinLlaves','sintactico.py',68),
  ('sinllaves -> variable','sinllaves',1,'p_sinLlaves','sintactico.py',69),
  ('conllaves -> LLAVEL bodyblock LLAVER','conllaves',3,'p_conLlaves','sintactico.py',71),
  ('condicionif -> initcondicion','condicionif',1,'p_condicionif','sintactico.py',73),
  ('condicionif -> statement','condicionif',1,'p_condicionif','sintactico.py',74),
  ('initcondicion -> varblock statement','initcondicion',2,'p_initcondicion','sintactico.py',77),
  ('statement -> expresion','statement',1,'p_statement','sintactico.py',79),
  ('statement -> EXCLAMACION boolean','statement',2,'p_statement','sintactico.py',80),
  ('statement -> EXCLAMACION LPAR expresion RPAR','statement',4,'p_statement','sintactico.py',81),
  ('statement -> EXCLAMACION IDENTIFICADOR','statement',2,'p_statement','sintactico.py',82),
  ('boolean -> TRUE','boolean',1,'p_boolean','sintactico.py',84),
  ('boolean -> FALSE','boolean',1,'p_boolean','sintactico.py',85),
  ('expresion -> valor','expresion',1,'p_expresion','sintactico.py',88),
  ('comparador -> IGUAL IGUAL','comparador',2,'p_comparacion','sintactico.py',91),
  ('comparador -> MENOR','comparador',1,'p_comparacion','sintactico.py',92),
  ('comparador -> MAYOR','comparador',1,'p_comparacion','sintactico.py',93),
  ('comparador -> MENOR IGUAL','comparador',2,'p_comparacion','sintactico.py',94),
  ('comparador -> MAYOR IGUAL','comparador',2,'p_comparacion','sintactico.py',95),
  ('comparador -> EXCLAMACION IGUAL','comparador',2,'p_comparacion','sintactico.py',96),
  ('claseimplementacion -> CLASS IDENTIFICADOR LLAVEL bloqueclase LLAVER','claseimplementacion',5,'p_claseimplementacion','sintactico.py',101),
  ('bloqueclase -> definicion definicion','bloqueclase',2,'p_bloqueclase','sintactico.py',103),
  ('bloqueclase -> <empty>','bloqueclase',0,'p_bloqueclase','sintactico.py',104),
  ('definicion -> tipo IDENTIFICADOR PUNTOCOMA','definicion',3,'p_definicion','sintactico.py',106),
  ('definicion -> <empty>','definicion',0,'p_definicion','sintactico.py',107),
]
