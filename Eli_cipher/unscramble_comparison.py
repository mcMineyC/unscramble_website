"""his file conpares the unscrambled text with the original text and
affirms that the letters in each word are the same."""

import re

with open("Eli_cipher/Eli_cipher2_cracked.txt", "r") as f:
    unscrambled_text = f.read().lower()

with open("Eli_cipher/Eli_cipher2.txt", "r") as f:
    original_text = f.read().lower()

output = ''
unmatched_words = 0

word_regex = re.compile(r"[\w\.,-]+")
unscrambled_words = word_regex.findall(unscrambled_text)
original_words = word_regex.findall(original_text)


for og_word, unscram_word in zip(original_words, unscrambled_words):
    if sorted(og_word) != sorted(unscram_word):
        output += f"Words do not match: {og_word} != {unscram_word}\n"
        unmatched_words += 1

with open("Eli_cipher/unscramble_comparison_output.txt", "w") as f:
    f.write(output)
print(f"Unmatched words: {unmatched_words}")