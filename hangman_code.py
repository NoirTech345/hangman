import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

class HangmanGame:
    def __init__(self, root):
        self.window = root
        self.window.title("Виселица")
        self.window.minsize(600, 400)

        current_date = datetime.now()
        if current_date.day == 22 and current_date.month == 9:
            self.window.title("Happy Birthday Doki Doki Literature Club!")
            messagebox.showinfo("Just Monika", "Just Monika")

        self.words = {
            # Тема: Техника
            "компьютер": "Электронное устройство, используемое для хранения и обработки данных",
            "смартфон": "Мобильное устройство, которое объединяет функции телефона и компьютера",
            "сервер": "Мощный компьютер, который обрабатывает запросы и выполняет задачи для других компьютеров",
            "база данных": "Организованная коллекция данных, хранящихся и доступных электронно",
            

            # Тема: Культура стран
            "матрешка": "Традиционная русская деревянная игрушка, представляющая собой набор кукол, вложенных одна в другую",
            "кимоно": "Традиционное японское платье, которое обычно носится в особых случаях, таких как фестивали и свадьбы",
            

            # Тема: Традиции стран
            "хэллоуин": "Праздник, отмечаемый в ночь с 31 октября на 1 ноября, особенно популярный в США, где люди наряжаются в костюмы и ходят от дома к дому, говоря \"trick or treat\" (\"урок или угощение\")",
            "день благодарения": "Праздник, отмечаемый в США в четвертый четверг ноября, во время которого семьи собираются вместе, чтобы поесть традиционный ужин и выразить благодарность за то, что у них есть",
            
        }

        # Центральный фрейм для виселицы и кнопки подсказки
        self.center_frame = tk.Frame(root)
        self.center_frame.pack(expand=True)

        # Виселица
        self.hangman_label = tk.Label(self.center_frame, font=('Courier', 10))
        self.hangman_label.pack(anchor='center')

        # Метка для отображения слова
        self.word_label = tk.Label(self.center_frame, font=('Courier', 24))
        self.word_label.pack(anchor='center')

        # Кнопка подсказки
        self.hint_button = tk.Button(self.center_frame, text="Подсказка", command=self.show_hint, font=('Courier', 24))
        self.hint_button.pack(anchor='center')

        # Создание виртуальной клавиатуры
        self.keyboard_frame = tk.Frame(root)
        self.keyboard_frame.pack(expand=True)

        self.buttons = []
        button_rows = ['абвгдеёжз', 'ийклмнопрс', 'туфхцчшщъы', 'ьэюя']
        for row_index, row_chars in enumerate(button_rows):
            for col_index, char in enumerate(row_chars):
                button = tk.Button(self.keyboard_frame, text=char, command=lambda char=char: self.guess(char), font=('Courier', 24))
                button.grid(row=row_index, column=col_index, padx=5, pady=5)
                self.buttons.append(button)

        # Иллюстрации для виселицы
        self.hangman_pics = [
            '''
               -----
               |   |
                   |
                   |
                   |
                   |
            ''',
            '''
               -----
               |   |
               O   |
                   |
                   |
                   |
            ''',
            '''
               -----
               |   |
               O   |
               |   |
                   |
                   |
            ''',
            '''
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
            '''
        ]

        self.start_game()

    def start_game(self):
        self.word, self.definition = random.choice(list(self.words.items()))
        self.guessed_letters = []
        self.attempts = 6
        self.update_display()

    def update_display(self):
        self.hangman_label.config(text=self.hangman_pics[6 - self.attempts])
        word_status = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
        self.word_label.config(text=word_status)

    def guess(self, letter):
        current_date = datetime.now()
        if letter not in self.word:
            self.attempts -= 1
            if current_date.day == 22 and current_date.month == 9:
                self.hint_button.config(text="Сайори, ты ли это?")
        else:
            self.guessed_letters.append(letter)
        self.update_display()
        self.check_game_over()

    def check_game_over(self):
        if self.attempts <= 0:
            messagebox.showinfo("Игра окончена", f"Вы проиграли! Слово было: {self.word}")
            self.start_game()
        elif "_" not in self.word_label['text']:
            messagebox.showinfo("Игра окончена", "Вы выиграли!")
            self.start_game()

    def show_hint(self):
        messagebox.showinfo("Подсказка", self.definition)

root = tk.Tk()
game = HangmanGame(root)
root.mainloop()