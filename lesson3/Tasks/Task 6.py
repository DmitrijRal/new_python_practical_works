# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной
# строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную
# ранее функцию int_func().
from numpy.core.defchararray import title

word = input("Enter word in lower register: ")
fst_word = word
def int_func(fst_word):
    return title(fst_word)
print(int_func(fst_word))
snd_sentence = input("Enter sentence in lower register devided by space: ")
print(int_func(snd_sentence))