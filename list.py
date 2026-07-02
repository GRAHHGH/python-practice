lst_1 = []
items = ["shoes", "bag", "phone", "wallet", "pen"]

items_length = len(items)
lst_1_length = len(lst_1)

print(items_length)
print(lst_1_length)

shoes_phone_pen = items[0::2]

print(shoes_phone_pen)

mixed_data_types = ["jayde", 19, 167, "single", "Davao City"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(mixed_data_types)
print(it_companies)

it_companies_length = len(it_companies)
print(it_companies_length)

facebook_apple_amazon = it_companies[0::3]
print(facebook_apple_amazon)

it_companies[0] = "Meta"
print(it_companies)

it_companies.append("YouTube")
print(it_companies)

it_companies.insert(3, "Samsung")
print(it_companies)

it_companies[2] = it_companies[2].upper()

print(it_companies)

check_in_companies = "Oracle" in it_companies

print(check_in_companies)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

youtube_samsung_oracle = it_companies[0:3]
print(youtube_samsung_oracle)

google_apple_amazon = it_companies[-3:]
print(google_apple_amazon)

del it_companies[3:6]
print(it_companies)

it_companies.remove("YouTube")
print(it_companies)

it_companies.remove("Google")
print(it_companies)

it_companies.remove("Amazon")
print(it_companies)

del it_companies[0:3]
print(it_companies)


