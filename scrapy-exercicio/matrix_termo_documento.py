import json
from builtins import print

import numpy as np
import re


def to_tokens(texto):
    tokens = re.findall(r'(\b\w+\b)+', texto)
    return [t.lower() for t in tokens]


lines = []
with open('./book_test.jl', 'r') as f:
    for line in f:
        lines.append(json.loads(line))

set_key_words = set()
for item in lines:
    set_token = set(to_tokens(item['descricao']))
    set_key_words = set_key_words.union(set_token)

print(len(set_key_words), len(lines))

matrix_i = {}

for i, key_word in enumerate(set_key_words):
    matrix_i[key_word] = []

# print(matrix_i)

for i, key_word in enumerate(set_key_words):
    for i, line in enumerate(lines):
        # print(key_word)
        # print(line)
        if key_word in to_tokens(line['descricao']):
            matrix_i[key_word].append(i)

print(matrix_i)
termo1 = set(matrix_i['now'])
termo2 = set(matrix_i['victims'])

print(termo1 & termo2)
