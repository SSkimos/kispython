import random

def parse_dictionary(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

dictionary = '''
V = Max | Sanya | Denis | Ivan | Eugeney
D = Smirnov | Ivanov | Sokolov | Popov
'''

for i in range(10):
    print(generate_phrase(parse_dictionary(dictionary), 'V'), generate_phrase(parse_dictionary(dictionary), 'D'))