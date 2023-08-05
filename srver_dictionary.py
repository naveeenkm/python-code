def sum_server_use_time(server):
    total_time=0.0
    for key,value in server.items():
        total_time+=server[key]
    return round(total_time,2)#round off two elements#
FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(sum_server_use_time(FileServer))
