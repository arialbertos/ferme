from django.db import models
from django.utils import timezone

class Administrador(models.Model):
	usuario_id = models.IntegerField()
	run = models.CharField(max_length=12)
	nombres = models.CharField(max_length=50)
	appaterno = models.CharField(max_length=50)
	apmaterno = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	genero = models.CharField(max_length=6)
	email = models.CharField(max_length=50)
	telefono = models.IntegerField()
	nombre_usuario = models.CharField(max_length=40)
	contrasena = models.CharField(max_length=50)
	cod_admin = models.CharField(max_length=6)

	def __str__(self):
		return self.nombre


class Empleado(models.Model):
	usuario_id = models.IntegerField()
	run = models.CharField(max_length=12)
	nombres = models.CharField(max_length=50)
	appaterno = models.CharField(max_length=50)
	apmaterno = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	genero = models.CharField(max_length=6)
	email = models.CharField(max_length=50)
	telefono = models.IntegerField()
	nombre_usuario = models.CharField(max_length=40)
	contrasena = models.CharField(max_length=50)
	cod_empleado = models.CharField(max_length=6)
	sucursal = models.CharField(max_length=55)
	fecha_contrato = models.DateField()
	area = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre


class Cliente(models.Model):
	usuario_id = models.IntegerField()
	run = models.CharField(max_length=12)
	nombres = models.CharField(max_length=50)
	appaterno = models.CharField(max_length=50)
	apmaterno = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	genero = models.CharField(max_length=6)
	email = models.CharField(max_length=50)
	telefono = models.IntegerField()
	nombre_usuario = models.CharField(max_length=40)
	contrasena = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class Vendedor(models.Model):
	usuario_id = models.IntegerField()
	run = models.CharField(max_length=12)
	nombres = models.CharField(max_length=50)
	appaterno = models.CharField(max_length=50)
	apmaterno = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	genero = models.CharField(max_length=6)
	email = models.CharField(max_length=50)
	telefono = models.IntegerField()
	nombre_usuario = models.CharField(max_length=40)
	contrasena = models.CharField(max_length=50)
	cod_vendedor = models.CharField(max_length=6)
	sucursal = models.CharField(max_length=55)
	fecha_contrato = models.DateField()

	def __str__(self):
		return self.nombre


class Compra(models.Model):
	vendedor_cod_vendedor = models.CharField(max_length=6)
	id_compra = models.IntegerField()
	monto_total = models.IntegerField()
	cliente_usuario_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	despacho_id = models.ForeignKey(DespachoDomicilios, on_delete=models.SET_NULL,
								null=True)

class Actividad(models.Model):
	fecha_hora = models.DateField()
	usuario = models.ForeignKey('auth.User', on_delete=models.SET_NULL,
								null=True)


class Categoria(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class Marca(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class Producto(models.Model):
	sku = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	color = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=100)
	stock = models.IntegerField()
	stock_critico = models.IntegerField()
	disponibilidad = models.CharField(max_length=1)
	precio_normal = models.IntegerField()
	precio_oferta = models.IntegerField()
	marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.nombre


class CategoriaProducto(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	def __str__(self):
		return self.producto + ' - ' + self.categoria


class Carro(models.Model):
	carro_id = models.CharField(max_length=8, primary_key=True)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

	def __str__(self):
		return self.carro_id


class CarroProducto(models.Model):
	cantidad = models.IntegerField()
	producto = models.ForeignKey(Producto, on_delete=models.SET_NULL,
								 null=True)
	carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

class Proveedor(models.Model):
	razon_social = models.CharField(max_length=55)
	sector_comercial = models.CharField(max_length=55)
	direccion = models.CharField(max_length=55)
	email = models.CharField(max_length=55)
	fono = models.CharField(max_length=55)

class OrdenDeCompra(models.Model):
	fecha_recepcion = models.DateField()
	estado = models.CharField(max_length=20)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class ProductoOc(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	orden_de_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.CASCADE)

class RetiroTienda(models.Model):
	fecha_entrega = models.DateField()
	rut_receptor = models.CharField(max_length=12)
	estado = models.CharField(max_length=20)
	sucursal = models.CharField(max_length=20)
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

class DespachoDomicilio(models.Model):
	fecha_entrega = models.DateField()
	rut_receptor = models.CharField(max_length=12)
	estado = models.CharField(max_length=20)
	direccion = models.CharField(max_length=60)
	telefono_contacto = models.CharField(max_length=12)
	comuna = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=20)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

class Boleta(models.Model):
	sucursal = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	comuna = models.CharField(max_length=45)
	fecha_compra = models.DateField()
	terminal = models.IntegerField()
	tipo_pago = models.IntegerField()
	anulada = models.CharField(max_length=1)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
	rut_persona = models.CharField(max_length=12)

class Factura(models.Model):
	sucursal = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	comuna = models.CharField(max_length=45)
	fecha_compra = models.DateField()
	terminal = models.IntegerField()
	tipo_pago = models.IntegerField()
	anulada = models.CharField(max_length=1)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
	rut_empresa = models.CharField(max_length=12)
	iva = models.IntegerField()

class NotaCredito(models.Model):
	sucursal = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	comuna = models.CharField(max_length=45)
	fecha_compra = models.DateField()
	terminal = models.IntegerField()
	tipo_pago = models.IntegerField()
	anulada = models.CharField(max_length=1)
	compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	fecha_anulacion = models.DateField()
	doc_asociado = models.CharField(max_length=10)
	desc_motivo = models.CharField(max_length=255)
