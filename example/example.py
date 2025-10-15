import matplotlib.pyplot as plt
from matplotlib import colors

x1_values = range(1, 1001)
y1_values = [x ** 2 for x in x1_values]

x2_values = range(1, 5001)
y2_values = [x ** 3 for x in x2_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Нормализация значений цвета (иначе всё тусклое)
norm1 = colors.Normalize(vmin=min(y1_values), vmax=max(y1_values))
norm2 = colors.Normalize(vmin=min(y2_values), vmax=max(y2_values))

# Первая серия — ярко-синие точки
ax.scatter(x1_values, y1_values, c=y1_values, cmap=plt.cm.Blues, norm=norm1, s=10, label='x³ (1–1000)')

# Вторая серия — ярко-красные точки
ax.scatter(x2_values, y2_values, c=y2_values, cmap=plt.cm.Reds, norm=norm2, s=10, label='x³ (1–5000)')

ax.set_title("Сравнение двух кубических зависимостей", fontsize=14)
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y = X³", fontsize=12)
ax.legend()
ax.grid(True)

plt.show()
