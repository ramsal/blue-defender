---
title: "LiteLLM Security Incident — Riesgos de seguridad en proxies LLM"
date: 2026-04-01
tags: ["litellm", "ai-security", "llm", "api-security", "proxy", "ciberseguridad"]
image: "/images/litlellm.png"
draft: false
---

# LiteLLM Security Incident — Riesgos de seguridad en proxies LLM

El crecimiento del uso de **LLM proxies** como **LiteLLM** está introduciendo una nueva superficie de ataque en arquitecturas modernas de inteligencia artificial.

Estas plataformas centralizan:

- API keys sensibles
- Acceso a múltiples proveedores
- Prompts internos
- Respuestas de modelos

Esto convierte a los **LLM gateways** en **activos críticos de seguridad**.

---

# ¿Qué es LiteLLM?

LiteLLM es un proxy y SDK que permite interactuar con múltiples modelos desde una única API.

Soporta:

- OpenAI
- Azure OpenAI
- Anthropic
- Google Gemini
- Ollama
- Modelos locales

Repositorio oficial:

https://github.com/BerriAI/litellm

LiteLLM permite:

- Centralizar llamadas a LLM
- Implementar fallback entre modelos
- Monitorizar costes
- Gestionar múltiples proveedores

---

# Arquitectura típica con LiteLLM

Una arquitectura común:

Application
    |
LiteLLM Proxy
    |
LLM Providers

Esto simplifica la arquitectura, pero también introduce un **single point of failure**.

---

# Riesgo 1 — Proxy expuesto a Internet

Uno de los errores más comunes:

Exponer LiteLLM directamente a Internet:

https://llm.company.com/chat/completions

Si no hay autenticación:

- Cualquiera puede usar tu proxy
- Posible abuso
- Costes elevados
- Denial of wallet

---

# Riesgo 2 — Exposición indirecta de API Keys

LiteLLM almacena:

- OPENAI_API_KEY
- ANTHROPIC_API_KEY
- AZURE_API_KEY

Si el proxy es accesible:

Un atacante puede:

- Consumir tu cuota
- Generar costes
- Acceder a modelos internos

Sin necesidad de conocer las claves originales.

---

# Riesgo 3 — Logging de prompts sensibles

LiteLLM permite logging de:

- Prompts
- Respuestas
- Tokens
- Costes

Si el logging no está controlado:

Puede provocar:

- Fuga de secretos
- Exposición de código
- Filtración de datos internos

---

# Riesgo 4 — Multi‑tenant sin aislamiento

LiteLLM permite:

- múltiples usuarios
- múltiples modelos
- múltiples proveedores

Sin controles adecuados:

- Acceso cruzado
- Consumo indebido
- Escalada de privilegios

---

# Arquitectura recomendada

Internet
   |
WAF / Reverse Proxy
   |
Authentication Layer
   |
LiteLLM Proxy
   |
LLM Providers

---

# Mitigaciones recomendadas

## Autenticación obligatoria

Implementar:

- API keys internas
- JWT
- OAuth

---

## Rate limiting

Limitar:

- Requests por minuto
- Tokens por usuario
- Costes por usuario

---

## Network isolation

- VPN
- Private network
- Zero trust

---

## Logging seguro

- Redacción de datos
- Retención limitada
- Acceso restringido

---

# Checklist de seguridad

- Autenticación obligatoria
- Rate limiting
- Network isolation
- Logging seguro
- Monitoring

---

# Conclusión

LiteLLM simplifica la integración de modelos LLM, pero introduce nuevos riesgos de seguridad.

Los proxies LLM deben tratarse como:

- Infraestructura crítica
- Activo sensible
- Componente de seguridad

---

# Fuentes

LiteLLM GitHub  
https://github.com/BerriAI/litellm

LiteLLM Documentation  
https://docs.litellm.ai

OWASP Top 10 for LLM  
https://owasp.org/www-project-top-10-for-large-language-model-applications/
