
def Palirdorm(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input('Please enter a word to check: ')
print(Palirdorm(word))
print('Your word backwards: ' + word[::-1])

# Or

# word = input('Write here: ')
# if word == word[::-1]:
#    print(True)
# else:
#    print(False)
    