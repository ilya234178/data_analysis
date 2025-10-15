import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Новые блуждания создаются до тех пор, пока программа остается активной
while True:
    #Создание случайного блуждания
    rw = RandomWalk()
    rw.fill_walk()

    #нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)
    ax.set_aspect('equal')
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
