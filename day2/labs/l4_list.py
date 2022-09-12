# Create a list
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]

# Access list items by index
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# DETERMINE THE LENGTH OF A LIST
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Add values to list
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# REMOVE VALUES FROM LIST

planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets,
      "planets in the solar system.")

# USE NEGATIVE INDEXES
print("The first planet is", planets[0])
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# FIND A VALUE IN A LIST
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")


# Exercise - Create and use Python lists ********************
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)
# Display the number of plantes
print(len(planets), "number of plantes ")

# Add a planet to the list

# Enter your code below:
planets.append("Pluto")

print("Actually, there are", len(planets), "planets")

print(planets[-1], "is the last planet")


# Work with numbers in lists
# Store numbers in lists

gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
# creates a list that shows the gravitational forces of all eight planets in the solar system, in G:
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650  # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs",
      bus_weight * gravity_on_planets[0], "kg")

# Use min() and max() with lists

bus_weight = 12650  # in kilograms, on Earth
# we use min an max to get the min and maax value of list of numbers
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is",
      bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is",
      bus_weight * max(gravity_on_planets), "kg")

# Manipulate list data
# Slice list
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:3]
print(planets_before_earth)


planets_after_earth = planets[3:8]
print(planets_after_earth)

planets_after_earth = planets[3:]
print(planets_after_earth)

# join lists

Copy
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


# sort list

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# EXERCISE - WORK WITH LIST DATA
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]

user_planet = input(
    "Please enter the name of the planet (with a capital letter to start)")

planet_index = planets.index(user_planet)

# Display planets closer to the sun
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])


# Display planets further
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])
