# API-Python

- Instalación del entorno
`py -3 -m venv .venv`
- Activar el entorno
`.venv\Scripts\activate`
- Instalar Flask (dentro del entorno)
`pip install Flask`
- Ejecutar la app
`flask --app main run`

### Autores

- Benito Gallardo Peral
- Pablo Javier Muñoz
- Luis Miguel García

### Lista de EndPoints:

- Producto
- Furgoneta
- Pedido
- ProductoEnPedido

# Peticiones

## Producto

Productos almacenados.

### Peticiones Get

**Obtener lista de productos:**

[http://localhost:5000/Productos](http://localhost:5000/Productos)

**Obtener producto por Id:**

[http://127.0.0.1:5000/Producto/1](http://127.0.0.1:5000/Producto/1)

### Peticiones Post

**Crear un producto, a través de su nombre, descripción y stock:**

[http://127.0.0.1:5000/Producto](http://127.0.0.1:5000/Producto)

Formulario:

- name
- description
- stock

### Peticiones Put

**Modificar un producto, nombre, descripción y stock:**

[http://127.0.0.1:5000/Producto](http://127.0.0.1:5000/Producto)

Formulario:

- name
- description
- stock

No es necesario cambiar todo.

### Peticiones Delete

**Eliminar un producto por id:**

[http://localhost:5000/Producto/1](http://localhost:5000/Productos)

## Furgoneta

Furgonetas de la empresa.

### Peticiones Get

**Obtener lista de furgonetas:**

[http://localhost:5000/Furgonetas](http://localhost:5000/Furgonetas)

**Obtener furgoneta por matricula:**

[http://127.0.0.1:5000/Furgoneta/1234ABC](http://127.0.0.1:5000/Furgoneta/1234ABC)

### Peticiones Post

**Crear una furgoneta, a través de su matricula y marca:**

[http://127.0.0.1:5000/Furgoneta](http://127.0.0.1:5000/Furgoneta)

Formulario:

- marca
- matricula

### Peticiones Put

**Modificar una furgoneta, marca y matricula:**

[http://127.0.0.1:5000/Furgoneta](http://127.0.0.1:5000/Furgoneta)

Formulario:

- marca
- matricula

No es necesario cambiar todo.

### Peticiones Delete

**Eliminar una furgoneta por id:**

[http://localhost:5000/Furgoneta/1](http://localhost:5000/Furgoneta/1)

## Pedido

Pedidos realizados.

### Peticiones Get

**Obtener lista de pedidos:**

[http://localhost:5000/Pedidos](http://localhost:5000/Pedidos)

**Obtener lista de pedidos por fecha:**

[http://localhost:5000/Pedidos/2024-02-20](http://localhost:5000/Pedidos/2024-02-20)

**Obtener pedido por Id:**

[http://127.0.0.1:5000/Pedido/1](http://127.0.0.1:5000/Pedido/1)

### Peticiones Post

**Crear un pedido, a través de su dirección, fecha y idFurgoneta:**

[http://127.0.0.1:5000/Pedido](http://127.0.0.1:5000/Pedido)

Formulario:

- direccion
- fecha
- idFurgoneta

### Peticiones Put

**Modificar un pedido, direccion, fecha y idFurgoneta:**

[http://127.0.0.1:5000/Pedido](http://127.0.0.1:5000/Pedido)

Formulario:

- direccion
- fecha
- idFurgoneta

No es necesario cambiar todo.

### Peticiones Delete

**Eliminar un pedido:**

[http://localhost:5000/Pedido/1](http://localhost:5000/Pedido/1)

También elimina los productos que se encuentren en el pedido.

## ProductoEnPedido

Productos que hay en un pedido.

### Peticiones Get

**Obtener lista de productos en un pedidos por id:**

[http://localhost:5000/ProductoEnPedido/1](http://localhost:5000/ProductoEnPedido/1)

### Peticiones Post

**Añadir un producto a un pedido, a través de la id del pedido, idProducto y cantidad:**

[http://localhost:5000/ProductoEnPedido/1](http://localhost:5000/ProductoEnPedido/1)

Formulario:

- idProducto
- cantidad

Si el producto ya está en el pedido añade la cantidad introducida.

### Peticiones Put

**Modificar un producto en un pedido, a través de la id del pedido, idProducto y cantidad:**

[http://127.0.0.1:5000/Pedido](http://127.0.0.1:5000/Pedido)

Formulario:

- idProducto
- cantidad

No es necesario cambiar todo.

### Peticiones Delete

**Eliminar un producto de un pedido por id:**

[http://localhost:5000/ProductoEnPedido/1](http://localhost:5000/ProductoEnPedido/1)

Formulario:

- idProducto
