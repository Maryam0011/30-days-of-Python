empty_tuple = tuple() #1
#2
siblings_name = ('Saifullahi Ango', 'Sadiq Bolt', 'Hassana Noble', 'Fati Ciki', 'Faruk Aski')
#3
bro_name =('Saifullahi', 'Sadiq' , 'Faruq')
sis_name = ('Hassana', 'Fatima')
sibling = bro_name + sis_name
print(sibling)
#4
num_sibling = len(sibling)
print(num_sibling)
#5
prnt_name = ('Abubakar','Juwairiya')
family_member = prnt_name + sibling
print(family_member)
#1
unpack_parent_change = list(family_member)
print(unpack_parent_change)
ab, ju,*scandic = unpack_parent_change
print(ab)
print(ju)
#2
fruit = ('Orange', 'Banana','Apple')
veges = ('Alayyahu', 'Zogale','Rame')
animal = ('Meat','Milk','Cheese')
food_stuff_tp = fruit + veges + animal
print(food_stuff_tp)
#3
food_stuff_list = list(food_stuff_tp)
print(food_stuff_list)
#4
middle_item = food_stuff_list[4]
print('The Middle item is:',middle_item)
#5
org,ba,ap,*scandic = food_stuff_list
print(org)
print(ba)
print(ap)
#6
del food_stuff_tp
#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)


