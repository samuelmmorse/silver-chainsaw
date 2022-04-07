import ply.lex as lex

class ClifLexer():

	# CONSTRUCTOR
	def __init__(self):
		print('Lexer constructor called.')
		self.lexer = lex.lex(module=self)
		# start in the (standard) initial state
		self.lexer.begin('INITIAL')

	# DESTRUCTOR
	def __del__(self):
		print('Lexer destructor called.')

	reserved_bool = {
		'and': 'AND',
		'or': 'OR',
		'not': 'NOT'
	}

	reserved_element = {
		'iff': 'IFF',
		'if': 'IF',
		'cl:comment' : 'CL_COMMENT',
	}

	tokens = ['OPEN', 'CLOSE', 'QUOTEDSTRING', 'RESERVEDELEMENT', 'NUMERAL']

	tokens += reserved_bool.values()
	tokens += reserved_element.values()

	t_ignore = ' \t\r\n\f\v'

	def t_NEWLINE(self,t):
		r'\n+'
		t.lexer.lineno += len(t.value)

	def t_error(self,t):
		print("Lexing error: Unknown character \"{}\" at line {}".format(t.value[0], t.lexer.lineno))
		t.lexer.skip(1)

	# token specification as a string (no regular expression)

	t_OPEN= '\('
	t_CLOSE= '\)'

	def t_RESERVEDELEMENT(self, t):
		# here we use a regular expression to say what matches this particular token:
		# any sequence of standard characters of length 1 or greater
		# but this does not yet cover all reservedelements
		r'[A-Za-z]+ ([A-Za-z]|:)*'
		if t.value in self.reserved_bool:
			t.type = self.reserved_bool[t.value]
			#print("Boolean reserved word: " + t.value)
			return t
		elif t.value in self.reserved_element:
			t.type = self.reserved_element[t.value]
			return t
		else:
			pass

	def t_QUOTEDSTRING(self, t):
		r'\'(\w*|\?*|\$*|/*|"*|=*|;*|\+*|:*|%*|\[*|\]*|,*)*\''
		return t
	
	def t_NUMERAL(self, t):
		r'\d+'
		return t

	def lex(self, input_string):
		self.lexer.input(input_string)
		while True:
			tok = self.lexer.token()
			if not tok:
				break
			print(tok)


lex = ClifLexer()
s = "(and ('max' 1 2 15) (or  ('Func' 'D')))"
print('Lexing '+s)
lex.lex(s)

s = "(and ('B' 'C') (or ('C' 'D'))))"
print('\nLexing '+s)
lex.lex(s)

s = "('who' ('is' '?') )"
print('\nLexing '+s)
lex.lex(s)

s = "(or (not ('TODAY=03/26/22')) \
(not ('TODAY=03/26/22')) (and 'FIRDAY' 13)) \
(and (0))(and (0 1 2 3 4 'more;'))(if (not 'True') \
(and (0 '=' 1) (0 '=' 2) (not 'FalseStatement3'))) \
(100 ('and' (1000) (1001) ('1001+')))"
print('\nLexing '+s)
lex.lex(s)

s = "('FuncA' 'a' 100 25) \
(and (('B' 'C') (or ('C' 'D'))) (or ('FuncB') ('Func' 100 'A') ('something')))\
('cl:comment' 'B100%') \n\
(cl:comment 'COMMENT:B100%')\
(iff (and ('B_100' 'B_101' '$100')) ('[TODAY]' '[4,5,6]' '[3+4]')) "
print('\nLexing '+s)
lex.lex(s)

