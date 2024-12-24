import datetime

def calcular_ciclo(fecha_inicio):
    """
    Calcula el ciclo en base a la fecha de inicio.
    Un ciclo dura 4 meses:
    - Ciclo 1: abril-julio
    - Ciclo 2: septiembre-diciembre
    Cada año tiene únicamente 2 ciclos.
    """
    hoy = datetime.date.today()

    # Validación: la fecha de inicio debe ser en abril o septiembre
    if fecha_inicio.month not in [4, 9]:
        raise ValueError("La fecha de inicio debe ser en abril o septiembre.")

    # Determinar el ciclo inicial basado en el mes de inicio
    ciclo_inicio = 1 if fecha_inicio.month == 4 else 2

    # Calcular el número de ciclos transcurridos desde el año de inicio hasta el año actual
    total_ciclos = 0

    # Iterar año por año para contar ciclos
    for year in range(fecha_inicio.year, hoy.year + 1):
        if year == fecha_inicio.year:  # Año de inicio
            if fecha_inicio.month == 4:
                total_ciclos += 2  # Cuenta ambos ciclos del año de inicio
            elif fecha_inicio.month == 9:
                total_ciclos += 1  # Solo cuenta el segundo ciclo
        elif year == hoy.year:  # Año actual
            if hoy.month >= 4 and hoy.month <= 7:
                total_ciclos += 1  # Ciclo 1 del año actual
            elif hoy.month >= 9:
                total_ciclos += 2  # Ambos ciclos del año actual
        else:
            total_ciclos += 2  # Cuenta ambos ciclos para años intermedios

    return total_ciclos

# Base de datos simulada
alumnos = {}

# Funciones del programa
def registrar_alumno():
    while True:
        nombre = input("Ingrese el nombre del alumno o escriba 'cancelar' para regresar: ")
        if nombre.lower() == 'cancelar':
            return
        if not nombre.isalpha():
            print("El nombre solo debe contener letras y no debe incluir números. Intente nuevamente.")
        else:
            break

    while True:
        fecha_str = input("Ingrese la fecha de inicio de estudios (YYYY-MM-DD) o escriba 'cancelar' para regresar: ")
        if fecha_str.lower() == 'cancelar':
            return
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()

            # Validación para que solo acepte fechas en abril o septiembre
            if fecha_inicio.month not in [4, 9]:
                print("La fecha de inicio debe ser en abril o septiembre. Intente nuevamente.")
                continue

            ciclo = calcular_ciclo(fecha_inicio)
            alumnos[nombre] = {
                "fecha_inicio": fecha_inicio,
                "ciclo": ciclo,
                "aulas": [],
                "cursos": {},
            }
            print(f"Alumno registrado exitosamente. {nombre} está en el ciclo {ciclo}.")
            break
        except ValueError:
            print("Fecha inválida. Por favor ingrese una fecha en el formato correcto (YYYY-MM-DD) y asegúrese de que sea válida.")

def asignar_datos():
    while True:
        nombre = input("Ingrese el nombre del alumno o escriba 'cancelar' para regresar: ")
        if nombre.lower() == 'cancelar':
            return
        if nombre not in alumnos:
            print("Alumno no encontrado. Intente nuevamente.")
        else:
            break

    while True:
        print("\nOpciones de asignación:")
        print("1. Asignar aula")
        print("2. Asignar cursos y créditos")
        print("3. Asignar horarios personalizados")
        print("4. Cancelar y regresar al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                aula = input("Ingrese el aula a asignar o escriba 'cancelar' para regresar: ")
                if aula.lower() == 'cancelar':
                    break
                alumnos[nombre]["aulas"].append(aula)
                print(f"Aula {aula} asignada a {nombre}.")
                break

        elif opcion == "2":
            while True:
                curso = input("Ingrese el nombre del curso o escriba 'cancelar' para regresar: ")
                if curso.lower() == 'cancelar':
                    break
                try:
                    creditos = int(input(f"Ingrese los créditos para el curso {curso} o escriba 'cancelar' para regresar: "))
                    if creditos == 'cancelar':
                        break
                    alumnos[nombre]["cursos"][curso] = {
                        "creditos": creditos
                    }
                    print(f"Curso {curso} con {creditos} créditos asignado a {nombre}.")
                    break
                except ValueError:
                    print("Los créditos deben ser un número entero. Intente nuevamente.")

        elif opcion == "3":
            while True:
                curso = input("Ingrese el nombre del curso para asignar horario o escriba 'cancelar' para regresar: ")
                if curso.lower() == 'cancelar':
                    break
                if curso not in alumnos[nombre]["cursos"]:
                    print(f"El curso {curso} no está registrado para {nombre}.")
                    continue
                horario = input("Ingrese el horario (ejemplo: Lunes 8:00-10:00) o escriba 'cancelar' para regresar: ")
                if horario.lower() == 'cancelar':
                    break
                alumnos[nombre]["cursos"][curso]["horario"] = horario
                print(f"Horario asignado al curso {curso} para {nombre}.")
                break

        elif opcion == "4":
            print("Regresando al menú principal.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrar_datos():
    while True:
        nombre = input("Ingrese el nombre del alumno o escriba 'cancelar' para regresar: ")
        if nombre.lower() == 'cancelar':
            return
        if nombre not in alumnos:
            print("Alumno no encontrado. Intente nuevamente.")
        else:
            break

    print("\nInformación del alumno:")
    print(f"Nombre: {nombre}")
    print(f"Fecha de inicio: {alumnos[nombre]['fecha_inicio']}")
    print(f"Ciclo actual: {alumnos[nombre]['ciclo']}")
    print(f"Aulas asignadas: {', '.join(alumnos[nombre]['aulas']) if alumnos[nombre]['aulas'] else 'Ninguna'}")
    print("Cursos y detalles:")
    for curso, detalles in alumnos[nombre]["cursos"].items():
        print(f"  - {curso}: {detalles['creditos']} créditos, Horario: {detalles.get('horario', 'No asignado')}")

# Menú principal
def menu():
    while True:
        print("\nMenú principal")
        print("1. Registrar alumno")
        print("2. Asignar datos a un alumno")
        print("3. Mostrar información de un alumno")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            asignar_datos()
        elif opcion == "3":
            mostrar_datos()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
menu()