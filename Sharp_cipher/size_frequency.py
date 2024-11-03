#finds how likely a word is to have a certain amount of letters.
import re, json

with open('./Sharp_cipher/long_text_sample.txt', 'r') as myFile:
    text = myFile.read()

with open('./Sharp_cipher/long_text_sample2.txt', 'r', encoding="utf8") as myFile:
    text2 = myFile.read()

word_regex = re.compile(r"[\w']+")

output = []


for text_sample in (text, text2):

    all_words = word_regex.findall(text_sample)
    # count num of letters in each word and sort
    for word in all_words:
        output.append(len(word))


with open("./Sharp_cipher/frequency.json", "w") as file_obj:
    json.dump(output, file_obj)