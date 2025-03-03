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

# optælling af bogstaver i navn

from collections import defaultdict

name_data_dict = defaultdict(list)

for name in name_data_list:
    count = len(name)
    name_data_dict[name].append(count)

        
# print(name_data_dict)

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
          

    
          
print(letter_count)