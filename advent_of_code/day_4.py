# --- Day 2: Corruption Checksum ---
import os
import utilities.utils as utils

def are_phrase_words_unique(phrase):
    num_words = len(phrase)
    for i in range(num_words):
        if phrase[i] in phrase[i+1:num_words]:
            return False
    return True


def does_phrase_contain_anagram(phrase):
    num_words = len(phrase)
    for i in range(num_words):
        for j in range(i + 1, num_words):
            if sorted(phrase[i]) == sorted(phrase[j]):
                return True
    return False

def total_valid_unique_phrases(phrases):
    total = 0
    for phrase in phrases:
        if are_phrase_words_unique(phrase):
            total += 1
    return total


def total_valid_anagram_phrases(phrases):
    total = 0
    for phrase in phrases:
        if not does_phrase_contain_anagram(phrase):
            total += 1
    return total


def main():
    phrases = utils.read_input_text(os.path.join("fixtures", "input_4.txt"), "txt")
    utils.pretty_print(4, total_valid_unique_phrases(phrases), 
                          total_valid_anagram_phrases(phrases))

if __name__ == "__main__":
    main()
