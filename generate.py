#!/usr/bin/python3
import itertools

# Definir os blocos da expressão regular
block_1 = ['ccd', 'ccdcd']
block_2 = ['cd', 'cddc']

# Função para gerar cadeias com comprimento exato
def generate_chains_for_exact_length(block_1, block_2, target_length):
    max_blocks_part1 = target_length // min(len(b) for b in block_1)
    # Tentar diferentes comprimentos para a primeira parte (block_1)
    for len_part1 in range(max_blocks_part1 + 1):
        for part1_combination in itertools.product(block_1, repeat=len_part1):
            part1 = ''.join(part1_combination)
            remaining_len = target_length - len(part1)
            if remaining_len < 0:
                continue  # Se o comprimento ultrapassar o alvo, ignorar essa combinação
            elif remaining_len == 0:
                yield part1  # Se a primeira parte já atinge o comprimento exato
            else:
                # Gerar a segunda parte (block_2) com o comprimento restante
                max_blocks_part2 = remaining_len // min(len(b) for b in block_2)
                for len_part2 in range(max_blocks_part2 + 1):
                    for part2_combination in itertools.product(block_2, repeat=len_part2):
                        part2 = ''.join(part2_combination)
                        if len(part1 + part2) == target_length:
                            yield part1 + part2

# Função para gerar todas as cadeias de um tamanho específico
def generate_all_chains_for_exact_length(target_length):
    return generate_chains_for_exact_length(block_1, block_2, target_length)

list = [0, 1, 2, 3, 4, 5, 7, 13, 24, 20, 33, 37, 41, 50]

for n in list:
    target_length = n
    for chain in generate_all_chains_for_exact_length(target_length):
        print(chain)
