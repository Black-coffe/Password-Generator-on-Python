# PASSWORD GENERATOR
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import os

# Функция для генерации пароля
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Функция, которая будет вызываться при нажатии кнопки генерации
def on_generate_clicked():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Ошибка", "Введите положительное число символов.")
            return
        password = generate_password(length)
        password_entry.config(state=tk.NORMAL)  # Снимаем ограничение для редактирования
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state=tk.READONLY)  # Возвращаем ограничение после вставки
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число.")

# Функция для копирования пароля в буфер обмена
def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Успех", "Пароль скопирован в буфер обмена.")

# Функция для сохранения пароля в txt файл
def save_to_file():
    password = password_entry.get()
    file_path = os.path.join(os.getcwd(), 'password.txt')  # Сохраняем в текущей директории
    with open(file_path, 'w') as file:
        file.write(password)
    messagebox.showinfo("Успех", f"Пароль сохранён в файл {file_path}.")

# Создание главного окна
root = tk.Tk()
root.title("Генератор паролей")
root.geometry("400x400")  # Установка ширины окна в 300 пикселей

# Поле для ввода количества символов
tk.Label(root, text="Введите количество символов:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Поле, куда будет сгенерирован пароль
tk.Label(root, text="Сгенерированный пароль:").pack(pady=5)
password_entry = tk.Entry(root)
password_entry.pack(pady=5)

# Кнопка генерации пароля
generate_button = tk.Button(root, text="Сгенерировать", command=on_generate_clicked)
generate_button.pack(pady=5)

# Кнопка копирования пароля
copy_button = tk.Button(root, text="Скопировать", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Кнопка сохранения пароля в файл
save_button = tk.Button(root, text="Сохранить в txt", command=save_to_file)
save_button.pack(pady=5)

# Запуск основного цикла Tkinter
root.mainloop()
