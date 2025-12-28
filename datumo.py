from datetime import datetime

# Vergangenheit definieren
Vergangenheit = datetime(2022, 12, 13) 

# Heutiger Datum bereitstellen
heute = datetime.now()

# Länge in Tagen bereschnen
Länge = (heute - Vergangenheit).days 

print(f"Das war {Länge} Tage her")
