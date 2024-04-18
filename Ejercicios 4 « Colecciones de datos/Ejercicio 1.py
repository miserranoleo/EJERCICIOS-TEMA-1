usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}

administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "- Administrador")
    else:
        print(usuario, "- No es administrador")