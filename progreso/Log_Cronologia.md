# LOG DE PROGRESO: CRONOLOGÍA DEL MASTER PLAN

> Este archivo registra cada hito significativo del proyecto. Se actualiza manualmente con cada avance real.
> **Inicio del proyecto:** 30/04/2026

## ✅ FASE 0 — Configuración del entorno y arquitectura base
| Fecha | Hito | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| **30/04/2026** | **Nacimiento del Proyecto** |  Definición conceptual del "Master Plan" y los pilares de estudio (Full Stack, ML/IA, NGS, Fitopatología, Drones, Proteómica, Seguridad). | Completado |
| **30/04/2026** | **Configuración del Entorno** | Creación del entorno virtual (`venv`) e instalación de FastAPI y Uvicorn. | Completado |
| **30/04/2026** | **Arquitectura Base** | Diseño de la estructura de carpetas (`backend/` / `frontend/`) y creación del archivo `main.py`. | Completado |
| **30/04/2026** | **Servidor Local** | Primer despliegue exitoso del servidor FastAPI en local (`http://127.0.0.1:8000`). | Completado |
| **30/04/2026** | **Optimización de Trabajo** | Decisión técnica de migrar el proyecto de OneDrive a disco local para evitar conflictos de sincronización y mejorar el rendimiento de Git. | Ejecutado |


---

## 🔥 FASE 1 — JavaScript puro y lógica de Gatekeepers

| Fecha | Hito | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| **16/05/2026** | **Diseño del sistema de Gatekeepers** | Definición de la regla de negocio central: las tareas de estudio permanecen bloqueadas hasta completar los hábitos diarios (deporte + idioma). | Completado |
| **16/05/2026** | **Primer script JavaScript** | Implementación de `addEventListener`, `querySelector`, `querySelectorAll` y `forEach` en `index.html` para habilitar/deshabilitar checkboxes dinámicamente. Primer contacto real con manipulación del DOM. | Completado |
| **16/05/2026** | **Comprensión del DOM** | Entendimiento del árbol de nodos que el navegador construye a partir del HTML y cómo JavaScript interactúa con él en tiempo real. | Completado |
| **16/05/2026** | **Ubicación correcta del `<script>`** | Aprendizaje de por qué el bloque `<script>` debe ir antes del cierre `</body>`: garantiza que todos los elementos del DOM existan antes de que JS intente seleccionarlos. | Completado |

---

## 📋 FASE DE PLANIFICACIÓN — Hoja de ruta y diseño de base de datos

| Fecha | Hito | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| **16/05/2026** | **Hoja de ruta completa (Excel)** | Generación de `masterplan_hoja_de_ruta.xlsx` con 3 hojas: fases de aprendizaje (0–9), diseño SQL completo con evaluación del script inicial, y tracker de progreso personal con fórmulas de días. | Completado |
| **16/05/2026** | **Diseño de base de datos** | Definición del esquema relacional de 3 tablas: `pillars`, `tasks` (basada en el script SQL inicial del autor), `daily_log`. Comprensión de claves primarias, foráneas y la diferencia entre definir tareas y registrar actividad. | Completado |
| **16/05/2026** | **Primer script SQL** | Escritura autónoma de `CREATE DATABASE`, `CREATE TABLE` con `INT AUTO_INCREMENT PRIMARY KEY`, `VARCHAR`, `ENUM`, `NOT NULL`, e `INSERT INTO ... VALUES`. Sintaxis validada como correcta. | Completado |
| **16/05/2026** | **Curriculum de conceptos** | Creación de `Curriculum_Conceptos.md`: documento público con todos los conceptos a dominar por fase y lenguaje para alcanzar los objetivos del Master Plan. | Completado |

---

## ⏳ PRÓXIMOS HITOS (planificados)

| Fase | Hito objetivo | Concepto clave a alcanzar |
| :--- | :--- | :--- |
| **Fase 1** | Consola del navegador sin errores JS | Debugging con DevTools (F12) |
| **Fase 2** | Rediseño visual con CSS Flexbox y Grid | Variables CSS, layouts responsivos |
| **Fase 3** | Primer endpoint `POST` en FastAPI | HTTP verbs, JSON, fetch() |
| **Fase 4** | Primera tabla real en SQLite desde Python | `sqlite3`, INSERT desde backend |
| **Fase 5** | Migración a MySQL | Motor cliente-servidor, permisos |
| **Fase 6** | Gráfico de productividad en R o Python | `ggplot2` / `pandas` + SQL |
| **Fase 7** | Login con JWT en la agenda | Autenticación, hash de contraseñas |
| **Fase 8** | Primer componente React | `useState`, props, hooks |
| **Fase 9** | App en VPS (no localhost) | Docker, variables de entorno |

---

*Este archivo se actualiza con cada avance significativo del proyecto.*
*Repositorio principal: [MACHARODRIGO @ GitHub](https://github.com/MACHARODRIGO)*
