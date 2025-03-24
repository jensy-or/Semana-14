def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Definimos la función calcular_descuento que toma dos parámetros: monto_total y porcentaje_descuento (10% por defecto).
    
    # Calcular el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)  # Calculamos el descuento multiplicando el monto total por el porcentaje.
    
    # Calcular el monto final después del descuento
    monto_final = monto_total - descuento  # Restamos el descuento del monto total para obtener el monto final a pagar.
    
    # Crear un diccionario con los resultados
    resultados = {
        "monto_total": monto_total,  # Almacenamos el monto total en el diccionario.
        "descuento": descuento,  # Almacenamos el monto del descuento en el diccionario.
        "monto_final": monto_final  # Almacenamos el monto final a pagar en el diccionario.
    }
    
    return resultados  # Devolvemos el diccionario con los resultados.

# Programa principal
if __name__ == "__main__":
    # Comprobamos si el script se está ejecutando directamente.
    
    continuar = "SI"  # Inicializamos la variable continuar con "SI" para entrar en el bucle.
    
    while continuar.upper() == "SI":  # Iniciamos un bucle que continuará mientras continuar sea "SI".
        # Solicitar al usuario el monto total de la compra
        monto_compra = float(input("Ingrese el monto total de la compra: "))  # Pedimos al usuario que ingrese el monto total.
        
        # Preguntar si desea aplicar un porcentaje de descuento diferente
        aplicar_descuento = input("¿Desea aplicar un porcentaje de descuento diferente? (S/N): ").upper()  # Pedimos al usuario que indique si desea un descuento diferente y convertimos la respuesta a mayúsculas.
        
        if aplicar_descuento == 'S':  # Si el usuario responde 'S' (sí)
            porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))  # Pedimos el porcentaje de descuento.
        else:  # Si el usuario responde cualquier otra cosa (incluyendo 'N')
            porcentaje_descuento = 10  # Usamos el porcentaje de descuento predeterminado del 10%.
        
        # Llamar a la función calcular_descuento y almacenar los resultados
        resultados = calcular_descuento(monto_compra, porcentaje_descuento)  # Llamamos a la función y almacenamos los resultados.
        
        # Retornar los resultados
        monto_total = resultados['monto_total']  # Almacenamos el monto total.
        descuento = resultados['descuento']  # Almacenamos el monto del descuento.
        monto_final = resultados['monto_final']  # Almacenamos el monto final a pagar.
        
        # Imprimir resultados en mayúsculas
        print(f"MONTO TOTAL: {monto_total} | DESCUENTO: {descuento} | MONTO FINAL A PAGAR: {monto_final}")  
        # Mostramos el monto total, el descuento y el monto final a pagar en letras mayúsculas.
        
        # Preguntar al usuario si desea realizar otro cálculo
        continuar = input("¿Desea realizar otro cálculo? (SI/NO): ").upper()  # Preguntamos si desea continuar y convertimos la respuesta a mayúsculas.
