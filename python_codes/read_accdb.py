import pyodbc
conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\PycharmProjects\flask_NLP_app\dataset\accdb\WiC_dataset.accdb;')
cursor = conn.cursor()
cursor.execute('select *')

for row in cursor.fetchall():
    print(row)
