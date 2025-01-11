import pyodbc
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=backend/dataset/accdb/WiC_dataset.accdb')  # You might need to adjust it to match the PATH. It worked on my machine
cursor = conn.cursor()
cursor.execute('select *')

for row in cursor.fetchall():
    print(row)
