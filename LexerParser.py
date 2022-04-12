from ast import Num, Str
import argparse
import time
from xmlrpc.client import Boolean, boolean
import ply.lex as lex
import ply.yacc as yacc
import sys

class ClifLexer():

	# CONSTRUCTOR
	def __init__(self):
		# print('Lexer constructor called.')
		self.lexer = lex.lex(module=self)
		# start in the (standard) initial state
		self.lexer.begin('INITIAL')
		self.is_error = False

	# DESTRUCTOR
	def __del__(self):
		# print('Lexer destructor called.')
		pass

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
		self.is_error = True

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
		r'''\'([A-Za-z0-9 ]* | \?* | \$* | \&* | /* | "* | =* | ;* | \+* | :* | %*
			| (\[ | \])* | (\{ | \})* | ,* | \|* | (\\\')* | (\\")* | \.* | \_*
			| -*
			)*\'
			'''
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


class ClifParser(object):

	tokens = ClifLexer.tokens

	# CONSTRUCTOR
	def __init__(self):
		# print('Parser constructor called.')
		self.lexer = ClifLexer()
		self.parser = yacc.yacc(module=self)
		self.count = 0
		self.atomic = False
		self.boolean = False
		self.comment = False
		self.input_string = ''
		self.numOps = 0
		self.numNames = 0
		self.parse_fail = False

	# DESTRUCTOR
	def __del__(self):
		pass

	def p_starter(self, p):
		"""
		starter : sentences
		"""
		# print("Starting the parsing process.")
		pass
	
	def p_interpretedname(self, p):
		"""
		interpretedname : NUMERAL 
				| quotedstringrule
		"""
		#print("interpretedname")

	def p_quotedstringrule(self, p):
		"""
		quotedstringrule : QUOTEDSTRING
		"""
		self.numNames += 1

	def p_sentence(self, p):
		"""
		sentence : atomsent
				| commentsent
				| boolsent
		"""
		#print("sentence")
		# note that the rule above is INCORRECT: it is just an example of how to specify a rule
		# print("Found a sentence: {} {} {} ".format(p[2], p[3], p[4]))
		# if p[3] == p[4]:
		# 	no_quotedstrings = 1
		# else:
		# 	no_quotedstrings = 2

		# print("Number of distinct quoted strings: " + str(no_quotedstrings))

	def p_sentences(self, p):
		"""
		sentences : sentence 
				| sentence sentences
				| empty
		"""
		#print("sentences")

	def p_empty(self, p):
		"""
		empty : 
		"""
		#print("empty")

	def p_predicate(self, p):
		"""
		predicate : interpretedname
		"""
		#print("predicate")

	def p_termseq(self, p):
		# """
		# termseq : { interpretedname }
		# """
		'''
		termseq : interpretedname
				| interpretedname termseq
				| empty
		'''
		#print("termseq")

	def p_atomsent(self, p):
		"""
		atomsent : OPEN predicate termseq CLOSE
		"""
		self.boolean = False
		self.atomic = True
		self.comment = False
		#print("atomsent")

	def p_boolsent(self, p):
		"""
		boolsent : OPEN AND sentences CLOSE
				| OPEN OR sentences CLOSE 
				| OPEN IF sentence sentence CLOSE 
				| OPEN IFF sentence sentence CLOSE 
				| OPEN NOT sentence CLOSE 
		"""
		self.atomic = False
		self.boolean = True
		self.comment = False
		self.numOps += 1
		#print("boolsent")

	def p_commentsent(self, p):
		"""
		commentsent : OPEN CL_COMMENT QUOTEDSTRING sentence CLOSE
		"""
		self.comment = True
		self.atomic = False
		self.boolean = False

	def p_error(self, p):

		if p is None:
			raise TypeError("Unexpectedly reached end of file (EOF)")

		# Note the location of the error before trying to lookahead
		error_pos = p.lexpos

		# Reading the symbols from the Parser stack
		stack = [symbol for symbol in self.parser.symstack][1:]

		print("Parsing error; current stack: " + str(stack))
		self.parse_fail = True

	def parse(self, input_string):
		# initialize the parser
		self.input_string = input_string
		self.parser.parse(input_string)
	
	def parsePrint(self):
		nums = ": ops = " + str(self.numOps) + ", names = " + str(self.numNames)
		if not self.parse_fail and not self.lexer.is_error:
			if self.atomic:
				print("Atomic: " + self.input_string.strip('\n') + nums)
			elif self.boolean:
				print("Boolean: " + self.input_string.strip('\n') + nums)
			elif self.comment:
				print("Comment: " + self.input_string.strip('\n') + nums)
		elif self.parse_fail:
			print("There was a parsing error, not able to parse... meep moop ¯\_(ツ)_/¯")
		else:
			print("There was a lexing error, not able to parse... meep moop ¯\_(ツ)_/¯")

def str_to_bool(v):
	if isinstance(v, bool):
		return v
	if v.lower() in ('yes', 'true', 't', 'y', '1'):
		return True
	elif v.lower() in ('no', 'false', 'f', 'n', '0'):
		return False
	else:
		raise argparse.ArgumentTypeError('Boolean value expected.')


def __main__():

	arg_parse = argparse.ArgumentParser(description='Parsing and Lexing tool for Clif Language')
	arg_parse.add_argument('filename', metavar='Filename', type=str,
						help='a CLIF file')
	arg_parse.add_argument('lex_and_parse', metavar='Boolean', type=str_to_bool,
						nargs = '?', const=True, default=False,
						help='True: Lexing included, False: Just parsing')

	args = arg_parse.parse_args()

	filename = args.filename
	lex_and_parse = args.lex_and_parse
	sentences = []
	with open(filename, 'r') as inputfile:
		for line in inputfile:
			if len(line) > 1:
				sentences.append(line)
	
	print("Number of sentences:", int(len(sentences)))
	for sentence in sentences:
		sentence = sentence.strip("\n")
		parser = ClifParser()
		print("Sentence: " + sentence + "\n... Lexing...")
		if not lex_and_parse:
			parser.lexer.lex(sentence)
		else:
			parser.lexer.lex(sentence)
			print("...Parsing...")
			parser.parse(sentence)
			parser.parsePrint()
			print("")

__main__()