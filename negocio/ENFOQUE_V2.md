# Enfoque v2 · Escalable y recurrente (2026-10-03)

**Petición del titular:** un negocio más rentable y más escalable, manteniendo la automatización y el presupuesto. El Kit IA en Regla queda en pausa (no se ha validado ni gastado nada).

## Qué cambia
| | Enfoque v1 | Enfoque v2 |
|---|---|---|
| Modelo | Pagos únicos de 12–69 € | **Ingreso recurrente (MRR)** que se acumula |
| Mercado | España, nichos pequeños | **UE e internacional**; España como ventaja local, no como techo |
| Canal | SEO en español (lento, saturado) | **Marketplaces de apps con demanda propia** (Shopify App Store y similares) |
| Producto | Contenido o plantillas (copiable con IA) | **Software integrado en el flujo del cliente** (difícil de sustituir con un prompt) |
| Primer euro | Objetivo de 30 días | Se acepta unos 45–75 días (desarrollo + revisión de la app); **se pide al titular confirmar este cambio** |

## Nueva ponderación del scoring
| Criterio | Peso |
|---|---|
| Escalabilidad (mercado internacional, coste marginal ≈0, recurrente) | 20 % |
| Acceso al canal / distribución | 20 % |
| Disposición a pagar recurrente | 15 % |
| Defensibilidad (localización, integración, normativa) | 10 % |
| Automatizabilidad | 10 % |
| Demanda verificable | 10 % |
| Economía unitaria | 5 % |
| Tiempo hasta el primer ingreso | 5 % |
| Riesgo (inverso) | 5 % |

## Hallazgos iniciales (extractos de buscador)
- **Shopify App Store:** el desarrollador se queda el 100 % del primer millón de dólares facturado (límite de por vida desde 2025) y luego el 85 %; procesamiento del 2,9 %; alta única de 19 $ (**requiere consentimiento del titular**). https://shopify.dev/docs/apps/launch/distribution/revenue-share
- **Tamaño:** más de 600.000 tiendas Shopify vivas en la UE-27; ES 65.600, IT 63.200, DE 121.300, FR 117.900, NL 77.600. https://eightx.co/blog/eu-shopify-landscape · https://storeleads.app/reports/shopify/ES/top-stores
- **Las apps de cumplimiento se saturan en meses:**
  - Verifactu: Shopify tiene la app oficial gratuita Comply.
  - GPSR: más de 10 apps (de gratis a 29 $/mes).
  - Botón de desistimiento: más de 6 apps.
  - Afirmaciones ecológicas: EU Green Claims & EmpCo Check.
  - Aviso de garantía: Clearmark.
  - Ya existen suites que agrupan varias: Dotcase, ShopCompliance, EU Shield.
- **Exceso de apps en las tiendas:** quienes tienen más de 16 apps puntúan unos 15 puntos menos de velocidad. Esto apoya una propuesta "una app ligera en lugar de cinco". https://hyperspeed.me/blog/how-many-shopify-apps-the-average-store-have/

## Ronda v2 en curso (3 subagentes)
1. Nichos de localización España/sur de Europa en Shopify (recargo de equivalencia, transportistas, Bizum, contabilidad, IRPF).
2. Suite de cumplimiento UE localizada: competidores, huecos, próximas obligaciones de 2027 y cómo ganar ranking.
3. Otros modelos escalables (WooCommerce, PrestaShop, API, SEO programático, temas).

## Resultado de la ronda v2 (hecha sin subagentes: se cortaron por el límite de uso)
| Nicho | Resultado | Evidencia (extractos de buscador) |
|---|---|---|
| **Recargo de equivalencia en Shopify** | **ELEGIDO como cuña** | Shopify no lo soporta de forma nativa (hilos de la comunidad de 2021 a 2026). En las búsquedas no aparece ninguna app dedicada. Sufio solo lo desglosa en la factura (7–129 $/mes, 4,9★ con 546 reseñas). En WooCommerce se paga: WC Tax Spain desde 79 €/año, otro plugin a 164 €. B2B en todos los planes de Shopify desde abr-2026. Viabilidad técnica según extractos: Cart Transform lineExpand (apps públicas, todos los planes) y orderEditAddCustomItem |
| Transportistas españoles | Descartado | Packlink PRO, Sendcloud, ShippyPro, módulo oficial de Correos |
| Verifactu, GPSR, desistimiento, green claims, garantía | Fase 3 (no como entrada) | Saturados; ya hay suites (Dotcase, ShopCompliance, EU Shield) |

## Decisión
- **Negocio:** Recargo+ (nombre provisional). App de Shopify para el recargo de equivalencia, a 19, 39 y 79 $/mes. Fase 2: fiscalidad española completa. Fase 3: suite de cumplimiento UE en ES, IT y PT.
- **Proyección:** `herramientas/proyeccion_v2.py`. Mes 12, escenario base: 42 clientes, ingreso recurrente de 1.192 €/mes, unos 750 € netos/mes. Optimista: 3.874 €/mes de ingreso recurrente.
- **Pérdida máxima:** unos 18 € (alta de 19 $ en la App Store, **pendiente de consentimiento**).
- **Criterio de pivote:** menos de 5 instalaciones y 0 de pago a los 60 días del lanzamiento → pasar a la fase 3.
- **Business plan:** https://claude.ai/artifact/Le4TBMDkk4y9R9tnsk5LWs

- Presentación explicativa del modelo (para el titular): https://claude.ai/artifact/AR9XjtKhaLXuDTVEnaa6uJ
- Corrección: el MVP no emite facturas (ver DECISIONES.md, por Verifactu).
- Calendario publicado: https://claude.ai/artifact/LuYbP213m8NhTpboUEfxA2
- Presentación de potencial (36 meses, 4 escenarios, sensibilidad, valoración): https://claude.ai/artifact/CJCQhjscoBf6H3iHZvnEZn · modelo: `herramientas/modelo_potencial.py`
