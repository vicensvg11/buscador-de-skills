"""Proyección a 6 meses del Kit IA art. 4 (tres escenarios). Uso: python3 proyeccion.py"""
NETO_KIT = 62.5        # 69 € + IVA, cobrado vía merchant of record, tras comisiones
NETO_GESTORIA = 180.0  # licencia de reventa para gestorías, 199 € + IVA al año, neto
COMISION_AFILIADO = 0.30
FIJO = {"reta": 80, "gestor": 35, "herramientas": 1}  # dominio prorrateado; resto en planes gratuitos
IRPF = 0.30            # tipo marginal supuesto (el titular es asalariado)

# (ventas directas, ventas vía afiliado, licencias de gestoría) por mes tras el lanzamiento
ESC = {
    "Pesimista": [(0,0,0)]*6,
    "Base":      [(0,0,0),(1,0,0),(1,1,0),(1,1,0),(2,1,0),(2,2,1)],
    "Optimista": [(1,0,0),(2,1,0),(3,2,1),(4,3,0),(5,5,1),(7,7,1)],
}

def main():
    for nombre, meses in ESC.items():
        acum = 0
        fila = []
        for i, (d, a, g) in enumerate(meses, 1):
            ingreso = d*NETO_KIT + a*NETO_KIT*(1-COMISION_AFILIADO) + g*NETO_GESTORIA
            # el alta en RETA se hace con la primera venta; antes solo alta censal (0 €)
            fijo = sum(FIJO.values()) if acum > 0 or ingreso > 0 else FIJO["herramientas"]
            benef = ingreso - fijo
            acum += benef
            fila.append(f"M{i}: {ingreso:6.0f}€ −{fijo:3.0f} = {benef:+5.0f}")
        neto6 = (meses[-1][0]*NETO_KIT + meses[-1][1]*NETO_KIT*(1-COMISION_AFILIADO) + meses[-1][2]*NETO_GESTORIA - sum(FIJO.values()))
        print(f"{nombre:<10} | " + " | ".join(fila))
        print(f"{'':<10}   acumulado 6 meses: {acum:+.0f} € · beneficio mes 6 tras IRPF: {max(neto6,0)*(1-IRPF):.0f} €\n")

if __name__ == "__main__":
    main()
