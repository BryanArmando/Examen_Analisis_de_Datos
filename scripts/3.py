import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd
import bson
from bson.raw_bson import RawBSONDocument

db_client = MongoClient()
my_db = db_client.cursos
my_posts = my_db.posts
    
def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))

response = requests.get("https://olympics.com/es/noticias/")
soup = BeautifulSoup(response.content, "lxml")

Course=[]
Provider=[]
Duration=[]
Start_Date=[]
Offered_By=[]
No_Of_Reviews=[]
Rating=[]


post_all = soup.find_all("div", class_="card__body")
post_course=soup.find_all("h2", class_="module-subtitle-big")
post_provider=soup.find_all("p", class_="")

extracted = []
    
for element in post_course:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Course.append(limpio.strip())

for element in post_provider:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element,'<')])
    Provider.append(limpio.strip())

print(Course)
print(Provider)


unavez=pd.DataFrame({'titulo':Course, 'noticia':Provider})
out=unavez.to_dict()
dfDS.to_csv('JuegosOlimpic.csv')