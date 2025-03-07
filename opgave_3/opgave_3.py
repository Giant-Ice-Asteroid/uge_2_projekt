""" 
Opret et script, der læser data fra en kildefil (source_data.csv) og skriver dem til en 
destinationsfil. 

• Scriptet skal håndtere forskellige typer fejl, som f.eks.: 
    - Manglende filer: Hvad skal der ske, hvis kildefilen ikke eksisterer? 
    - Formateringsfejl: Håndter situationer, hvor dataformatet er forkert eller uventet. 
    - Skrivebeskyttelse: Håndter fejl, hvis destinationsfilen ikke kan skrives til. 
"""
import csv
import os

def csv_file_readnwrite(file_path, dest_path): 

    """
    Funktion som læser data fra en csv fil, og skriver pågældende data til en ønsket fildestination 

    file_path: Sti til kildefil
    dest_path: Sti hvortil data ønskes skrevet over i en destinationsfil
    
    Returnerer True hvis hvis det lykkedes, False hvis det mislykkedes 

    """

# Først tjekkes om kildefilen eksisterer: 
    
    if not os.path.exists(file_path):
        print(f"Error: Source file '{file_path}' does not exist :<")
        return False    

# Kildefil læses..

    try:
        with open(file_path, "r") as file:
            content = file.read()
        print("Csv-file has been read successfully!")          
    
    except csv.Error as e: # forkert filtype(ikke csv)
        print(f"Error: {e}")
        return False
    except Exception as e: # andre fejl
        print(f"Unexpected error: {e}")
        return False

# Data skrives til destination: 

    try: 
        with open(dest_path, "w") as dest_file:
            dest_file.write(content)
            print("Data successfully written to destination file!")
            return True

    except FileNotFoundError: # filen kan ikke findes
        print("Error: file not found;___;")
        return False
      
    except Exception as e: # andre fejl
        print(f"Unexpected error: {e}")
        return False


# Test af funktion:

def main():

    # filstier til afprøvning
    file_path = os.path.join("data", "source_data.csv")
    dest_path = os.path.join("data", "dest_file.csv")


    csv_file_readnwrite(file_path, dest_path)

if __name__=="__main__":
    main()