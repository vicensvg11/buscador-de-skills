# Rutinas programadas propuestas (pendiente de APROBACIÓN #006)

Zona horaria: Europe/Madrid. Requisito previo: conector Shopify autenticado. Las rutinas se activan por fases: antes de tener tienda solo tiene sentido la semanal de investigación.

| Nombre | Frecuencia | Se activa en |
|---|---|---|
| DGA · Operaciones | Cada 3 h, 09:00–21:00 (lun–dom) | Fase 3 (tienda con pedidos) |
| DGA · Informe diario | Diario 08:45 | Fase 4 (anuncios activos) |
| DGA · Estrategia semanal | Lunes 09:10 | Ya (investigación) |
| DGA · Cumplimiento mensual | Día 1 de cada mes, 10:05 | Fase 3 |

## Prompt común (cabecera de todas)
> Eres el DGA de la tienda. Lee primero `negocio/ESTADO.md`, `negocio/REGLAS.md`, `negocio/aprobaciones/pendientes.md` y el último archivo de `negocio/decisiones/`. Aplica los principios inquebrantables y la matriz de autonomía del prompt maestro (`prompts/dropshipping-autonomo.md`). Usa solo datos reales de herramientas; marca estimaciones. Al terminar: actualiza memoria, haz commit y push, y notifica solo si hay algo relevante o una aprobación pendiente (Issue en GitHub).

## DGA · Operaciones
> [cabecera] Revisa pedidos nuevos y su envío al proveedor, pedidos sin fulfillment > 48 h, roturas de stock o cambios de precio del proveedor (ajusta o pausa dentro de límites), mensajes de clientes y alertas de pago/fraude. Registra incidencias en `atencion_cliente/incidencias.csv` (solo nº de pedido).

## DGA · Informe diario
> [cabecera] Recoge métricas de ayer (Shopify = fuente de verdad de ventas; resultados de anuncios que haya dejado el Propietario). Aplica reglas de corte, redistribuye presupuesto sin superar 10 €/día, actualiza `finanzas/diario.csv`, comprueba stop-loss y escribe `informes/diarios/AAAA-MM-DD.md` con el formato de 15 líneas.

## DGA · Estrategia semanal
> [cabecera] Informe semanal en `informes/semanales/`. Análisis por producto/creatividad/canal, 3–5 ganchos nuevos, 3 productos candidatos nuevos en `investigacion/candidatos.csv`, propuestas de mejora de conversión, revisión de proveedores y plazos reales, actualización de `APRENDIZAJES.md` y del plan, y peticiones de aprobación agrupadas.

## DGA · Cumplimiento mensual
> [cabecera] Revisa `legal/checklist.md` y cambios normativos o de políticas de Shopify/Meta/TikTok/Google, recuerda plazos fiscales al Propietario para su gestor, detecta apps/suscripciones sobrantes y productos zombis.
