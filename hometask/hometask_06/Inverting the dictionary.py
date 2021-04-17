"""
Дан словарь ключами которого являются английские слова, а значения - списки латинских слов. Необходимо развернуть
словарь. Другими словами, необходимо, на основании заданого словаря, создать новый словарь, у которого в качестве ключей
будут взяты латинские слова, из первого словаря, а значениями будут, соответствующие им, английские слова.

Исходный словарь:
d = {
    'apple': ['malum', 'pomum', 'popula'],

    'fruit': ['baca', 'bacca', 'popum'],

    'punishment': ['malum', 'multa']
}
"""

d = {'apple': ['malum', 'pomum', 'popula'], 'fruit': ['baca', 'bacca', 'popum'], 'punishment': ['malum', 'multa']}
rev_d = {}

for key in d:
    for value in d[key]:
        if value not in rev_d:
            rev_d[value] = [key]
        else:
            rev_d[value].append(key)
print(rev_d)
