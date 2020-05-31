import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup


result=input('İlçe ismini giriniz(ingilizce karakter ile): ')
z = int(input("Kaç metrekare? "))


url="https://www.-----.com/"+result+"-satilik-daire"

html=response=requests.get(url).content
soup=BeautifulSoup(html, 'html.parser')




list=soup.find_all("li", {"class":"zl-card"})
x=[]
y=[]

for li in list:
    squares=float(li.find('div',{'class':'zlc-tags'}).find_all('span')[1].text.strip().strip('m²'))
    prices=float(li.find('div',{'class':'zlc-features'}).find('div',{'class':'feature-item feature-price'}).text.strip().strip('TL'))
    
    
    x.append(squares)
    y.append(prices)
    
   
x = np.reshape(x,(21,1))
y = np.reshape(y,(21,1))

lineerregresyon = lr()

lineerregresyon.fit(x,y)

lineerregresyon.predict(x)

m=lineerregresyon.coef_
b=lineerregresyon.intercept_

a = np.arange(150)

plt.scatter(x,y) # nokta nokta yazmak için
plt.scatter(a, m*a+b)


tahmin = m*z+b
print(tahmin)

plt.show()




