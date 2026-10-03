# Calendario de octubre 2026 · Recargo+

**Regla:** como máximo 2 h/semana del titular, en sesiones de 30–60 min. Horario propuesto a las 19:00 (Madrid); muévelo como quieras.
**Gasto:** el único pago del mes son los 19 $ de la sesión 8, y solo con tu OK explícito ese día.
**Seguridad:** nunca pegues claves ni contraseñas en el chat. Las claves van en los ajustes del entorno, como variables de entorno (ver cada sesión).
Al terminar cada sesión, escríbeme "hecha la sesión N" y la marco aquí.

| # | Fecha | Duración | Sesión | Estado |
|---|---|---|---|---|
| 0 | Dom 4 oct | 15 min | Red del entorno | ☐ |
| 1 | Mar 6 oct | 45 min | Cuentas de Shopify y repositorio | ☐ |
| 2 | Vie 9 oct | 45 min | Claves de acceso técnicas | ☐ |
| 3 | Mié 14 oct | 30 min | Correo de soporte y conectores | ☐ |
| 4 | Vie 16 oct | 45 min | Gestoría: elegir y consultar | ☐ |
| 5 | Mié 21 oct | 45 min | Banco y datos de cobro en Shopify | ☐ |
| 6 | Vie 23 oct | 45 min | Respuestas del gestor y textos legales | ☐ |
| 7 | Mar 27 oct | 30 min | Prueba de la app (QA) | ☐ |
| 8 | Jue 29 oct | 30 min | Alta en la App Store (19 $) y envío a revisión | ☐ |
| 9 | Sáb 31 oct | 30 min | Revisión mensual y rutina semanal | ☐ |

Carga semanal: dom 4: 15 min · semana del 5 al 11: 1 h 30 min · del 12 al 18: 1 h 15 min · del 19 al 25: 1 h 30 min · del 26 al 31: 1 h 30 min.

---

## Sesión 0 · Dom 4 oct · 15 min · Red del entorno
Para qué: poder abrir webs (Shopify, Cloudflare, normativa) y verificar fuentes. Hasta ahora solo veía resultados de búsqueda.
1. En esta sesión de Claude Code: menú del entorno (barra de título) → **Edit** → **Network access**.
2. Elige **Full** (opción recomendada). Si prefieres algo más restringido, elige *Custom*, conserva la lista por defecto y añade: `*.shopify.com`, `*.myshopify.com`, `shopify.dev`, `*.shopifycdn.com`, `api.cloudflare.com`, `*.workers.dev`, `www.boe.es`, `sede.agenciatributaria.gob.es`, `community.shopify.com`, `apps.shopify.com`.
3. Guarda.
Guía: https://code.claude.com/docs/en/cloud-environments#network-access

## Sesión 1 · Mar 6 oct · 45 min · Cuentas de Shopify y repositorio
Para qué: tener donde construir y probar la app sin coste.
1. **Shopify Partners** (gratis, 15 min): https://partners.shopify.com → *Join now*. Usa tu email y datos reales (eres el titular legal).
2. **Tienda de desarrollo** (gratis, 10 min): en el panel de Partners → *Stores* → *Add store* → *Development store* → nombre `recargo-dev`. Sirve para probar sin pagar plan.
3. **Repositorio propio** (15 min): en GitHub, crea un repositorio **privado** llamado `recargo-plus`. Después, en https://github.com/apps/claude/installations/select_target, da acceso a la app de Claude a ese repositorio.
4. Escríbeme: "hecha la sesión 1". Yo añado el repo a la sesión y empiezo la estructura de la app.

## Sesión 2 · Vie 9 oct · 45 min · Claves de acceso técnicas
Para qué: que pueda desplegar y probar la app yo solo, con permisos mínimos.
Te guiaré en el chat paso a paso. Las claves se guardan en: menú del entorno → **Edit** → variables de entorno (o *API credentials* si aparece).
1. **App en Partners** (15 min): Partners → *Apps* → *Create app* → *Create app manually* → nombre "Recargo+". Copia el *Client ID* y guárdalo como variable `SHOPIFY_API_KEY` (no es secreto, pero así queda ordenado).
2. **Token de la CLI de Shopify** (10 min): en Partners → *Settings* → *CLI token* → genera uno → guárdalo como `SHOPIFY_CLI_PARTNERS_TOKEN`. [Verificaré contigo el nombre exacto del menú, que Shopify cambia a menudo.]
3. **Cloudflare** (20 min): crea una cuenta gratis en https://dash.cloudflare.com/sign-up. Luego *My Profile* → *API Tokens* → *Create Token* → plantilla **"Edit Cloudflare Workers"**, limitada a tu cuenta → guárdalo como `CLOUDFLARE_API_TOKEN`. Copia también el *Account ID* (barra lateral) como `CLOUDFLARE_ACCOUNT_ID`.
4. Abre una **sesión nueva** de Claude Code (las variables se leen al arrancar) y escríbeme "hecha la sesión 2".
→ Esa semana hago la **prueba técnica del recargo** en `recargo-dev`.

## Sesión 3 · Mié 14 oct · 30 min · Correo de soporte y conectores
Para qué: la App Store exige un email de soporte, y con los conectores opero sin pedirte cosas.
1. **Email de soporte** (10 min): crea una cuenta de Gmail gratuita solo para el negocio (p. ej. `recargoplus.soporte@gmail.com`, si está libre).
2. **Conectores** (15 min) en https://claude.ai/customize/connectors:
   - **Gmail**: conéctalo con la cuenta de soporte, **no** con tu correo personal. Lo uso para redactar respuestas; tú decides si las envío yo.
   - **Shopify**: reconéctalo (la sesión caducó) y elige la tienda `recargo-dev`.
   - **Cloudflare Developer Platform**: conéctalo con la cuenta del paso de la sesión 2.
3. Abre una sesión nueva y escríbeme "hecha la sesión 3". Registraré los accesos en `ACCESOS.md`.

## Sesión 4 · Vie 16 oct · 45 min · Gestoría: elegir y consultar
Para qué: resolver las 4 dudas fiscales antes de cobrar el primer euro.
1. Te dejo preparada una comparativa de 3 gestorías online (precio, si incluyen el alta, valoraciones). Elige una (15 min).
2. Envíale el email que te redacto con las 4 dudas (10 min):
   - el IVA de los pagos de Shopify (inversión del sujeto pasivo, ROI, modelo 349);
   - el epígrafe de IAE;
   - el momento del alta en RETA con pluriactividad;
   - el límite de responsabilidad.
3. **No contrates todavía**: la cuota mensual del gestor es un gasto recurrente y te lo pediré cuando llegue el primer cobro.

## Sesión 5 · Mié 21 oct · 45 min · Banco y datos de cobro en Shopify
Para qué: que Shopify pueda pagarte.
1. (Recomendado, 20 min) Abre una **cuenta bancaria separada gratuita** para el negocio, en un banco online sin comisiones.
2. (20 min) En Partners → *Settings* → *Payouts*: añade el IBAN o PayPal. Rellena el **formulario fiscal** que pide Shopify (para residentes fuera de EE. UU. suele ser el W-8BEN). Te explico cada casilla en el chat.
3. Escríbeme "hecha la sesión 5".

## Sesión 6 · Vie 23 oct · 45 min · Respuestas del gestor y textos legales
1. (20 min) Repasamos juntos la respuesta del gestor y fijamos la fecha del alta censal (modelo 036/037), que debe ser anterior al primer pago de Shopify. Te dejo el borrador preparado.
2. (25 min) Lee y aprueba los textos que te preparo:
   - política de privacidad,
   - condiciones de uso,
   - aviso de que la app no es asesoramiento fiscal,
   - ficha de la App Store en español e inglés.

## Sesión 7 · Mar 27 oct · 30 min · Prueba de la app (QA)
1. Sigue mi guion de prueba de 15 pasos en `recargo-dev`: crear un cliente B2B con recargo, hacer un pedido, ver la línea de recargo y ver el desglose.
2. Anota cualquier cosa rara. Lo corrijo antes de enviar a revisión.

## Sesión 8 · Jue 29 oct · 30 min · Alta en la App Store (19 $) y envío a revisión
**Requiere tu OK explícito**, porque es el único gasto del mes (≈18 €, pago único).
1. Partners → *Apps* → Recargo+ → *Distribution* → *Shopify App Store* → paga el registro de 19 $.
2. Revisa la ficha que dejo preparada (capturas, textos, precios de 19, 39 y 79 $ con 14 días de prueba) y pulsa **Submit for review**.
3. Shopify suele tardar varias semanas [supuesto]. Mientras, preparo las guías SEO y la respuesta para la comunidad.

## Sesión 9 · Sáb 31 oct · 30 min · Revisión mensual y rutina semanal
1. Repasamos el estado: app en revisión, caja (gastado ≈18 €), plan de noviembre.
2. Apruebas la **rutina semanal automática**: yo programo una sesión cada lunes en la que reviso KPIs, soporte y normativa y te dejo un informe de una página.
3. Decidimos si te paso el panel de KPIs al móvil.

---

## Lo que hago yo en paralelo (sin consumir tu tiempo)
| Semana | Claude |
|---|---|
| 5–11 oct | Estructura de la app en `recargo-plus`, prueba técnica del recargo (carrito y pedidos) en `recargo-dev` |
| 12–18 oct | MVP: marca de recargo por cliente B2B, línea en el carrito, ajuste de pedidos, desglose para la factura; comparativa de gestorías y email al gestor |
| 19–25 oct | Facturas, exportación para la gestoría, webhooks de RGPD, despliegue en Cloudflare, textos legales, página de privacidad, ficha y capturas |
| 26–31 oct | Correcciones de la prueba, guías SEO, kit para la comunidad de Shopify, SOPs de soporte y operación semanal |

Si algo de lo mío se bloquea, te lo digo en cuanto pase, sin esperar a la sesión siguiente.
