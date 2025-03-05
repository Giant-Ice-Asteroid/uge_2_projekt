""" 
Opret et script, der læser data fra en kildefil (source_data.csv) og skriver dem til en 
destinationsfil. 

• Scriptet skal håndtere forskellige typer fejl, som f.eks.: 
    - Manglende filer: Hvad skal der ske, hvis kildefilen ikke eksisterer? 
    - Formateringsfejl: Håndter situationer, hvor dataformatet er forkert eller uventet. 
    - Skrivebeskyttelse: Håndter fejl, hvis destinationsfilen ikke kan skrives til. 
"""
import csv

def csv_file_readnwrite(file_path, dest_path): # funktion som læser csv filer fra en cvs fil (file_path) og skriver den til en ønsker destination (dest_path)
    
    try:
        with open(file_path, "r") as file:
            content = file.read()
        print("Csv-file read successfully!")
          

    except FileNotFoundError: # filen kan ikke findes
        print("Error: file not found.")
    except csv.Error as e: # forkert filtype(ikke csv)
        print(f"Error: {e}")
    except Exception as e: # andre fejl
        print(f"Unexpected error: {e}")

    try: 
        with open(dest_path, "w") as destfile:
            destfile.write(content)
            print("Data successfully written to destination file!")

    except FileNotFoundError: # filen kan ikke findes
        print("Error: file not found.")
      
    except Exception as e: # andre fejl
        print(f"Unexpected error: {e}")

file_path = "opgave_3\\source_data.csv"
destfile = "opgave_3\\text.txt"

csv_file_readnwrite(file_path, destfile)