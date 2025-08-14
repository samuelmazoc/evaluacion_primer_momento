import csv
from datetime import datetime
import json

def cargar_compras(ruta):
    compras_validas = []
    try:
        with open(ruta, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for fila in reader:
                try:
                    cantidad = int(fila["cantidad"])
                    precio_unitario = int(fila["precio_unitario"])
                    if cantidad <= 0 or precio_unitario <= 0:
                        print(f"Advertencia: Fila inválida {fila}")
                        continue
                    try:
                        datetime.strptime(fila["fecha"], "%Y-%m-%d")
                    except ValueError:
                        print(f"Advertencia: Fecha inválida {fila['fecha']}")
                        continue
                    compras_validas.append({
                        "cliente": fila["cliente"],
                        "fecha": fila["fecha"],
                        "producto": fila["producto"],
                        "cantidad": cantidad,
                        "precio_unitario": precio_unitario
                    })
                except Exception as e:
                    print(f"Error procesando fila {fila}: {e}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta}")
    return compras_validas

def estadisticas(data):
    total_ingresos = 0
    ingresos_por_producto = {}
    compras_por_cliente = {}
    for compra in data:
        ingreso = compra["cantidad"] * compra["precio_unitario"]
        total_ingresos += ingreso
        producto = compra["producto"]
        ingresos_por_producto[producto] = ingresos_por_producto.get(producto, 0) + ingreso
        cliente = compra["cliente"]
        compras_por_cliente[cliente] = compras_por_cliente.get(cliente, 0) + compra["cantidad"]
    top_producto = max(ingresos_por_producto, key=ingresos_por_producto.get)
    resumen = {
        "total_ingresos": total_ingresos,
        "top_producto_por_ingresos": top_producto,
        "compras_por_cliente": compras_por_cliente,
        "bono": total_ingresos > 6_000_000
    }
    return resumen

def generar_reporte(resumen, ruta_salida):
    if resumen.get("bono"):
        resumen["mensaje"] = "Umbral superado, aplicar descuento corporativo 5% en próxima compra"
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(resumen, f, indent=4, ensure_ascii=False)
    print("Archivo de reporte listo en", ruta_salida)

