"""Escenarios de costes fijos mensuales y break-even (Fase 0).

Uso: python3 costes_fijos.py
Todas las cifras son supuestos documentados en FASE0_INVENTARIO.md; cámbialas aquí.
"""

CAPITAL = 1500
RESERVA_PCT = 20
GASTO_MENSUAL_MAX = 150

# Coste fijo mensual por escenario (€/mes)
ESCENARIOS = {
    "A · Autónomo + gestor (sin cuota cero)": {"cuota_reta": 80, "gestor": 35, "herramientas": 15},
    "B · Autónomo + cuota cero CCAA + gestor": {"cuota_reta": 0, "gestor": 35, "herramientas": 15},
    "C · Autónomo, contabilidad propia (sin gestor)": {"cuota_reta": 80, "gestor": 0, "herramientas": 15},
    "D · Validación previa al alta en RETA (a confirmar con gestor)": {"cuota_reta": 0, "gestor": 0, "herramientas": 10},
}

# Producto digital tipo vendido vía merchant of record (Lemon Squeezy: 5 % + 0,50 $ ≈ 0,46 €)
PRECIO_CON_IVA = 29.0
IVA = 0.21                     # el MoR repercute el IVA del país del comprador; usamos 21 % como referencia
COMISION_PCT = 0.05 + 0.015    # base + tarjeta internacional
COMISION_FIJA = 0.46
PAYOUT_PCT = 0.01              # pago a banco no estadounidense


def margen_unitario(precio_con_iva: float) -> float:
    base = precio_con_iva / (1 + IVA)
    comision = precio_con_iva * COMISION_PCT + COMISION_FIJA
    neto = base - comision
    return neto * (1 - PAYOUT_PCT)


def main() -> None:
    disponible = CAPITAL * (1 - RESERVA_PCT / 100)
    m = margen_unitario(PRECIO_CON_IVA)
    print(f"Capital disponible (sin reserva): {disponible:.0f} €")
    print(f"Margen de contribución por venta de {PRECIO_CON_IVA:.0f} € (IVA incl.): {m:.2f} € (CAC=0)\n")
    print(f"{'Escenario':<62}{'Fijo/mes':>9}{'Ventas/mes BE':>15}{'Meses de pista':>16}")
    for nombre, c in ESCENARIOS.items():
        fijo = sum(c.values())
        ventas_be = fijo / m
        pista = disponible / fijo if fijo else float("inf")
        print(f"{nombre:<62}{fijo:>8.0f}€{ventas_be:>15.1f}{pista:>16.1f}")
    objetivo = 1000
    fijo_a = sum(ESCENARIOS["A · Autónomo + gestor (sin cuota cero)"].values())
    # IRPF aproximado marginal 19-24 % sobre el rendimiento: usamos 20 % para el objetivo neto
    bruto_necesario = objetivo / 0.80 + fijo_a
    print(f"\nObjetivo mes 6 (1.000 € netos tras IRPF ~20 %, escenario A):"
          f" {bruto_necesario:.0f} € de margen/mes ≈ {bruto_necesario / m:.0f} ventas/mes de {PRECIO_CON_IVA:.0f} €")


if __name__ == "__main__":
    main()
