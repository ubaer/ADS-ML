import random
import numpy as np
import json
from random import randint

prefered_words = {'Pieter': ['work', 'first', 'chair', 'table', 'house', 'clock'],
                  'Anita': ['train', 'cable', 'stone', 'lamp', 'display', 'battery']}

# 100% preference rate = 10/10 words are from their preferences. 70% = 7/10 words are from their preferences
total_words = 10
preference_rate_percentage = 40

amount_prefered_words = int(total_words / 100
                            * preference_rate_percentage)


def create_prefered_words_string(name):
    words = []
    for i in range(int(amount_prefered_words)):
        random = randint(0, len(prefered_words.get(name)) - 1)
        words.append(prefered_words.get(name)[random])
    # print('Generated ' + str(amount_prefered_words) + ' amount of prefered words')
    return words


def create_random_words():
    words = []
    for i in range(int(total_words - amount_prefered_words)):
        random_person = randint(0, len(prefered_words) - 1)
        random_word = randint(0, len(list(prefered_words.keys())[random_person]) - 1)
        words.append(list(prefered_words.items())[random_person][1][random_word])
    # print('Generated ' + str(total_words - amount_prefered_words) + ' amount of random words')
    return words


def create_sentence(name):
    words = np.concatenate([create_prefered_words_string(name), create_random_words()])
    random.shuffle(words)  # Shuffle the data so the machine learning is not recognizing a pattern in order
    return [name, words.tolist()]

sentences = []

for i in range(50):
    sentences.append(create_sentence('Pieter'))

for i in range(50):
    sentences.append(create_sentence('Anita'))

with open('sentences_rate_'+str(preference_rate_percentage)+'.json', 'w') as f:
    json.dump(sentences, f)
