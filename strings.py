challenge_1 = ['Thirty', 'Days', 'Of', 'Python']
result1 = ' '.join(challenge_1)
print(result1)

challenge_2 = ['Coding', 'For', 'All']
result2 = ' '.join(challenge_2)
print(result2)

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize().title().swapcase())
print(company.strip("Coding"))
print(company.replace("Coding", "Python"))

sub_string = "Coding"
print(company.index(sub_string, 0) is 0)

company1 = "Python for Everyone"
print(company1.replace("Everyone", "All"))

print(company.split())

company2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(company2.split(", "))

print(company[0])
print(company[-1])
print(company[10])
print(company1[0], company1[7], company1[11])