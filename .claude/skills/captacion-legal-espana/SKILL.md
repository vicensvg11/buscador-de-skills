---
name: captacion-legal-espana
description: Reglas obligatorias para captar clientes en España (llamadas comerciales, email, WhatsApp, agentes de voz o chat con IA, anuncios de reformas, datos de leads). Úsala SIEMPRE antes de planificar, redactar o ejecutar prospección, llamadas en frío, campañas de email/SMS/WhatsApp, guiones de llamada, agentes IA que hablen con personas, o listas de prospectos; y cuando otra skill de marketing (prospecting, ads, sales-enablement, churn-prevention, referrals) proponga una táctica de contacto. Prevalece sobre consejos pensados para EE. UU.
---

# Captación legal en España

Capa de cumplimiento para el negocio *Sistema de Citas* (servicio B2B a reformistas). Las skills de marketing instaladas están escritas para EE. UU. (CAN-SPAM, TCPA). En España rigen otras normas: **esta skill prevalece**.

Esto es guía operativa con fuentes, no asesoramiento jurídico. Ante dudas en un caso concreto, para y pregunta al fundador.

## Semáforo rápido

| Táctica | Estado | Condiciones |
|---|---|---|
| Llamada en frío **hecha por una persona** a empresa, autónomo o persona de contacto profesional | 🟢 Permitida con condiciones | Ver "Llamadas humanas B2B" |
| Llamada en frío a **particulares** | 🔴 No | Requiere consentimiento previo o base legal clara (art. 66.1.b LGTel) |
| Llamada **automatizada / robocall / agente de voz IA** saliente en frío | 🔴 No | Art. 66.1.a LGTel: llamadas automáticas sin intervención humana con fines comerciales solo con **consentimiento previo**. Un agente de voz IA se trata como automático (criterio prudente; la AEPD no lo ha excluido) |
| Agente de voz o WhatsApp IA que **responde** a quien pidió contacto | 🟢 Sí | Consentimiento del formulario + aviso de IA al inicio (art. 50 Ley de IA) |
| Email comercial en frío, también a info@ | 🔴 No | Art. 21 LSSI no distingue B2B. Multas 1.500–12.000 € habituales |
| Email a clientes actuales sobre servicios similares | 🟢 Sí | Art. 21.2 LSSI, con baja en cada envío |
| WhatsApp/SMS en frío | 🔴 No | Opt-in obligatorio (política de Meta + LSSI) |
| Automatizar LinkedIn (bots, extensiones) | 🔴 No | Viola sus condiciones (cierre de cuenta) |
| Anuncios de Meta/Google para captar reformistas | 🟢 Sí | Formulario con consentimiento y política de privacidad |

## Llamadas humanas B2B (la vía permitida)

Base: interés legítimo presumido para empresarios individuales, autónomos y personas de contacto de empresas (Circular AEPD 1/2023 + art. 19 LOPDGDD). Requisitos, todos obligatorios:

1. **Solo números profesionales** de la empresa o autónomo, obtenidos de fuentes públicas del propio negocio (web, Google Business Profile, directorios). Guardar fuente y fecha de cada contacto.
2. **Consultar la Lista Robinson** antes de llamar (servicio de Adigital) y excluir a los inscritos.
3. **Ponderación de interés legítimo por escrito** (documento breve, una vez, actualizado si cambia la campaña).
4. **Al inicio de cada llamada** decir: quién llama y en nombre de qué empresa, que la llamada es comercial, y cómo oponerse a recibir más llamadas. Registrar las oposiciones y no volver a llamar.
5. **Número de origen fijo, 800/900 o numeración autorizada; nunca un móvil** (Orden TDF/149/2025, en vigor desde el 7-06-2025).
6. La llama **una persona** (el fundador o un teleoperador contratado). Si interviene IA, solo como apoyo al humano (guion, notas), nunca marcando y hablando sola.
7. Nada de llamadas a particulares desde estas listas.

Multas recientes de referencia: 5.000 € a una pequeña agencia por una sola llamada a un número de la Lista Robinson (2025); 10.000 € a Más Sol Energía por llamadas sin consentimiento (2026).

## Agentes IA que hablan con leads

- Primer mensaje: "Hola, soy el asistente virtual (IA) de [empresa del cliente]…" (art. 50 Reglamento UE 2024/1689, aplicable desde 2-08-2026).
- El número de WhatsApp es **del cliente** (su cuenta de WhatsApp Business); nosotros somos proveedor técnico.
- Bot limitado a la función de negocio (calificar, agendar, seguimiento). Meta prohíbe en la API los bots de propósito general desde el 15-01-2026.
- Ofrecer siempre pasar con una persona.

## Datos personales

- Somos **encargados del tratamiento** de los leads de cada cliente: contrato del art. 28 RGPD firmado antes de empezar, con Anthropic y el servidor de n8n como subencargados.
- No reutilizar leads de un cliente para otro ni para la marca propia.
- Nunca reutilizar datos de leads de la antigua agencia del fundador.

## Anuncios de reformas en Meta

"Housing repairs" puede caer en la categoría especial de vivienda (sin segmentar por edad, sexo ni código postal). Verificar si Meta la exige en España; si la pide, declararla. No arriesga la cuenta y la segmentación amplia funciona.

## Fuentes

- Art. 66 Ley 11/2022 General de Telecomunicaciones y FAQ de la AEPD sobre llamadas automatizadas: https://www.aepd.es/preguntas-frecuentes/5-publicidad-no-deseada/FAQ-0502-llamadas-automatizadas-sin-intervencion-humana-con-fines-comerciales
- Circular AEPD 1/2023: https://www.boe.es/buscar/doc.php?id=BOE-A-2023-15071 · resumen: https://www.ecija.com/actualidad-insights/criterio-de-la-aepd-en-la-circular-1-2023-sobre-el-envio-de-llamadas-comerciales-en-la-reforma-de-la-ley-general-de-telecomunicaciones/
- Orden TDF/149/2025 (sin móviles): https://www.boe.es/buscar/doc.php?id=BOE-A-2025-2870
- LSSI art. 21 (criterio AEPD): https://www.aepd.es/documento/2018-0164.pdf
- Multas: https://www.autonomosyemprendedor.es/articulo/empresas/agencia-espanola-proteccion-datos-multa-pequenos-negocios-que-realizan-llamadas-comerciales/20250717165659044210.html · https://www.xataka.com/legislacion-y-derechos/aepd-recomendo-grabar-llamadas-spam-para-denunciar-primer-caso-real-ha-acabado-multa-10-000-euros
- Ley de IA art. 50: https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon
- Bots de WhatsApp: https://respond.io/blog/whatsapp-general-purpose-chatbots-ban

Verificado el 4-10-2026 con extractos de buscador (el entorno no abre páginas). Revisar cada 6 meses.
