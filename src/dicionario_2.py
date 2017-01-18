cars = {}

cars['corola'] = "red"
cars['fit'] = "green"
cars['bmw320'] = "black"

#for car in cars:
#    print(car + ": " + cars[car])
for key, value in cars.items():
    print(key + ": " + value)