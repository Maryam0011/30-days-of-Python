#lvl1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1
length_company =len(it_companies)
print(length_company)
#2
it_companies.add('Twitter')
print(it_companies)
#3
it_companies.update(['WhatsApp','SnapChat','Telegram'])
print(it_companies)
#4
it_companies.pop()
print(it_companies)
#5
#We can remove an item from a set using remove() method. 
#If the item is not found remove() method will raise errors, 
#so it is good to check if the item exist in the given set. 
#However, discard() method doesn't raise any errors.

#lvl2
#1
c = A.union(B)
print(c)
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(A.union(B))
print(B.union(A))
#6
print(A.symmetric_difference(B))
#7
del A
del B
#lvl3
#1
age1 = set(age)
print(age1)
print(len(age)==len(age1))
#2
#List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
#Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
#Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
#3
sentence = 'I am a teacher and I love to inspire and teach people'
sen_to_list = sentence.split()
print(sen_to_list)
sentence_list = set(sen_to_list)
print(sentence_list)

