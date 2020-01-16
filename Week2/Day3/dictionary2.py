def find_avg_year(years):
    sum = 0
    for year in years:
        sum += year
    return int(sum/len(years))

def find_avg_year_short(years):
    return int(sum(years)/len(years))
list_of_cars =["Toyota", "Ford", "BMW", "Audi", "Benz"]
list_of_models = ["Camry", "F150", "I8", "A4","S550"]

car = {
    "make" : list_of_cars,
    "model" : list_of_models,
    "years" : [2010, 2017, 2020, 2006, 2020]
    }

for key in car:
    print(key)
    pass


car_years = car["years"]
print(car_years)


avg_year = find_avg_year(car_years)
print(avg_year)


car_colors =["red", "bleu", "black", "bleu", "silver"]
car["color"] = car_colors


# small exercise
#  

car["Num in stock"] = [3,5,6,1,3]

for key in car:
    print(key)



for value in car.values():
    #print(value)
    pass

#tiny excercise: Tell me how many cras we have in stock by accessing
# the "num is stock" key from the dictionary

inventory = car(["Num in stock"])
print(f"We have {inventury} cars in stock!")
#print(f"We have {sum(car["Num in stock]} cars in stock!")


car["dealers"] = ["amy", "Bob", "Charlie", "Dylan", "Elephant"]

for key in car:
    print(key)

    #for value in car.value():



print("Firing all the dalers...")
car.pop("dealers")
for key in car:
    print(key)

#car["dealers].clear()

print(car)
print("n\ We're going to close our dealership")
car.clear() # Erase the contents of the dictionary
print(car)
del car # delete the hole dictionary
#print(car)
