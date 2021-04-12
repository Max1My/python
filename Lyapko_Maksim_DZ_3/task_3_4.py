from random import choice

def get_jokes(num):
    jokes = num
    random_list = []
    while jokes > 0:
        random_jokes = choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
        random_list.append(random_jokes)
        jokes -= 1
    print(random_list)
    return num

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes(2, flag = true)
