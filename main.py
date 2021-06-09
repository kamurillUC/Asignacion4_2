import funciones

autos_espacio_mensual = [
     {
        'Marca': 'Toyota',
        'Estilo': 'Corolla',
        'Modelo': 1995,
        'Placa': 'ABC333'
    },

     {
        'Marca': 'Suzuki',
        'Estilo': 'Vitara',
        'Modelo': 2017,
        'Placa': 'BND947'
    },

    {
        'Marca': 'Mazda',
        'Estilo': '323',
        'Modelo': 2010,
        'Placa': '456875'
    },

    {
        'Marca': 'Hyundai',
        'Estilo': 'Tucson',
        'Modelo': 2020,
        'Placa': 'ABC555'
    }
]

todos_autos = autos_espacio_mensual[:]

bandera = 0

while bandera == 0:

    funciones.limpiar_consola()
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    print(f"Menú de opciones:")
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    print(f"1. Ver todos los vehículos\n2. Ver vehiculos con espacio mensual\n3. Registrar vehículo\n4. Remover vehículo\n5. Limpiar lista de vehículos\n6. Salir")    
    print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
    respuesta = funciones.opcion_menu(6)

    if respuesta == 1:  

        funciones.limpiar_consola()
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"1. Ver todos los vehículos")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(funciones.ver_diccionario(todos_autos, 'Lista de todos los vehículos'))
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        respuesta = input("Presione ENTER para continuar...") 

    elif respuesta == 2:
        funciones.limpiar_consola()
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"2. Ver vehiculos con espacio mensual")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(funciones.ver_diccionario(autos_espacio_mensual, 'Lista de vehículos con espacio mensual'))
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        respuesta = input("Presione ENTER para continuar...")

    elif respuesta == 3:      

        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"3. Registrar vehículo")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        marca = input("Marca: ")
        estilo = input("Estilo: ")        
        modelo = funciones.menu_ingreso_numero('Modelo: ')   
        placa = input("Placa: ")           
        
        funciones.ingresar_auto(marca, estilo, modelo, placa, todos_autos)
        print(">< >< >< >< >< Vehículo registrado >< >< >< >< ><") 
        respuesta = input("Presione ENTER para continuar...")   

    elif respuesta == 4:      

        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"4. Remover vehículo")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")        
        print(funciones.ver_diccionario(todos_autos, 'Lista de todos los vehículos'))
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><") 
        numero = funciones.menu_ingreso_numero('Número: ')                        
          
        auto_eliminado = funciones.remover_auto(numero, todos_autos)   
                    
        print(f">< >< >< >< >< El vehículo de Marca: {auto_eliminado['Marca']}, Estilo: {auto_eliminado['Estilo']}, Modelo: {auto_eliminado['Modelo']} y Placa: {auto_eliminado['Placa']} fue removido >< >< >< >< ><") 
        
        respuesta = input("Presione ENTER para continuar...")  

    elif respuesta == 5:      

        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"5. Limpiar lista de vehículos")
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        respuesta = input("¿Está seguro que quiere eliminar todos los vehículos?(Si/No)\n")

        if respuesta.lower().strip() == 'si':
            todos_autos.clear()
            print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
            print(">< >< >< >< >< Todos los vehículos fueron removidos >< >< >< >< ><")             
        else:
            print(">< >< >< >< >< Ningun vehículo fue removido >< >< >< >< ><") 
        print(">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")       
        respuesta = input("Presione ENTER para continuar...")        
    else:
        funciones.limpiar_consola()  
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        print(f"GitHub: kamurillUC")        
        print(f">< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< >< ><")
        break