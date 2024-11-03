#variable names and usage is very sloppy...

import itertools, json, copy

with open('Misc_projects/unscramble/word_bank.json', 'r') as file_obj:
    all_words = json.load(file_obj)

letters = []
for _ in 'KLNCUOHTDEITEHOCW': letters.append(_)
letters = tuple(letters) #ensure that letters are upper case
len_letters = len(letters)
phrase = None
phrases_found = []


#tests if word can be spelled with the provided letters
def word_fits(wfWord, wfLetters): #TODO this func may glitch if the word has more letters than wfLetters does. Fixed already?
    if len(wfLetters) < len(wfWord):
        return False
    wfLetters = copy.deepcopy(wfLetters) #buggy?
    for wfLetter in wfWord:
        try:
            wfLetters.remove(wfLetter.upper())
        except ValueError:
            return False
    return True


def find_remaining_letters(frlPhrase):
    global letters, len_letters
    frlLettersRemaining = list(letters)
    for out in frlPhrase:
        try:
            frlLettersRemaining.remove(out.upper())
        except ValueError:
            raise Exception(frlPhrase, len(frlPhrase))
    return frlLettersRemaining


def loop_thingy(maxWordLen):
    global letters, phrase, phrases_found
    lettersLeft = find_remaining_letters(''.join(phrase))
    for letCnt in all_words:
        if int(letCnt) <= maxWordLen and int(letCnt) <= len(lettersLeft): #prevents unecessary repetition since bigger words were not already caught
            for possibleWord in all_words[letCnt]:

                if word_fits(possibleWord, lettersLeft):
                    phrase.append(possibleWord)
                    if len(''.join(phrase)) == len_letters and set(phrase) not in phrases_found: #if a phrase is found then:
                        phrases_found.append(set(phrase))
                        #print('Phrase found! "%s"' % str(phrase))
                    else:
                        loop_thingy(int(letCnt))
                    del phrase[-1]

num_of_words = 0
for letter_count in all_words:
    for prime_word in all_words[letter_count]:
        num_of_words += 1

#main code loops:

#finds all possible words and phrases that can be created with the given letters
def find_all(): #TODO may have some local/global variable issues
    global all_words, phrases_found, phrase, num_of_words, len_letters

    counter = 0
    all_words_copy = copy.deepcopy(all_words)

    for letter_count in all_words_copy:
        phrases_found = []
        for prime_word in all_words_copy[letter_count]:
            counter += 1
            print('processing word %s of %s: "%s"' % (counter, num_of_words, prime_word))

            phrase = [prime_word] #attempt at creating a phrase
            if len(prime_word) == len_letters:#if single word matches:
                phrases_found.append(set(phrase))
                #print('Word found! "%s"' % str(phrase))
            else:
                loop_thingy(len(prime_word))
            all_words[letter_count].remove(prime_word)

        #save copy each pass
        print('saving phrase list to file...')
        output = []
        for item in phrases_found: output.append(list(item))
        with open("Misc_projects/unscramble/output_phrases%s.json" % letter_count, "w") as file_obj:
            json.dump(output, file_obj)


#accepts specific word, and searches for all phrases that contain that word. This func is a slightly modded version of find_all
def find_specific(fsDesiredWord):
    global all_words, phrases_found, phrase, num_of_words, len_letters

    counter = 0
    fsLenDesired = len(fsDesiredWord)
    #all_words[str(fsLenDesired)].remove(fsDesiredWord)
    all_words_copy = copy.deepcopy(all_words)

    for letter_count in all_words_copy:
        phrases_found = []
        for prime_word in all_words_copy[letter_count]:
            counter += 1
            print('processing word %s of %s: "%s"' % (counter, num_of_words, prime_word))

            phrase = [fsDesiredWord, prime_word] #attempt at creating a phrase
            if fsLenDesired + len(prime_word) == len_letters:#if two words match:
                phrases_found.append(set(phrase))
            else:
                loop_thingy(fsLenDesired + len(prime_word))
            all_words[letter_count].remove(prime_word)

        #save
        print('saving phrase list (%s) to file...' % letter_count)
        output = []
        for item in phrases_found: output.append(list(item))
        with open("Misc_projects/unscramble/output_phrases_specific%s.json" % letter_count, "w") as file_obj:
            json.dump(output, file_obj)




find_specific('Unlock')