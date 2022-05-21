function pintarRazas(razas) {
	var select = document.getElementById("select-razas");

	for (var raza of razas) {
		var option = document.createElement("option"); // <option />
		option.setAttribute("value", raza); // <option value="chihuahua"/>
		option.innerHTML = raza; //<option value="chihuahua">chihuahua</option>

		select.appendChild(option);
	}
}

function obtenerRazas() {
	fetch("http://localhost:5000/razas")
		// response es la respuesta del servidor que estoy consumiendo
		// en este caso, contiene la respuesta de Flask
		.then(function (response) {
			// Extrayendo el JSON de la respuesta de Flask
			return response.json();
		})
		// "body" es la lista de todas las razas obtenidas desde Flask
		.then(function (body) {
			pintarRazas(body.data);
		});
}

function obtenerImagenAleatoria(raza) {
	fetch("http://localhost:5000/razas/" + raza)
		.then(function (response) {
			return response.json();
		})
		.then(function (body) {
			pintarImagenAleatoria(body.data);
		});
}

function pintarImagenAleatoria(url) {
	var img = document.getElementById("imagen-perritos");
	img.setAttribute("src", url);
}

var form = document.getElementById("form-perritos");

form.addEventListener("submit", function (event) {
	// Cancelar la actualización de la página
	event.preventDefault();

	// Obtenemos la raza seleccionada por el usuario
	// y realizamos la petición a Flask
	var select = document.getElementById("select-razas");
	obtenerImagenAleatoria(select.value);
});

// Al cargar la página obtenemos la lista de las razas
obtenerRazas();
