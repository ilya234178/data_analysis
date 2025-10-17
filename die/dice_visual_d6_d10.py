import plotly.express as px
from die import Die


#Создание кубика
die_1 = Die()
die_2 = Die(10)
#моделирование серии бросков
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#визуализация результатов
title = "Results of rolling d6 and d10 50,000 times"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#дальнейшая настройка диаграммы
fig.update_layout(xaxis_dtick=1)
fig.show()