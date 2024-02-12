#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_n_before_comma(sentence):
    comma_index = sentence.find(',')
    if comma_index != -1:
        n_before_comma = sentence[:comma_index].count('н')
        return n_before_comma
    else:
        return 0

if __name__ == "__main__": 
    # Ввод предложения с клавиатуры
    user_sentence = input("Введите предложение: ")

    # Определение и вывод количества букв "н" перед первой запятой
    result = count_n_before_comma(user_sentence)
    print(f"Количество букв 'н', предшествующих первой запятой: {result}")
