def replace_date(scedule,old_date,new_date):
    if scedule.endswith(old_date):
        p=len(old_date)
        new_scedule=scedule[:-p]+new_date
        return new_scedule
    return scedule
print(replace_date("Last years annual report will be released in March 2023", "2023", "2024")) 
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
print(replace_date("The convention is scheduled for October", "October", "June"))