def thesaurus(keys,names):
    dict_of_name = {}
    dict_of_name[keys] = names
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
        print(i)
    return l
A_name = input('')
SplitName = Split(A_name)
Names = ','.join(SplitName)
Keywords = SplitKeyWords(SplitName)
Keys = ','.join(Keywords)
thesaurus(Keys,Names)
print(Keywords,SplitName)