#SkillsUSA Computer Programming Competition
#Kincade Burroughs - North Point High School - #101

'''
Function Purpose: This function takes user input for two cars: their types (electric/gas),
makes and models, their initial costs, and their miles per gallon/miles per kWh
Precondition: User knows car information for certain gas-powered and electric cars to be compared.
Postcondition: Information about each type of car's model, cost, and mpg/mpkWh is stored in
variables to be used for later calculations.
'''
for i in range (2):
    car_type = input("What type of car would you like (gas or electric)? ")
    if car_type == "electric":
        if i == 0:
            car1_type = "electric"
            car1_model = input("What is the make and model of the electric car? ")
            car1_cost = int(input("What is the initial cost of the electric car? "))
            car1_mpkWh = int(input("What is the miles per kWh of the electric car (3-5 miles per kWh)? "))
            if not (2 < car1_mpkWh < 6):
                print("You must submit a value between 3 and 5.")
        elif i == 1:
            car2_type = "electric"            
            car2_model = input("What is the make and model of the electric car? ")
            car2_cost = int(input("What is the initial cost of the electric car? "))
            car2_mpkWh = int(input("What is the miles per kWh of the electric car (3-5 miles per kWh)? "))
            if not (2 < car2_mpkWh < 6):
                print("You must submit a value between 3 and 5.")          
    elif car_type == "gas":
        if i == 0:
            car1_type = "gas"
            car1_model = input("What is the make and model of the gas car? ")
            car1_cost = float(input("What is the initial cost of the gas car? "))
            car1_mpg = int(input("What is the miles per gallon of the gas car (15-50 mpg)? "))
            if not (14 < car1_mpg < 51):
                print("You must submit a value between 15 and 50.")
        elif i == 1:
            car2_type = "gas"
            car2_model = input("What is the make and model of the gas car? ")
            car2_cost = float(input("What is the initial cost of the gas car? "))
            car2_mpg = int(input("What is the miles per gallon of the gas car (15-50 mpg)? "))
            if not (14 < car2_mpg < 51):
                print("You must submit a value between 15 and 50.")
    else:
        print("You need to either type \"electric\" or \"gas\".")
        i = i + 1

#Gathers static information concering gas price, electricity price, miles they plan to drive
#per year, and number of years they plan to use the car
cost_per_gallon = float(input("What is the average cost per gallon ($3.00-$5.00)? "))
if not (2 < cost_per_gallon < 6):
    print("You must submit a value between 3 and 5.")
cost_per_kWh = float(input("How much does a kWh of electricity cost ($0.09-$0.35 per kWh)? "))
if not (0.089 < cost_per_kWh < 0.351):
    print("You must submit a value between 0.09 and 0.35.")
miles_per_year = int(input("How many miles do you play to drive per year (1000-30000)? "))
if not (999 < miles_per_year < 30001):
    print("You must submit a value between 1000 and 30000.")
years_owned = int(input("How many years do you plan to own this car? "))

#Calculations for green house gas emissions of each car
if car1_type == "electric":
    total_car1_ghg = float(0.000433 * ((miles_per_year * years_owned) / car1_mpkWh))
else:
    total_car1_ghg = float(0.008887 * ((miles_per_year * years_owned) / car1_mpg))

if car2_type == "electric":
    total_car2_ghg = float(0.000433 * ((miles_per_year * years_owned) / car2_mpkWh))
else:
    total_car2_ghg = float(0.008887 * ((miles_per_year * years_owned) / car2_mpg))

#Calculations for total cost of each car
if car1_type == "electric":
    total_car1_cost = float(car1_cost + (((miles_per_year * years_owned) / car1_mpkWh) * cost_per_kWh))
else:
    total_car1_cost = float(car1_cost + (((miles_per_year * years_owned) / car1_mpg) * cost_per_gallon))

if car2_type == "electric":
    total_car2_cost = float(car2_cost + (((miles_per_year * years_owned) / car2_mpkWh) * cost_per_kWh))
else:
    total_car2_cost = float(car2_cost + (((miles_per_year * years_owned) / car2_mpg) * cost_per_gallon))

#Lists all of cars' features
print("Car #1's Attributes")
print("Type: " + car1_type)
print("Make and Model: " + car1_model)
print("Total cost: $" + str(total_car1_cost))
print("Total CO2 emissions: " + str(total_car1_ghg) + " metric tons of CO2")

print("Car #2's Attributes")
print("Type: " + car2_type)
print("Make and Model: " + car2_model)
print("Total cost: $" + str(total_car2_cost))
print("Total CO2 emissions: " + str(total_car2_ghg) + " metric tons of CO2")

'''
Precondition: Total cost of each car is calculated
Postcondition: The car costing the least amount of money is
printed first in the terminal with the more expensive car under it.
'''
print("List of Cars - least expensive to most expensive")
if total_car1_cost < total_car2_cost:
    print("1. " + car1_model + ": $" + str(total_car1_cost))
    print("2. " + car2_model + ": $" + str(total_car2_cost))
elif total_car2_cost < total_car1_cost:
    print("1. " + car2_model + ": $" + str(total_car2_cost))
    print("2. " + car1_model + ": $" + str(total_car1_cost))
else:
    print("1. " + car1_model + ": $" + str(total_car1_cost))
    print("1. " + car2_model + ": $" + str(total_car2_cost))
    print("These cars would cost the same amount.")


'''
Precondition: Total CO2 emissions of each car is calculated
Postcondition: The car which produces less CO2 emissions is printed
to the terminal above the car which produces more CO2 emissions.
'''
print("List of Cars - least CO2 emissions to most CO2 emissions.")
if total_car1_ghg < total_car2_ghg:
    print("1. " + car1_model + ": " + str(total_car1_ghg) + "metric tons of CO2")
    print("2. " + car2_model + ": " + str(total_car2_ghg) + "metric tons of CO2")
elif total_car2_ghg < total_car1_ghg:
    print("1. " + car2_model + ": " + str(total_car2_ghg) + " metric tons of CO2")
    print("2. " + car1_model + ": " + str(total_car1_ghg) + " metric tons of CO2")
else:
    print("1. " + car1_model + ": " + str(total_car1_ghg) + " metric tons of CO2")
    print("1. " + car2_model + ": " + str(total_car2_ghg) + " metric tons of CO2")
    print("These cars would produce the same amount of carbon emissions.")