from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re


cars = urlopen("https://americanmusclecar.ru")
cars = bs(cars, "html.parser")
cars = str(cars)
catal = re.compile('g/\D+\/"') #Регулярное выражение для поиска авто
catalog = catal.findall(cars)  #Поиск авто по выражению
count = 0
while count != len(catalog):
    ref = catalog[count]
    car = urlopen("https://americanmusclecar.ru/catalog" + ref[1 : -1])
    car = bs(car, "html.parser")
    car = car.find_all('p')
    f = open(ref[2 : -2] + '.txt', 'w')
    for mcar in car:
        car = mcar.get_text()
        f.write(car)
        f.write('\t')
    f.close
    count += 1
    


