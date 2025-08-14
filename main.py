from utils import cargar_compras, estadisticas, generar_reporte

if __name__ == "__main__":
    ruta_csv = "data/compras.csv"
    datos = cargar_compras(ruta_csv)
    resumen = estadisticas(datos)
    print("\n--- Resumen de Ventas ---")
    print(f"Total ingresos: {resumen['total_ingresos']}")
    print(f"Producto top por ingresos: {resumen['top_producto_por_ingresos']}")
    print(f"Compras por cliente: {resumen['compras_por_cliente']}")
    print(f"Bono: {'Sí' if resumen['bono'] else 'No'}")
    generar_reporte(resumen, "reporte.json")
