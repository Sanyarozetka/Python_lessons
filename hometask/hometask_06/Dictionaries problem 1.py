"""
В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом
тексте.
Задачу необходимо решить с использованием словаря.
"""
s = "Einstein excelled at math and physics from a young age, reaching a mathematical level years ahead of his peers."\
    "The 12 years old Einstein taught himself algebra and Euclidean geometry over a single summer. Einstein also "\
    "independently discovered his own original proof of the Pythagorean theorem at age 12. A family tutor Max Talmud "\
    "says that after he had given the 12 years old Einstein a geometry textbook, after a short time Einstein had" \
    "worked "\
    "through the whole book. He thereupon devoted himself to higher mathematics. Soon the flight of his mathematical "\
    "genius was so high I could not follow. His passion for geometry and algebra led the 12 years old to become "\
    "convinced that nature could be understood as a mathematical structure. Einstein started teaching himself calculus"\
    "at 12, and as a 14 years old he says he had mastered integral and differential calculus."

s = s.lower()
s = s.replace(".", "")
s = s.replace(",", "")
lst = s.split()
# print(lst)
dic = {}
for word in lst:
    new_dic = {word: lst.count(word)}
    dic.update(new_dic)
print(len(dic), dic)
