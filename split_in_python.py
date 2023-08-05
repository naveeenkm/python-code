def change_string(my_string):
    new_string=""
    new_list=my_string.split()
    for element in new_list:
        new_string+=element[1:]+"-"+element[0]+"  "
    return new_string
print(change_string("1one 2two 3three 4four 5five"))     
        