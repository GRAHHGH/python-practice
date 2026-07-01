# Day 1: 30 days of python programming

import math


first_name = "John David"
last_name = "Jaca"
full_name = first_name + " " + last_name
country = "Philippines"
city = "Davao"
age = 19
year = 2007
is_married = False
is_true = True
is_light_on = True

game, hobby, fav_number, prog_language = "Minecraft", "Gaming", 5,"python"

print(game, hobby, fav_number, prog_language)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

compare_name = first_name == last_name

print(compare_name)

num_one = 5
num_two = 4

num_sum = num_one + num_two

print(num_sum)

num_subtraction = num_two - num_one

print(num_subtraction)

num_product = num_two * num_one

print(num_product)

num_division = num_one / num_two

print(num_division)

num_modulus = num_two % num_one

print(num_modulus)

num_power = num_one**num_two

print(num_power)

num_floor_division = num_one // num_two

print(num_floor_division)

radius = int(input("input radius: "))

area_circle = math.pi * radius**2

print(area_circle)

circumference_circle = 2* math.pi * radius

print(circumference_circle)

user_first_name = input("what is your first name: ")
user_last_name = input("what is your last name: ")
user_country = input("where is your country: ")
user_age = input("what is your age: ")