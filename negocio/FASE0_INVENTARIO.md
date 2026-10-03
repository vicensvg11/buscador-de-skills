# Fase 0 · Inventario y encuadre

Fecha: 2026-10-03 · Sesión 1

## 1. Herramientas que tengo de verdad en esta sesión

| Herramienta | Estado | Qué puedo hacer con ella | Límite real |
|---|---|---|---|
| Búsqueda web (WebSearch) | ✅ funciona | Títulos, URLs y extractos de resultados (solo índice de EE. UU.) | No abre páginas: los datos que saco de aquí son de "resultado de búsqueda, no abierto" |
| Lectura web (WebFetch) / curl | ❌ bloqueada | — | La política de red del entorno rechaza boe.es, seg-social.es, reddit.com, google.com, wikipedia, stripe.com, etc. |
| Ejecución de código (Python, Node) | ✅ | Proyecciones, scoring, análisis de datos, generación de sitios estáticos | Sin red de salida salvo los gestores de paquetes |
| Repositorio Git `vicensvg11/buscador-de-skills` | ✅ lectura y escritura | Memoria persistente (esta carpeta), código, landing estática | Hay que hacer commit y push; el contenedor es efímero |
| GitHub MCP | ✅ | Ramas, PRs, archivos, Actions (despliegue en GitHub Pages) | Solo este repositorio |
| Subagentes en paralelo | ✅ | Investigación por idea o por competidor, abogado del diablo | Tienen las mismas restricciones de red |
| Artifacts (claude.ai) | ✅ | Panel de KPIs y caja privado, que el titular puede abrir desde el móvil | — |
| Rutinas programadas (create_trigger / send_later) | ✅ | Ciclo semanal automático, revisiones mensuales | Mínimo, una por hora |
| Claude Docs | ✅ | Documentos compartibles (GATE 1 en una página) | — |
| Shopify | ⚠️ conectado pero la sesión ha caducado | Tienda y productos digitales | El titular debe volver a autenticarlo; no tiene sentido hasta la Fase 3 |
| Google Drive | ❌ instalado, no conectado | — | No es necesario: la memoria vive en el repositorio |
| Chromium sin interfaz (Playwright) | ✅ local | Probar la landing y los flujos de pago de extremo a extremo | Sin red externa: no sirve para navegar por plataformas |
| Pagos, email, CRM, analítica, redes | ❌ | — | Se pedirán en la Fase 2, justo antes de usarlos |

**Conclusión:** puedo pensar, calcular, programar y desplegar, pero la investigación de mercado (Fase 1) queda limitada por la red. Pedir una red más abierta es la solicitud más importante de esta sesión (ver `TAREAS_TITULAR.md`).

## 2. Variables vacías o incoherentes

| Variable | Problema | Impacto |
|---|---|---|
| `habilidades_activos_contactos` vacía | Sin activos, el canal (lo más difícil) parte de cero | Crítico para la Fase 1.1 |
| `horas_semana_disponibles: 2` | Descarta servicios, outreach manual y venta directa intensiva | Solo cabe producto digital, herramienta o contenido automatizado |
| `beneficio_neto_mensual_mes_6_eur: 1000` con 2 h/semana, 1.500 € y canal desde cero | Requiere unas 64 ventas al mes de 29 € (ver §4) | Muy improbable: la mayoría de productos nuevos sin canal venden casi nada. Propongo tratarlo como escenario optimista |
| Comunidad autónoma desconocida | Decide si aplica la "cuota cero" (devolución de los 80 €) | Cambia el break-even de 6 a 2 ventas al mes |
| Situación laboral desconocida | Tarifa plana solo si no ha sido autónomo en los 2 años anteriores; pluriactividad | Coste fijo legal |

## 3. Restricciones duras derivadas

- **Descartados por tiempo (2 h/semana):** servicio productizado con entrega manual, consultoría, cold outreach B2B a mano, comunidad que hay que dinamizar a diario, vídeo con presentador semanal, marketplaces con atención al cliente intensiva.
- **Descartados por capital (1.500 €):** inventario físico, desarrollos a medida pagados a terceros, adquisición de pago antes de validar, compra de webs o newsletters existentes.
- **Descartados por país/legal:** cualquier cosa que exija facturar a consumidores UE sin un merchant of record (añade la carga de OSS), además de los sectores excluidos del prompt.
- **Quedan:** producto digital de nicho (plantillas, kits, bases de datos), micro-SaaS o herramienta de un solo problema, directorio de nicho con listados de pago, newsletter o SEO automatizados con producto propio. Todo vendido a través de un **merchant of record** (Lemon Squeezy, Gumroad o Paddle) para que sea él quien gestione el IVA UE/OSS.

## 4. Costes fijos mensuales mínimos (script: `herramientas/costes_fijos.py`)

| Escenario | Cuota RETA | Gestor | Herramientas | **Fijo/mes** | Ventas/mes para break-even (29 €) |
|---|---|---|---|---|---|
| A · Autónomo + gestor | 80 € | 35 € | 15 € | **130 €** | 6,1 |
| B · Autónomo + cuota cero autonómica + gestor | 0 €* | 35 € | 15 € | **50 €** | 2,3 |
| C · Autónomo sin gestor | 80 € | 0 € | 15 € | **95 €** | 4,4 |
| D · Validación antes del alta en RETA | 0 € | 0 € | 10 € | **10 €** | 0,5 |

\* Se pagan 80 € y la comunidad autónoma los devuelve en un plazo de 3 a 12 meses: hace falta liquidez.

- Margen de contribución por venta de 29 € (IVA incluido) con Lemon Squeezy: **21,41 €** (IVA 21 %, comisión del 6,5 % + 0,46 €, 1 % de payout). Con Gumroad (10 % + 0,50 $ + procesamiento) sería unos 2 € menos.
- **El escenario A cabe en `gasto_mensual_max_eur` (150 €) pero solo deja unos 20 €/mes para todo lo demás.** El escenario A obliga a vender al menos 6 unidades al mes desde el día 90; es exigente pero posible si hay canal.
- **Objetivo del mes 6 (1.000 € netos):** unos 1.380 € de margen al mes, es decir, unas 64 ventas de 29 € o unos 46 suscriptores de 30 €/mes. Lo dejo como escenario optimista, no como objetivo base.
- **Alternativa D:** la "alta censal" en Hacienda (modelo 036/037) es gratuita y debe hacerse antes de la primera venta. El alta en RETA depende de la *habitualidad*. Según los resultados de búsqueda, el Tribunal Supremo (STS 162/2026, 16-feb-2026) ha dicho que tener ingresos por debajo del SMI no excluye por sí solo la habitualidad. **[VALIDAR CON GESTOR]** si unas pocas preventas de validación obligan ya al alta en RETA. Mi recomendación es hacer el alta en RETA en cuanto pase el GATE de validación (Fase 2) y nunca más tarde de la primera venta recurrente.

Fuentes (resultados de búsqueda del 2026-10-03; **no he podido abrir las páginas** por la política de red):
- Tarifa plana 2026 de 80 €/mes durante 12 meses, prorrogable otros 12 si el rendimiento es inferior al SMI: https://guiafiscal.es/autonomos/tarifa-plana-autonomos-2026/ · https://declarando.es/tarifa-plana-autonomos
- Cuota cero en 2026 (Madrid, Andalucía, Cantabria, Extremadura, Aragón, Castilla-La Mancha, Galicia…): https://www.autonomosyemprendedor.es/articulo/autonomos/son-comunidades-autonomas-que-ofreceran-cuota-cero-autonomos-2026/20260216182652051989.html
- Gestorías online de 24 a 60 €/mes: https://guiafiscal.es/comparativas/mejor-gestoria-online/ · https://www.billeo.es/precios
- Habitualidad e ingresos por debajo del SMI: https://www.idealista.com/news/fiscalidad/2025/12/16/876509-autonomos-el-supremo-aclara-como-influyen-los-ingresos-inferiores-al-smi-en-la-obligacion-de · https://www.qualitax.es/el-supremo-aclara-cuando-un-autonomo-con-ingresos-bajos-debe-darse-de-alta-en-reta/
- Comisiones de Lemon Squeezy (5 % + 0,50 $, +1,5 % tarjeta internacional, +1 % payout fuera de EE. UU.): https://www.swell.is/content/lemon-squeezy-pricing
- Gumroad como merchant of record desde el 1-ene-2025, comisión del 10 % + 0,50 $: https://www.swell.is/content/gumroad-pricing

## 5. Reparto inicial del capital (1.500 €)

| Partida | € | % | Nota |
|---|---|---|---|
| Reserva intocable | 300 | 20 % | — |
| Validación (Fase 2) | 225 | 15 % | Dominio (unos 12 €), un posible tope de anuncios y herramientas en plan gratuito |
| Legal y fiscal, meses 1–6 | 690 | 46 % | Escenario A: 6 × (80 + 35). Si hay cuota cero, se liberan unos 480 € |
| Herramientas, meses 1–6 | 90 | 6 % | Plan gratuito o de pago por uso; tope de 15 €/mes |
| Adquisición posvalidación / colchón | 195 | 13 % | Solo si el CAC es inferior al 50 % del margen |

Aunque el capital alcanza para unos 9 meses en el escenario A, **el gasto legal pesa casi la mitad**. Por eso el alta en RETA debe coincidir con la validación, no adelantarse a ella.

## 6. Matriz de capacidades (tarea → responsable)

| Tarea | Claude | Automatización | Operador (solo lo que exige una persona) |
|---|---|---|---|
| Investigación de mercado y scoring | ✅ (subagentes) | — | Ampliar el acceso de red |
| Decisiones de negocio reversibles | ✅ | — | Aprobar los GATES |
| Landing y web (código y despliegue) | ✅ | GitHub Actions → Pages | — |
| Producto digital (creación) | ✅ | — | Revisión puntual de calidad |
| Checkout, entrega e IVA | Configuración | Merchant of record (entrega automática) | Crear la cuenta (identidad, IBAN, KYC) |
| Email y onboarding | Textos y secuencias | Herramienta de email (plan gratuito) | Crear la cuenta y verificar el dominio |
| Contenido y SEO | ✅ | Publicación programada | — |
| Soporte de nivel 1 | Respuestas tipo y FAQ | Respuestas automáticas | Escalados (reembolsos por encima del límite, temas legales) |
| Conciliación y KPIs | ✅ (sesión semanal) | Rutina semanal programada | — |
| Alta en Hacienda y RETA, firmas, banco | — | — | ✅ |
| Gestor (modelos 130, 303, 390) | Preparar los datos | — | Contratarlo |

## 7. Stack de capacidades objetivo (todo el ciclo)

| Fase | Capacidad | ¿La tengo? | Cuándo la pido |
|---|---|---|---|
| 1 | Red abierta (lectura de foros, reseñas y marketplaces) | ❌ | **Ya** |
| 1 | Activos del titular (perfil, red, LinkedIn) | Parcial | **Ya** (preguntas) |
| 2 | Dominio propio | ❌ | Tras el GATE 1 (unos 12 €/año) |
| 2 | Merchant of record (Lemon Squeezy o Gumroad) con clave API restringida | ❌ | Tras el GATE 1 (gratis, cobra por venta) |
| 2 | Analítica sin cookies (Plausible de pago, o GoatCounter/Cloudflare Web Analytics gratis) | ❌ | Tras el GATE 1 |
| 2 | Email (Brevo, MailerLite o Buttondown en plan gratuito) | ❌ | Tras el GATE 1 |
| 3 | Re-autenticar Shopify (solo si el negocio elegido es una tienda) | ⚠️ | Depende de la Fase 1 |
| 3–4 | Rutina semanal programada + panel de KPIs (Artifact) | ✅ | En la Fase 3 |
