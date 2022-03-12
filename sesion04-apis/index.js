//1. Importar un módulo que permita crear un servidor (http)
const http = require("http");

// La función require() importa un módulo en una variable.

// 2. Crear un servidor HTTP
const server = http.createServer(function (request, response) {
  // 4. Programar lo que haga el servidor
  // Cada vez que haya una petición, se ejecutará esta función
  // El objetivo es construir la respuesta del servidor

  // Dar contexto de que el BODY de la respuesta es un "texto plano"
  response.writeHead(200, { "Content-Type": "text/html" });

  // Escribir en el BODY (de la respuesta) la palabra "HELLO WORLD"
  response.write("<h1>Hello World</h1>");

  // Para terminar la petición
  response.end();
});

// 3. Asignar un PUERTO (0 - 65550)
// Los primeros 1024 puertos (0 - 1023) "son de uso exclusivo"
// del sistema operativo.
// 22 - SSH
// 80 - HTTP
// 443 - HTTPS
server.listen(8080);
