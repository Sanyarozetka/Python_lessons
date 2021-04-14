"""
Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов
несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""
s = "Tesla, Inc. is an American electric vehicle and clean energy company based in Palo Alto, California. Tesla's " \
    "current products include electric cars, battery energy storage from home to grid scale, solar panels and solar" \
    "roof tiles, as well as other related products and services. Tesla is ranked as the world's best-selling plug-in" \
    "and battery electric passenger car manufacturer, with a market share of 16% of the plug-in segment and 23% of" \
    "the battery electric segment 2020 sales. Through its subsidiary SolarCity, Tesla develops and" \
    "is a major installer of solar photovoltaic systems in the United States. Tesla is also one of the largest global" \
    "suppliers of battery energy storage systems, with 3 GWh of battery storage supplied in 2020. Founded in July" \
    "2003 by Martin Eberhard and Marc Tarpenning as Tesla Motors, the company's name is a tribute to inventor and" \
    "electrical engineer Nikola Tesla. Elon Musk, who contributed most of the funding in the early days, has served" \
    "as CEO since 2008. According to Musk, the purpose of Tesla is to help expedite the move to sustainable transport" \
    "and energy, obtained through electric vehicles and solar power. Tesla began production of their first car model," \
    "the Roadster, in 2009. This was followed by the Model S sedan in 2012, the Model X SUV in 2015, the higher" \
    "volume Model 3 sedan in 2017, and the Model Y crossover in 2020. The Model 3 is the world's all-time" \
    "best-selling plug-in electric car, with more than 800,000 delivered through December 2020." \
    "Tesla's global vehicle" \
    "sales were 499,550 units in 2020, a 35.8% increase over the previous year. In 2020, the company surpassed the" \
    "1 million mark of electric cars produced. Tesla has been the subject of numerous lawsuits and controversies" \
    "arising from statements and acts of CEO Elon Musk, allegations of whistleblower retaliation, alleged worker" \
    "rights violations, and allegedly unresolved and dangerous technical problems with their products."

s = s.lower()
s = s.replace(".", "")
s = s.replace(",", "")
s = s.replace("-", " ")
lst = s.split()
dic = {}
for word in lst:
    new_dic = {word: lst.count(word)}
    dic.update(new_dic)
# print(dic)
max_value = max(dic.values())
dic1 = {key: value for key, value in dic.items() if value == max_value}
if len(dic1) > 1:
    print(dic1[-1])
else:
    print(dic1)
