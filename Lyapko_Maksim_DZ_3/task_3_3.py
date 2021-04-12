def thesaurus(keys,names):
    dict_of_name = {}
    n = len(keys)
    while n > 0:
        y = keys.pop()
        y = ''.join(y)
        z = names.pop()
        dict_of_name.setdefault(y,z)
        n -= 1
    print(dict_of_name)

def Split(name):
    name = name.title()
    name = name.split()
    return name
def SplitKeyWords(key):
    l = []
    for i in key:
        i = ''.join(i)
        l.append(i[0])
    return l
A_name = input('')
SplitName = Split(A_name)
Names = ','.join(SplitName)
Keywords = SplitKeyWords(SplitName)
thesaurus(Keywords,SplitName)