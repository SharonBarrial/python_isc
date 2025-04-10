"""
✅ 1. What is the primary added value of relational databases over flat files?
✔️ Respuesta correcta: Ability to scan large amounts of data quickly
📌 Los RDBMS están optimizados para búsquedas, filtrado y combinaciones rápidas en grandes cantidades de datos, lo cual es muy lento con archivos planos.

✅ 2. What is the purpose of a primary key?
✔️ Respuesta correcta: To look up a particular row in a table very quickly
📌 El primary key es único y permite encontrar una fila específica de forma eficiente.

✅ 3. Which of the following is NOT a good rule to follow when developing a database model?
✔️ Respuesta correcta: Use a person's email address as their primary key
📌 Los correos pueden cambiar o no ser únicos. Es mejor usar claves numéricas (integers).

✅ 4. How should we model repeated strings in the UI?
✔️ Respuesta correcta: Make a table that maps the strings in the column to numbers and then use those numbers in the column
📌 Esto se llama normalización: se usa una tabla para evitar redundancia.

✅ 5. What is the label we give a column that the "outside world" uses to look up a particular row?
✔️ Respuesta correcta: Logical key
📌 Ej: el correo electrónico. Es significativo para los usuarios externos.

✅ 6. What is the label for a column used to point to a row in a different table?
✔️ Respuesta correcta: Foreign key
📌 Es una referencia a otra tabla, clave para relacionar datos.

✅ 7. SQLite keyword that auto-generates values in primary keys?
✔️ Respuesta correcta: AUTOINCREMENT
📌 Se usa para que SQLite asigne automáticamente un valor único al insertar.

✅ 8. SQL keyword to reconnect rows with foreign keys?
✔️ Respuesta correcta: JOIN
📌 JOIN une filas basadas en relaciones definidas por claves (como foreign keys).

✅ 9. What happens when you JOIN two tables without ON clause?
✔️ Respuesta correcta: The number of rows you get is the number of rows in the first table times the number of rows in the second table
📌 Eso es un "producto cartesiano", porque no se especificó una condición de unión.

✅ 10. How do you distinguish column names from different tables in a JOIN?
✔️ Respuesta correcta: tablename.columnname
📌 Es la sintaxis estándar para evitar confusión cuando los nombres de columnas se repiten.
"""
