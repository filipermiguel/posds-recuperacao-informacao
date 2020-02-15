import re


def parse(texto):
    regex = r'^(\d+)\.\s*([\w\s,.:;\-]+?)(?:\s+by\s+([\w\s]+?))?\s*\((\d+)\)$'
    match = re.search(regex, texto)
    return (match[1], match[2], match[3], match[4])


test_cases = [
    ('2. Pride and Projudice by Jane Austen (1302)',
     ('2', 'Pride and Projudice', 'Jane Austen', '1302')),
    ('5. Beowulf: An Anglo-Saxon Epic Poem (815)',
     ('5', 'Beowulf: An Anglo-Saxon Epic Poem', None, '815'))

]

for (texto, resultado) in test_cases:
    assert parse(texto) == resultado, f'Erro {texto}'
print('Sucesso!')
