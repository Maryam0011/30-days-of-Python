#lvl
#1
import re 
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
word=re.findall('[a-z]+', paragraph,re.I)
words=set(word)
j=()
for i in words:
    x=len(re.findall(i, paragraph))
    j=(x,i)
    print(j)
#2
sentence='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between them two furthest particles.'
var=r'-?[0-9]+'
points=re.findall(var, sentence)
print("points: ",points)
lst=[]
for i in points:
    i=int(i)
    lst.append(i)
lst.sort()
print("sorted_points: ",lst)
print (f"distance {lst[-1]} - ({lst[1]}) = ", lst[-1]-lst[1])

#lvl 2
#1
def is_valid_variable(variable):
    if re.search(r"^[_a-zA-Z]\w*$", variable):
        return True
    else:
        return False


print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("_firstname"))

#lvl 3
#1
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?''' 
sub = re.sub("[$?!?@?!?:?;?,?&?%?#?\??]","",sentence)
print (sub)
def most_frequent_words(text):
    
    words = text.split()
    d = {}
    for word in words:
        d[word] = d.get(word,0) + 1
    list = [(val,key) for key,val in d.items()]
    list.sort(reverse=True)
    return list[:3]

print(most_frequent_words(sub))
