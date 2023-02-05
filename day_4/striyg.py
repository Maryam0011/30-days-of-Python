#1
word1 = 'Thirty'
word2 = 'Days'
word3 = 'Of'
word4 = 'Python'
space = ' '
full_word = word1 + space + word2 + space + word3 + space+ word4
print(full_word)
#2,3,4,5,6,7,8,
con_str1 = 'Coding'
con_str2 = 'For'
con_str3 = 'A'
company = con_str1 + space + con_str2 + space + con_str3
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
first_word = company[0:6]
print(first_word)
#10,11,12
sub_string = 'Coding'
print(company.index(sub_string))
company_new = 'Coding for All'
print(company_new.replace('Coding', 'Python'))
a = 'Python for Everyone'
print(a.replace('Everyone', 'All'))
print(company_new.split())
apps = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print (apps.split(',' ))
chrt_at_0 = company_new[0]
print(chrt_at_0)
last_index = company_new[-1]
print(last_index)
index_10 = company_new[10]
print(index_10)
acrym_name = a[0:20:4]
print(acrym_name)
#print(company_new.strip('for'))
acrym_name1 = company_new[0:12:2]
print(acrym_name1)
occran_c = 'C'
print(company_new.index(occran_c))
occran_f = 'f'
print(company_new.index(occran_f))
b = 'Coding for All People'
print(b.rfind('l'))
c= 'You cannot end a sentence with because because because is a conjunction'
print(c.find('because'))
print(c.rindex('because'))
bcos_txt = c[31:54]
print(bcos_txt)
#26
print(c.find('because'))
#27
bcos_txt = c[31:54]
print(bcos_txt)
#28
print(company_new.startswith('Coding'))
#29
print(company_new.endswith('Coding'))
#30
d = '   Coding For All   '
print(d.strip())
#31
e = '30DaysOfPython'
f = 'thirty_days_of_python'
print(e.isidentifier())
print(f.isidentifier())
#32
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = ' '.join(python_libraries)
print(formated_string)
#33
print('I am enjoying this challenge.\njust wonder what is next.')
#34
print('Name\t         Age\t Country\tCity') 
print('Asabeneh \t250\tFinland\tHelsinki')
#35
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print('radius = 10')
print('pi = 3.14')
print('area = pi * radius ** 2')
print(formated_string)
#36
g = 8
h = 6
print('{} + {} = {}'.format(g, h, g + h))
print('{} - {} = {}'.format(g, h, g - h))
print('{} * {} = {}'.format(g, h, g * h))
print('{} / {} = {:.2f}'.format(g, h, g / h)) 
print('{} % {} = {}'.format(g, h, g % h))
print('{} // {} = {}'.format(g, h, g // h))
print('{} ** {} = {}'.format(g, h, g ** h))





