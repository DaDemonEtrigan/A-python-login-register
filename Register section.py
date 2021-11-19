# -*- coding: utf-8 -*-
# dev : BloodHunter
# state : Indev (In development)
#About : this is the code for putting a username in the json file, its in write mode
# you can write as much as users with passwords you want it will save but if you do it again the last data will be deleted
# this will be fixed soon its still indev
import json

mydict = {}
print("Put username and password 0 once and the loop will break")
while True:
    user = input("username : ")
    passw = input("password : ")
    if user == "0" and passw == "0":
        break
    mydict[user] = passw
print(mydict)

Data = json.dumps(mydict, indent=4)
with open('userpass.json', 'w') as file:
    file.write(Data)
