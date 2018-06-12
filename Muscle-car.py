from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re


cars = urlopen("https://americanmusclecar.ru")
cars = bs(cars, "html.parser")
cars = str(cars)
catal = re.compile('g/\D+\/"') #Expression for searching cars references
catalog = catal.findall(cars)  #Function of searching
count = 0
while count != len(catalog): #Parse the catalog of cars
    ref = catalog[count] # choose ref in catalog
    car = urlopen("https://americanmusclecar.ru/catalog" + ref[1 : -1]) #firstly cleaning up ref for opening like a object
    car = bs(car, "html.parser") #parse 
    car = car.find_all('p') #find all text
    f = open(ref[2 : -2] + '.txt', 'w') # create file of car
    for mcar in car:  #cleaning info and then whiting to file
        car = mcar.get_text()
        f.write(car)
        f.write('\t')
    f.close #closed file
    count += 1 #increase count
    


