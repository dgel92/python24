lista_alumnos: list[dict] = []

nombre = input("nombre del alumno: ")
materia = input("nombre de la materia: ")

alumno = {
    "nombre": nombre,
    "materia": materia,
}

lista_alumnos.append(alumno)
nombre = input("nombre del alumno: ")
materia = input("nombre de la materia: ")

alumno = {
    "nombre": nombre,
    "materia": materia,
}


lista_alumnos.append(alumno)
print(lista_alumnos)
