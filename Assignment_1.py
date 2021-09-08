def countOccurrences(verse, word):
  
    wordslist = list(verse.split())
    return wordslist.count(word)
verse = "If you can keep your head when all about you\n Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,And yet don’t look too good, nor talk too wise"
print(verse)

print('\v')
print('\v')

print("----- Verse Analysis Program! ------")

print('\v')

print("The length of the verse is: " , len(verse))
print("True or false. The  13th character is uppercase: " , 'verse[12]'.isupper())

result = verse.find('and')
res = verse.rfind('And')
print("The index of first occurance of word 'and' is:" , result)
print("The index of last occurance of the word 'And' is: " + str(res))


print("The word 'you' appears this number of times: " ,verse.count("you"))

print("The word 'mike' appears this number of times: " , verse.count("mike"))

print("The text between the first and last occurrences of “and” is: ")
start = verse.find('and') + 3
end = verse.find('And', start)
verse[start:end]

