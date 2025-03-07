"""
Opgave 2: Logfil analyse 

Opret et script, der læser indholdet fra en logfil (app_log.txt) og filtrerer bestemte typer 
af logmeddelelser, som ERROR og WARNING. 
Gem de filtrerede logmeddelelser i en ny fil, så kritiske hændelser er lette at overskue 

"""

import os

# Funktion som læser en log fil, leder efter ERROR and WARNING advarsler og gemmer dem i en ny fil.

def analyse_log_file(log_file_path, output_file_path):

    warning_count = 0  # optælling  af "WARNING" forekomster
    error_count = 0  # optælling af "ERROR" forekomster

    filtered_lines = []  # Linjer i tekstfilen hvor ordet "WARNING" eller "ERROR" forekommer

    # Sikrer at logfilen eksisterer:
    if not os.path.exists(log_file_path):
        print(f"Error: Log file '{log_file_path}' does not exist!! :'(")
        return
    
    try:
        # Dernæst læses logfilen og gennemgås linje for linje for advarsler
        with open(log_file_path, "r") as file:
            for line in file:                
                if "WARNING" in line or "ERROR" in line:
                    filtered_lines.append(line.strip())
                    
                    # optælling
                    if "WARNING" in line:
                        warning_count += 1
                    if "ERROR" in line:
                        error_count += 1

        # Filtrerede advarsler skrives til output file
        with open(output_file_path, "w") as output_file:
            # overskrift og mellemrum for læsbarhed:
            output_file.write("FILTERED LOG MESSAGES (WARNINGS AND ERRORS)\n")
            output_file.write("="*50 + "\n\n")
            
            # hver linje i filtered_lines skrives til output filen
            for line in filtered_lines:
                output_file.write(line + "\n")
            
            # Mellemrum og opsummering af fund:
            output_file.write("\n" + "="*50 + "\n")
            output_file.write(f"SUMMARY: Found {warning_count} warnings and {error_count} errors.\n")
        
        # Print summary to console
        print(f"Log analysis now complete.")
        print(f"Found a total of {warning_count} warnings and {error_count} errors.")
        print(f"Filtered messages have been saved to '{output_file_path}'")

     # advarsel såfremt der opstår andre fejl   
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__=="__main__":
    # Filstier
    log_file = os.path.join("data", "app_log.txt")
    output_file = os.path.join("data", "filtered_log.txt")

    # For at køre analysen...:
    analyse_log_file(log_file, output_file)


