#!/usr/bin/python3
import itertools

# Definir os blocos da expressão regular
block_1 = ['ccd', 'ccdcd']
block_2 = ['cd', 'cddc']

# Função para gerar todas as combinações válidas de uma lista de blocos
def generate_chains(blocks, max_len):
    for length in range(0, max_len + 1):
        for combination in itertools.product(blocks, repeat=length):
            chain = ''.join(combination)
            if len(chain) <= max_len:
                yield chain

# Gerar cadeias para a expressão (ccd U ccdcd)*
def generate_part1(max_len):
    yield from generate_chains(block_1, max_len)

# Gerar cadeias para a expressão (cd U cddc)*
def generate_part2(max_len):
    yield from generate_chains(block_2, max_len)

# Combina as duas partes gerando todas as cadeias válidas
def generate_all_chains(max_len=50):
    for part1 in generate_part1(max_len):
        remaining_len = max_len - len(part1)
        for part2 in generate_part2(remaining_len):
            yield part1 + part2

# Imprime todas as cadeias geradas até 50 caracteres
for chain in generate_all_chains(50):
    print(chain)
