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

d = {'apple': ['malum', 'pomum', 'popula'],
     'fruit': ['baca', 'bacca', 'popum'],
     'punishment': ['malum', 'multa']}
rev_d = {}

for key, value in d.items():
    rev_d1 = d.fromkeys(value, key)
    rev_d.update(rev_d1)
print(rev_d)
