#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def unique_letters(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    
    unique_in_word1 = set1 - set2
    unique_in_word2 = set2 - set1
    
    result = list(unique_in_word1 | unique_in_word2)
    result.sort()  # Сортировка для вывода в порядке возрастания
    
    return result

if __name__ == "__main__": 
    # Ввод двух слов с клавиатуры
    word1 = input("Введите первое слово: ")
    word2 = input("Введите второе слово: ")

    # Получение уникальных букв и вывод результата
    result_letters = unique_letters(word1, word2)
    print(f"Буквы, присутствующие только в одном из слов: {result_letters}")
