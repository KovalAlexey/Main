#Яша плавал в бассейне размером N × M метров и устал. В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков
#(не обязательно от ближайшего) и y метров от одного из коротких бортиков. Какое минимальное расстояние должен проплыть Яша, 
#чтобы выбраться из бассейна на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести число метров, которое нужно проплыть Яше до бортика.


n = int(input())
m = int(input())
x = int(input())
y = int(input())

if m < n:
    short = m
    long = n
else:
    short = n
    long = m

miny = long - y 
minx = short - x

countx = 0
county =0

if minx < x:
    countx += minx
else:
    countx += x
if miny < y:
    county +=miny
else:
    county += y

if countx < county:
    print(countx)
else:
    print(county)