import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

df = pd.read_csv('ListodCarLinks.csv')
sleep(2)
counter = 0
Brand=[]
Model=[]
Adtype = []
FuelType=[]
Price=[]
PriceType=[]
Year=[]
Kilometers =[]
TransmissionType = []
Condition= []
Color = []
BodyType = []
CarUrl=[]
tries = 0
for row in range (len(df.iloc[:])):
    x = df.iloc[row]
    while True:
        try:
            r = requests.get(x[0])

            soup = BeautifulSoup(r.content ,"lxml")
            Data = soup.find_all("div" , class_="b44ca0b3")
            for element in Data:
                try:

                    if element.findNext('span').text =="Brand":
                        Brand.append(element.findNext('span').find_next_sibling('span').text)
                        CarUrl.append(x[0])
                except:pass
                try:
                    if element.findNext('span').text =="Model":
                        Model.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Ad Type":
                        Adtype.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Fuel Type":
                        FuelType.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Price":
                        Price.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Price Type":
                        PriceType.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Year":
                        Year.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Kilometers":
                        Kilometers.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Transmission Type":
                        TransmissionType.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Condition":
                        Condition.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Color":
                        Color.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
                try:
                    if element.findNext('span').text =="Body Type":
                        BodyType.append(element.findNext('span').find_next_sibling('span').text)
                except:pass
            if len(Kilometers)<len(Brand):Kilometers.append("Not Availiable")
            if len(BodyType)<len(Brand): BodyType.append("Not Availiable")
            if len(Year)<len(Brand):Year.append('Not Available')
            if len(Color) < len(Brand): Color.append('Not Available')
            if r.status_code in [200 , 404]:
                break

        except Exception as e:
            tries += 1
            sleep(2)
            if tries > 6:
                print(e)
                print(" breaking while loop after scraping all data")
                sleep(5)
                break
    counter+=1
    print(f"We are now in link: {counter}")


print("Congratulations You finished your first step")


print(len(Brand) , len(Model) ,len(Adtype),len(FuelType),len(Year) , len(Price) ,len(PriceType),len(Kilometers) ,len(Condition) ,len(Color) , len(BodyType),len(TransmissionType) , len(CarUrl))
df1 = pd.DataFrame({"Brand":Brand ,"Model": Model ,"Adtype" : Adtype , "Fuel" : FuelType , "Year":Year ,"Price":Price ,"PriceType":PriceType,"Kilometers":Kilometers,
                    "Condition":Condition ,"Color" : Color , "Transimition" : TransmissionType , "Bodytype":BodyType ,"CarUrl":CarUrl},
                    columns= ['Brand' , 'Model' , 'Adtype' ,'Fuel' , 'Year' , 'Price' ,'PriceType' , 'Kilometers' ,'Condition' ,'Color' , 'Transimition' ,'Bodytype' ,'CarUrl'])
df1.to_csv("HazemCarsDataOLXfinally.csv" , index= False)