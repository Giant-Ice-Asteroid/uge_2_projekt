"""
Opgave 4: Pandas

1. Læs filen ind 
    a. Brug read_csv 
    b. Print de første 10 data ud 
2. Group by bruges til at  sortere colouner efter grupper 
    a. Lav et group by på region 
    b. Lav et gennemsnit over purchases 
    c. Print resultatet ud 
3. Mere advanceret Group by 
    a. Lav group by på house_type 
    b. Lav et group by på region 
    c. Lav et gennemsnit over purchases 
    d. Plot det vedhjælp af matplotlib 
4. Eksperimenter med at group by og avarage over forskellige coulumns og plot resulteter
"""

# opgave 4.1

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("opgave_4\\DKHousingPricesSample100k.csv") 
#print(df) # printer by default de første 5 og sidste 5 entries
#df.info()
#print(df.describe())


# opgave 4.2


price_by_region = (df.groupby("region")["purchase_price"].mean())


# opgave 4.3


price_by_house_type = df.groupby("house_type")["purchase_price"].mean()

price_by_region_and_house_type = df.groupby(["region", "house_type"])["purchase_price"].mean()

# Plotter bar plot
plt.figure(figsize=(10, 6))
price_by_region_and_house_type.plot(kind='bar', width=0.8)
plt.title('Mean price by region and house type')
plt.xlabel('region')
plt.ylabel('purchase_price')
plt.legend(loc='best')
plt.grid(axis='y')
plt.show()

# opgave 4.4