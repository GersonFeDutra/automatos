#!/usr/bin/python3
import itertools
import random

# Definir o alfabeto
alphabet = ['c', 'd']

# Função para verificar se uma string pertence à linguagem
def belongs_to_language(string):
    block_1 = ['ccd', 'ccdcd']
    block_2 = ['cd', 'cddc']

    # Divida a string em partes com base no comprimento dos blocos
    for i in range(1, len(string)):
        part1 = string[:i]
        part2 = string[i:]
        
        # Verifica se part1 é uma combinação de blocos válidos de block_1
        valid_part1 = all(part1[j:j+len(b)] == b for b in block_1 for j in range(0, len(part1), len(b)))
        
        # Verifica se part2 é uma combinação de blocos válidos de block_2
        valid_part2 = all(part2[j:j+len(b)] == b for b in block_2 for j in range(0, len(part2), len(b)))
        
        if valid_part1 and valid_part2:
            return True
    return False

# Função para gerar uma string aleatória de comprimento específico
def generate_random_string(length):
    return ''.join(random.choice(alphabet) for _ in range(length))

# Função para gerar strings que NÃO pertencem à linguagem
def generate_non_language_strings(target_length, num_strings=10):
    non_language_strings = []
    while len(non_language_strings) < num_strings:
        random_string = generate_random_string(target_length)
        if not belongs_to_language(random_string):
            non_language_strings.append(random_string)
    return non_language_strings

list = [1, 2, 3, 4, 5, 7, 13, 23, 30, 33, 37, 41, 49, 50]

for n in list:
    target_length = n
    non_language_strings = generate_non_language_strings(target_length, 10)

    for string in non_language_strings:
        print(string)
