# More Dictionaries

states = {
    'province1': '01',
    'province2': '02',
    'province3': '03',
    'province4': '04',
    'province5': '05',
    'province6': '06',
    'province7': '07',

}

cities = {
    '01': 'Biratnagar',
    '02': 'Janakpur',
    '03': 'Hetauda',
    '04': 'Pokhara',
    '05': 'Deukhuri',
    '06': 'Birendranagar',
    '07': 'Godawari'

}
print('~~$' * 10)
print("provience3 state has", cities['03'], "city")

print("Hetauda is the city of", states['province3'], "province")

print("Provience3 has", cities[states['province3']])


for state in states.items():
    print(f"{state}")

for state in states.keys():
    print(f"{state}")

for state in states.values():
    print(f"{state}")


state = states.get('Provience8')
if not state:
    print("There is only 7 states in total")
