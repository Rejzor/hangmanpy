import getpass
def read_data():
	# key_word = input("Provide key word: ") #visible input data
	key_word = getpass.getpass('Provide key word: ') #getpass module for hide input data
	return list(key_word) #return list of key word character for example word TEST ['T','E','S','T']
def guess_word():
	guess_char = input("Provide character which key word contain: ")
	return guess_char
def check_char(key_word,guess_char):
	answer_characters = ['_' for i in range(len(key_word))]
	# for char in key_word:
	for count, char in enumerate(key_word):
		if char == guess_char:
			answer_characters.pop(count)
			answer_characters.insert(count,guess_char)
	print(answer_characters)		

check_char(read_data(),guess_word())