# importer listen af navne fra txt filen og omdanner til en liste i python..

# åbner txt filen i read mode
name_file = open("opgave_1\\Navne_liste.txt", "r")

# læser filen
name_data = name_file.read()

# opdeler elementerne ved komma i en liste
name_data_list = name_data.split(",")

# lukker txt filen
name_file.close()

# printe listen alfabetisk
name_data_list_alpha = sorted(name_data_list)
#print(name_data_list_alpha)

# printe listen efter længden af navne
name_data_list_len = sorted(name_data_list, key=len)
#print(name_data_list_len)


#optælling af enkelte bogstaver

# opretter en tom dict
letter_count = {}

#itererer over navne i vores liste
for name in name_data_list:
    # gør alle bogstaver små så der ikke skelnes
    name_low = name.lower()
    #itererer over hvert bogstav i enkelte navne og inkrementerer en værdi for det enkelte bogstav som sættes som key, værdien som value
    for letter in name_low:      
            if letter in name:
                
                letter_count[letter] = letter_count.get(letter,0) + 1
          

    
          
#print(letter_count)
#### work in progress

import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np
from PIL import Image

keys = list(letter_count.keys())
values = list(letter_count.values())

# Frekvensanalyse

# sns.barplot(data = letter_count, x=keys, y = values)
# plt.show()

# Wordcloud
wc = WordCloud(background_color="white",width=1000,height=1000).generate_from_frequencies(letter_count)
plt.figure(figsize=(15,8))
#plt.imshow(wc)
#plt.show()


# NAVNELÆNGDE ANALYSE

# optælling af antal bogstaver i navne

from collections import defaultdict

name_data_dict = defaultdict(list)

for name in name_data_list:
    count = len(name)
    name_data_dict[name].append(count)

        
# print(name_data_dict)

# frekvensen af navne af en given længde..
dict(name_data_dict)

freq_dict = defaultdict(int)

for key, val in name_data_dict.items():
    for count in val:
        freq_dict[count] += 1

print(freq_dict)

len_key = list(freq_dict.keys())
len_val = list(freq_dict.values())
sns.barplot(data = freq_dict, x = len_key, y = len_val)
#plt.show()

# median navnelængde

alle_values = []
for key, value in freq_dict.items():
    alle_values.extend([key] * value)

median = np.median(alle_values)
print(f"Medianen er = {median}")
      
# mean navnelængde

total_count = sum(freq_dict.values())

mean = sum(key * value for key, value in freq_dict.items()) / total_count

print(f"Gennemsnittet er = {mean}")

"""
plt.figure(figsize=(10, 8))
sns.boxplot(x=len_key,
            y=len_val,
            data=freq_dict,
            showmeans=True)  # notice the change
plt.ylabel("Antal_personer", size=14)
plt.xlabel("Antal_bogstaver", size=14)
plt.show()"""