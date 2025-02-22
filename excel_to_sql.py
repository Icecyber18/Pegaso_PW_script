#script per convertire un file Excel in comandi SQL
#realizzato da Pastore Pietro
#Progetto: 2.1 PW Pegaso

# Il programma legge il file Excel dell'anagrafica clienti e crea:
# - Un comando CREATE TABLE per creare la tabella
# - Comandi INSERT per inserire tutti i dati

# ibrerie necessarie
import pandas as pd
import os

def converti_tipo_dato(tipo_pandas):
    # Converte i tipi di dato pandas nei corrispondenti tipi SQL
    if 'int' in str(tipo_pandas):
        return 'INT'
    elif 'float' in str(tipo_pandas):
        return 'FLOAT'
    elif 'datetime' in str(tipo_pandas):
        return 'DATETIME'
    else:
        return 'VARCHAR(255)'

#
def crea_comando_create_table(dati):
    # Preparo la lista delle colonne
    colonne = []
    
    # Aggiungo l'ID come chiave primaria
    colonne.append("id INT AUTO_INCREMENT PRIMARY KEY")
    
    # Aggiungo le altre colonne
    for nome_colonna in dati.columns:
        # Pulisco il nome della colonna
        nome_pulito = nome_colonna.lower().replace(' ', '_')
        tipo_sql = converti_tipo_dato(dati[nome_colonna].dtype)
        colonne.append(f"{nome_pulito} {tipo_sql} NOT NULL")

    # comando SQL completo
    comando_sql = f"""
CREATE TABLE users (
    {',\n    '.join(colonne)}
);
"""
    return comando_sql

# crea i comandi SQL per inserire i dati    
def crea_comandi_insert(dati):
    comandi_insert = []
    
    # Preparo i nomi delle colonne
    nomi_colonne = [col.lower().replace(' ', '_') for col in dati.columns]
    
    # Per ogni riga di dati
    for _, riga in dati.iterrows():
        valori = []
        
        # Formatto ogni valore
        for valore in riga:
            if pd.isna(valore):  # Se è vuoto
                valori.append('NULL') #
            elif isinstance(valore, (int, float)):  # Se è un numero
                valori.append(str(valore))
            else:  # Se è testo
                # Gestisco gli apostrofi
                testo_pulito = str(valore).replace("'", "''")
                valori.append(f"'{testo_pulito}'")
        
        # Creo il comando INSERT
        comando = f"""
INSERT INTO users ({', '.join(nomi_colonne)})
VALUES ({', '.join(valori)});"""
        comandi_insert.append(comando)
    
    return "\n".join(comandi_insert)




# funzione principale del programma
def main():
    # Percorso del file Excel
    file_excel = "C:/Project_Work_Pegaso/Anagrafica_clienti_Pw_Pegaso.xlsx"
    
    # Controllo se il file esiste
    if not os.path.exists(file_excel):
        print(f"Non trovo il file Excel in: {file_excel}")
        return
    
    try:
        # Leggo il file Excel
        dati = pd.read_excel(file_excel)
        
        # Creo i comandi SQL
        create_table = crea_comando_create_table(dati)
        insert_data = crea_comandi_insert(dati)
        
        # Unisco tutti i comandi
        sql_completo = f"{create_table}\n{insert_data}"
        
        # Salvo il file SQL
        file_sql = "C:/Project_Work_Pegaso/tabella_clienti.sql"
        with open(file_sql, 'w', encoding='utf-8') as f:
            f.write(sql_completo)
            
        print(f"Ho creato il file SQL in: {file_sql}")
        
    except Exception as errore:
        print(f"Si è verificato un errore: {errore}")

# Avvio il programma
if __name__ == "__main__":
    main() 