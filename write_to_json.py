import json
from html_parser import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#scrap workouts from swimmingworldmagazine .com
# """ create a dictionary(dic) with the difficulty of the workout at the keys
# 	for each key fill it with a dictionary with the workout name as the keys
# 	for the inner dictionary have tags for (author,duration,type,link)

# 	for each key in the dictionary dic(referenced above) find the drop down for workout difficulty from
# 	"http://www.swimmingworldmagazine.com/swim-cgi/work_search.pl" and select the value of the dropdown option list
# 	according to the loop iteration then click the search button all using Selenium and the chrome webdriver

# 	Next, scrape the table loaded through the search query using html_tables and save it to the corresponding key in 
# 	dic
# 																		"""


counter = 1
dic = {}
dic["Lap Swimmer"] = {}
dic["Masters Level 1"] = {}
dic["Masters Level 2"] = {}
dic["Masters Level 3"] = {}
dic["USS ABC Level"] = {}
dic["USS Pre-Senior Level"] = {}
dic["USS Sr./Jr. National Level"] = {}
dic["Aquatic Fitness"] = {}

driver = webdriver.Chrome()
driver.get("http://www.swimmingworldmagazine.com/swim-cgi/work_search.pl")
assert "Swimming World - Workouts" in driver.title

for keys in dic.keys():
	if counter == 1:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =1]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#work
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()

	if counter == 2:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =2]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#works
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()

	if counter == 3:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =3]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#works
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()

	if counter == 4:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =4]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#works
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()

	if counter == 5:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =5]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#works
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()
		
	if counter == 6:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =6]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#works
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()

	if counter == 7:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =7]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#works
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()

	if counter == 8:
		element = driver.find_element_by_xpath("//select[@name='work_cat']/option[@value =8]").click()#works
		submit = driver.find_element_by_xpath("//input[@type='submit' and @value='    Search    ']").click()#works
		workouts = html_tables(driver.current_url)
		dic[keys] = workouts.read_swim_workouts_table()
	counter += 1
driver.close()

# for keys in dic.keys():
# 	print(keys)
# 	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# 	for item in dic[keys].keys():
# 		print (item +"\n\t" + dic[keys][item]["link"] + "\n\t" + dic[keys][item]["type"] + "\n\t" + dic[keys][item]["author"] + "\n\t" + dic[keys][item]["duration"])

with open("workouts.json", "w") as writeJSON:
    json.dump(dic, writeJSON)
