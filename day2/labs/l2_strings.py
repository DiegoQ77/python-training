fact = "The Moon has no atmosphere."


# Multiline text

multiline = "Facts about the Monn :\n There is no atmosphere. \n There is no sound."
print(multiline)

# Other form

multiline2 = """Facts about the Moon:
    There is no atmosphere.
    there is no sound."""

print(multiline2)

# String methos in python
# "temperatures and facts abouty the monn".title()

# SPLIT A STRING

temperatures = """Daylight: 260 F 
  Nighttime: -280F"""

split_temperature = temperatures.split()
print(split_temperature)

split_line = temperatures.split('\n')
print(split_line)

# SEARCH FOR A STRING

search = "Moon" in "This text will describe facts and challenges with space travel"
print(search)
search_moon = "Moon" in "This text will describe facts about the Moon"
print(search_moon)

# if i need to search the position use .find()
temperatures = """Saturn has a daytime temperature of -170 degress Celcius 
While Mars has -28 Celsius"""
find_temperature = temperatures.find("Moon")
print(find_temperature)  # - 1 when the word is not found

# CHECK CONTENT
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"

for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

is_numeric = "-60".startswith('-')
print(is_numeric)

# .endswith() method helps with verifying the las character of a string

if "30 C".endswith("C"):
    print("this temperature  is in celcius")

# TRANSFORM TEXT

transform_text = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace(
    "Celsius", "C")
print(transform_text)

text = "Temperatures on the Moon can vary wildly."
text_in = "temperatures" in text
text_in_lower = "temperatures" in text.lower()

# JOIN

moon_facts = ["The Moon is drifting away from the Earth.",
              "On average, the Moon is moving about 4cm every year"]

'\n'.join(moon_facts)

print(moon_facts)


# EXERCISE - TRANSFORM TEXT BY USING STRING METHODS

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

sentences = text.split('. ')
print(sentences)

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)


# PERCENT SIGN (%%) FORMATTING

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" %
      mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# THE FORMAT() METHOD
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(
    mass_percentage))

# You don't need to assign repeated variables multiple times, making it less verbose because fewer variables need to be assigned:

print("""You are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))


print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth""".format(
    moon="Moon", mass=mass_percentage))


# ABOUT F-STRINGS
print(
    f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
print(
    f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
subject = "interesting facts about the moon"
subject_f = f"{subject.title()}"
print(subject_f)


# EXERCISE
name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'

template = """Gravity Facts about {name} 
--------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2

"""
print(template)
# asigment the values of name planet an gravity in tempalte variable
print(template.format(name=name, planet=planet, gravity=gravity))
