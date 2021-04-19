from random import randrange

def get_jokes(num): #сложение в одну фразу
    while num > 0:
        joke = []
        joke.append(sort_nouns())
        joke.append(sort_adverbs())
        joke.append(sort_adjectives())
        jokes_list.append(joke)
        num -= 1
    return jokes_list

def sort_nouns(): #генерация nouns
    index_random_nouns = randrange(len(nouns))
    random_nouns = nouns[index_random_nouns]
    nouns.pop(index_random_nouns)
    return random_nouns
def sort_adverbs(): #генерация adverbs
    index_random_adverbs = randrange(len(adverbs))
    random_adverbs = adverbs[index_random_adverbs]
    adverbs.pop(index_random_adverbs)
    return random_adverbs
def sort_adjectives(): #генерация adjectives
    index_random_adjectives = randrange(len(adjectives))
    random_adjectives = adjectives[index_random_adjectives]
    adjectives.pop(index_random_adjectives)
    return random_adjectives

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

jokes_list = []
num_jokes = int(input('Количество шуток: '))
if num_jokes > 5:
    print('Максимальное количество шуток - 5')
else:
    jokes_list = get_jokes(num_jokes)
print(' '.join(map(str,jokes_list)))