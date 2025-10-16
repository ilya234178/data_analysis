import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Новые блуждания создаются до тех пор, пока программа остается активной
while True:
    #Создание случайного блуждания
    rw = RandomWalk(100_000)
    rw.fill_walk()

    #нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    #ax.plot(rw.x_values, rw.y_values,c='red', linewidth = 1)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=1)
    ax.set_aspect('equal')

    #выделение первой и последней точек
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s= 100)

    #удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
