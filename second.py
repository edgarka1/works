import tkinter as tk
import random


def draw_abstract():
    # Генерируем случайные параметры для линий
    x1, y1 = random.randint(0, 800), random.randint(0, 800)
    x2, y2 = random.randint(0, 800), random.randint(0, 800)
    color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
    thickness = random.randint(1, 5)

    # Рисуем линию
    canvas.create_line(x1, y1, x2, y2, fill=color, width=thickness)

    # Запускаем анимацию рекурсивно
    root.after(50, draw_abstract)


# Создаем главное окно
root = tk.Tk()
root.title("Абстракция")
root.geometry("800x800")

# Создаем холст
canvas = tk.Canvas(root, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)

# Запускаем рисование
draw_abstract()

# Запускаем главный цикл
root.mainloop()
