num = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
negetive_and_zero = [num for num in num if num <= 0]
#print(negetive_and_zero)
#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_lst = [ number for row in list_of_lists for number in row]
flattened_list = [ number for row in flattened_lst for number in row]
#print(flattened_list)    

#3
numbers = [(i**1,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
#print(numbers) 
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened = [[i[0].upper(),i[0][:3].upper(), i[1].upper()] for row in countries for i in row]
#print(flattened)
#5
dictionary = [{'country':i[0],'city':i[1]} for row in countries for i in row]
#print(list(dictionary))
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
con_name = [(name[0] + " " + name[1]) for row in names for name in row]
print(con_name)
#7
slope = lambda x1 ,x2, y1, y2 : (y2 -y1)/ (x2 - x1)
print(slope(6,8,2,8))    