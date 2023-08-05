def replace_domain(email,old_domain,new_domain):
    if "@"+old_domain in email:
        index=email.index("@"+old_domain)
        new_email=email[:index]+"@"+new_domain
        return new_email
    return email
email=input("enter the email")
i=email.index("@")
old_domain=email[i+1:] 
new_domain=input("enter the new domain")
print(replace_domain(email,old_domain,new_domain))

    