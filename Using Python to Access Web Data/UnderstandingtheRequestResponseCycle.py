"""
Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:

Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Enter the header values in each of the fields below and press "Submit".
"""

import socket

# Crear el socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# Enviar solicitud HTTP GET correctamente
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

# Recibir e imprimir la respuesta
response = b""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    response += data

mysock.close()

# Convertir la respuesta a string
response_str = response.decode()

# Separar encabezados y cuerpo del mensaje
headers, body = response_str.split("\r\n\r\n", 1)

# Imprimir encabezados
print("=== HEADERS ===")
print(headers)

# Imprimir solo el contenido del archivo
print("\n=== BODY ===")
print(body)

####
"""
=== HEADERS ===
HTTP/1.1 200 OK
Date: Thu, 03 Apr 2025 14:35:11 GMT
Server: Apache/2.4.52 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate    
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

=== BODY ===
Why should you learn to write programs?

Writing programs (or programming) is a very creative
and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping       
someone else solve a problem.  This book assumes that
everyone needs to know how to program, and that once
you know how to program you will figure out what you want        
to do with your newfound skills.
"""
