import tkinter as tk
import random


def move_button_smoothly():
    global target_x, target_y, animating
    # Если кнопка уже в нужной позиции, завершаем анимацию
    if abs(target_x - current_x[0]) < 2 and abs(target_y - current_y[0]) < 2:
        animating = False
        return
    # Вычисляем новые координаты для плавного перемещения
    current_x[0] += (target_x - current_x[0]) / 5
    current_y[0] += (target_y - current_y[0]) / 5
    button.place(x=int(current_x[0]), y=int(current_y[0]))
    # Продолжаем анимацию
    root.after(20, move_button_smoothly)


def move_button(event):
    global target_x, target_y, animating
    # Получаем размеры окна
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    # Выбираем новые случайные координаты внутри окна
    target_x = random.randint(0, window_width - 100)  # 100 - примерный размер кнопки
    target_y = random.randint(0, window_height - 50)  # 50 - примерный размер кнопки
    # Запускаем плавное перемещение, если оно ещё не идёт
    if not animating:
        animating = True
        move_button_smoothly()
# Создаем главное окно
root = tk.Tk()
root.title("Прыгающая кнопка")
root.geometry("400x300")
# Текущие и целевые координаты кнопки
current_x, current_y = [150], [100]  # Начальная позиция
target_x, target_y = 150, 100
animating = False
# Создаем кнопку
button = tk.Button(root, text="Поймай меня!")
button.place(x=150, y=100)
# Привязываем событие аводки мыши
button.bind("<Enter>", move_button)
# Запускаем главный цикл
root.mainloop()
