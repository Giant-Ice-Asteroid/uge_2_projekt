"""
Opgave 1

Sortering af Navne: Start med at oprette en liste af navne (eventuelt kopier fra listen her) 
Brug Python's indbyggede sortering med en brugerdefineret nøgle for at sortere navnene 
først alfabetisk og derefter efter længde. 

Optælling af Bogstaver: Gå igennem hvert navn i den sorterede liste og tæl forekomsten af 
hvert bogstav. Gem disse tællinger i et dictionary, hvor nøglen er bogstavet og værdien er 
antallet af forekomster. 

Byg videre på den oprindelige opgave ved at udføre en detaljeret analyse af navnedataene. Efter at 
have talt forekomsten af hvert bogstav i alle navne, udfør følgende: 

Frekvensanalyse: Beregn og visualiser frekvensen af hvert bogstav anvendt i navnelisten. 
Overvej at bruge biblioteket matplotlib eller seaborn til at lave et histogram- eller 
søjlediagram, der viser de mest almindelige bogstaver 

Ordsky: Generer en ordsky (word cloud) baseret på hyppigheden af hvert bogstav. Jo oftere 
et bogstav forekommer, desto større skal det vises i ordskyen. Dette kan gøres 
med wordcloud biblioteket i Python. 

Navnelængde Analyse: Analyser fordelingen af navnelængder i dit dataset. 
Beregn gennemsnitlig og median for navnelængderne, og visualiser dataen med passende 
plots.
"""


import os
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from wordcloud import WordCloud



def name_list(name_file_path): 

    """funktion som læser listen af navne fra txt filen og omdanner til en liste."""    

    try:
        # forsøger at åbne den givne fil
        with open(name_file_path, "r") as file:
            data = file.read()
            names = [name.strip() for name in data.split(",")]
    except FileNotFoundError:
        print("File not found ;__;")
    #returner listen
    return names 
 

def sort_names(names):   

    """funktion som sorterer efter alfabetisk og efter længde. Returnerer en dict""" 

    alpha = sorted(names)
    length = sorted(names, key=len)    

    return {
        "Names sorted alphabetically: ": alpha,
        "Names sorted by length :": length,        
    }



def letter_counter(names):

    """ 
    funktion som tæller antal bogstaver i navnene i listen 
    """

    letter_count = {}

    #itererer over navne i vores liste
    for name in names:
        # gør alle bogstaver små så der ikke skelnes
        name_low = name.lower()
        #itererer over hvert bogstav i enkelte navne og inkrementerer en værdi for det enkelte bogstav som sættes som key, værdien som value
        for letter in name_low:
                     
                if letter.isalpha():
                    
                    letter_count[letter] = letter_count.get(letter,0) + 1

    print(f"Occourence of individual letters: {letter_count}")
    return letter_count
    
def letter_frequency_bar_chart(letter_count):
    """Søjlediagram som viser for hyppigt de enkelte bostaver optræder"""
    # Sorterer efter frekvens - .items metoden gør at key/val ses som tuple, lambda funktionen fortæller sorted funktion, at den skal sortere efter val
    sorted_items = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)  
    letters = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]
    
    # Genererer søjlediagrammet
    plt.figure(figsize=(12, 6))
    plt.bar(letters, counts, color='skyblue')
    plt.title('Letter Frequency in Names')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()    
    plt.show()


def create_letter_wordcloud(letter_count):

    """Funktion som genererer em wordcloud som visualiserer hvor hyppigt individuelle bogstaver forekommer"""

    # Generate the word cloud
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=50
    ).generate_from_frequencies(letter_count)
    
    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Letter Frequency Word Cloud')
    plt.tight_layout()
    plt.show()          


def analyse_names(names):

    """Funktion som optæller antal bogstaver for navne i listen, og printer en dictionary
      samt Udregner median og gennemsnit og printer resultatet
      """
    
    name_data_dict = defaultdict(list)
    freq_dict = defaultdict(int)

    # optælling af antal bogstaver i navne(navnelængde)
    for name in names:
        count = len(name)
        name_data_dict[name].append(count)    

    for key, val in name_data_dict.items():
        for count in val:
            freq_dict[count] += 1
    
        
    # Median og gennemsnit for navnelængde
    alle_values = []
    for key, value in freq_dict.items():
        alle_values.extend([key] * value)

    median = np.median(alle_values)
    print(f"Median name length = {median}")      

    total_count = sum(freq_dict.values())

    mean = sum(key * value for key, value in freq_dict.items()) / total_count

    print(f"Mean name length = {mean}")

    # visualisering

    print("Generating histogram visualising name length distribution..")
    # variable som anvendes.. 
    lengths = sorted(freq_dict.keys())
    frequencies = [freq_dict[length] for length in lengths]
    
    # histogram hvor frekvens ses y aksen, og distribution af navnelængder
    plt.figure(figsize=(12, 6))
    plt.bar(lengths, frequencies, color='lightgreen')
    plt.title('Distribution of Name Lengths')
    plt.xlabel('Name Length (number of characters)')
    plt.ylabel('Frequency (number of names)')  
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(lengths)
    plt.tight_layout()
    
    #viser histogrammet

    plt.show()
    
    return {
        "mean": mean,
        "median": median,
        "Number of names by length:": dict(freq_dict)
    }

        
          
# Anvendelse af funktionerne

def main():


    name_file_path = os.path.join("data" ,"Navne_liste.txt")

    names = name_list(name_file_path)    
    print(f"List of {len(names)} names has been created!")

    sort_names(names)
    print("Sorted names alphabetically")
    print("Sorted names by length")
    
    letter_count = letter_counter(names)
    letter_frequency_bar_chart(letter_count)
    create_letter_wordcloud(letter_count)

    analyse_names(names)
    

# Visualisering     



"""



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
"""
plt.figure(figsize=(10, 8))
sns.boxplot(x=len_key,
            y=len_val,
            data=freq_dict,
            showmeans=True)  # notice the change
plt.ylabel("Antal_personer", size=14)
plt.xlabel("Antal_bogstaver", size=14)
plt.show()"""

if __name__=="__main__":
    main()