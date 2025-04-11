"""
✅ 1. ¿Cómo se modela una relación de muchos a muchos entre dos tablas?
Respuesta: ✅ We add a table with two foreign keys
👉 Esto se llama una tabla intermedia o de relación. Es la forma estándar.

✅ 2. ¿A qué se parece más un cursor de base de datos en Python?
Respuesta: ✅ A file handle
👉 Igual que con los archivos, se usa para leer paso a paso los resultados.

✅ 3. ¿Qué método usas para ejecutar un comando SQL con un cursor de SQLite?
Respuesta: ✅ execute()
👉 Es el método principal para ejecutar comandos SQL como SELECT, INSERT, etc.

✅ 4. En esta línea:
python
Copy code
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
¿Para qué sirve el "?"?
Respuesta: ✅ Es un marcador de posición para la variable "org"
👉 Previene ataques de SQL Injection y hace tu código más seguro.

✅ 5. ¿Qué valor tiene row si no hay coincidencias en la búsqueda?
python
Copy code
row = cur.fetchone()
Respuesta: ✅ None
👉 Si no encuentra nada, no devuelve lista vacía ni -1, simplemente None.

✅ 6. ¿Qué hace el LIMIT en esta consulta?
sql
Copy code
SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10
Respuesta: ✅ Solo recupera las primeras 10 filas
👉 Ideal para ver "Top 10", por ejemplo.

✅ 7. ¿Qué hace executescript() que execute() no puede hacer?
Respuesta: ✅ Permite múltiples sentencias SQL separadas por punto y coma
👉 Se usa para crear tablas o insertar datos en bloque.

✅ 8. ¿Para qué sirve el OR IGNORE en este SQL?
sql
Copy code
INSERT OR IGNORE INTO Course (title) VALUES ( ? )
Respuesta: ✅ Evita duplicados si el valor ya existe
👉 Si title ya está en la tabla y es UNIQUE, no lanza error, solo ignora.

✅ 9. ¿Qué debe tener la columna title en Course para que esto funcione?
python
Copy code
INSERT OR IGNORE INTO Course (title) ...
Respuesta: ✅ A UNIQUE constraint
👉 Para que SQLite sepa cuándo "ignorar" valores duplicados.
"""
