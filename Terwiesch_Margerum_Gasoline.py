"""
File: Terwiesch_Margerum_Gasoline.py
Author: Mats Terwiesch and Avery Margerum
Description:
    After prompting user for some number of barrels of gasoline, the program outputs the number
    of pounds of CO2 produced, the number of barrels of crude oil required
    to produce this many barrels, and the average cost to purchase
    this number of gallons of gas in the United States. 
"""

#ask user to input number of gallons of gasoline gas_gallons
gas_gallons = float( raw_input ('Please enter the number of gallons of gasoline: '))

#1 gallon of gasoline produces approximately 19.64 pounds of carbon dioxide (eia.gov)
carbon_dioxide_pounds = gas_gallons * 19.64

#1 barrel of crude oil produces approximately 19 gallons of gasoline, thus 1 gallon of gasoline
#requires 1/19 of a barrel of crude oil (eia.gov)
barrels_of_crude = gas_gallons / 19

#Average cost of gasoline in the United States, as of 30/4/2015, is $2.580 per gallon of regular
#gasoline in 2015 United States Dollars (fuelgaugereport.com)
average_cost = gas_gallons * 2.580

#output the pounds of carbon dioxide produced
print gas_gallons, 'gallons of gasoline produes approximately', carbon_dioxide_pounds,'pounds of carbon dioxide.'

#output the number of barrels of crude oil required
print gas_gallons, 'gallons of gasoline requires approximately', barrels_of_crude, 'barrels of crude oil to produce.'

#output the average cost of gasoline
print gas_gallons, 'gallons of gasoline requires approximately', average_cost, 'USD to purchase in the United States'







