---
title: "Supply Chain Attack en Axios (npm) — Análisis técnico marzo 2026"
date: 2026-04-01
tags: ["supply-chain", "npm", "axios", "javascript", "open-source", "ciberseguridad"]
image: "/images/axios-supply-chain.png"
draft: false
---

# Supply Chain Attack en Axios (npm) — Marzo 2026

El **30 de marzo de 2026**, la librería **Axios**, uno de los paquetes más utilizados del ecosistema JavaScript, fue comprometida en un **ataque de supply chain** que introdujo código malicioso en versiones publicadas en npm.

Axios cuenta con **más de 100 millones de descargas semanales**, lo que convierte este incidente en uno de los más relevantes del año en seguridad de la cadena de suministro.

---

# ¿Qué es Axios?

Axios es una librería HTTP ampliamente utilizada para:

- Node.js
- Aplicaciones frontend
- Backends
- APIs REST

Repositorio oficial:

https://github.com/axios/axios

Paquete npm:

https://www.npmjs.com/package/axios

---

# Timeline del ataque

## 30 marzo 2026

Investigadores detectaron versiones maliciosas publicadas en npm:

Versiones afectadas:

- 1.14.1  
- 0.30.4

Estas versiones fueron publicadas desde una **cuenta legítima comprometida de un maintainer**.

Fuente:

https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan

---

# Vector de ataque

Según los primeros análisis:

- Compromiso de cuenta del maintainer
- Publicación de versiones aparentemente legítimas
- Inclusión de código malicioso
- Ejecución durante instalación npm

El malware:

- Instalaba un Remote Access Trojan (RAT)
- Multiplataforma
- Persistencia en sistema comprometido

---

# 31 marzo 2026

Investigadores vincularon el ataque a:

- Grupo UNC1069
- Actor vinculado a Corea del Norte

Objetivos:

- Robo de credenciales
- Acceso persistente
- Movimiento lateral potencial

Fuente:

https://www.reuters.com/sustainability/boards-policy-regulation/north-korea-linked-hack-hits-largely-invisible-software-that-powers-online-2026-03-31/

---

# ¿Qué hacía el malware?

Según análisis preliminares:

- Descarga de payload secundario
- Robo de credenciales
- Acceso remoto
- Persistencia

Características:

- Código ofuscado
- Activación post-install
- Dependencias maliciosas ocultas

---

# Impacto

Axios es utilizado por:

- React
- Vue
- Node.js
- Microservicios
- CLI tools

Impacto potencial:

- CI/CD comprometido
- Builds contaminados
- Robo de credenciales

---

# Indicadores de Compromiso

Versiones comprometidas:

- [ ] axios@1.14.1
- [ ] axios@0.30.4


---

# Mitigación

## Actualizar Axios

npm install axios@latest


---

## Revisar lockfiles

Verificar:

- package-lock.json
- yarn.lock
- pnpm-lock.yaml

---

## Rotar credenciales

Especialmente:

- Tokens CI/CD
- API keys
- Credenciales cloud

---

# Lecciones aprendidas

## Supply chain es crítico

Una sola librería puede afectar:

- miles de proyectos
- pipelines
- organizaciones

---

## Maintainers son objetivo

Ataques comunes:

- Phishing
- Token compromise
- Account takeover

---

# Incidentes similares

- event-stream (2018)
- eslint-scope (2018)
- ua-parser-js (2021)
- campañas npm 2025

---

# Conclusión

El ataque a Axios demuestra que:

- La supply chain sigue siendo crítica
- Las dependencias son un vector de ataque
- La seguridad open-source es fundamental

---

# Fuentes

StepSecurity

https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan

Reuters

https://www.reuters.com/sustainability/boards-policy-regulation/north-korea-linked-hack-hits-largely-invisible-software-that-powers-online-2026-03-31/

GitHub Axios

https://github.com/axios/axios

npm Axios

https://www.npmjs.com/package/axios
