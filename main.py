#Ejercicio
print("HAMBURGUESAS EL CORRAL")
print("*" * 20)

nombreUsuario = input("Digite su nombre: ")
documentoUsuario = input("Digite su documento: ")
doble = {"Hamburguesa": "Hamburguesa doble", "precio": 20000}
vegetariana = {"Hamburguesa": "Hamburguesa vegetariana", "precio": 10000}
sencilla = {"Hamburguesa": "Hamburguesa sencilla", "precio": 15000}

pedido = input(
  f"¿Cuál hamburguesa desea, {nombreUsuario}? Hamburguesa sencilla: $15,000, Hamburguesa vegetariana: $10,000, Hamburguesa doble: $20,000 ==> "
)
pedido = pedido.lower()
cantidad = int(
  input(f"¿Cuántas hamburguesas desea pedir, {nombreUsuario}? ==> "))
print("*" * 20)
print(" Hamburguesas El Corral")
if pedido == "vegetariana":
  print(
    f" Cliente: {nombreUsuario}\n Documento: {documentoUsuario}\n Su pedido es {cantidad}  hamburguesa(s) {pedido}(s) con un valor total de $ ",
    vegetariana["precio"] * cantidad)

if pedido == "sencilla":
  print(
    f" Cliente: {nombreUsuario}\n Documento:{documentoUsuario}\n Su pedido es {cantidad}  hamburguesa(s) {pedido}(s) con un valor total de $ ",
    sencilla["precio"] * cantidad)

if pedido == "doble":
  print(
    f" Cliente: {nombreUsuario}\n Documento:{documentoUsuario}\n su pedido es {cantidad}  hamburguesa(s) {pedido}(s) con un valor total de $ ",
    doble["precio"] * cantidad)

print(" Gracias por elegirnos")
