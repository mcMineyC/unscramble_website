import json, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print('Letter Unscrambler online\n')
word = input('Enter the letters you would like unscrambled: ')
if word == '': word = "KLNCUOHTDEITEHOCW"
print('unscrambling "' + word + '"')

start = int(time.time())

website = "https://www.wordunscrambler.net/"
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(website)
print('external website successfully opened:\n    ' + website + '\n    ' + driver.title)


print('entering "' + word + '" into website... (this may take two or three minutes)')
text_box = driver.find_element(By.ID, 'uw')
text_box.clear()
text_box.send_keys(word)
text_box.send_keys(Keys.RETURN)
#driver.execute_script("document.getElementById(\"uw\").value = \"%s\"" % (word)) # I (Jedi) tried a faster solution, it wasnt faster. wait maybe it is
#driver.execute_script("document.querySelector(\"input[type='submit']\").click()")

print('downloading word list elements from website...')
all_word_elements = driver.find_elements(By.CLASS_NAME, 'words')
print(str(len(all_word_elements)) + ' words found.')

print('processing word list elements...')
all_words = {} #sorts words by their length
for element in all_word_elements:
    string = str(element.get_attribute('innerHTML'))
    if not (' ' in string or string[0].isupper()):
        if len(string) in all_words:
            all_words[len(string)].append(string[0].upper() + string[1:]) #capitalizes 1st letter
        else:
            all_words[len(string)] = [string[0].upper() + string[1:]] #capitalizes 1st letter
    #else:
        #print('rejected "' + string + '"')

driver.quit()
print(website + ' closed')

end = int(time.time())


print('saving word list to file...')
with open("Misc_projects/unscramble/word_bank.json", "w") as file_obj:
    json.dump(all_words, file_obj)
#There ya go, now you can just open it in unscrambler2.py :)
# file_obj = open('word_save_bank.py', 'w')
# file_obj.write("all_words = \"" + pprint.pformat(all_words)+"\"")
# file_obj.close()

print("took %s minutes" % ((end-start)/60))
print('Done! To finish unscrambling your letters, now run unscrambler2.py')
print(all_words)