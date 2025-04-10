import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Elimina la tabla si ya existe
cur.execute('DROP TABLE IF EXISTS Counts')

# Crea una nueva tabla con columnas: org (dominio) y count (cantidad)
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Fijamos directamente el nombre del archivo de texto
fname = 'mbox.txt'  # También puedes usar 'mbox-short.txt' para pruebas más rápidas

# Abre el archivo y comienza a procesar línea por línea
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]  # Extrae el dominio (organización)
    
    # Consulta si ese dominio ya está en la tabla
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    
    # Si no existe, lo inserta con valor 1; si existe, incrementa en 1
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    
    # Guardar los cambios en la base de datos (puedes optimizar quitando esto del bucle)
    conn.commit()

# Muestra los 10 dominios más comunes
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Cierra la conexión a la base de datos
cur.close()
