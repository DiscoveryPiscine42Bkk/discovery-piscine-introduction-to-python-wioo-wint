#!/bin/python3
def find_the_redheads(family):
    red_hairs = dict(filter(lambda family: "red" in family, family.items()))
    return list(red_hairs.keys())
    

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))