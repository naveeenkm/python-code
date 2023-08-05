def get_username():
    username=input("enter the username")
    return username
def valid_username(username):
    if(username=="naveen"):
        print("user name is valid")
        return True
    else:
        return False
username=get_username()
while not valid_username(username):
    print("enter the correct user name")
    username = get_username()