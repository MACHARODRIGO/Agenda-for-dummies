# PROYECTO: MASTER PLAN - AGENDA PORTFOLIO

>**Visión:**
Este proyecto se concibe como un "segundo doctorado" personal de largo aliento (escala de años). El objetivo es la construcción de una herramienta de gestión diaria propia que no solo organice el tiempo, sino que sirva como piedra angular de un portfolio profesional de alto nivel en Bioinformática, Desarrollo Full Stack e Inteligencia Artificial.

**Stack actual:** `FastAPI` · `HTML/CSS/JS` · `SQLite → MySQL` · `Python` · `R` · `Git/GitHub`
**Editor:** Visual Studio Code · **OS:** Windows (disco local)


---

## I. Objetivos Profesionales y Pilares de Aprendizaje

### 1. Desarrollo y Arquitectura Full Stack
- **Backend:** Python con FastAPI — servidor, rutas, endpoints REST.
- **Frontend:** HTML5, CSS3 (Flexbox/Grid, variables CSS), JavaScript puro → React.
- **Bases de datos:** SQLite (aprendizaje) → MySQL (producción).
- **Seguridad:** JWT, bcrypt, HTTPS, CORS, prevención de SQL injection.

### 2. Ciencia de Datos e Inteligencia Artificial
- **Estadística avanzada:** Probabilidad, distribuciones, inferencia — fundamento científico real.
- **Machine Learning:** Matemática primero (álgebra lineal, cálculo), implementación después.
- **Deep Learning:** Redes neuronales, arquitecturas, activaciones. Sin "ensamblar código sin entender".

### 3. Integración de Hardware y Sensores
- **Drones:** Teoría de vuelo, telemetría (MAVLink, DroneKit), integración con Python.
- **Cámaras remotas:** OpenCV, RTSP, streaming, scripts de captura y procesamiento de imágenes.

### 4. Ciencias Biológicas y NGS
- **Fitopatología:** Patógenos vegetales, taxonomía, mecanismos de infección.
- **NGS:** Actualización más allá de Bulk RNA-Seq con Illumina. Workflows en Galaxy, automatización Python/Bash.
- **Proteómica:** Interacciones proteína-proteína, modelado molecular. Retomar proyecto [tRNASec-Study-Project](https://github.com/MACHARODRIGO/tRNASec-Study-Project) con mayor madurez técnica.

---

## II. Metodología de la Agenda — The Gatekeepers

La aplicación implementa una **lógica de desbloqueo basada en hábitos diarios**:

| Hábito | Tiempo | Lógica |
| :--- | :--- | :--- |
| 🏃 Deporte matutino | 20–30 min | Gatekeeper 1 |
| 🗣️ Práctica de idioma | 20–30 min | Gatekeeper 2 |

**Regla de negocio:** Las tareas de los pilares de estudio permanecen `disabled` (bloqueadas visualmente con opacidad reducida) hasta que ambos gatekeepers estén completados. Implementado en JavaScript puro con `addEventListener` y `querySelector`.

---

## III. Arquitectura del Sistema (evolución por fases)

```
FASE ACTUAL (1–2)
├── frontend/
│   └── index.html          ← HTML + CSS inline + <script> JS al final del body
└── backend/
    └── main.py             ← FastAPI sirviendo el HTML estático

FASE 3–4 (próxima)
├── frontend/
│   ├── index.html
│   ├── style.css           ← CSS separado
│   └── app.js              ← JS separado
└── backend/
    ├── main.py             ← FastAPI con endpoints POST/GET
    ├── database.py         ← Conexión SQLite
    └── agenda.db           ← Base de datos local

FASE 5–7 (mediano plazo)
├── frontend/               ← Igual
└── backend/
    ├── main.py
    ├── models.py           ← Modelos de datos (SQLAlchemy)
    ├── auth.py             ← JWT + bcrypt
    └── MySQL               ← Motor de base de datos externo

FASE 8–9 (largo plazo)
├── frontend/               ← React (reescritura del frontend)
├── backend/                ← FastAPI consolidado
└── Docker / VPS            ← Deploy real, accesible desde cualquier lugar
```

---

## IV. Diseño de Base de Datos

### Esquema relacional — `agenda_master_plan`

```sql
-- Tabla 1: Pilares de estudio
CREATE TABLE pillars (
    id   INT          AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    icon VARCHAR(50)
);

-- Tabla 2: Tareas (definición estática — no cambia día a día)
CREATE TABLE tasks (
    id            INT                            AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(150)                   NOT NULL,
    category      ENUM('habit','professional')   NOT NULL,
    pillar_id     INT,
    estimated_min INT DEFAULT 30,
    FOREIGN KEY (pillar_id) REFERENCES pillars(id)
);

-- Tabla 3: Log de actividad (registro dinámico — el corazón del análisis)
CREATE TABLE daily_log (
    id             INT      AUTO_INCREMENT PRIMARY KEY,
    task_id        INT      NOT NULL,
    completed_date DATE     NOT NULL,
    completed_at   DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);
```

**Relación entre tablas:**
`daily_log.task_id` → `tasks.id` → `tasks.pillar_id` → `pillars.id`

Esto permite queries como: *"¿Cuántos minutos dediqué a cada pilar en el último mes?"*

---

## V. Hoja de Ruta de Aprendizaje (9 fases)

| Fase | Tecnología | Qué construís en la agenda | Estado |
| :---: | :--- | :--- | :--- |
| ✅ 0 | FastAPI + HTML básico | Servidor sirviendo el frontend | Completado |
| 🔥 1 | JavaScript puro (DOM, eventos) | Gatekeepers funcionales | En curso |
| 2 | CSS avanzado (Flexbox, Grid) | Rediseño visual profesional | Pendiente |
| 3 | FastAPI endpoints + `fetch()` | Cada check llama a la API | Pendiente |
| 4 | SQL — SQLite | Log guardado en base de datos | Pendiente |
| 5 | MySQL | Migración a motor de producción | Pendiente |
| 6 | Python / R análisis | Dashboard de productividad | Pendiente |
| 7 | JWT + seguridad web | Login real, datos privados | Pendiente |
| 8 | React | Reescritura del frontend | Futuro |
| 9 | Docker + VPS | Deploy accesible online | Futuro |

> Documento de referencia detallado: [`masterplan_hoja_de_ruta.xlsx`](./masterplan_hoja_de_ruta.xlsx)
> Curriculum de conceptos por fase: [`Curriculum_Conceptos.md`](./Curriculum_Conceptos.md)

---

## VI. Portfolio y Certificaciones

- **Repositorio principal:** [MACHARODRIGO @ GitHub](https://github.com/MACHARODRIGO)
- **Proyecto activo:** [Genomegym](https://github.com/MACHARODRIGO) — expandir con análisis de datos de productividad.
- **Proyecto referencia biología:** [tRNASec-Study-Project](https://github.com/MACHARODRIGO/tRNASec-Study-Project) — retomar con madurez técnica.
- **Estrategia:** Cada fase completada de la agenda es en sí misma un hito de portfolio. El código es evidencia.

---

## VII. Stack Tecnológico completo (objetivo final)

| Capa | Tecnología | Estado |
| :--- | :--- | :--- |
| Editor | Visual Studio Code | ✅ Activo |
| Backend | FastAPI (Python) | ✅ Activo |
| Frontend inicial | HTML + CSS + JS puro | 🔥 En desarrollo |
| Frontend final | React | ⏳ Futuro |
| DB aprendizaje | SQLite | ⏳ Próximo |
| DB producción | MySQL | ⏳ Próximo |
| Análisis de datos | Python (pandas) + R (ggplot2) | ⏳ Próximo |
| Autenticación | JWT + bcrypt | ⏳ Futuro |
| Control de versiones | Git / GitHub | ✅ Activo |
| Deploy | Docker + VPS | ⏳ Futuro |

---

*Última actualización: 16/05/2026*