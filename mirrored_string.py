def mirrored_string(my_string):
    forword=""
    backword=""
    for charcter in my_string:
        if charcter.isalpha():
            forword+=charcter
            backword=charcter+backword
    
    if forword.lower()==backword.lower():
        return True
    return False
print(mirrored_string("12 noon"))
print(mirrored_string("vineeth is chodu is vineeth"))
print(mirrored_string("eve ,maDam EVE"))
        