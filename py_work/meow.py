#script for CatTimes
#modified for test

stairs = ['thud', 'meow', 'thud', 'hiss']
def edit_story(words, func):
	for word in words:
		print(func(word))
edit_story(stairs, lambda word: word.capitalize() + '!')
