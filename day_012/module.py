import random
import string

def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"
print(rgb_color_gen())

print(rgb_color_gen())

def list_of_rgb_colors(x):
    return [rgb_color_gen() for i in range(x)]

print(list_of_rgb_colors(7))
def list_of_hexa_colors(x):
     a= ["".join(str(random.choice('abcdef' + string.digits)) 
                 for i in range(6)) 
                 for j in range(x)]
     b =['#' + item for item in a]
     return b
print(list_of_hexa_colors(6))

def generate_colors(col_type,many):
    if col_type == 'hexa':
        return list_of_hexa_colors(many)
    elif col_type == 'rgb':
        return list_of_rgb_colors(many)
    else:
        return "Invalid Input"
print(generate_colors("hexa", 18))

def shuffle_list(list):
    random.shuffle(list)
    return list
print(shuffle_list([1,2,3,4,5]))