"""
Opgave 2: Logfil analyse 

Opret et script, der læser indholdet fra en logfil (app_log.txt) og filtrerer bestemte typer 
af logmeddelelser, som ERROR og WARNING. 
Gem de filtrerede logmeddelelser i en ny fil, så kritiske hændelser er lette at overskue 

"""

import os
import re

log_file = "opgave_2\\app_log.txt"

warning_count = 0  # optælling  af "WARNING" forekomster
error_count = 0  # optælling af "ERROR" forekomster
warning_lines = []  # Linjer i tekstfilen hvor ordet "WARNING" forekommer
error_lines = []  # Linjer i tekstfilen hvor ordet "ERROR" forekommer

with open(log_file, "r") as file:
    for line_number, line in enumerate(file, 1):  # Starter line_number fra 1 
        warning_matches = re.findall(r"WARNING", line)  # Finder "WARNING" på pågældende linje
        error_matches = re.findall(r"ERROR", line)  # ditto "ERROR" 
        
        if warning_matches:  #hvis  "WARNING" optræder på linje
            warning_count += len(warning_matches)  # inkrementerer count
            warning_lines.append(line_number)  # tilføjer linje nummer til warning liste
        
        if error_matches:  
            error_count += len(error_matches)  
            error_lines.append(line_number)  

# resultat
print(f"Antal forekomster af 'WARNING': {warning_count}")
print(f"Linjer hvor 'WARNING' forefindes: {warning_lines}")
print(f"Antal forekomster af 'ERROR': {error_count}")
print(f"Linjer hvor 'ERROR' forefindes: {error_lines}")


