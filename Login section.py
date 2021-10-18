# -*- coding: utf-8 -*-
# dev : BloodHunter
# state : Indev
#About : this is the code for just logging into the user(s) you saved in Register Section.py
# it will search for every user and their own password
# if its wrong it will send login failed and if its right it will say welcome and close the program
# idk what your going to do with this but this is just for my project and it might be useful when its finished
#P.S : the json file will be created if you dont create it yourself
import json

with open('userpass.json', 'r') as file:
    json_obj = json.loads(file.read())

flag = False
while True:
    username = input("Username : ")
    password = input("password : ")

    for key in json_obj:
        if json_obj[key] == password and key == username:
            flag = True
            break
        elif json_obj[key] != password and key != username:
            flag = False

    if flag:
        print('welcome')
        break
    else:
        print('login failed, try again')
