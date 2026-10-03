"""Proyección a 12 meses de la app de Shopify (enfoque v2). Uso: python3 proyeccion_v2.py
Supuestos (todos [SUPUESTO] salvo las comisiones de Shopify):
- ARPU 32 $/mes ≈ 29 € (mezcla de los planes de 19, 39 y 79 $)
- Shopify: 0 % de reparto de ingresos hasta 1 M$ de por vida; 2,9 % de procesamiento
- Hosting en plan gratuito al principio; 5 €/mes a partir de 30 clientes
- Churn mensual del 3 %
- Coste fijo legal: RETA 80 + gestor 35 = 115 €/mes desde el primer cobro
- Mes 1 = mes de lanzamiento en la App Store (aprox. 6–8 semanas después de aprobar)
"""
ARPU_EUR = 29 * (1 - 0.029)
CHURN = 0.03
IRPF = 0.30
ALTAS = {  # nuevos clientes de pago por mes (incluye la fase 2: suite UE desde el mes 7 en optimista)
    "Pesimista": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "Base":      [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6],
    "Optimista": [2, 4, 6, 8, 9, 10, 14, 16, 18, 20, 22, 24],
}

def main():
    for nombre, altas in ALTAS.items():
        subs, acum, fila = 0.0, 0.0, []
        for m, a in enumerate(altas, 1):
            subs = subs * (1 - CHURN) + a
            mrr = subs * ARPU_EUR
            fijo = (115 if subs > 0 else 0) + (5 if subs >= 30 else 0)
            ben = mrr - fijo
            acum += ben
            if m in (3, 6, 9, 12):
                fila.append(f"M{m}: {subs:4.0f} clientes · MRR {mrr:6.0f} € · beneficio {ben:+5.0f} €")
        neto12 = max(ben, 0) * (1 - IRPF)
        print(f"{nombre}\n  " + "\n  ".join(fila))
        print(f"  Acumulado 12 m: {acum:+.0f} € · neto mes 12 tras IRPF: {neto12:.0f} €/mes · ARR mes 12: {mrr*12:.0f} €\n")

if __name__ == "__main__":
    main()
