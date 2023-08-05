def full_emails(people):
    result=[]
    for email,name in people:
        result.append("{}<{}>".format(name,email))
    return result
print(full_emails([("kmnaveen2410@gmail.com","naveen k m"),("kmnaveen1110@gmail.com","naveeeen k m")]))
