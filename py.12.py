import re
text = input("Enter a paragraph: ")
words = re.findall(r'\b\w+\b', text.lower())
word_freq = {}
for word in words:
 word_freq[word] = word_freq.get(word, 0) + 1
longest_word = max(words, key=len)
num_sentences = text.count('.') + text.count('!') + text.count('?')
print("\n--- Text Analysis ---")
print(f"Word Frequencies: {word_freq}")
print(f"Longest Word: {longest_word}")
print(f"Number of Sentences: {num_sentences}")