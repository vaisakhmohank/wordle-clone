import random
from english_words import english_words_lower_alpha_set as words_set

words = list(words_set)
word = random.choice(words)

while len(word) != 5:
    word =random.choice(words)

s = ['_','_','_','_','_']
life = 6
absent_letters = set()

u_word = input('Enter a five-letter word. \n').lower()
if u_word == word:
    print(f'You found the right word, {word.upper()}')
else:
    while u_word != word and life > 1:
        while u_word.isalpha() == False or len(u_word) != 5 or u_word not in words:
            if u_word.isalpha() == False:
                u_word = input('Your entry contains non-alphabets. Please enter a word containing alphabets only.\n').lower()
            elif len(u_word) < 5:
               u_word = input('The word you entered is too short. Please enter a 5-letter word.\n').lower()
            elif len(u_word) > 5:
                u_word = input('The word you entered is too long. Please enter a 5-letter word.\n').lower()
            elif u_word not in words:
                u_word = input(f'Sorry, {u_word} is not in out word-list. Please enter a different word\n').lower()

        life -= 1

        word_d = word
        for n in range(5):
            if u_word[n] == word_d[n]:
                s[n] = '$'
                word_d = word_d[:n] + ' ' + word_d[n+1:]
            elif u_word[n] not in word_d:
                s[n] = '_'
                absent_letters.add(u_word[n].upper())
            elif u_word[n] in word_d:
                for letter_numb in range(5):
                    if u_word[n] == word_d[letter_numb]:
                        if u_word.count(u_word[n]) == 1 and word_d.count(u_word[n]) == 1:
                            s[n] = '*'
                            word_d = word_d[:letter_numb] + ' ' + word_d[letter_numb+1:]
                        elif u_word.count(u_word[n]) == 1 and word_d.count(u_word[n]) == 2:
                            s[n] = '*'
                            word_d = word_d[:letter_numb] + ' ' + word_d[letter_numb+1:]
                        elif u_word.count(u_word[n]) == 2 and word_d.count(u_word[n]) == 1:
                            if u_word[n] in u_word[n+1:] and u_word[n] in word_d[n+1:] and u_word[n+1:].index(u_word[n]) == word_d[n+1:].index(u_word[n]):
                                s[n] = '_'
                            else:
                                s[n] = '*'
                                word_d = word_d[:letter_numb] + ' ' + word_d[letter_numb+1:]
                        elif u_word.count(u_word[n]) == 2 and word_d.count(u_word[n]) == 2:
                            s[n] = '*'
            #                word_d = word_d[:letter_numb] + ' ' + word_d[letter_numb+1:]
                        
        print(' '.join(u_word.upper()))
        print(' '.join(s))
        print(' ')
        print('Letters which are not present in the word: ',' '.join(sorted(absent_letters)))
        if life > 1:
            u_word = input(f'Enter another word. You have {life} attempts left.\n').lower()
        if life == 1:
            u_word = input(f'Enter another word. You have {life} attempt left.\n').lower()
    if u_word == word :
        print(f'Congrats! you found out the word - {word.upper()}')
    else:
        print(f'Better luck next time. The word is {word.upper()}')
