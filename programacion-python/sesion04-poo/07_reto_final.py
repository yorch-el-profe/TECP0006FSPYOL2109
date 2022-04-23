"""
Maquina Expendedora

1. Es una máquina de refrescos, por lo tanto la máquina por dentro tiene N refrescos
2. Estos refrescos tienen una marca y un precio
3. Para comprar un refresco, se necesita la marca del producto y el dinero
4. Al momento de comprar el refresco, se debe "descontar" el refresco del inventario de la máquina
5. Esta máquina no debe ser manipulable por alguien externo

maquina = MaquinaExpendedora()

maquina.comprar("Pepsi", 100) -> 85 (y quita el refresco de la máquina)
maquina.revisar() -> Lista de los refrescos que hay
"""