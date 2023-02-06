#1
#age = input('Enter your age: ')
#if int(age) >= 18:
    #print('You are old enough to drive')
#else:
    #print('You need', 18 - int(age), 'more years to learn to drive')

#2
#my_age = 30
#your_age = input('Enter Your Age:') 
#if my_age - int(your_age) == 1 or int(your_age) - my_age == 1:
    #print('Just a year different maybe is even months')
#elif my_age > int(your_age):
    #print('Am', 30 - int(your_age),'years older than you') 
#elif my_age < int(your_age):
    #print('You are',int(your_age) - 30,'years older than me') 
#else:
    #print('We have same age')

#3
#a = input('Enter Number one:')
#b = input('Enter Number Two:')
#if int(a > b):
    #print(b ,'is greater than', a)
#else:
    #print('They are the same')

#lvl2
#1
#score = input('Enter your score:')
##if int(score) >= 80:
    #print('A')
##elif int(score) >= 60:
    #print('C')
##elif int(score) >= 50:
    #print('D')
#else:
    #print('F')

#2
season = input('Enter the Month:')
if season == 'September' or season =='October' or season == 'November':
    print('The season is Autumn')
elif season == 'December' or season =='January' or season == 'February':
    print('The season is Winter')
elif season == 'March' or season == 'April' or season == 'May':
    print('The season is Spring')
elif season == 'June' or season == 'July' or season == 'August':
    print('The season is Summer')
else:
    print('Wrong input: Hint-start with capital letter')

#3
#fruits = ['banana', 'orange', 'mango', 'lemon']  
#add_fruit = input('Write a Fruit: ')
#if add_fruit in fruits:
    #print('That fruit already exist in the list')
#else:
    #fruits.append(add_fruit)
    #print(fruits)

#4
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if ('skills' in person):
    print('It has skills as a key')
    print(person['skills'][(int(len(person['skills'])/2))])   
else:
    print('')

if ('skills' in person):
       print('It has skills as a key')
       skill_check = 'Python' in person['skills']
       if skill_check == True:
            print('Python is in skill' )
       else:
            print('Learn Python')
else:
        print('No Python')

if 'JavaScript' in person['skills'] and 'React' in person['skills'] :
     print('He is a front end developer')
elif 'Node' and 'Python'and 'MongoDB' in person['skills']:
     print('He is a backend developer')
elif 'React' and 'Node' and 'MongoDB' in person['skills']:
     print('He is a fullstack developer')
else:
     print('unknown title')


if person['is_marred'] is True and person['country'] == 'Finland':
     print(person['first_name'],'',person['last_name'],'','lives in',person['country'],'','He is Married')