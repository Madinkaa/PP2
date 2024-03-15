#A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. 
#Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def grams_to_ounes(grams):
    ounes = 28.3495231 * grams
    return ounes
grams = 500
ounes = grams_to_ounes(grams)
print(f"{grams} grams is equal to {ounes} ounes")

#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
# The following formula is used for the conversion: C = (5 / 9) * (F – 32)
def fahrenheit_to_temp(F):
    temp = (5 / 9) * (F - 32)
    return temp
F = 35
temp = fahrenheit_to_temp(F)
print(f"{F} farenheit is equal to {temp} temp")

#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
#How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
def solve(numheads, numlegs):
    

