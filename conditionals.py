
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn drive.")
else:
    limit_age = 18 - age
    print(f"You need {limit_age} more years to learn to drive")

your_age = int(input("Enter your age: "))
his_age = int(input("Enter your age: "))

if your_age > his_age:
    your_age = your_age - his_age
    if your_age > 5:
        print(f"Damn your are old, we have a {your_age} year gap")
    elif your_age <= 5:
        print(f"You are {your_age} years older than me.")
else:
    his_age = his_age - your_age
    print(f"he is {his_age} years older than you.")


person={
    'first_name': 'John David',
    'last_name': 'Jaca',
    'age': 250,
    'country': 'Philippines',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Communal Street',
        'zipcode': '8000'
        }
    }

skills_input = str(input("Do you have skills? "))
bigger_skills_input = skills_input.upper()

if bigger_skills_input == 'YES':
    print('he does have skills')
    print(f"middle of the skills is {person['skills'][2]}")
else:
    print("he doesnt have any skills")


