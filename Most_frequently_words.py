# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    words = [each for each in words if each.count("'") != len(each)]
    word_counts = Counter(words)
    return [word[0] for word in word_counts.most_common(3)]

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))

'''import re
from collections import Counter

def top_words(text):
    # Replacing all non-alphanumeric characters with whitespace and converting to lower case
    clean_text = re.sub("[^a-zA-Z0-9']", " ", text).lower()

    # Splitting the text into words
    words = clean_text.split()

    # Counting the occurrences of each word
    word_counts = Counter(words)

    # Sorting the counts in descending order
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Extracting the top 3 words or all available words if there are fewer than 3
    top_words = [word_count[0] for word_count in sorted_counts[:3]]

    return top_words'''
