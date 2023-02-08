empty_list = list() #1
lst_with_5 = ['Sadiya','Alamin','Khadija','Hassana','Abubakar'] #2
print('Lenght of my list', len(lst_with_5)) #3
#4
first_item = lst_with_5[0]
print('First item:',first_item)
middle_item = lst_with_5[2]
print('Middle item',middle_item)
last_item = lst_with_5[4]
print('last item',last_item)
#5
mixed_data_types = ['Maryam', 32 , 63 ,'Married','Kano,Nigeria']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
first_company,secoud_company,third_company,forth_company,fifth_company,sixth_company,seventh_company = it_companies
#7
print(first_company)
print(secoud_company)
print(third_company)
print(forth_company)
print(fifth_company)
print(sixth_company)
print(seventh_company)
print('The number of companies are:',len(it_companies)) #8
#9
print('First Company',it_companies[0])
print('Middle Company' , it_companies[3])
print('Last Company', it_companies[6])
#10
it_companies[0] = 'WhatsApp'
print(it_companies)
#11
it_companies.append('Twitter')
print(it_companies)
#12
it_companies.insert(4,'Facebook')
print(it_companies)
#13
upper_one_company = it_companies[0].upper()
print(upper_one_company)
#14
new_str = ['#']
new_join = it_companies + new_str
print(new_join)
#15
does_exist = 'Facebook' in it_companies
print(does_exist)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.sort(reverse=True)
print(it_companies)
#18
company_3 = it_companies[0:3]
print(company_3)
#19
company_3_19 = it_companies[4:7]
print(company_3_19)
#20
middle_it_company = it_companies[4:5]
print(middle_it_company)
#21
it_companies.remove('WhatsApp')
print(it_companies)
#22
middle_it_2_company = it_companies[3:5]
print(middle_it_2_company)
#23
last_it_company = it_companies[-1]
print(last_it_company)

it_companies.pop()
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
#del it_companies
#print(it_companies)
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
#27
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)
#exercise level 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('Minimum Age is:', ages[0])
print('Maximum Age is:' , ages[-1])
min_age = [19]
max_age = [26]
new_ages = ages + min_age + max_age
print(new_ages)
new_ages.sort()
print(new_ages)
median_age = new_ages[5:7]
print(median_age)
import statistics
print('The Median is:', statistics.median(new_ages))
average_age = sum(new_ages)/len(new_ages)
print('The Average of the Ages is:',average_age)
range_age = ages[-1] - ages[0]
print(range_age)

a = max_age[0] - average_age
print(abs(a))

b = min_age[0] - average_age
print(abs(b))
print('Compare min-averge and max averge if they are the same: ',abs(a) == abs(b))
#2
countries = ['Afghanistan',
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
Total_countries = len(countries)
print(Total_countries)
mid_index = (int(Total_countries/2))
print(mid_index)
middle_country = countries[mid_index]
print(middle_country)
#2
divi_countries = countries[0:96]
print(divi_countries)
divi_countries2 = countries[96:193]
print(divi_countries2)
#4
secound_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us,*scandic, = secound_countries
print(ch)
print(ru)
print(us)
print(scandic)
