
#Funcion para ver la lista 
def ver_diccionario(lista, titulo):    
    respuesta = ""
    numero = 1
    respuesta += "*********************************************************************************************\n"
    respuesta += f"{titulo}\n"
    respuesta += "---------------------------------------------------------------------------------------------\n"
       
    if len(lista) > 0:         
        columnas = list(lista[0].keys())
        for item in lista:     
            respuesta += f"| {numero}. "
            for columna in columnas:
                respuesta += f"| {columna}: {item[columna]} "
            respuesta += '\n---------------------------------------------------------------------------------------------\n'
            numero += 1
    else:
        respuesta += f"No hay objetos en la lista\n"    
    
    respuesta += "*********************************************************************************************\n"   

    return respuesta


#Funcion para agregar nuevos estudiantes
def ingresar_auto(marca, estilo, modelo, placa, autos):
    nuevo_auto = {
        'Marca': marca,
        'Estilo': estilo, 
        'Modelo': int(modelo), 
        'Placa': placa
    }
    autos.append(nuevo_auto)

#Funcion para remover estudiante
def remover_auto(numero, autos):    
    posicion = numero - 1
    auto_eliminado = autos[posicion]
    autos.pop(posicion)    
    return auto_eliminado

#Funcion para limpiar consola segun OS
def limpiar_consola():
    import os
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def opcion_menu(cantidad_opciones):
    bandera = 0
    opcion = 0
    while bandera == 0:
        respuesta = input(f"Opción: ")
        es_numero = respuesta.isdigit()
        if es_numero == True:                    
            opcion = int(respuesta)
            if opcion > 0 and opcion <= cantidad_opciones:                
                break          
                            
        print(f"¡Por favor ingresar un número válido!")   
               
    return opcion

def menu_ingreso_numero(texto_input):
    bandera = 0    
    while bandera == 0:
        respuesta = input(f"{texto_input}")
        es_numero = respuesta.isdigit()
        if es_numero == True:                    
            numero_ingresado = int(respuesta)
            if numero_ingresado > 0:                
                break          
                            
        print(f"¡Por favor ingresar un número!")   
               
    return numero_ingresado





