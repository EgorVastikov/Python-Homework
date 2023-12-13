import re


numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_car_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b')

taxi_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}\b')


private_cars = private_car_pattern.findall(numbers)
taxis = taxi_pattern.findall(numbers)

print(private_cars)
print(taxis)