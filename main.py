import sqlite3
import pandas as pd

# Leer el archivo CSV
csv_file = "PremierLeagueMatches.csv"
df = pd.read_csv(csv_file)

# Conectar a la base de datos SQLite
conn = sqlite3.connect("premier_league.db")

# Insertar los datos en la tabla 'raw_data'
df.to_sql("raw_data", conn, if_exists="append", index=False)

# Confirmar y cerrar la conexión
conn.commit()
conn.close()

print("Datos importados correctamente a la tabla 'raw_data'.")