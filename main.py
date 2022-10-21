import requests
from bs4 import BeautifulSoup
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="exampledb",
    user="docker",
    password="docker"
)
conn.autocommit = True
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS scrapeData(id SERIAL PRIMARY KEY, postDay VARCHAR, postHead VARCHAR, postBody VARCHAR, postAuthor VARCHAR);")



getUrl = requests.get('https://blog.python.org')
recvHtml = getUrl.content



bsObj = BeautifulSoup(recvHtml,'html.parser')

# print(bsObj.find_all( class_ = "date-outer" ))
pbar=""
for post in bsObj.find_all("div",class_ = "date-outer" ):
    postVar=""
    date = post.find("h2",class_="date-header")
    dateVar = date.text


    main_head = post.find(class_="post-title entry-title")
    headVar = main_head.text
