import json
import requests
from html_parser import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# data = json.load(open('workouts.json'))

# print(data["Lap Swimmer"][" breastroke workout "]["link"])

#How to create a file with a name and write to it
# filename = "%s.text" %list(data["Lap Swimmer"].keys())[0]
# f = open(filename, "w")
# f.write("test")
# f.close()

url = "http://www.swimmingworldmagazine.com/swim-cgi/show_workout.pl?pri_id=10000001279&work_cat=1"


workouts = html_tables(url)
workouts.write_swim_workout()