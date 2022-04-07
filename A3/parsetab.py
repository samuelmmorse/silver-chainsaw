
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CLOSE CL_COMMENT IF IFF NOT NUMERAL OPEN OR QUOTEDSTRING RESERVEDELEMENT\n\t\tinterpretedname : NUMERAL \n\t\t\t\t| QUOTEDSTRING\n\t\t\n\t\tsentence : atomsent\n\t\t\t\t| boolsent\n\t\t\n\t\tpredicate : interpretedname\n\t\t\n\t\ttermseq : interpretedname\n\t\t\t\t| interpretedname termseq\n\t\t\n\t\tatomsent : OPEN predicate termseq CLOSE\n\t\t\n\t\tandOr : AND \n\t\t\t\t| OR\n\t\t\n\t\tifIff : IF\n\t\t\t\t| IFF\n\t\t\n\t\toneOrMoreSentences : sentence\n\t\t\t\t| sentence oneOrMoreSentences\n\t\t\n\t\tboolsent : OPEN andOr oneOrMoreSentences CLOSE \n\t\t\t\t| OPEN ifIff sentence sentence CLOSE \n\t\t\t\t| OPEN NOT sentence CLOSE \n\t\t'
    
_lr_action_items = {'NUMERAL':([0,],[2,]),'QUOTEDSTRING':([0,],[3,]),'$end':([1,2,3,],[0,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'interpretedname':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> interpretedname","S'",1,None,None,None),
  ('interpretedname -> NUMERAL','interpretedname',1,'p_starter','a3-parser-provided.py',97),
  ('interpretedname -> QUOTEDSTRING','interpretedname',1,'p_starter','a3-parser-provided.py',98),
  ('sentence -> atomsent','sentence',1,'p_sentence','a3-parser-provided.py',105),
  ('sentence -> boolsent','sentence',1,'p_sentence','a3-parser-provided.py',106),
  ('predicate -> interpretedname','predicate',1,'p_predicate','a3-parser-provided.py',119),
  ('termseq -> interpretedname','termseq',1,'p_termseq','a3-parser-provided.py',124),
  ('termseq -> interpretedname termseq','termseq',2,'p_termseq','a3-parser-provided.py',125),
  ('atomsent -> OPEN predicate termseq CLOSE','atomsent',4,'p_atomsent','a3-parser-provided.py',134),
  ('andOr -> AND','andOr',1,'p_andOr','a3-parser-provided.py',139),
  ('andOr -> OR','andOr',1,'p_andOr','a3-parser-provided.py',140),
  ('ifIff -> IF','ifIff',1,'p_ifIff','a3-parser-provided.py',145),
  ('ifIff -> IFF','ifIff',1,'p_ifIff','a3-parser-provided.py',146),
  ('oneOrMoreSentences -> sentence','oneOrMoreSentences',1,'p_oneOrMoreSentences','a3-parser-provided.py',151),
  ('oneOrMoreSentences -> sentence oneOrMoreSentences','oneOrMoreSentences',2,'p_oneOrMoreSentences','a3-parser-provided.py',152),
  ('boolsent -> OPEN andOr oneOrMoreSentences CLOSE','boolsent',4,'p_boolsent','a3-parser-provided.py',157),
  ('boolsent -> OPEN ifIff sentence sentence CLOSE','boolsent',5,'p_boolsent','a3-parser-provided.py',158),
  ('boolsent -> OPEN NOT sentence CLOSE','boolsent',4,'p_boolsent','a3-parser-provided.py',159),
]
