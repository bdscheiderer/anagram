# Find Ana - a program to find anagrams
# Author = Bryan Scheiderer, Date = January 2018
#
# Word dictionary from http://wordlist.aspell.net/12dicts/
# From the 12dicts readme file:
#
#    Copyright 2000-2015 by Kevin Atkinson
#
#    Permission to use, copy, modify, distribute and sell these word
#    lists, the associated scripts, the output created from the scripts,
#    and its documentation for any purpose is hereby granted without fee,
#    provided that the above copyright notice appears in all copies and
#    that both that copyright notice and this permission notice appear in
#    supporting documentation. Kevin Atkinson makes no representations
#    about the suitability of this array for any purpose. It is provided
#    "as is" without express or implied warranty.

from collections import Counter

# load dictionary
# max length word in dict2of12.txt is 23 (electroencephalographic)
dictionary_file = 'dict2of12.txt'
with open(dictionary_file) as f:
    dictionary = f.read()
dictionary = dictionary.split()

def cls():
    # funtion to clear screen in terminal window
    print('\n' * 99)

def inputWord():
    # get scrambled word from user and error check
    print('''
\nWelcome to the Anagram Solver!
\nEnter a word or set of scrambled letters at the prompt,
and this program will find matching anagrams. The input word
must be at least 3 and not more than 23 letters in length, and
must contain only letters, not numbers or special charaters.''')
    error = '1'
    while error == '1':
        word = input('Enter the anagram --> ')
        if len(word) < 3:
            print('\nYour word is too short! Please try again.')
        elif len(word) > 23:
            print('\nYour word is too long! Please try again.')
        else:
            error = '0'
    word = ''.join(word.split())
    word = word.lower()
    print('\nYou entered the word: {}'.format(word))
    return word

def subsetDict(anagram):
    # subset dictionary to only words that equal the length of user's word
    L = len(anagram)
    subDict = []
    for word in dictionary:
        if len(word) == L:
            subDict.append(word)
    return subDict

def findAnagram(anagram, subDict):
    # ths function finds all the words in the dictionary that match the user's
    # input word; using the Counter function to generate a formula for the word
    formula = Counter(anagram)
    answers = []
    for word in subDict:
        c = Counter(word)
        if word == anagram:
            pass
        elif c == formula:
            answers.append(word)
    return answers

def printAnswers(answerList):
    # print the anagrams found in the dictionary
    if len(answerList) == 0:
        print('\nSorry, no possible answers were found.')
    else:
        print('\nThe following anagrams were found:')
        print(*answerList, sep=', ')

def main():
    again = 'y'
    while again.lower() not in ('n'):
        cls()
        anagram = inputWord()
        wordList = subsetDict(anagram)
        answerList = findAnagram(anagram, wordList)
        printAnswers(answerList)
        again = input('\nSolve another anagram? (Y/N) ')
    else:
        print('\nGoodbye\n')

if __name__ == '__main__':
    main()
