import getpass
def read_data():
	# key_word = input("Provide key word: ") #visible input data
	key_word = getpass.getpass('Provide key word: ') #getpass module for hide input data
	return list(key_word) #return list of key word character for example word TEST ['T','E','S','T']
def check_char(key_word):
	bad_answers = 0 # bad answers counter
	life = 7 # how many tries left
	answer_characters = ['_' for i in range(len(key_word))] # create list with _ characters
	while key_word != answer_characters: # while true until you win or lose
		
		guess_char = input("Provide character which key word contain: ")
		good_answer = False # variable to correct count bad answers. Necessary FALSE state before you starting checking new character.
		for count, char in enumerate(key_word):
			if char == guess_char:
				answer_characters.pop(count)
				answer_characters.insert(count,guess_char)
				good_answer = True #If good answer then TRUE. Logic.
		if (good_answer == False):
			bad_answers+=1
			life-=1
			print('Its your {} bad answer. Left {} tries '.format(bad_answers, life))

			hangman = [
			'''
	___________
          |/      |
          |      (_)
          |      \|/
          |       |
          |      / |
          |
         _|___
         GAME OVER
		''',
		'''
	___________
          |/      |
          |      (_)
          |      \|/
          |       |
          |      / 
          |
         _|___
		''',
		'''
	___________
          |/      |
          |      (_)
          |      \|/
          |       |
          |      
          |
         _|___
		''',
		'''
	___________
          |/      |
          |      (_)
          |      \|/
          |       
          |      
          |
         _|___
		''',
		'''
	___________
          |/      |
          |      (_)
          |      \|
          |       
          |      
          |
         _|___
		''',
		'''
	___________
          |/      |
          |      (_)
          |       |
          |       
          |      
          |
         _|___
		''',
				''' 
	___________
          |/      |
          |      (_)
          |       
          |       
          |      
          |
         _|___
		'''
					]
			print(hangman[life])
		if life == 0:
			break	
		print(answer_characters)
					
if __name__ == "__main__":
	check_char(read_data())

