tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
def gen_zip():
    for index in range(len(klasses)):
        try:
            yield tutors[index], klasses[index]
        except IndexError:
            yield klasses[index], None

gen = gen_zip()

print(*gen)
print(next(gen))
