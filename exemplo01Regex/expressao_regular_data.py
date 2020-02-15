import re


def parse(texto):
    regex = r'^(\d{1,2})\/(\d{1,2})\/(\d{2}|\d{4})$'
    match = re.search(regex, texto)
    return (match[1], match[2], match[3])


test_cases = [
    ('01/01/2019',
     ('01', '01', '2019')),
    ('1/01/20',
     ('1', '01', '20'))

]

for (texto, resultado) in test_cases:
    assert parse(texto) == resultado, f'Erro {texto}'
print('Sucesso!')
