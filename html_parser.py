import os
import re
import requests
import urllib
import math
import copy
import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup 

class html_tables(object):
    
    def __init__(self, url):
        
        self.url      = url
        self.r        = requests.get(self.url)
        self.url_soup = BeautifulSoup(self.r.text,"lxml")
        
    def read_swim_workouts_table(self):
        prefix = "http://www.swimmingworldmagazine.com/swim-cgi/"
        self.data      = {}
        self.tables_html = self.url_soup.find_all("table")

        n_columns = 0
        n_rows = 0

        for row in self.tables_html[3].find_all("tr"):
            column_data = row.find_all("td")
            href_link = row.find_all("a")
            name = re.sub("\s+",' ',column_data[2].text)
            if href_link != []:    
                self.data[name] ={}

        for row in self.tables_html[3].find_all("tr"):
            column_data = row.find_all("td")
            href_link = row.find_all("a")
            if href_link != []:

                self.data[re.sub("\s+",' ',column_data[2].text)]["link"] = prefix + href_link[0]["href"]
                temp = re.sub("\s+",' ',column_data[1].text)
                self.data[re.sub("\s+",' ',column_data[2].text)]["type"] = temp
                temp = re.sub("\s+",' ',column_data[3].text)
                self.data[re.sub("\s+",' ',column_data[2].text)]["author"] = temp
                temp = re.sub("\s+",' ',column_data[4].text)
                self.data[re.sub("\s+",' ',column_data[2].text)]["duration"] = temp


        return (self.data)

    def write_swim_workout(self):
        self.tables_html = self.url_soup.find_all("table")
        data = []

        for row in self.tables_html[5].find_all("tr"):
            temp = ""
            for column in row.find_all("td"):
                text = column.text
                text = " ".join(text.split())
                if text == "":
                    break
                data.append(text)
        print(data[0] + "\t\t" + data[1] + "\t\t" + data[2])
        print(data[3] + "\t\t" + data[4] + "\t\t" + data[5])
        print(data[6] + "\t\t" + data[7] + "\t\t" + data[8])
        print(data[9] + "\t\t" + data[10] + "\t\t" + data[11])
        print(data[12] + "\t\t" + data[13] + "\t\t" + data[14])
        print(data[15] + "\t\t" + data[16] + "\t\t" + data[17])
        print(data[18] + "\t\t" + data[19] + "\t\t" + data[20])


                



