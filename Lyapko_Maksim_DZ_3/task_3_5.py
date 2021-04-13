from random import randrange

def get_jokes(num):
    while num > 0:
        random_joke1 = randrange(len(nouns))
        random_joke2 = randrange(len(adverbs))
        random_joke3 = randrange(len(adjectives))
        joke = nouns[random_joke1] + ' ' + adverbs[random_joke2] + ' ' + adjectives[random_joke3]
        jokes_list.append(joke)
        num -= 1
    return num

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokes_list = []
joke = get_jokes(2)
while all(jokes_list[i] == jokes_list[i+1] for i in range(len(jokes_list)-1)):
    jokes_list =[]
    get_jokes(2)
else:
    print(jokes_list)