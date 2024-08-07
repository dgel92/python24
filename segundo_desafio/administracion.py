from base_datos import usuarios, guardar_usuarios


class Administracion:
    def __init__(self) -> None:
        self.usuarios = usuarios

    def listar_usuarios(self):
        print("\nLista de usuarios")
        for usuario in self.usuarios:
            print(usuario)

    def crear_usuario(self):
        print("\nCreación de usuario")
        username = input("Username: ")
        for usuario in self.usuarios:
            if username == usuario["username"]:
                print("El usuario ya existe.")
                return
        password = input("Password: ")
        password_confirm = input("Confirma tu contraseña: ")
        if password != password_confirm:
            print("Las contraseñas no coinciden.")
            return
        while True:
            telefono = input("Ingresa tu celular (10 dígitos): ")
            if len(telefono) == 10 and telefono.isdigit():
                telefono = int(telefono)
                break
            else:
                print("Número no válido. Por favor, ingresa un número de 10 dígitos.")
        nuevo_usuario = {
            "username": username,
            "password": password,
            "telefono": telefono,
        }
        self.usuarios.append(nuevo_usuario)
        guardar_usuarios(self.usuarios)
        print("Usuario creado exitosamente, ¡bienvenido!")
        print("Usuarios después de crear:")
        self.listar_usuarios()

    def eliminar_usuario(self):
        print("\nEliminar usuario")
        username = input("Ingresa el nombre de usuario que deseas eliminar: ")
        usuario_a_eliminar = None
        for usuario in self.usuarios:
            if username == usuario["username"]:
                password = input("Ingresa la contraseña del usuario: ")
                if password == usuario["password"]:
                    usuario_a_eliminar = usuario
                    break
                else:
                    print("Contraseña incorrecta. No se pudo eliminar el usuario.")
                    return

        if usuario_a_eliminar:
            self.usuarios.remove(usuario_a_eliminar)
            guardar_usuarios(self.usuarios)
            print(f"Usuario '{username}' eliminado exitosamente.")
            print("Usuarios después de eliminar:")
            self.listar_usuarios()
        else:
            print(f"Usuario '{username}' no encontrado.")

    def login(self):
        print("\nLogin")
        username = input("Username: ")
        for usuario in self.usuarios:
            if username == usuario["username"]:
                password = input("Ingresa la contraseña: ")
                if password == usuario["password"]:
                    print("\nLogin exitoso.")
                    return
                else:
                    print("Contraseña incorrecta.")
                    return
        print(f"Usuario '{username}' no encontrado.")


def menu(admin: Administracion):
    while True:
        print("\nMenu de Administracion")
        print("1. Listar usuarios")
        print("2. Crear usuario")
        print("3. Eliminar usuario")
        print("4. Login")
        print("5. Salir")
        entrada = input("Seleccione una opción: ")
        if entrada == "1":
            admin.listar_usuarios()
        elif entrada == "2":
            admin.crear_usuario()
        elif entrada == "3":
            admin.eliminar_usuario()
        elif entrada == "4":
            admin.login()
        elif entrada == "5":
            print("Saliendo...")
            return
        else:
            print("Opción inválida, intenta nuevamente.")
            continue


def main():
    admin = Administracion()
    menu(admin)


if __name__ == "__main__":
    main()
