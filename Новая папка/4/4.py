import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand = ''.join(random.choice(letters) for i in range(length))
    print("Рандомное слово из количества букв", length, "это:", rand)


generate_random_string(10)


#def fix(string):
    #s = set()
    #list = []
    #for ch in string:
        #if ch not in s:
            #s.add(ch)
            #list.append(ch)
    
    #return ''.join(list)        

#fix(string)
#print(fix(string))