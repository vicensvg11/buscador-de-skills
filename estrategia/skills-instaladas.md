# Skills instaladas

Instaladas el 4-10-2026 en `.claude/skills/`. Se cargan solas en cualquier sesión de Claude Code abierta sobre este repositorio.

**Criterios de selección:**
- Fuentes reconocidas, con licencia permisiva (MIT / Apache 2.0).
- Útiles para el negocio *Sistema de Citas*.
- **Auditadas antes de instalar.** Se revisaron todos los archivos no markdown y se buscaron patrones de inyección de instrucciones, exfiltración, comandos `curl | sh` y unicode oculto. Resultado: limpio. Los únicos scripts son un ayudante de servidor local (`webapp-testing`) y un script estándar de Postgres para n8n.

## Origen y versión

| Repositorio | Commit | Licencia | Skills instaladas |
|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) (oficial) | `8a1541c` | Apache 2.0 | 2 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `dda3841` | MIT | 18 (sin la carpeta `evals`) |
| [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) | `19cd793` | MIT | 14 (sin los hooks del repositorio) |
| Propia | — | — | 1 |

## Para qué sirve cada una

| Área | Skills | Uso en el negocio |
|---|---|---|
| **Cumplimiento España (propia)** | `captacion-legal-espana` | Llamadas, email, WhatsApp, agentes IA, RGPD. **Prevalece** sobre los consejos de EE. UU. de las demás |
| Anuncios | `ads`, `ad-creative`, `ab-testing`, `analytics` | Campañas Meta de captación propia y de los clientes, creatividades, test, métricas |
| Textos y conversión | `copywriting`, `copy-editing`, `cro`, `marketing-psychology` | Landing, anuncios, mensajes del agente de WhatsApp |
| Oferta y precio | `offers`, `pricing` | Garantía, planes de 149 € y 390 € |
| Ventas | `prospecting`, `sales-enablement`, `revops` | Listas de reformistas, guion de llamada, propuesta, embudo |
| Clientes | `customer-research`, `competitor-profiling`, `onboarding`, `churn-prevention`, `referrals` | Entender al reformista, competencia, alta, retención, referidos |
| Automatización (n8n) | `using-n8n-mcp-skills`, `n8n-workflow-patterns`, `n8n-node-configuration`, `n8n-expression-syntax`, `n8n-code-javascript`, `n8n-code-python`, `n8n-code-tool`, `n8n-agents`, `n8n-error-handling`, `n8n-validation-expert`, `n8n-subworkflows`, `n8n-binary-and-data`, `n8n-mcp-tools-expert`, `n8n-self-hosting` | Construir y desplegar los flujos: formulario → WhatsApp IA → agenda → seguimiento |
| Web | `frontend-design`, `webapp-testing` | Landing page y pruebas automáticas |

## Descartadas a propósito

- `cold-email` y `sms`: ilegales en frío en España.
- SEO, ASO, paywalls, popups, programmatic-seo: no encajan con el modelo.
- `n8n-multi-instance`: innecesaria al principio.
- Documentos (pptx, docx, xlsx, pdf) y `skill-creator`: ya están disponibles en tu cuenta.

## Pendiente para aprovecharlas al 100 %

- Las skills `n8n-mcp-tools-expert` y `using-n8n-mcp-skills` rinden más con el servidor MCP `n8n-mcp` conectado a tu instancia de n8n. Se configura cuando tengamos el servidor de n8n (gasto pendiente de tu aprobación).
