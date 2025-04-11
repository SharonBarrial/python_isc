import sqlite3
import csv

# Conexión a la base de datos (se creará si no existe)
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Borrar tablas si ya existen y crear nuevas
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Abrir el archivo CSV con codificación UTF-8
with open('tracks.csv', encoding='utf-8') as file:
    reader = csv.reader(file)

    for row in reader:
        if len(row) < 6:
            continue

        title = row[0]
        artist = row[1]
        album = row[2]
        genre = row[3]
        count = row[4]
        rating = row[5]
        length = row[6]

        # Insertar artista
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # Insertar género
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        # Insertar álbum
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        # Insertar canción
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (title, album_id, genre_id, length, rating, count))

# Guardar cambios
conn.commit()
