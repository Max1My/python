duration = []
ye = 31104000
mo = 2592000
d = 86400
h = 3600
m = 60
time = int(input('Введите промежуток: '))
while(time > ye):
    years = time // ye
    time = time - (ye * years)
    duration.append(years)
    duration.append('год')
while(time > mo):
    month = time // mo
    time = time - (mo * month)
    duration.append(month)
    duration.append('мес')
while(time > d):
    days = time // d
    time = time - (d * days)
    duration.append(days)
    duration.append('дн')
while time > h:
    hours = time // h
    time = time - (h * hours)
    duration.append(hours)
    duration.append('час')
while time > m:
    minutes = time // m
    time = time - (m * minutes)
    duration.append(minutes)
    duration.append("мин")
else:
    second = time % m
    duration.append(second)
    duration.append("сек")
print(duration)
