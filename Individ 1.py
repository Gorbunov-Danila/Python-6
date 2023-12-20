def print_all_occurrences(sentence):
    for char in sentence:
        if char.lower() == 'и':
            print(char)

# Ввод предложения с клавиатуры
user_sentence = input("Введите предложение: ")

# Печать всех букв "и"
print_all_occurrences(user_sentence)
