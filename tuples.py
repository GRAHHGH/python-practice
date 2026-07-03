# so basically list is [] and tuples is ()

students = ('mac', 'josh', 'von', 'james', 'kirby', 'neil', 'jam', 'jd')
teachers = ('machica', 'ivy', 'tupas', 'rogers')

student_and_teachers = students + teachers

print(students)
print(teachers)
print(student_and_teachers)

print(len(student_and_teachers))

school = list(student_and_teachers)

school[11] = 'CIC'
print(school)

school.append('UAGC')

print(school)
