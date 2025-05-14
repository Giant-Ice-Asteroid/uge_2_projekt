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

import pandas as pd # datanalyse
import matplotlib.pyplot as plt  # visualisering af data
import os # håndtering af filstier

file_path = os.path.join("data", "DKHousingPricesSample100k.csv")
df = pd.read_csv(file_path) 

# Print de første 10 data ud:
print("First 10 row of the dataset: ") 
print(df.head(10))

# Info om datasættet:
print("\nDataset info: ")
df.info()

# Statistisk overblik:
print("\nStatistical summary:")
print(df.describe())

# resume over manglende værdier:
print("\nMissing values per individual column:")
print(df.isnull().sum())


# opgave 4.2

# grouped efter regionen sammenholdt med gennemsnitlig salgspris, og sorteret (faldende)
price_by_region = (df.groupby("region")["purchase_price"].mean().sort_values(ascending=False))

print("\nAverage purchase price by each region:")
print(price_by_region)


# opgave 4.3

# grouped ejendomstype type og sammenholdt med gennemsnitlig salgspris(faldende)
price_by_house_type = df.groupby("house_type")["purchase_price"].mean().sort_values(ascending=False)
print("\nAverage purchase price by house type:")
print(price_by_house_type)

# grouped region OG huse type og sammenholdt med gns salgspris(unstack for seperate søjler ved plot):

price_by_region_and_house_type = df.groupby(["region", "house_type"])["purchase_price"].mean().unstack()

# Visualisering - søjlediagram/barplot
price_by_region_and_house_type.plot(kind='bar', figsize=(12, 8))
# tilføjer titler og labels og justerer 
plt.title('Average Purchase Price by Region and House Type', fontsize=14)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Average Purchase Price (DKK)', fontsize=12)
plt.legend(title='House Type') # legend boks 
plt.xticks(rotation=45, ha='right') # roterer skrift på x-aksen
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # holder grafikken inden for boksen
plt.show()


# opgave 4.4

# grouped region efter pris per kvadratmeter  
sqm_price_by_region = df.groupby("region")["sqm_price"].mean().sort_values(ascending=False)

print("\nPrice per Square meter by region:")
print(sqm_price_by_region)

# Visualisering med søjlediagram
sqm_price_by_region.plot(kind='bar', figsize=(12, 8))
plt.title('Average Price per Square Meter by Region', fontsize=16, pad=20)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Average Price per sqm (DKK)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()