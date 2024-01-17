import logging
import unittest

logging.basicConfig(level = logging.INFO)

def crate_dict_with_brackets( input_array : list ):
    brackets_dict = {}

    for i,char in enumerate(input_array):
        if char == "(" or char == ")":
            brackets_dict[i] = char

    return brackets_dict

def create_arrays( brackets_dict : dict ):
    for i in brackets_dict:
        print(i)
    

    
#Tests
#print(search_for_brackets(['(' ,'3','-', '2' ,')','+' ,'(', '3' , '+' , '5' , ')' , '=' ]))
#print(search_for_brackets(['(','(','3','+','3',')',')']))
#print(search_for_brackets(['3','+','3']))
        

print(create_arrays(crate_dict_with_brackets(['(','3','+','(','4','+','3',')','+','3',')'])))
    




           

       

