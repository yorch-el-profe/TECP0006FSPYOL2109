const http = require("http");
const url = require("url");

const server = http.createServer(function (request, response) {
  const query = url.parse(request.url, true).query;
  const a = Number(query.a);
  const b = Number(query.b);

  if (!isNaN(a) && !isNaN(b)) {
    const suma = a + b;
    response.write("<h1>La suma de " + a + " + " + b + " = " + suma + "</h1>");
  } else {
    response.write("<h1>ERROR NO ES UN NUMERO</h1>");
  }

  response.end();
});

server.listen(8080);
