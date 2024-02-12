#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def print_all_occurrences(sentence):
    for char in sentence:
        if char.lower() == 'и':
            print(char)

if __name__ == "__main__": 
    # Ввод предложения с клавиатуры
    user_sentence = input("Введите предложение: ")

    # Печать всех букв "и"
    print_all_occurrences(user_sentence)
