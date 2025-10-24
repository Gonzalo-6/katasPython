#Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
# a. Solicitar al usuario el precio original de un artículo.
#b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
#e.Mostrar el precio final de la compra, considerando o no el descuento.
#f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.

def calcular_precio_final(precio_original, tiene_cupon, valor_cupon=0):
    if tiene_cupon.lower() == 'sí' or tiene_cupon.lower() == 'si':
        if valor_cupon > 0:
            precio_final = precio_original - valor_cupon
            if precio_final < 0:
                precio_final = 0
            return precio_final
        else:
            return "Valor del cupón inválido. Debe ser mayor a cero."
    elif tiene_cupon.lower() == 'no':
        return precio_original
    else:
        return "Respuesta inválida. Por favor, responde 'sí' o 'no'."
if __name__ == "__main__":
    try:
        precio_original = float(input("Introduce el precio original del artículo: "))
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        if tiene_cupon == 'sí' or tiene_cupon == 'si':
            valor_cupon = float(input("Introduce el valor del cupón de descuento en euros: "))
            precio_final = calcular_precio_final(precio_original, tiene_cupon, valor_cupon)
        elif tiene_cupon == 'no':
            precio_final = calcular_precio_final(precio_original, tiene_cupon)
        else:
            precio_final = "Respuesta inválida. Por favor, responde 'sí' o 'no'."
        print(f"El precio final de la compra es: {precio_final}.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número válido para el precio y el valor del cupón.")