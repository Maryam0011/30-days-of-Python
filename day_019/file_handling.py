import re
import json
import csv

#1
def count_words_lines(file):
    with open(file) as f:
        lines = f.readlines()
        words = []
        for line in lines:
            line = re.sub(r'[^\w\s]','',line)
            words.extend(line.split())
    print(f'The number of lines and words in the file are {len(lines)} and {len(words)} respectively')
count_words_lines('obama_speech.txt')
count_words_lines('donald_speech.txt')
count_words_lines('michelle_obama_speech.txt')
count_words_lines('melania_trump_speech.txt')

#2
def most_spoken_languages(file,n):
   
    with open(file , encoding='utf8') as f:
        list = json.loads(f.read())
    languages = []
    for i in range(len(list)):
        languages.extend(list[i]['languages'])
    lang = {}
    for language in languages:
        lang[language] = lang.get(language,0) + 1
    sorted_lang = sorted(lang.items(), key= lambda x:x[1],reverse=True)
    result = [(item[1],item[0]) for item in sorted_lang]
    return result[:n]
most_spoken_languages('day_019/countries_data.json',3)

#3
def most_populated_countries(filename,n):
    
    with open(filename) as f:
        dic_list = json.loads(f.read())
    population = dict()
    for i in range(len(dic_list)):
        keys = dic_list[i]['name']
        values = dic_list[i]['population']
        population[keys] = values
    sorted_lt = sorted(population.items(), key= lambda x:x[1],reverse=True)
    final_list = [{'country':item[0],'population':item[1]} for item in sorted_lt]
    return final_list[:n]

most_populated_countries('day_019/countries_data.json',7)

#4
with open('day_019/email_exhange_big.txt') as f:
    lines = f.readlines()
email_addresses = []
for line in lines:
    email_addresses.extend(re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line))
email_addresses[:] 

#5
from collections import Counter
def find_most_common_words(fname, value):
    text = open(fname).read()
    split_it = text.split()
    Cnter = [(sub[1], sub[0]) for sub in Counter(split_it).most_common()]

    return Cnter[:value]


print(find_most_common_words('romeo_and_juliet.txt', 10))
print(find_most_common_words('donald_speech.txt', 10))
print(find_most_common_words('melania_trump_speech.txt', 10))
print(find_most_common_words('michelle_obama_speech.txt', 10))
print(find_most_common_words('obama_speech.txt', 10))





def clean_text(file):
   
    with open(file) as f:
        lines = f.readlines()
        words = []
        for line in lines:
            words.extend(line.split())
    return words


clean_text('day_019/michelle_obama_speech.txt') 

def check_text_similarity(list_one,list_two):
    res = [x for x in (list_one + list_two) if x in list_one and x in list_two]
    similar_words_percent = (len(res)/(len(list_one) + len(list_two))) * 100
    return similar_words_percent
check_text_similarity(['apple','banana','mango','pawpaw'],['apple','mango','pear']) 


from stop_words import stop_words

def remove_stop_words(list):
    return [word for word in list if word.lower() not in stop_words]
remove_stop_words(clean_text('michelle_obama_speech.txt'))  

def comparing_text_in_file_similarity(file_one,file_two):
    '''Gives the percentage of similar words in two different files'''
    file_one_words = remove_stop_words(clean_text(file_one))
    file_two_words = remove_stop_words(clean_text(file_two))
    return check_text_similarity(file_one_words,file_two_words)

comparing_text_in_file_similarity('michelle_obama_speech.txt','day_019/melania_trump_speech.txt') # Got 41.73% similarity. 
#8
print('10 most common words in romeo and juliet: ',find_most_common_words('romeo_and_juliet.txt'))

#9
def hacker_count(fname):
    csvFile = csv.reader(open(fname, mode="r"))
    count_a = 0
    count_b = 0
    count_c = 0
    for lines in csvFile:
        plain_text_line = " ".join(lines)
        if "python" in plain_text_line or "Python" in plain_text_line:
            count_a += 1
        if (
                "JavaScript" in plain_text_line
                or "Javascript" in plain_text_line
                or "javascript" in plain_text_line
        ):
            count_b += 1
        if not (not ("Java" in plain_text_line) or "Javascript" in plain_text_line):
            count_c += 1
    print(count_a, count_b, count_c)

hacker_count('hacker_news.csv')