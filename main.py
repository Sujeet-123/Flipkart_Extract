import requests
from bs4 import BeautifulSoup
import pandas as pd

# page_nums = input("Enter number of pages ")


phn_Name = []
phn_Price = []
phn_Rating = []
phn_Spec = []


# for i in range(1,int(page_nums)+1):
url ="https://www.flipkart.com/search?q=apple%20iphone%2011%20&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
req = requests.get(url)
content = BeautifulSoup(req.content,'html.parser')

name = content.find_all('div',{"class":"_4rR01T"})
price = content.find_all('div',{"class":"_30jeq3 _1_WHN1"})
rating = content.find_all('div',{"class":"_3LWZlK"})
spec = content.find_all('div',{"class":"fMghEO"})

for i in name:
    phn_Name.append(i.text)
# print(phn_Name)

for i in price:
    phn_Price.append(i.text)
# print(phn_Price)


for i in rating:
    # print(i)
    phn_Rating.append(i.text)
# print(phn_Rating)


for i in spec:
    phn_Spec.append(i.text)
# print(phn_Spec)



print(len(phn_Name))
print(len(phn_Price))
print(len(phn_Rating))
print(len(phn_Spec))




data ={
    "Phone Nam": phn_Name,
    "Phone Price": phn_Price,
    "Phone Rating": phn_Rating,
    "Feture": phn_Spec
}

df = pd.DataFrame.from_dict(data, orient='index')
df = df.transpose()

df.to_csv("flipkart.csv")





