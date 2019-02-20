#!/usr/bin/python3
#Made by RootX & Fangs
#02/19/2019

import os 
import sys
import colorama
from termcolor import colored

colorama.init()

print(colored("""

  _____             _____       _       _ _   
 |  __ \           / ____|     | |     (_) |  
 | |  | | _____  _| (___  _ __ | | ___  _| |_ 
 | |  | |/ _ \ \/ /\___ \| '_ \| |/ _ \| | __|
 | |__| | (_) >  < ____) | |_) | | (_) | | |_ 
 |_____/ \___/_/\_\_____/| .__/|_|\___/|_|\__|
                         | |                  
                         |_|                  
""", "red"))
print(colored("Codename   : Info Release", "green"))
print(colored("Version    : 1.0", "green"))
print(colored("Homepage   : https://discord.gg/bVVFBH", "green"))
print(colored("Join Slack : https://star-security.slack.com", "green"))

alias = input("Alias(S): ")
ssn = input("SSN: ")
name = input("Name: ")
age = input("Age: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zipcode = input("ZipCode: ")
country = input("Country: ")
continent = input("Continent: ")
occ = input("Occupation: ")
occadd = input("Occupation Address: ")
amount = int(input("How many social medias?: "))
sm = ""
for i in range(amount):
    social = input(">")
    sm +=  social + "\r\n"
fi = input("Family Info: ")
ch = input("Criminal History: ")
misc = input("Misc. Info: ")


with open("dox.txt", "a") as fd:
    fd.write("Alias(S): {}\r\n".format(alias))
    fd.write("SSN: {}\r\n".format(ssn))
    fd.write("Name: {}\r\n".format(name))
    fd.write("Age: {}\r\n".format(age))
    fd.write("Address: {}\r\n".format(address))
    fd.write("City: {}\r\n".format(city))
    fd.write("City: {}\r\n".format(state))
    fd.write("ZipCode: {}\r\n".format(zipcode))
    fd.write("Country: {}\r\n".format(country))
    fd.write("Continent: {}\r\n".format(continent))
    fd.write(":Occupation: {}\r\n".format(occ))
    fd.write("Occupation Address: {}\r\n".format(occadd))
    fd.write("How many social medias?: {}\r\n".format(amount))
    fd.write("Social Medias: {}\r\n".format(sm))
    fd.write("Family Info: {}\r\n".format(fi))
    fd.write("Criminal History: {}\r\n".format(ch))
    fd.write("Misc Info: {}\r\n".format(misc))

        