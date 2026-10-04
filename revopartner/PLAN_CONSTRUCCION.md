# Plan de construcción de RevoPartner

*4-10-2026 · Todo lo que hay que construir para captar clientes, entregar el servicio y gestionar la agencia. Cada pieza indica quién la hace (C = Claude, V = Vicenç), si tiene coste y de qué depende.*

**Regla de oro del calendario:** nada se cobra ni se factura hasta que te des de alta (036 + RETA). Hasta entonces se construye, se prueba y se hacen pilotos gratuitos. El alta se hace **antes de la primera factura**, no después.

---

## 0. Decisión previa sobre Vapi (bloqueante)

Tu agente de Vapi **no puede hacer llamadas en frío**: es un sistema automático sin intervención humana, y el art. 66.1.a de la LGTel exige consentimiento previo para cualquier llamada comercial automática, también a empresas. Presentarse al inicio no basta. Multas recientes: 5.000–10.000 € a pequeñas empresas. Detalle en la skill `captacion-legal-espana`.

**Cómo sí aprovechamos Vapi (y es mejor argumento de venta):**

| Uso | Legal | Para qué |
|---|---|---|
| **"Llámame ahora" (demo en vivo)**: el reformista deja su teléfono en la landing o en un anuncio, con casilla de consentimiento → Vapi le llama en <60 s, le hace la demostración y agenda la reunión contigo | ✅ Hay consentimiento previo | Captación: el reformista *vive* el producto antes de comprarlo |
| **Llamada inmediata al lead del cliente**: el particular pide presupuesto → Vapi le llama en <60 s, califica y agenda | ✅ Consentimiento en el formulario | Es parte del servicio (plan "voz") |
| **Recordatorio de cita / reprogramación** a quien ya agendó | ✅ Relación previa | Reduce las ausencias |
| Llamar en frío a tu lista de empresas | ❌ | — |

**Tu lista de empresas sí se usa**, pero la llama una persona (tú o un teleoperador por horas) cumpliendo las 5 condiciones: números profesionales, Lista Robinson, interés legítimo por escrito, presentación al inicio y número fijo o 900. Vapi entra después, cuando el reformista acepta "te enviamos una demo": a partir de ahí hay consentimiento.

---

## 1. Captación de clientes

| # | Pieza | Qué es | Quién | Coste | Depende de |
|---|---|---|---|---|---|
| 1.1 | **Revisión de la lista** | Comprobar fuente y fecha de cada número, que sean profesionales, deduplicar y filtrar la Lista Robinson | C prepara, V confirma el origen | Robinson: consulta según tarifa de Adigital `[pendiente de verificar]` | La lista (me la pasas) |
| 1.2 | **Número de llamada** | Verificar que el que compraste es fijo, 800/900 o numeración autorizada, no móvil (Orden TDF/149/2025) | V | 0 € si ya vale; si es móvil, un fijo virtual ~5–15 €/mes | — |
| 1.3 | **Documento de interés legítimo** | Ponderación por escrito para llamar a empresas | C redacta, V firma | 0 € | — |
| 1.4 | **Guion de llamada humana** | Presentación obligatoria + 3 preguntas de calificación + objeciones + cierre a "¿te llamamos con la demo?" | C | 0 € | 1.3 |
| 1.5 | **Pipeline de ventas** | Hoja o CRM con las etapas: lista → llamado → interesado → demo → propuesta → piloto → cliente | C | 0 € (Google Sheets) | Cuenta Google de la marca |
| 1.6 | **Landing de RevoPartner nueva** | Rehacer la web actual: es genérica y tiene testimonios y cifras de ejemplo que **no se pueden publicar** (serían reseñas falsas). Nueva propuesta para reformistas, botón "Llámame ahora" con consentimiento, aviso legal y privacidad | C | Dominio: 0 € si reutilizas; hosting: Netlify gratis | 1.7 |
| 1.7 | **Vapi "Llámame ahora"** | Adaptar tu agente: prompt de demo, aviso de IA, agenda en tu calendario, sin llamadas salientes en frío | C configura, V da acceso | Vapi por minuto `[confirmar tarifa de tu cuenta]` | Acceso a Vapi |
| 1.8 | **Anuncios Meta B2B** | Campaña a dueños de reformas con formulario → Vapi llama en <60 s | C | 150 € del piloto (pendiente de tu aprobación) | 1.6, 1.7 |
| 1.9 | **Oferta piloto** | Primer mes gratis, solo pagan anuncios, garantía de visitas | C (skill `offers`) | 0 € | — |
| 1.10 | **Kit de venta** | Presentación de 6 diapositivas, propuesta tipo, preguntas frecuentes, cálculo de retorno por reformista | C (skill `sales-enablement`) | 0 € | 1.9 |
| 1.11 | Referidos y socios | 1 mes gratis por cliente traído; 15 % recurrente a socios (tiendas de material, interioristas) | C | Solo si hay venta | Primeros clientes |

## 2. El servicio que se entrega

**Arquitectura** (una instancia por cliente, plantilla común):

```
Anuncio Meta (cuenta del cliente)
  → formulario con consentimiento (+ casilla "acepto que me llamen o escriban")
  → n8n recibe el lead (webhook)
  → [WhatsApp del cliente] agente IA (Claude) en <1 min  y/o  [Vapi] llamada en <60 s
  → calificación (tipo de obra, m², presupuesto, plazo, zona, fotos)
  → descarte de basura / derivación a humano
  → cita en Google Calendar del cliente + recordatorios
  → seguimiento del presupuesto enviado (días 2, 5, 10, 20)
  → hoja de resultados + informe semanal automático al cliente
```

| # | Pieza | Quién | Coste | Notas |
|---|---|---|---|---|
| 2.1 | **Servidor n8n** propio (VPS + Docker + HTTPS) | C (skill `n8n-self-hosting`), V paga | ~5–10 €/mes | Pendiente de aprobación |
| 2.2 | **Flujo "lead → respuesta → cita"** | C | — | Plantilla reutilizable por cliente |
| 2.3 | **Agente calificador** (prompt + criterios por tipo de obra, aviso de IA, paso a humano) | C | API Claude ~0,5–2 €/cliente/mes `[estimación]` | Limitado a calificar y agendar (política de Meta) |
| 2.4 | **Integración WhatsApp Cloud API** del cliente | C, cliente verifica su número | Mensajes de servicio: casi 0; plantillas de marketing ~0,05 € | Número del cliente, no nuestro |
| 2.5 | **Integración Vapi** para la llamada inmediata (plan voz) | C | Por minuto | Solo leads con consentimiento |
| 2.6 | **Seguimiento de presupuestos** (plan de entrada de 149 €) | C | — | Funciona también sin anuncios |
| 2.7 | **Plantilla de campaña Meta para reformas** (creatividades, textos, formulario, posible categoría especial de vivienda) | C (skills `ads`, `ad-creative`) | Inversión: la paga el cliente | — |
| 2.8 | **Informe semanal al cliente** (leads, citas, coste por cita, presupuestos) | C | — | Automático desde la hoja |
| 2.9 | **Kit de alta del cliente** (checklist de accesos, reunión de arranque de 30 min, objetivos del mes) | C | — | — |
| 2.10 | **Contratos**: servicio (3 meses mínimo, garantía) + encargado del tratamiento (art. 28 RGPD) | C redacta, V valida con la gestoría | Gestoría | Plantillas, no asesoramiento |
| 2.11 | **Prueba completa** con un "cliente ficticio" (tus propios datos) antes del primer piloto | C + V | 0 € | — |

## 3. Gestión de la agencia

| # | Pieza | Quién | Coste |
|---|---|---|---|
| 3.1 | **Repositorio RevoPartner** como única fuente de verdad (este proyecto) | C | 0 € |
| 3.2 | **ESTADO, DECISIONES, ACCESOS (sin secretos), TAREAS_TITULAR, KPIS** | C mantiene | 0 € |
| 3.3 | **Informe semanal para ti** (email + documento): pipeline, CAC, clientes, bajas, gasto | C, con una rutina programada | 0 € |
| 3.4 | **Cuentas de la marca**: Gmail/Workspace, Google Calendar, Meta Business (cuenta publicitaria nueva), Stripe | V crea, C configura | Workspace ~7 €/mes (opcional) |
| 3.5 | **Facturación y cobro**: Stripe (cobro recurrente) + software de facturación compatible con Verifactu | V | Según software |
| 3.6 | **Alta 036 + RETA + gestoría online** | V | 80 €/mes + 30–60 €/mes |
| 3.7 | **Aviso legal, privacidad, cookies** de la web | C redacta | 0 € |
| 3.8 | **Registro de incidencias y soporte** (WhatsApp de la agencia → hoja) | C | 0 € |
| 3.9 | **Finanzas**: gastos, ingresos, margen por cliente, previsión | C | 0 € |

## 4. Orden de construcción

| Semana | Entregable | Tú haces |
|---|---|---|
| **1** | Repo RevoPartner, guion humano, documento de interés legítimo, lista revisada, pipeline, prompt de Vapi adaptado | Crear el repo, pasarme la lista, confirmar el tipo de número, dar acceso a Vapi |
| **2** | Landing nueva con "Llámame ahora", Vapi conectado a tu calendario, kit de venta, oferta piloto | Revisar y aprobar los textos; empezar las llamadas (2 tardes) |
| **3** | Servidor n8n, flujo de servicio completo, prueba con cliente ficticio, contratos | Aprobar el gasto del servidor; probar el flujo como si fueras un lead |
| **4** | Primeros pilotos gratuitos en marcha; anuncios B2B si los apruebas | Llamadas de venta y demos |
| **5–8** | Pilotos → primeros clientes de pago | **Alta 036 + RETA antes de la primera factura**; Stripe |

## 5. Gastos que necesitarán tu aprobación

| Gasto | Importe | Cuándo |
|---|---|---|
| Número fijo virtual (solo si el tuyo es móvil) | ~5–15 €/mes | Semana 1 |
| Consulta de la Lista Robinson | Según tarifa | Semana 1 |
| Vapi (minutos de demo) | Por uso | Semana 2 |
| Servidor n8n | ~5–10 €/mes | Semana 3 |
| API de Claude | ~10–30 €/mes | Semana 3 |
| Anuncios B2B (opcional) | 150 € de piloto | Semana 4 |
| Cuota de autónomo + gestoría | ~110–140 €/mes | Antes de la primera factura |

Tope propuesto para los primeros 3 meses: **250 €/mes**.
