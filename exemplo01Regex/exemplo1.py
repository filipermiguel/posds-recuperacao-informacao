import re

#dir(re)

texto = "2. Pride and Projudice by Jane Austen (1302)"
# #r para validar que é regex
# m = re.search(r'(\d)\.\s([\w\s]+)\sby\s([\w\s]+)\((\d+)\)', texto)
# print(m)
#
# #m.group(1)
# print(m[0])
# print(m[1])
# print(m[2])
# print(m[3])
# print(m[4])


# m = re.search(r'(?P<pos>\d)\.\s([\w\s]+)\sby\s([\w\s]+)\((\d+)\)', texto)
# print(m)
# print(m.group('pos'))
# # <re.Match object; span=(0, 44), match='2. Pride and Projudice by Jane Austen (1302)'>
# # 2

texto = "5. Beowulf: An Anglo-Saxon Epic Poem (815)"

m = re.search(r'^(?P<pos>\d+)\.\s*([\w\s,.:;\-]+?)\s+by\s+([\w\s]+?)\s*\((\d+)\)$', texto)
print(m.group(1))
print(m.group(2))