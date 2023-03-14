# GET BASIC INFORMATION ABOUT AN ATHLETE AND CREATE ATHLETE OBJECTS
# -------------------------------------------------------

# LIBRARIES AND MODULES
import kuntoilija
import questions


# Ask a question and convert the answer to float


# Enter information about an athlete
name = input('Nimi: ')

# Ask details about her/him

weight = questions.Question.ask_user_float('Kuinka paljon painat (kg): ', True)[0]
height = questions.Question.ask_user_float('Kuinka pitkä olet (cm): ', True)[0]
age = questions.Question.ask_user_integer('Kuinka vanha olet', True)[0]
gender = questions.Question.ask_user_integer('Sukupuoli 1 mies, 0 nainen: ', True)[0]
neck = questions.Question.ask_user_float('Mikä on kaulanympäryksesi (cm): ', True)[0]
waist = questions.Question.ask_user_float('Mikä on vyötärönympäryksesi: ', True)[0]

# If woman ask circumference of her hips
if gender == 0:
    hips = questions.Question.ask_user_float('Mikä on lantionympäryksesi: ', True)[0]

# Create an athelete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)

# Print some information about the athlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi tänään on {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()

# If male use usa_rasvaprosentti_mies method
if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(
        height, waist, hips, neck)

text_to_show = f'suomalainen rasva-% on {fat_percentage} ja amerikkalainen on {usa_fat_percentage}'
print(text_to_show)

# TODO: Save user information to a file