# Fase 0 · Inventario y encuadre (2026-10-03)

## 1. Herramientas que tengo de verdad en esta sesión

| Capacidad | Estado | Qué puedo hacer | Límite real |
|---|---|---|---|
| WebSearch | ✅ | Buscar y leer títulos y fragmentos de resultados | No abre páginas: los fragmentos no cuentan como "fuente abierta" |
| WebFetch / curl a webs | ❌ bloqueado por la red del entorno | — | Sin citas reales de clientes, precios de competidores ni reseñas → **S-1** |
| Ejecución de código (Python 3, Node 22, npm/pip) | ✅ | Modelos financieros, scoring, análisis, construir web/landing/herramientas | pandas no instalado (se instala con pip) |
| Repositorio Git + GitHub MCP | ✅ | Control de versiones, memoria, código, PRs, GitHub Actions | El hosting público necesita una cuenta (Cloudflare Pages/Netlify gratis) o un repo público |
| Subagentes | ✅ | Investigación en paralelo, revisión con abogado del diablo antes de cada gate | Heredan el mismo bloqueo de red |
| Artifacts | ✅ | Panel de KPIs y caja consultable desde el móvil | — |
| Rutinas programadas (triggers) | ✅ | Ciclo semanal y revisión mensual automáticos | Hay que configurarlas con aprobación del titular |
| Shopify (conector) | ⚠️ requiere reautenticación | Tienda, productos digitales, pedidos | Plan de pago: probablemente excede el 50 % de herramientas (verificar) |
| Google Drive | ❌ no conectado | — | No necesario |
| Email, pagos (Stripe/MoR), analítica, navegador (Chrome), redes | ❌ no disponibles | — | Se pedirán en la Fase 2–3 |

**Señal de perfil detectada (sin confirmar):** en esta cuenta hay skills de LinkedIn configuradas para "Vicenç" que apuntan a **gestión de proyectos, I+D, post-award y consultoras de I+D**. Si se confirma, es un activo de canal y de conocimiento de nicho muy valioso (pregunta 1).

## 2. Ronda única de preguntas (responde con la letra)

1. **Tus activos.** `habilidades_activos_contactos` está vacío. ¿Cuál describe mejor tu perfil?
   a) Gestión de proyectos / subvenciones de I+D (pre/post-award, CDTI, Horizonte Europa…) con red en LinkedIn · b) a) + otro sector que domines (dime cuál) · c) Otro perfil (descríbelo en 2 líneas) · d) Prefiero empezar sin usar mi experiencia
2. **Situación laboral.** a) Asalariado/a a tiempo completo (pluriactividad; revisa si tu contrato tiene exclusividad o no competencia) · b) Desempleado/a (posible capitalización o compatibilidad del paro: consultar al SEPE/gestor) · c) Autónomo/a o empresa propia ya · d) Otra
3. **¿Puedo usar tu LinkedIn como canal de distribución** (publicaciones y mensajes redactados por mí y aprobados por ti, dentro de las 2 h)? a) Sí · b) Solo publicaciones, sin mensajes directos · c) No, canal 100 % independiente de mi persona
4. **Mercado objetivo.** a) España/Latam en español (recomendado: menos competencia, ventaja de idioma) · b) Internacional en inglés · c) Ambos, empezando por uno
5. **Objetivo del mes 6 (1.000 €/mes netos con 2 h/semana y 1.500 €).** Es ambicioso: la mayoría de negocios digitales nuevos sin canal propio no lo alcanzan [SUPUESTO · confianza media]. a) Mantenerlo como objetivo y aplicar las reglas de pivote · b) Bajar a 400–500 €/mes y mantener los demás plazos · c) Mantener 1.000 € y subir a 4–5 h/semana
6. **Alta de autónomo.** a) Alta solo justo antes del primer cobro, con visto bueno del gestor (recomendado) · b) Me doy de alta ya · c) Ya tengo una forma jurídica que puede facturar

## 3. Restricciones duras y costes fijos mínimos

### Costes fijos mensuales inevitables (desde el alta)
| Concepto | €/mes | Fuente |
|---|---|---|
| Cuota RETA, tarifa plana (80 € + MEI 0,9 %) | 88,64 | [SUPUESTO · confianza alta] fragmento de búsqueda (cuentica.com, infoautonomos.com), página no abierta. 12 meses, prorrogable 12 más si el rendimiento neto < SMI |
| Gestoría online (autónomo con IVA) | 30–80 (asumo **40**) | [SUPUESTO · confianza media] fragmentos de búsqueda de billeo.es y cronoshare.com, páginas no abiertas |
| Dominio | ~1 | [SUPUESTO · confianza alta] |
| Hosting, email, automatización | 0 (planes gratuitos) | Se verificará en la Fase 3.2 |
| **Total fijo mínimo** | **≈ 130 €/mes** | 87 % de `gasto_mensual_max_eur` (150 €) |

**Consecuencias:**
- Quedan **≈ 20 €/mes** para herramientas y publicidad hasta el break-even → la adquisición de pago queda prácticamente descartada al principio; el canal debe ser orgánico o directo.
- **Break-even** (día 90): margen de contribución ≥ **130 €/mes**, p. ej. 5 ventas de 29 € con un MoR (~26,5 € netos tras IVA y comisiones) o 1 cliente B2B de 150 €/mes.
- **Mes 6** (1.000 € netos): margen de contribución ≈ 1.130 €/mes antes de IRPF → ~45 ventas/mes de 29 € o ~8 clientes B2B de 150 €/mes.
- Opción de ahorro: sin gestor (yo preparo los modelos 303/130 y tú los presentas, ~15 min/trimestre) → fijo ≈ 90 €/mes. Recomiendo gestor el primer año: un error en IVA/OSS cuesta más que 40 €/mes. **A validar con el gestor.**
- Si eres asalariado (pregunta 2), la tarifa plana también aplica en pluriactividad [SUPUESTO · confianza media]. A validar con el gestor.

### Modelos descartados por restricción
| Restricción | Descarta |
|---|---|
| 2 h/semana del titular | Consultoría o servicios entregados por ti, llamadas de venta, comunidades que exijan tu presencia diaria, marca personal basada en vídeo propio |
| ≈20 €/mes libres | Adquisición de pago antes de validar, SaaS que dependan de APIs caras por usuario sin precio que lo cubra, Shopify de pago (verificar el plan) |
| 1.500 € de capital | Inventario físico, desarrollo externo, compra de webs o newsletters existentes |
| País/UE | B2C digital a toda la UE sin MoR (carga OSS); sectores regulados (salud, finanzas, legal) |
| Sin navegador ni email todavía | Outreach automatizado (queda para cuando haya cuenta de email propia y base legal: B2B, interés legítimo, LSSI art. 21 → validar) |

**Favorecidos:** producto digital de nicho o plantillas/herramientas B2B en español, micro-SaaS de un problema, directorio o base de datos de nicho, servicio productizado entregado por IA con revisión mía, todos con venta en self-service.

## 4. Matriz de capacidades (ciclo completo)

| Tarea | Claude | Automatización | Operador | Acceso necesario | Cuándo |
|---|---|---|---|---|---|
| Investigación de mercado | ✔ | | | Red completa (S-1) | Ya |
| Scoring, proyecciones, pre-mortem | ✔ (subagentes) | | | — | Ya |
| Landing, web, producto digital, herramientas | ✔ | GitHub Actions | | Hosting gratuito (S-3) | Fase 2 |
| Dominio | | | Comprar (pago) | Registrador | Fase 2 |
| Cobro y checkout | ✔ configura | Webhooks MoR | Alta de la cuenta (KYC) | Paddle/Lemon Squeezy, clave restringida (S-4) | Fase 2 |
| Entrega del producto | | ✔ (MoR entrega archivos/licencias) | | — | Fase 2 |
| Analítica | ✔ | ✔ | | Plausible/Umami gratis o GoatCounter (S-5) | Fase 2 |
| Email transaccional / newsletter | ✔ redacta | ✔ | Alta de la cuenta | Brevo/MailerLite gratis, API key restringida | Fase 3 |
| Contenido y SEO | ✔ | Publicación programada | | Repo/CMS | Fase 2–4 |
| LinkedIn (si la pregunta 3 es sí) | ✔ redacta | | Aprueba y publica (o vía skills existentes) | Navegador | Fase 2 |
| Soporte de primer nivel | ✔ | Respuestas tipo | Escalados (reembolsos, temas legales) | Bandeja compartida | Fase 3 |
| Alta censal, RETA, firma, contratos | | | ✔ | Certificado digital/Cl@ve | Antes del primer cobro |
| Gestor (contratación) | ✔ prepara comparativa | | Firma | — | Fase 2 |
| Conciliación, KPIs, informe semanal | ✔ | Rutina semanal | Lee el panel (5 min) | Lectura de pagos | Fase 3–4 |
| Modelos trimestrales | Prepara datos | | Gestor presenta | — | Fase 4 |

## 5. Stack de capacidades objetivo
Ahora: red completa (S-1). Fase 2: dominio, hosting gratuito, MoR, analítica. Fase 3: email, gestor, rutinas programadas, panel de KPIs. Lo pediré en cada fase; aquí se anticipa para que no haya sorpresas.
