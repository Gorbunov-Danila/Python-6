#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def remove_duplicate_letters(sentence):
    seen_letters = set()
    result = []
    for char in sentence:
        if char.isalpha() and char.lower() not in seen_letters:
            seen_letters.add(char.lower())
            result.append(char)
    return ''.join(result)

if __name__ == "__main__": 
    # Ввод предложения с клавиатуры
    user_sentence = input("Введите предложение: ")

    # Удаление повторяющихся букв и вывод результата
    result_sentence = remove_duplicate_letters(user_sentence)
    print(f"Результат после удаления повторяющихся букв: {result_sentence}")
