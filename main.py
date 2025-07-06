# Iniciamos con la formula para calcular el IMC
def calculadora(peso, altura, lista): # Creamos una funcion que calcula el IMC, esta funcion solicita el peso, la altura y la lista donde se comparara
    respuesta = [] # Creamos la variable repuesta que almacenara los resultados
    estado = None # Creamos una variable que almacenara el estado de salud

    # Realizamos el calculo del IMC
    imc = peso / altura**2
    
    # Recorremos la lista y comparamos
    for limite, etiqueta in lista: # Este ciclo for es un foreach que traera los datos la lista para poder trabajar con ellos
        if imc < limite: # si imc es menor a limite guardaremos la etiqueta en nuestra variable estado
            estado = etiqueta 
            respuesta = [imc, estado] # almacenamos el imc y el estado en nuestra variable respuesta
            return respuesta # retornamos la variable respuesta

# Creamos una funcion dedicada para romper el ciclo while que nos permitira ejecutar el programa en bucle, recibe como parametro una entrada que en este caso sera un caracter del teclado
def decision(entrada):
    entrada=entrada.strip()
    if entrada=="n": # Si la respuesta es n retornaremos False
        return False
    elif entrada!="y": # Si la respuesta es diferente de y haremos una llamada recursiva a la funcion y notificaremos que la opcion elegida es invalida
        print(impresiones[8])
        if(decision(input(f"{impresiones[1]} \n{impresiones[2]}\n"))==False): # En caso de que la respuesta sea falsa retornaremos false
            return False

#Creamos una funcion que detecta si los datos ingresados son o no numeros
def verificacion(entrada):
    try: # intentamos convertir la entrada en un flotante en caso de exito devolvemos true
        float(entrada)
        return True
    except ValueError: # en caso de error devolvemos false
        return False
    
def captura(entrada): # Creamos una funcion que devuelve la entrada como flotante en caso de ser numero
    if verificacion(entrada) == True: # si verificacion devuelve true transformamos el dato a numero flotante y lo retornamos
        return float(entrada)
    else: # caso contrario devolvemos false
        return False

def verificacionEntrada(entrada): # verificacionEntrada nos ayuda a verificar que el usuario ingreso texto en formato stribg y no dejo el campo vacio
  solo_letras = ''.join(d for d in entrada if not d.isdigit()) # Con ayuda de una expresion generadora devomvemos de entrada todo aquel caracter que no sea digito, con join() unimos el elemento generado a la cadena de texto
  
  if len(solo_letras) > 0: # En caso de que solo_letras sea mayor a 0 retornaremos la misma
    return solo_letras
  elif solo_letras=='': # En caso de que sea '' Solicitaremos que se ingrese el dato solicitado
    entrada=input("Porfavor ingresa el dato solicitado: ").strip() # Pedimos el dato y lo almacenamos en entrada
    solo_letras = verificacionEntrada(entrada) # Hacemos una llamada recursiva a verificacionEntrada y almacenamos la respuesta rn solo_letras
    if solo_letras is not None: # En caso de que solo_letras no sea None retornamos el mismo
      return solo_letras
      

# Creamos una lista de tuplas con los datos de IMC para adultos otorgados por la OMS
CATEGORIAS_ADULTOS = [
    (18.5, "Bajo peso"),
    (25.0, "Peso saludable"),
    (30.0, "Sobrepeso (pre obesidad)"),
    (35.0, "Obesidad I"),
    (40.0, "Obesidad II"),
    (float("inf"), "Obesidad III"),
]
# Creamos una lista con los mensajes que se mostraran en pantalla
impresiones =[
    "Bienvenidos, calculemos tu Indice de Masa Corporal juntos.",
    "Para calcular de nuevo presione: y",
    "Para salir presione: n ",
    "Porfavor ingresa tu peso: ",
    "Porfavor ingresa tu estatura: ",
    "Porfavor ingresa tu edad: ", # Para escalar el proyecto para cualquier edad
    "Porfavor ingresa tu sexo: ", # Para escalar el proyecto por sexo
    "Hasta luego",
    "Opción invalida",
    "Porfavor ingresa tu nombre: ",
    "Porfavor ingresa tu apellido paterno: ",
    "Porfavor ingresa tu apellido materno: ",
    "Porfavor ingresa la cantidad con numeros"
]

print(impresiones[0]) # Imprimimos en pantalla la bienvenida
while True: # Creamos un bucle infinito para que el usuario pueda elegir cuando salir del mismo
    nombre = verificacionEntrada(input(impresiones[9]).strip())
    apellido_paterno = verificacionEntrada(input(impresiones[10]).strip())
    apellido_materno = verificacionEntrada(input(impresiones[11]).strip())
    
    # Creamos las variables edad, peso y altura para almacenar los datos
    edad = 0
    peso = 0
    altura = 0
    # Con los ciclos while solicitaremos que ingresen los datos los ciclos se rompera cuando los datos sean correctos
    while True:
        edad = captura(input(impresiones[5]).strip())
        if edad != False:
            break
        print(impresiones[12])
    while True:
        peso = captura(input(impresiones[3]).strip())
        if peso != False:
            break
        print(impresiones[12])
    while True:
        altura = captura(input(impresiones[4]).strip())
        if altura != False:
            break
        print(impresiones[12])


    # Llamamos a nuestra funcion calculadora y le pasamos los datos que solicita, almacenamos su respuesta en una variable llamada res
    res=calculadora(peso,altura,CATEGORIAS_ADULTOS) 
    # Imprimimos en pantalla las respuestas primero el resultado del calculo en la posicion 0 y posteriormente el estado de salud en la posicion 1 
    print(f"\nNOMBRE: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"EDAD: {int(edad)} años")
    print(f"\nTu IMC es: {res[0]:.2f} kg/m²\n")
    print(f"Estado nutricional: {res[1]}\n")

    # solicitamos al usuario que decida que accion tomar, salir o calcular un nuevo IMC, para tomar esta decision llamamos a nuestra funcion decision() la cual nos devolvera un booleano y lo almacenara en nuestra variable res
    res=decision(input(f"{impresiones[1]} \n{impresiones[2]}\n"))

    if res==False: # Si la respuesta es False mostraremos en pantalla un mensaje de despedida y romperemos el ciclo para terminar el programa
        print(impresiones[7])
        break