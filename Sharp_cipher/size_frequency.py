#finds how likely a word is to have a certain amount of letters.
import re, json

myFile = open('./Sharp_cipher/long_text_sample.txt', 'r')
text = myFile.read()
myFile.close()

word_regex = re.compile(r"[\w']+")


all_words = word_regex.findall(text)

output = []

#TODO count num of letters in each word and sort
for word in all_words:
    output.append(len(word))


file_obj = open("./Sharp_cipher/frequency.json", "w")
json.dump(output, file_obj)
file_obj.close()