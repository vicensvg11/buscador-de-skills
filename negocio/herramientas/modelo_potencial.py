"""Modelo de potencial de Recargo+ a 36 meses: 3 escenarios + sensibilidad.
Uso: python3 modelo_potencial.py
Supuestos marcados [S]; fuentes en negocio/ENFOQUE_V2.md y en la presentación de potencial.
"""
SHOPIFY_FEE = 0.029           # procesamiento; 0 % de reparto de ingresos hasta 1 M$ (shopify.dev)
IRPF = 0.30                   # marginal [S], el titular es asalariado
GESTOR = 35                   # €/mes [S]
TRAMOS = [(670,200),(900,220),(1166.7,260),(1300,291),(1500,294),(1700,294),(1850,310),(2030,315),
          (2330,320),(2760,340),(3190,370),(3620,390),(4050,420),(6000,500),(1e12,590)]  # cuotas RETA 2026

def cuota_reta(m, neto_mensual, neto_12m):
    if m <= 12: return 80                                   # tarifa plana
    if m <= 24 and neto_12m < 17000: return 80              # prórroga si rendimiento < SMI [S]
    base = max(neto_mensual, 0) * 0.93                      # 7 % de gastos genéricos
    return next(c for lim, c in TRAMOS if base <= lim)

def ramp(a, b, m0, m1, m):
    if m < m0: return 0
    if m >= m1: return b
    return a + (b - a) * (m - m0) / (m1 - m0)

# Altas mensuales por fase y ARPU (€/mes); churn mensual
ESC = {
 "Pesimista": dict(churn=0.05, p1=lambda m: 1, p2=lambda m: 0, p3=lambda m: 0, arpu=(27, 0, 0)),
 "Conservador": dict(churn=0.03, p1=lambda m: ramp(1, 6, 1, 12, m) if m <= 18 else 5,
                    p2=lambda m: 0, p3=lambda m: 0, arpu=(29, 0, 0)),
 "Base":      dict(churn=0.03, p1=lambda m: ramp(1, 6, 1, 12, m) if m <= 18 else 5,
                    p2=lambda m: ramp(2, 8, 4, 24, m), p3=lambda m: 0, arpu=(29, 22, 0)),
 "Optimista": dict(churn=0.025, p1=lambda m: ramp(2, 10, 1, 12, m),
                    p2=lambda m: ramp(3, 15, 4, 24, m), p3=lambda m: ramp(5, 60, 7, 24, m), arpu=(29, 24, 12)),
}

def simular(e, meses=36, churn=None, arpu_mult=1.0):
    churn = e["churn"] if churn is None else churn
    s = [0.0, 0.0, 0.0]; caja = -18; netos = []; out = []; be = None
    for m in range(1, meses + 1):
        s = [s[0]*(1-churn) + e["p1"](m), s[1]*(1-churn) + e["p2"](m), s[2]*(1-churn) + e["p3"](m)]
        mrr = sum(x*a for x, a in zip(s, e["arpu"])) * arpu_mult
        subs = sum(s)
        hosting = 0 if subs < 30 else 5 + 0.05*subs
        ingreso = mrr * (1 - SHOPIFY_FEE)
        pre = ingreso - GESTOR - hosting
        reta = cuota_reta(m, pre, sum(netos[-12:])) if subs > 0 else 0
        neto = pre - reta if subs > 0 else 0
        netos.append(neto); caja += neto
        if be is None and neto > 0: be = m
        out.append(dict(m=m, subs=subs, mrr=mrr, neto=neto, despues_irpf=max(neto,0)*(1-IRPF), caja=caja, reta=reta))
    return out, be

def main():
    for nombre, e in ESC.items():
        r, be = simular(e)
        print(f"== {nombre} (break-even mensual en el mes {be})")
        for m in (6, 12, 24, 36):
            x = r[m-1]
            print(f"  M{m:>2}: {x['subs']:5.0f} clientes · MRR {x['mrr']:7.0f} € · ARR {x['mrr']*12:8.0f} € · "
                  f"neto {x['neto']:+7.0f} €/mes (RETA {x['reta']:.0f}) · tras IRPF {x['despues_irpf']:6.0f} € · caja acum. {x['caja']:+8.0f} €")
        b12 = sum(x['neto'] for x in r[24:36])
        print(f"  Beneficio de los meses 25–36: {b12:.0f} € → valoración orientativa 2–4×: {2*b12:.0f}–{4*b12:.0f} € (antes del descuento por depender de una plataforma)\n")
    print("== Sensibilidad (escenario base, MRR en el mes 24)")
    for ch in (0.02, 0.03, 0.05):
        for am in (0.8, 1.0, 1.2):
            r, _ = simular(ESC["Base"], churn=ch, arpu_mult=am)
            print(f"  churn {ch:.0%} · ARPU ×{am}: MRR M24 {r[23]['mrr']:6.0f} € · neto M24 {r[23]['neto']:+6.0f} €")
    need = (1000/(1-IRPF) + GESTOR + 300) / (28*(1-SHOPIFY_FEE))
    print(f"\nClientes necesarios para 1.000 €/mes netos tras IRPF (con RETA de unos 300 €): ≈{need:.0f}")

if __name__ == "__main__":
    main()
