# Use mathematical operations in Python

# Addition
from math import ceil, floor
answer = 30 + 12
print(answer)

difference = 30 - 12
print(difference)

product = 30 * 12
print(product)

quotient = 30 / 12
print(quotient)

seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)


# Enter code below

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)

# Convert

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# Output:
# 215
# 215.3

print(abs(39 - 16))
print(abs(16 - 39))
# Output
# 23
# 23

print(round(14.5))

# Output: 15


round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Output
# 13
# 12

# CALCULO PLANETAS
first_planet_input = input(
    'Ingrese la distancia del sol con el primer planeta en KM')
second_planet_input = input(
    'Ingrese la dincancia entre el sol y el segundo planeta en KM')

# Enter code below
first_planet = int(first_planet_input)
second_planet = int(second_planet_input)


# Enter code below

distance_km = abs(second_planet - first_planet)
print(distance_km)
