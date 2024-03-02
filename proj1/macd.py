import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('xauusd_d.csv')

def ema(dane,N):
    numerator=dane.at[N,'Zamkniecie']
    denominator=1
    alfa=(2/(N+1))
    for i in range(1,N):
        numerator+=((1-alfa)**i)*dane.at[N-i,'Zamkniecie']

    for i in range(1,N):
        denominator+=(1-alfa)**i

    return numerator/denominator


#print(data.to_string())
essa=ema(data,12)
plt.subplot(2, 1, 1)
plt.plot(data['Zamkniecie'])
plt.xlabel('nig')
plt.ylabel('er')
plt.subplot(2, 1, 2)
plt.plot(data['Otwarcie'])
plt.xlabel('Weight')
plt.ylabel('MPG')

# Wyświetlamy wykresy
plt.show()
print(essa)