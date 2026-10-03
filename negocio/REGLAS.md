# Reglas vigentes

> Valores marcados con (P) están pendientes de aprobación (aprobaciones/pendientes.md).

## Dinero
- Capital de riesgo máximo: **300 €**
- Stop-loss (pérdida acumulada): **270 €** (P #001)
- Publicidad máxima en test: **10 €/día** en total (todos los canales)
- Gasto autónomo por operación: **20 €** (P #002)
- Descuentos autónomos: ≤ 15 %
- Ajuste autónomo de precio: ±20 %, nunca por debajo de MC ≥ 0

## Economía unitaria (por producto, en finanzas/unit_economics.csv)
- Precio sin IVA = precio con IVA / 1,21 (tipo general; revisar tipo por producto)
- MC = precio sin IVA − coste producto − envío − comisión pasarela − derechos de aduana (3 €/artículo si viene de fuera de la UE) − reserva de incidencias (5 % del precio)
- CPA de equilibrio = MC · ROAS de equilibrio = precio sin IVA / MC · CPA objetivo = MC × 0,7
- Criterio de entrada a test: MC ≥ 15 € (con 10 €/día, MC menor no deja margen para aprender)

## Reglas de corte de anuncios
- Gasto ≥ 1× CPA equilibrio y 0 añadidos al carrito → pausar anuncio
- Gasto ≥ 1,5× CPA equilibrio sin ventas → pausar anuncio
- Producto con gasto ≥ 3× CPA equilibrio sin ventas → descartar para pago y notificar
- CTR enlace < 0,8 % tras 1.000 impresiones → cambiar gancho
- CPA ≤ objetivo 3 días seguidos con ≥ 3 ventas → candidato a escalar (aprobación)

## Alertas rojas
- Chargebacks > 0,5 % · reembolsos > 10 % · aviso/bloqueo de cuenta · stop-loss alcanzado

## Historial de cambios
| Fecha | Regla | Antes | Después | Motivo |
|---|---|---|---|---|
| 2026-10-03 | Stop-loss | 800 € | 270 € (P) | Superaba el capital |
| 2026-10-03 | Gasto autónomo | 50 € | 20 € (P) | Proporción al capital |
