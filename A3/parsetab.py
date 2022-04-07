
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CLOSE CL_COMMENT IF IFF NOT NUMERAL OPEN OR QUOTEDSTRING RESERVEDELEMENT\n\t\tstarter : sentences\n\t\t\n\t\tinterpretedname : NUMERAL \n\t\t\t\t| QUOTEDSTRING\n\t\t\n\t\tsentence : atomsent\n\t\t\t\t| boolsent\n\t\t\n\t\tsentences : sentence \n\t\t\t\t| sentence sentences\n\t\t\t\t| empty\n\t\t\n\t\tempty : \n\t\t\n\t\tpredicate : interpretedname\n\t\t\n\t\ttermseq : interpretedname\n\t\t\t\t| interpretedname termseq\n\t\t\t\t| empty\n\t\t\n\t\tatomsent : OPEN predicate termseq CLOSE\n\t\t\t\t| empty\n\t\t\n\t\tboolsent : OPEN andOr sentences CLOSE \n\t\t\t\t| OPEN ifIff sentence sentence CLOSE \n\t\t\t\t| OPEN NOT sentence CLOSE \n\t\t\n\t\tandOr : AND \n\t\t\t\t| OR\n\t\t\n\t\tifIff : IF\n\t\t\t\t| IFF\n\t\t'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,27,29,31,32,],[-9,0,-1,-6,-8,-4,-5,-7,-14,-16,-18,-17,]),'OPEN':([0,3,4,5,6,10,11,12,14,15,16,17,24,25,27,29,31,32,],[7,7,-15,-4,-5,7,7,7,-19,-20,-21,-22,7,-15,-14,-16,-18,-17,]),'CLOSE':([3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,],[-6,-8,-4,-5,-7,-9,-9,-9,-9,-10,-19,-20,-21,-22,-2,-3,27,-9,-13,29,-9,-15,31,-14,-12,-16,32,-18,-17,]),'NOT':([7,],[12,]),'AND':([7,],[14,]),'OR':([7,],[15,]),'IF':([7,],[16,]),'IFF':([7,],[17,]),'NUMERAL':([7,9,13,18,19,21,],[18,18,-10,-2,-3,18,]),'QUOTEDSTRING':([7,9,13,18,19,21,],[19,19,-10,-2,-3,19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'starter':([0,],[1,]),'sentences':([0,3,10,],[2,8,23,]),'sentence':([0,3,10,11,12,24,],[3,3,3,24,26,30,]),'empty':([0,3,9,10,11,12,21,24,],[4,4,22,4,25,25,22,25,]),'atomsent':([0,3,10,11,12,24,],[5,5,5,5,5,5,]),'boolsent':([0,3,10,11,12,24,],[6,6,6,6,6,6,]),'predicate':([7,],[9,]),'andOr':([7,],[10,]),'ifIff':([7,],[11,]),'interpretedname':([7,9,21,],[13,21,21,]),'termseq':([9,21,],[20,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> starter","S'",1,None,None,None),
  ('starter -> sentences','starter',1,'p_starter','a3-parser-provided.py',97),
  ('interpretedname -> NUMERAL','interpretedname',1,'p_interpretedname','a3-parser-provided.py',104),
  ('interpretedname -> QUOTEDSTRING','interpretedname',1,'p_interpretedname','a3-parser-provided.py',105),
  ('sentence -> atomsent','sentence',1,'p_sentence','a3-parser-provided.py',110),
  ('sentence -> boolsent','sentence',1,'p_sentence','a3-parser-provided.py',111),
  ('sentences -> sentence','sentences',1,'p_sentences','a3-parser-provided.py',124),
  ('sentences -> sentence sentences','sentences',2,'p_sentences','a3-parser-provided.py',125),
  ('sentences -> empty','sentences',1,'p_sentences','a3-parser-provided.py',126),
  ('empty -> <empty>','empty',0,'p_empty','a3-parser-provided.py',131),
  ('predicate -> interpretedname','predicate',1,'p_predicate','a3-parser-provided.py',136),
  ('termseq -> interpretedname','termseq',1,'p_termseq','a3-parser-provided.py',141),
  ('termseq -> interpretedname termseq','termseq',2,'p_termseq','a3-parser-provided.py',142),
  ('termseq -> empty','termseq',1,'p_termseq','a3-parser-provided.py',143),
  ('atomsent -> OPEN predicate termseq CLOSE','atomsent',4,'p_atomsent','a3-parser-provided.py',151),
  ('atomsent -> empty','atomsent',1,'p_atomsent','a3-parser-provided.py',152),
  ('boolsent -> OPEN andOr sentences CLOSE','boolsent',4,'p_boolsent','a3-parser-provided.py',157),
  ('boolsent -> OPEN ifIff sentence sentence CLOSE','boolsent',5,'p_boolsent','a3-parser-provided.py',158),
  ('boolsent -> OPEN NOT sentence CLOSE','boolsent',4,'p_boolsent','a3-parser-provided.py',159),
  ('andOr -> AND','andOr',1,'p_andOr','a3-parser-provided.py',164),
  ('andOr -> OR','andOr',1,'p_andOr','a3-parser-provided.py',165),
  ('ifIff -> IF','ifIff',1,'p_ifIff','a3-parser-provided.py',170),
  ('ifIff -> IFF','ifIff',1,'p_ifIff','a3-parser-provided.py',171),
]
