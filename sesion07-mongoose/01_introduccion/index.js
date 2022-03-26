const mongoose = require("mongoose");

// 1. Establecer conexión con MongoDB
mongoose
  .connect(
    "mongodb+srv://root:root@cluster0.iejwi.mongodb.net/ejemplo?retryWrites=true&w=majority"
  )
  .then(function () {
    console.log("La conexión se realizó con éxito");
  })
  .catch(function () {
    console.log("Falló la conexión");
  });

console.log("Conectando a base de datos");

// 2. Crear un schema (la estructura de mis colecciones)

const UserSchema = new mongoose.Schema(
  {
    username: { type: String, required: true, unique: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true, minlength: 8 },
    name: { type: String },
  },
  { collection: "usuarios" }
);

// 3. Crear un modelo a partir de un schema

const UserModel = mongoose.model("users", UserSchema);

// 4. A disfrutar

// 4.1 Crear un nuevo registro

/*const model = new UserModel({
  username: "paquito",
  email: "paq@mail.com",
  password: "12345678",
});

model
  .save()
  .then(function () {
    console.log("Documento insertado");
  })
  .catch(function () {
    console.log("No se pudo insertar el documento");
  });*/

// 4.2 Consulta de documentos

// Obtiene todos los documentos
/*UserModel.find().then(function (documentos) {
  console.log(documentos);
});*/

// Obtiene los documentos cuyo username es "paquito" y correo es "paq@mail.com"

/*UserModel.find({ username: "paquito123", email: "paq@mail.com" }).then(
  function (documentos) {
    console.log(documentos);
  }
);*/

// 4.3 Actualización de un documento

/*UserModel.updateOne(
  { username: "paquito123" },
  {
    $set: { name: "Paquito Perez" },
  }
).then(function (data) {
  console.log(data);
  console.log("Documento actualizado");
});*/

// 4.4 Eliminación de documentos

UserModel.deleteOne({ username: "paquito123" }).then(function () {
  console.log("Documento eliminado");
});
