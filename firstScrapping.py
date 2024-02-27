#1nd import libraries
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest


job_title=[]#-->return list
company_name=[]
clocation_name=[]
job_skill=[]
links=[]
salary=[]

# 2nd step use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
# 3rd step save page content/markup
src = result.content
#print(src)
# 4th step create soup object to parse content
soup = BeautifulSoup (src, "lxml")
#soup = BeautifulSoup(src, 'html.parser')
#print(soup)
# 5th step find the elements containing info we need
#-- job titles, job skills, company names, location names
job_titles=soup.find_all("h2",{"class":"css-m604qf"})#-->return list
company_names=soup.find_all("a",{"class":"css-17s97q8"})
clocation_names=soup.find_all("span",{"class":"css-5wys0k"})
job_skills=soup.find_all("div",{"class":"css-y4udm8"})
# 6th step loop over returned lists to extract needed info into other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    clocation_name.append(clocation_names[i].text)
    job_skill.append(job_skills[i].text)
"""for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup (src, "lxml")
    #get salaries
    salaries=soup.find("span",{"class":"css-4xky9y"})
    print(salaries)
    #salary.append(salaries.text)"""
    
# 7th step create csv file and fill it with values
file_list=[job_title,company_name,clocation_name,job_skill,links]
exported=zip_longest(*file_list)
with open("C:\\Users\\user\\Desktop\\Coding\\Script_Project_files\\jobs1_egypt.csv",'w') as myFile:
    wr=csv.writer(myFile)
    wr.writerow(["job titles","company names","clocation names","job skills","links"])
    wr.writerows(exported)


