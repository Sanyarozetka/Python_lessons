import random

"""
 #1                 1   |    2
new_list = [expression for item in list]
 #2               1   |        2       |       3
new_list = [expression for item in list if conditional]
"""
# 1
lst = [round(random.uniform(1, 100), 2) for _ in range(15)]
print(lst)

lst0 = []
for _ in range(15):
    lst0.append(round(random.uniform(1, 100), 2))
print(lst0)

# 2
lst2 = [elem for elem in lst if elem > 20]
print(lst2)
