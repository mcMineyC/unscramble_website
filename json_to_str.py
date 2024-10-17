import pyperclip, json

output_str = ''

for counter in range(2, 9):
    print(counter)
    file_obj = open('Misc_projects/unscramble/output_phrases_specific%s.json' % counter, 'r')
    all_phrases = json.load(file_obj)
    file_obj.close()

    for phrase in all_phrases:
        output_str = output_str + ' '.join(phrase) + '\n'
    output_str += '\n'


#pyperclip.copy(output_str)
#print(output_str)
file_obj = open('Misc_projects/unscramble/str_phrases.txt', 'w')
file_obj.write(output_str)
file_obj.close()