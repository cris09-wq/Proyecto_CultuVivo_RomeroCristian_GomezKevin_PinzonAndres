# SISTEMA CULTUVIVO - MVP EN PYTHON


# Listas principales para almacenar los datos
eventos = []
asistentes = []

# Variables para generar IDs sencillos
id_evento_contador = 1
id_asistente_contador = 1


def crear_evento():
    global id_evento_contador

    print("\n--- CREAR NUEVO EVENTO ---")
    nombre = input("Nombre del evento: ")
    fecha = input("Fecha y hora (ej: 2026-10-15 18:00): ")
    lugar = input("Lugar del evento: ")

    try:
        capacidad = int(input("Capacidad máxima de asistentes: "))
    except ValueError:
        print(" Error: La capacidad debe ser un número entero.")
        return

    # Diccionario para representar el evento
    nuevo_evento = {
        "id": id_evento_contador,
        "nombre": nombre,
        "fecha": fecha,
        "lugar": lugar,
        "capacidad": capacidad,
        "inscritos": 0,
    }

    eventos.append(nuevo_evento)
    print(f" Evento '{nombre}' creado con éxito (ID: {id_evento_contador})")
    id_evento_contador = id_evento_contador + 1


def listar_eventos():
    print("\n--- LISTA DE EVENTOS ---")
    if len(eventos) == 0:
        print("No hay eventos registrados.")
        return

    for evento in eventos:
        print(f"ID: {evento['id']}")
        print(f"  Nombre: {evento['nombre']}")
        print(f"  Fecha: {evento['fecha']}")
        print(f"  Lugar: {evento['lugar']}")
        print(f"  Cupos: {evento['inscritos']} / {evento['capacidad']}")
        print("-" * 30)


def registrar_asistente():
    global id_asistente_contador

    print("\n--- INSCRIPCIÓN DE ASISTENTE ---")
    if len(eventos) == 0:
        print("No hay eventos disponibles para inscribirse.")
        return

    listar_eventos()

    try:
        id_buscado = int(
            input("Ingrese el ID del evento al que desea asistir: ")
        )
    except ValueError:
        print(" Error: Ingrese un ID válido.")
        return

    # Buscar el evento seleccionado
    evento_encontrado = None
    for evento in eventos:
        if evento["id"] == id_buscado:
            evento_encontrado = evento

    if evento_encontrado is None:
        print(" Error: No existe un evento con ese ID.")
        return

    # ALGORITMO DE CONTROL AUTOMÁTICO DE AFORO (HU02)
    if evento_encontrado["inscritos"] >= evento_encontrado["capacidad"]:
        print("\n BLOQUEADO: El evento ha alcanzado su capacidad máxima.")
        print("No es posible inscribir más asistentes a este evento.")
        return

    # Pedir datos del asistente (HU01)
    identificacion = input("Número de identificación: ")
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    tipo_boleto = input("Tipo de boleto (VIP / General): ")

    print("\nSeleccione el estado inicial de la reserva:")
    print("1. Confirmado")
    print("2. En espera")
    print("3. Cancelado")
    opcion_estado = input("Opción (1-3): ")

    estado = "Confirmado"
    if opcion_estado == "2":
        estado = "En espera"
    elif opcion_estado == "3":
        estado = "Cancelado"

    # Si la reserva es confirmada, aumentamos los inscritos del evento
    if estado == "Confirmado":
        evento_encontrado["inscritos"] = evento_encontrado["inscritos"] + 1

    nuevo_asistente = {
        "id": id_asistente_contador,
        "evento_id": evento_encontrado["id"],
        "evento_nombre": evento_encontrado["nombre"],
        "identificacion": identificacion,
        "nombre": nombre,
        "correo": correo,
        "tipo_boleto": tipo_boleto,
        "estado": estado,
    }

    asistentes.append(nuevo_asistente)
    print(f"\n Asistente '{nombre}' registrado con éxito.")
    print(f"Estado de la reserva: {estado}")
    id_asistente_contador = id_asistente_contador + 1


def listar_asistentes():
    print("\n--- LISTA DE ASISTENTES REGISTRADOS ---")
    if len(asistentes) == 0:
        print("No hay asistentes registrados.")
        return

    for asistente in asistentes:
        print(f"ID Registro: {asistente['id']}")
        print(f"  Nombre: {asistente['nombre']}")
        print(f"  Identificación: {asistente['identificacion']}")
        print(f"  Evento: {asistente['evento_nombre']}")
        print(f"  Tipo de boleto: {asistente['tipo_boleto']}")
        print(f"  Estado de reserva: {asistente['estado']}")
        print("-" * 30)



# MENÚ PRINCIPAL

ejecutando = True

while ejecutando:
    print("\n=================================")
    print("   SISTEMA FUNDACIÓN CULTUVIVO   ")
    print("=================================")
    print("1. Crear evento (Administrador)")
    print("2. Ver eventos")
    print("3. Registrar/Inscribir asistente")
    print("4. Ver lista de asistentes")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        crear_evento()
    elif opcion == "2":
        listar_eventos()
    elif opcion == "3":
        registrar_asistente()
    elif opcion == "4":
        listar_asistentes()
    elif opcion == "5":
        print("\nSaliendo del sistema... ¡Hasta luego!")
        ejecutando = False
    else:
        print("\n Opción no válida. Intente de nuevo.")