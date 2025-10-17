import plotly.express as px
from die import Die


#Создание кубика
die = Die()
#моделирование серии бросков
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Анализ результатов
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#визуализация результатов
title = "Results of rolling one d6 1000 times"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
