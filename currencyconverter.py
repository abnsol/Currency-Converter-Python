print()                                                                                              # i used print() through out the proram to make the interface look good thats all
print('For the inputs please only use formal currency abreviations')
print()
k=str(input("""Do you like to convert your currency using stored exchange rate or live exchange rate?
            If you want live exchange rates type 'live' ,else type 'stored':  """ ))
k=k.lower()
print()

# THE NEXT FUNCTION I BUILT WILL FETCH LIVE EXCHANGE RATES FROM RAPID API, I USED THAT EXCHANGE RATE TO CONVERT OUR CURRENCIES
if k=='live':
    print("""#DEPENDENCY 
        To have online exchange rates you have to download a request library and have internet access.
        If You don't have request the library download 'virtual enviroment' folder from the drive link below
        First watch the video on how to extract the file and then extarct the folder in 'DESKTOP'.It contains all the libraries needed
        https://drive.google.com/drive/folders/1v-NSaPx9PDVx1QshDByUwslAd4_XQES1?usp=drive_link""")
    print()  
    x=str(input("Currency you want to convert: "))
    x=x.upper()
    print()              
    y=str(input("Currency you want to convert to: "))
    y=y.upper()
    print()
    try:                                                                                             # defensive programming for error that might happen
        z=float(input("Amount to be converted: "))
    except ValueError:
        pass
    print()

    try:
        import requests
    except (ModuleNotFoundError,ImportError):
        print(""" # you don't have request library.
              To have online exchange rates you have to download a request library
              If You don't have request the library download 'virtual enviroment' folder from the drive link below
              First watch the video on how to extract the file and then extarct the folder in 'DESKTOP'.It contains all the libraries needed
              https://drive.google.com/drive/folders/1v-NSaPx9PDVx1QshDByUwslAd4_XQES1?usp=drive_link""")
        print()
        exit()                                                                                       # stop running this file
    
    def every_currency(x,y,z):
        #I used RapidAPI to get our live exchange rates.
        Ex_rate_fetch_link = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest"  # the link where i get our exchange rates from
        #from line 44-48 the code is provided by the rapidAPI website to satisfy its input
        p = {'base':x}                                                                               # required by the api to show the base currency from which i convert 
        headers = { "X-RapidAPI-Key": "c87d5b1b4cmsh69c1cf3ed13b35fp1c3445jsn3ead3d585a5d",          # contains an info required by the api(subscription info)                            
                    "X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com" }                                                
        ex_rates_data1 = requests.get(Ex_rate_fetch_link, headers=headers, params=p)                 # fetches all exchange rate datas from website
        All_Exchange_rates1= ex_rates_data1.json()                                                   # this json file contain all the exchange rates(check it by print())                                                                                              
        
        Exchange_rate1= All_Exchange_rates1['rates'][y]                                              # this will extract the exchange rate needed from the json file
        print("The exchange rate is 1",x,"=",round(Exchange_rate1,3),y)
        print()
        a=z*Exchange_rate1
        return round(a,4)

elif k=='stored':
    print()
    print("""The stored currency converter only converts USD,ETB and GBP(with exchange rate recorded on 29/08/2023).
        Therefore only choose from the 3.""")
    print()
    x=str(input("Currency you want to convert: "))
    print()              
    y=str(input("Currency you want to convert to: "))
    print()
    try:
        z=float(input("Amount to be converted: "))
    except ValueError:
        pass
    print()
    x=x.upper()
    y=y.upper()

    # THE NEXT 3 FUNCTIONS WILL NOT USE LIVE EXCHANGE RATE (DOESN'T UPDATE EXCHANGE RATE VALUES), The exhange rates are according to the date 29/08/2023

    def GBP_ETB(x,y,z):                                
        if x=="GBP" and y=="ETB":
            a=z*69.66
            return round(a,4)
        elif x=="ETB" and y=="GBP":
            a=z*0.014
            return round(a,4)

    def USD_ETB(x,y,z):
        if x=="USD" and y=="ETB":
            a=z*55.23
            return round(a,4)
        elif x=="ETB" and y=="USD":
            a=z*0.018
            return round(a,4)

    def GBP_USD(x,y,z):
        if x=="GBP" and y=="USD":
            a=z*1.26
            return round(a,4)
        elif x=="USD" and y=="GBP":
            a=z*0.79
            return round(a,4)
else:
    print('Invalid Input')
        
# MAIN FUNCTION 
def main():
    if k=='stored':
        try:                                                                                         # defensive programming for errors that could result                    
            m=GBP_ETB(x,y,z)
            n=USD_ETB(x,y,z)
            o=GBP_USD(x,y,z)
            if (m or n or o)==None:                                                                  # defensive programming for error that might occur in input 
                print('Invalid input')
            else:
                print(z,x,"is",m or n or o,y)
        except (ValueError,NameError):
            print("Invalid Amount")
         
    elif k=='live':
        try:                                                                                        # defensive programming for errors that could result
           l=every_currency(x,y,z)  
           print(z,x,"is",l,y) 
        except (KeyError,NameError,ValueError):
            print("""Couldn't be executed. check if you used correct currency abbreviation and amount number.""")
        except (requests.exceptions.ConnectionError):
            print("""Couldn't be executed. check if you have connected to internet""")
    print()  

if __name__=='__main__':
    main()
