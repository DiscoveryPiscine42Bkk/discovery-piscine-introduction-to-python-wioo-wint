#!/bin/python3
def array_of_names(persons):
    persons_array = []
    for fname in persons:
        persons_array.append(fname.capitalize()+" "+persons[fname].capitalize())
    return persons_array

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))