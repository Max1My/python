lst1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
lst1.insert(1,'"')
lst1.insert(3,'"')
lst1.insert(5,'"')
lst1.insert(7,'"')
lst1.insert(12,'"')
lst1.insert(14,'"')
lst1 = ' '.join(lst1)
print(lst1)