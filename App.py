
special_chars = [':=', ';', '(', ')', '+', '-', '*', '/', '=', '<', '>', '<=', '>=']
reserved_words = ["if", "then", "else", "end", "repeat", "until", "read", "write"]

def	reserved_word_s(r_word):
	if r_word == 'if':
		return "IF"
	if r_word == 'then':
		return "THEN"
	if r_word == 'else':
		return "ELSE"
	if r_word == 'end':
		return "END"
	if r_word == 'repeat':
		return "REPEAT"
	if r_word == 'until':
		return "UNTIL"
	if r_word == 'read':
		return "READ"
	if r_word == 'write':
		return "WRITE"

def special_char_s(sp_char):
	if sp_char == ';':
		return "SEMICOLON"
	if sp_char == ':=':
		return "ASSIGN"
	if sp_char == '(':
		return "OPENBRACKET"
	if sp_char == ')':
		return "CLOSEDBRACKET"
	if sp_char == '+':
		return "PLUS"
	if sp_char == '-':
		return "MINUS"
	if sp_char == '*':
		return "MULT"
	if sp_char == '/':
		return "DIV"
	if sp_char == '=':
		return "EQUAL"
	if sp_char == '<':
		return "LESSTHAN"
	if sp_char == '>':
		return "GREATERTHAN"
	if sp_char == '<=':
		return "LESSTHANOREQUAL"
	if sp_char == '>=':
		return "GREATERTHANOREQUAL"


with open('input.txt', 'r') as inputF, open('output.txt', 'w') as outputF:
	
	output_list = []
	for line in inputF:
		in_comment = 0
		semicolon_after = 0
		# check if the line is empty; go to next line
		if line.isspace():
			continue
		# # scan the line letter by letter
		# for letter in line:
		# 	if letter.isspace():
		# 		continue
		words = line.strip().split()
		# print(words)
		for word in words:
			if word == '{':
				in_comment = 1
				continue
			elif word == '}':
				in_comment = 0
				continue
			elif in_comment == 1:
				continue
			
			if '{' in word:
				if word.index('{') == 0:
					in_comment = 1
					continue
				word = word[:word.index('{')]
				in_comment = 1
			
			elif '}' in word:
				if word.index('}') == len(word) - 1:
					in_comment = 0
					continue
				word = word[(word.index('}') + 1):]
				in_comment = 0
			
			if ';' in word:
				word = word[:word.index(';')]
				semicolon_after = 1
			
			if word in special_chars:
				type = special_char_s(word)
				output_list.append((word, type))
			
			elif word in reserved_words:
				type = reserved_word_s(word)
				output_list.append((word, "Reserved word: ", type))
			
			elif word.isnumeric():
				output_list.append((word,"NUMBER"))
			
			elif word.isalnum():
				output_list.append((word,"IDENTIFIER"))

			if semicolon_after == 1:
				output_list.append((';', "SEMICOLON"))
	# print(output_list)
	for t in output_list:
		# print(t[0],',', t[1])
		# outputF.write(f"{t[0]} , {t[1]}\n")
		for a in t:
			# method 1 (renove ':' from "Reserved word: " above)
			# # print(t.index(a), len(t), ' ', end='')
			# if t.index(a) == len(t) - 1:
			# 	print(a, end='')
			# 	outputF.write(a)
			# else:
			# 	print(a, ', ', end='')
			# 	outputF.write(a + ' , ')
			# method 2 (add ':' to "Reserved word " above)
			if t.index(a) == 0:
				print(a, ', ', end='')
				outputF.write(a + ' , ')
			else:
				print(a, end='')
				outputF.write(a)
		outputF.write('\n')
		print('\n', end='')

