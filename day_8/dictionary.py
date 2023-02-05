#1
dog = {}
#2
dog = {'Name':'Police','Color':'Brown','Legs':'Four'}
#3
student = {
    'first_name':'Maryam',
    'last_name':'Abubakar',
    'Gender':'Female',
    'age':6,
    'country':'Nigeria',
    'City':'Kano',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Gwale,Karshen Waya',
        'zipcode':'07703'
    }
    }
#4
print(len(student))
#5
print(student['skills'])
print(type(student['skills']))
#6

student['skills'].append('Cooking')
student['skills'].append('Reading')
print(student)

#7
lst_keys = student.keys()
print('These are the keys values: ',lst_keys)

#8
lst_values = student.values()
print('These are values assign to the keys: ',lst_values)

#9
print(student.items())
print(student.popitem())
