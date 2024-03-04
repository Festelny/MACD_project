import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

data = pd.read_csv('xauusd_d.csv')
data2=  pd.read_csv('wig20_d.csv')

def getData(column_name):
    data = pd.read_csv('Dane historyczne dla WIG20.csv')
    return data[column_name].to_numpy()


def ema(dane,N,pocz):
    numerator=dane.at[N,'Zamkniecie']
    denominator=1
    alfa=(2/(N+1))
    for i in range(1,N):
        if(pocz-i>=0):
            numerator+=((1-alfa)**i)*dane.at[pocz-i,'Zamkniecie']
        
    for i in range(1,N):
        if(pocz-i>=0):
            denominator+=(1-alfa)**i

    return numerator/denominator

def signalfunction(macd,N,pocz):
    numerator=macd[pocz]
    denominator=1
    alfa=(2/(N+1))
    for i in range(1,N):
        if(pocz-i>=0):
            numerator+=((1-alfa)**i)*macd[pocz-i]
        
    for i in range(1,N):
        if(pocz-i>=0):
            denominator+=(1-alfa)**i

    return numerator/denominator

def macdfunction(dane):
    i=0
    macd=[]
    signal=[]
    for i in range(1,dane.shape[0]):
        ema12=(ema(dane,12,i))
        ema26=(ema(dane,26,i))
        macd.append(ema12-ema26) 
        signal.append(signalfunction(macd,9,i-1))
    return macd,signal

def buysellplt(dane):
    plt.subplot(2, 1, 1)
    for i in range(2,dane.shape[0]):    
        leftcol=i-1
        lefftcol=i-2
        if macdf[leftcol]>signal[leftcol] and macdf[lefftcol]< signal[lefftcol]:
            plt.scatter(i,dane.at[i,'Zamkniecie'],c='green',s=12)
        elif macdf[leftcol]<signal[leftcol] and macdf[lefftcol]>signal[lefftcol]:
            plt.scatter(i,dane.at[i,'Zamkniecie'],c='red',s=12)
    plt.plot(data['Zamkniecie'])
    return 

def investor(stock,dane,macdf,signal):
    zarobek=stock*dane.at[0,'Zamkniecie']
    for i in range(2,dane.shape[0]):    
        leftcol=i-1
        lefftcol=i-2
        if macdf[leftcol]>signal[leftcol] and macdf[lefftcol]< signal[lefftcol]:
            #kupowanie
            stock=zarobek/dane.at[i,'Zamkniecie']
            math.floor(stock)
            zarobek-=stock*dane.at[i,'Zamkniecie']
        elif macdf[leftcol]<signal[leftcol] and macdf[lefftcol]>signal[lefftcol]:
            if(stock>0):#sprzedaz
                zarobek+=stock*dane.at[i,'Zamkniecie']
                stock=0
    if(stock!=0):
        zarobek+=stock*dane.at[dane.shape[0],'Zamkniecie']
    return zarobek


#print(data.to_string())
"""
plt.subplot(2, 1, 1)
plt.plot(data['Zamkniecie'])
plt.xlabel('nr rekordu')
plt.ylabel('wartosc')
"""

macdf,signal=macdfunction(data)
buysellplt(data)
plt.subplot(2, 1, 2)
plt.plot(macdf, linestyle='-',label='MACD')
plt.plot(signal, linestyle='-',color='red',label='SIGNAL')
plt.legend()
#wynik=investor(1000,data,macdf,signal)
#print("Wynik kocowy to:"+wynik)

# Wyświetlamy wykresy
plt.show()
