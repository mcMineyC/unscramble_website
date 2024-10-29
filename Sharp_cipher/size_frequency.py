#finds how likely a word is to have a certain amount of letters.
import re, json

myFile = open('./Sharp_cipher/long_text_sample.txt', 'r')
text = myFile.read()
myFile.close()

myFile = open('./Sharp_cipher/long_text_sample2.txt', 'r', encoding="utf8")
text2 = myFile.read()
myFile.close()

word_regex = re.compile(r"[\w']+")

output = []


for text_sample in (text, text2):

    all_words = word_regex.findall(text_sample)
    # count num of letters in each word and sort
    for word in all_words:
        output.append(len(word))


file_obj = open("./Sharp_cipher/frequency.json", "w")
json.dump(output, file_obj)
file_obj.close()