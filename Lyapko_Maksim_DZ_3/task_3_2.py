def num_translate_adv(num):
    translate = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'}
    print(translate[num])


word = input('your word for translate from one to ten: ')
num_translate_adv(word)
