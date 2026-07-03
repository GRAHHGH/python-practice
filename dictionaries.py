
student = {
            'first_name' : 'John David',
            'last_name' : 'Jaca',
            'gender' : 'Male',
            'age' : '19',
            'marital_status' : 'single',
            'skills' : {'Python' : 'Beginner',
                        'Java' : 'intermediate',
                        'Git' : 'intermediate'},
            'country' : 'Philippines',
            'city' : 'Davao',
            'address' : 'Communal street',
            'favourite number' : ['4', '5', '6']
        }

print(student)
print(len(student))

student['job title'] = 'Student'
student['favourite number'].append('7')

print(student)