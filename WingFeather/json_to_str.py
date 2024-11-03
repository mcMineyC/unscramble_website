import pyperclip, json

output_str = ''

for counter in range(2, 9):
    print(counter)
    with open('Misc_projects/unscramble/output_phrases_specific%s.json' % counter, 'r') as file_obj:
        all_phrases = json.load(file_obj)

    for phrase in all_phrases:
        output_str = output_str + ' '.join(phrase) + '\n'
    output_str += '\n'


#pyperclip.copy(output_str)
#print(output_str)
with open('Misc_projects/unscramble/str_phrases.txt', 'w') as file_obj:
    file_obj.write(output_str)