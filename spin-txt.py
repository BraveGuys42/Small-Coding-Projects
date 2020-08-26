def spiral(word):
	for i in range(len(word)):
		final_word = word[len(word)-i:len(word)] + word[0:len(word)-i]
		output = ""
		for x in range(len(final_word)):
			output += final_word[x] + " "
		print(output)
