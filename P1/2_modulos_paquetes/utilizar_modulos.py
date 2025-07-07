from paquete1 import modulos

print(modulos.saludar("Daniel contreras"))
modulos.borrarPantalla()

nom,tel=modulos.solicitarDatos2()
print(f"\n\t..::Agenda telefonica::.\n\t Nombre: {nom}\n\t\t Telefono: {tel}")
modulos.espereTecla()