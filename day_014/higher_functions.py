countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#4
for country in countries:
    print(country)

#5
for name in names:
    print(name)

#6
for num in numbers:
    print(num)
#lvl 1
#1
def change_to_upper(countries):
    return countries.upper()
names_upper_cased = map(change_to_upper, countries)
print(list(names_upper_cased))

#2
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared)) 

#3  
names_upper_case = map(change_to_upper, names)
print(list(names_upper_case))

#4
def filter_country(countries):
    if 'land' in countries:
        return True
    return False
country_with_land = filter(filter_country,countries)
print(list(country_with_land))

#5
def filter_con_6(country):
 if len(country) == 6:
        return True
 return False

country_with_6 = filter(filter_con_6,countries)
print(list(country_with_6))

#6
def filter_con_6_more(country):
 if len(country) >= 6:
        return True
 return False

country_with_6_more = filter(filter_con_6_more,countries)
print(list(country_with_6_more))

#7
def filter_con_e(country):
    if country.startswith("E"):
        return True
    return False

country_wih_e = filter(filter_con_e,countries)
print(list(country_wih_e))

#8()
from functools import reduce

squared_even_numbers_sum = reduce(lambda x, y: x + y, 
list(filter(lambda x: x % 2 == 0,
map(lambda x: x**2, numbers))))
print(squared_even_numbers_sum)

#9
def get_string_lists(lis):
  return list(filter(lambda x : isinstance(x,str),lis))

print(get_string_lists([1,2,3,"a","baba"]))

#10
def add_two_nums(x, y):
  return int(x) + int(y)

total = reduce(add_two_nums, numbers)
print(total)

#11
def concatenate_countries(x,y):
 return f"{x},{y}"
total = reduce(concatenate_countries, countries)
print(f"{total} are countries.")

#12()countries = 
Countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
def categorize_countries(pattern):
    list_countries = []
    for country in Countries:
        if pattern.lower() in country:
            list_countries.append(country)
    return list_countries

print(f'Countries with "pattern": ',categorize_countries('land'))

#13
def country_dictionary(Countries):
  dict = {}
  for country in Countries:
    if country[0] in dict:
      dict[country[0]]+=1
    else:
      dict[country[0]]=1
  return dict

print(country_dictionary(Countries))

#14
def get_first_ten_countries(lis):
  return lis[:10]
print(get_first_ten_countries(Countries))

#15
def get_last_ten_countries(lis):
  return lis[-10:]
print(get_last_ten_countries(Countries))

#level 3
from country_data import countries_data
# by name
def name(data):
 arr = []
 for i in data:
    arr.append(i["name"])
    arr.sort()
 return arr 
print(name(countries_data))

#by capital
def capital(data):
 arr = []
 for i in data:
    arr.append(i["capital"])
    arr.sort()
 return arr 
print(capital(countries_data))

# by population
def population(data):
  arr = []
  for i in data:
    arr.append(i["population"])
    arr.sort()
  return arr
    
print(population(countries_data))

#language
lang_dict = dict()
for i in range(len(countries_data)):
    for language in countries_data[i]['languages']:
        lang_dict[language] = lang_dict.get(language,0) + 1
lang_tpl = sorted(lang_dict.items(),key= lambda x:x[1],reverse=True)
lang_tpl[:10]

#most populated
pop = sorted(countries_data,key= lambda d:d['population'],reverse=True)
top_ten =  pop[:10]
top_ten

