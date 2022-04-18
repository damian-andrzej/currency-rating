from bs4 import BeautifulSoup
from datetime import date
import requests,xlsxwriter,openpyxl
import pandas as pd

#links to site for appropiate currency
site = f"https://www.bankier.pl/waluty/kursy-walut/nbp/"
euro_site=f"{site}EUR"
chf_site=f"{site}CHF"
usd_site=f"{site}USD"
rubel_site=f"{site}RUB"
print(euro_site)
today = date.today()
#load excel data
dane_excel = pd.read_excel("abc.xlsx",index_col=False)
print(dane_excel)

def currency(site):

    respone = requests.get(site)
    web_page = respone.text
     # pobiera aktualny kurs euro
    soup = BeautifulSoup(web_page,"html.parser") #webScraper object
    res = soup.find(name="div", class_='profilLast') #div with currency value
     #scrap Text value from div
    res1 = res.getText()# display 4,682 zl
    #split() divide variable on 2 parts, space is default separator
    res2 = res1.split()[0] #display 4,582
    res3 = float(res2.replace(",",".")) #string to float convertsion
    return res3


def save_data(data,euro,chf,usd,rubel):
    #creating new dataFrame object with values of currencies, currency() function
    df = pd.DataFrame({'Data': [today], 'EURO': [euro],'CHF':[chf],'USD':[usd],'Rubel':[rubel]})
    #add df dataFrame to dane_excel dataFrame(loaded excel sheet)
    d = dane_excel.append(df)
    print(d)
    #save to file operation, without that data wont be saved
    d.to_excel('abc.xlsx', sheet_name='Sheet1', index=False)

#execution of program
save_data(today,currency(euro_site),currency(chf_site),currency(usd_site),currency(rubel_site))


