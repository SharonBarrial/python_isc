"""
¿Cuál de las siguientes expresiones regulares extraería 'uct.ac.za' de la cadena dada usando re.findall?
✅ @(\S+)

@(\S+) captura cualquier secuencia de caracteres no espaciales (\S+) después de @, y los paréntesis () hacen que se extraiga solo uct.ac.za.

¿Cómo se representa el "inicio de una línea" en una expresión regular?
✅ ^

El carácter ^ indica el inicio de una línea en una expresión regular.

¿Qué significa [a-z0-9] en una expresión regular?
✅ "Match a lowercase letter or a digit"

[a-z0-9] significa "cualquier letra minúscula de la a a la z o cualquier número del 0 al 9".

¿Cuál es el tipo de retorno del método re.findall()?
✅ "A list of strings"

re.findall() devuelve una lista de coincidencias encontradas en la cadena.

¿Cuál es el "comodín" en expresiones regulares?
✅ .

. en una regex significa "cualquier carácter excepto un salto de línea".

¿Diferencia entre + y * en expresiones regulares?
✅ "The + matches at least one character and the * matches zero or more characters"

+ requiere al menos una coincidencia, mientras que * permite cero o más coincidencias.

¿Qué hace [0-9]+ en una expresión regular?
✅ "One or more digits"

[0-9]+ busca uno o más dígitos consecutivos.

¿Qué imprimirá este código?

python
Copy
Edit
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
✅ "['From: Using the :']"

^F.+: captura desde F hasta el último : de manera "codiciosa".

¿Qué carácter hace que + o * sean no "codiciosos"?
✅ ?

+? o *? hacen que la búsqueda no sea "greedy", es decir, que se detenga en la primera coincidencia posible.

¿Qué extraería la regex \S+?@\S+?
✅ "stephen.marquard@uct.ac.za"
