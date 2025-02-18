original_poem = open("original_poem.txt", "r")
original_poem_contents = original_poem.read()
original_poem.close()

new_poem = open("new_poem.txt", "w")
new_poem.write(original_poem_contents.replace("I", chr(int("1F61B", 16))))
new_poem.close()