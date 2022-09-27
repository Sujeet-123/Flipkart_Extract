
import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=6c7d370e-4497-4254-aeb1-7d10232d9778"

req = requests.get(url)

content = BeautifulSoup(req.content,'html.parser')


ln2=[]

ln = []
lp = []
lr = []
lf = []


for d in content.find_all('div',{"class":"_2kHMtA"}):
    name = d.find('div',{"class":"_4rR01T"})
    price = d.find('div',{"class":"_30jeq3 _1_WHN1"})
    rating  = d.find('div',{"class":"_3LWZlK"})
    features = d.find('ul',{"class":"_1xgFaf"})

    # # print(name)

    
  
    ln.append(name.text)
    lp.append(price.text)
    lf.append(features.text)

    if rating==None:
        rating = 0


    lr.append(rating.text)

    
  

for i in ln:
    name = i.split("-")
    ln2.append(name[0])





data ={
    "Laptop Name": ln2,
    "laptop Price":lp,
    "laptop Rating": lr,
    "Feture": lf
}


df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()

df.to_csv("project2.csv")