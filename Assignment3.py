#1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

person = [ 
            {
            'name': 'Tom',
            'age': 20,
            'hobbies' : ['football', 'armwrestling']
            },

            {
            'name': 'Dick',
            'age': 30,
            'hobbies' : ['MMA', 'Dancing']
            },

            {
            'name': 'Harry',
            'age': 40,
            'hobbies' : ['golf']
            }
         ]


#2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
def name_conversion():
    list_of_names = []
    return [list_of_names.append(n['name']) for n in person if 'name' in n]

y  = name_conversion()
print(y)
#3) Use a list comprehension to check whether all persons are older than 20.
'''
def check_age():
    return [person['name'] for el in person['name'] if person['age'] > 20 ]


#4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

def first_person():
    return [person['name'][0] for n, keys, in person.values()]

#5) Unpack the persons of the original list into different variables and output these variables.

a, b, c = person
[print() for el in person]
'''