usuarios_coder = {}


def registrar_usuario():
    usuario = {}
    usuario["DNI"] = input("Ingrese DNI: ")

    if usuario["DNI"] in usuarios_coder:
        print("El DNI ya está registrado.")
        return

    usuario["email"] = input("Ingrese email: ")

    if any(u["email"] == usuario["email"] for u in usuarios_coder.values()):
        print("El email ya está registrado.")
        return

    usuario["nombre"] = input("Ingrese nombre: ")
    usuario["apellido"] = input("Ingrese apellido: ")
    usuario["contraseña"] = input("Ingrese contraseña: ")

    """ Registramos el usuario """
    usuarios_coder[usuario["DNI"]] = usuario
    print("Usuario registrado con éxito.")


""" Eliminar un usuario """


def eliminar_usuario(self):
    print("\nEliminar usuario")
    username = input("Ingresa el nombre de usuario que deseas eliminar: ")
    for usuario in self.usuarios:
        if username == usuario["username"]:
            password = input("Ingresa la contraseña del usuario: ")
            if password == usuario["password"]:
                self.usuarios.remove(usuario)
                print(f"Usuario '{username}' eliminado exitosamente.")
                return
            else:
                print("Contraseña incorrecta. No se pudo eliminar el usuario.")
                return
    print(f"Usuario '{username}' no encontrado.")


def traer_usuario_dni():
    dni = input("Ingrese el DNI del usuario a traer: ")

    if dni in usuarios_coder:
        usuario = usuarios_coder[dni]
        print(f"Usuario encontrado: {usuario}")
    else:
        print("Usuario no encontrado.")


""" traer un usuario especifico buscando con su email """


def traer_usuario_email():
    email = input("Ingrese el Email del usuario a traer: ")

    for usuario in usuarios_coder.values():
        if usuario["email"] == email:
            print(f"Usuario encontrado: {usuario}")
            return

    print("Usuario no encontrado.")


"""traer todo el diccionario"""


def traer_todos_los_usuarios():
    if usuarios_coder:
        for dni, usuario in usuarios_coder.items():
            print(f"DNI: {dni}, Usuario: {usuario}")
    else:
        print("No hay usuarios registrados.")


def login_usuario():
    dni = input("Ingrese su DNI: ")
    contraseña = input("Ingrese su contraseña: ")

    if dni in usuarios_coder and usuarios_coder[dni]["contraseña"] == contraseña:
        print(f"Bienvenido, {usuarios_coder[dni]['nombre']}!")
    else:
        print("DNI o contraseña incorrecta.")


def menu_usuario():
    while True:
        print("\nMenú de Usuario:")
        print("1. Registrar Usuario")
        print("2. Eliminar Usuario")
        print("3. Traer Usuario por DNI")
        print("4. Traer Usuario por Email")
        print("5. Traer Todos los Usuarios")
        print("6. Login Usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            eliminar_usuario()
        elif opcion == "3":
            traer_usuario_dni()
        elif opcion == "4":
            traer_usuario_email()
        elif opcion == "5":
            traer_todos_los_usuarios()
        elif opcion == "6":
            login_usuario()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


def main():
    menu_usuario()


if __name__ == "__main__":
    main()
