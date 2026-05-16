# CURRICULUM DE CONCEPTOS — MASTER PLAN

> Este documento lista todos los conceptos que hay que **entender de verdad** para construir la agenda portfolio y alcanzar los objetivos del Master Plan.

---

## FASE 0 — Completada ✅

### Python (FastAPI)
- [ ] ✅ Qué es un servidor web y qué hace
- [ ] ✅ Qué es un framework y por qué FastAPI
- [ ] ✅ Qué es un entorno virtual (`venv`) y por qué aislarlo del sistema
- [ ] ✅ Qué hace `uvicorn` y por qué es necesario
- [ ] ✅ Qué es una ruta (`@app.get("/")`) y qué devuelve
- [ ] ✅ Cómo servir archivos estáticos con `StaticFiles`
- [ ] ✅ Qué es `FileResponse` y cuándo usarlo

---

## FASE 1 — JavaScript puro · DOM y eventos

### Conceptos fundamentales de JS
- [ ] Qué es el DOM y cómo el navegador construye el árbol de nodos a partir del HTML
- [ ] Diferencia entre HTML (estructura) y JS (comportamiento)
- [ ] Por qué el `<script>` va antes de `</body>` y no en el `<head>`
- [ ] Qué es una variable: `const` vs `let` vs `var` — cuándo usar cada una
- [ ] Qué es un tipo de dato: string, number, boolean, null, undefined
- [ ] Qué es una función: declarada vs anónima vs arrow function (`() => {}`)
- [ ] Qué es un callback — una función que se pasa como argumento a otra

### Selección de elementos
- [ ] `document.querySelector(selector)` — devuelve el primero que matchea
- [ ] `document.querySelectorAll(selector)` — devuelve una NodeList con todos
- [ ] Selectores CSS en JS: `'#id'`, `'.clase'`, `'elemento'`, `'.clase input'`
- [ ] Diferencia entre `null` (elemento no encontrado) y un elemento real
- [ ] Cómo leer propiedades de un elemento: `.id`, `.checked`, `.disabled`, `.value`

### Eventos
- [ ] Qué es un evento del navegador (click, change, input, submit, keydown)
- [ ] `element.addEventListener('evento', callback)` — cómo funciona internamente
- [ ] Qué es el objeto `event` y para qué sirve `event.preventDefault()`
- [ ] Por qué `.checked` es `true/false` en checkboxes
- [ ] Cómo un mismo callback puede escuchar múltiples elementos

### Manipulación del DOM
- [ ] `element.disabled = true/false` — habilitar/deshabilitar inputs
- [ ] `element.style.opacity = '0.5'` — modificar estilos inline
- [ ] `element.classList.add('clase')` / `.remove()` / `.toggle()` — mejor que style inline
- [ ] `element.textContent` vs `element.innerHTML` — diferencia y riesgos de XSS
- [ ] `element.setAttribute('atributo', 'valor')` vs asignación directa

### Lógica y control de flujo
- [ ] Operadores lógicos: `&&` (AND), `||` (OR), `!` (NOT)
- [ ] Operador ternario: `condicion ? valorSiTrue : valorSiFalse`
- [ ] `if / else if / else`
- [ ] `forEach` en NodeList y arrays — cómo iterar colecciones
- [ ] Qué es `undefined` vs `null` vs `false` en contexto booleano (falsy values)

---

## FASE 2 — CSS avanzado

### Modelo de caja
- [ ] Qué es el box model: `content`, `padding`, `border`, `margin`
- [ ] Diferencia entre `width: 100%` con y sin `box-sizing: border-box`
- [ ] Qué hace `display: block` vs `display: inline` vs `display: inline-block`

### Flexbox
- [ ] Qué es un flex container y qué son flex items
- [ ] `display: flex` en el padre — qué cambia en los hijos
- [ ] `flex-direction: row | column`
- [ ] `justify-content`: alinear en el eje principal
- [ ] `align-items`: alinear en el eje cruzado
- [ ] `gap`: espacio entre items
- [ ] `flex: 1` en un hijo — qué significa y cuándo usarlo
- [ ] `flex-wrap: wrap` — para que los items salten de línea

### CSS Grid
- [ ] Diferencia conceptual entre Flexbox (1D) y Grid (2D)
- [ ] `display: grid` + `grid-template-columns`
- [ ] `repeat(3, 1fr)` — qué es `fr` y por qué es útil
- [ ] `grid-column: span 2` — para que un elemento ocupe más de una columna
- [ ] `gap` en grids

### Variables CSS (Custom Properties)
- [ ] Cómo declarar: `--mi-variable: #valor;` dentro de `:root {}`
- [ ] Cómo usar: `color: var(--mi-variable);`
- [ ] Por qué son mejores que repetir colores hardcodeados
- [ ] Cómo sobreescribir variables en componentes específicos

### Diseño visual y responsivo
- [ ] `border-radius` para cards
- [ ] `box-shadow` para profundidad
- [ ] `transition: propiedad duración ease` para animaciones suaves
- [ ] `opacity` vs `visibility` vs `display: none` — diferencias reales
- [ ] Media queries: `@media (max-width: 600px) {}` — qué son y cuándo usarlas
- [ ] Unidades: `px`, `%`, `rem`, `em`, `vh`, `vw` — cuándo usar cada una

### Organización del CSS
- [ ] Por qué separar el CSS a un archivo `style.css` y cómo linkear con `<link>`
- [ ] Especificidad en CSS: qué gana cuando hay reglas que se contradicen
- [ ] Convención BEM (Block Element Modifier) — nomenclatura de clases legible

---

## FASE 3 — FastAPI avanzado + comunicación frontend-backend

### HTTP y APIs REST
- [ ] Qué es HTTP: request y response
- [ ] Métodos HTTP: `GET` (leer), `POST` (crear), `PUT` (actualizar), `DELETE` (borrar)
- [ ] Qué es JSON y cómo se estructura (`{}`, `[]`, `"clave": "valor"`)
- [ ] Qué es un endpoint y qué es una ruta parametrizada (`/tasks/{id}`)
- [ ] Qué son los status codes: `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`
- [ ] Qué es CORS y por qué bloquea requests del frontend al backend en desarrollo

### FastAPI — nivel 2
- [ ] Cómo definir un endpoint `POST` con `@app.post("/ruta")`
- [ ] Cómo recibir datos en el body con `BaseModel` de Pydantic
- [ ] Qué hace Pydantic: validación automática de tipos
- [ ] Cómo usar `HTTPException` para devolver errores claros
- [ ] Cómo configurar CORS con `CORSMiddleware`
- [ ] Qué es la documentación automática en `/docs` (Swagger UI) y cómo usarla

### JavaScript — fetch API
- [ ] Qué es `fetch()` y para qué sirve
- [ ] Qué es una Promesa (`Promise`) en JS — el concepto de operación asíncrona
- [ ] Qué es `async/await` y cómo simplifica el manejo de promesas
- [ ] Cómo hacer un `POST` con `fetch`: `method`, `headers`, `body: JSON.stringify(...)`
- [ ] Cómo leer la respuesta: `response.json()`
- [ ] Cómo manejar errores con `try/catch`
- [ ] Qué es el ciclo de vida de una request: envío → espera → respuesta → actualización del DOM

---

## FASE 4 — SQL y bases de datos relacionales (SQLite)

### Conceptos fundamentales de bases de datos
- [ ] Qué es una base de datos relacional y por qué "relacional"
- [ ] Qué es una tabla, una fila (registro) y una columna (campo)
- [ ] Qué es una clave primaria (`PRIMARY KEY`) y por qué cada tabla la necesita
- [ ] Qué es `AUTO_INCREMENT` y qué problema resuelve
- [ ] Qué es una clave foránea (`FOREIGN KEY`) y qué relación establece
- [ ] Qué significa `NOT NULL` y `DEFAULT`
- [ ] Diferencia entre SQLite (archivo local) y MySQL (servidor cliente-servidor)

### DDL — Definición de estructura
- [ ] `CREATE DATABASE nombre`
- [ ] `CREATE TABLE nombre (columnas...)`
- [ ] Tipos de datos esenciales: `INT`, `VARCHAR(n)`, `TEXT`, `DATE`, `DATETIME`, `BOOLEAN`, `ENUM(...)`
- [ ] `ALTER TABLE` — cómo modificar una tabla existente
- [ ] `DROP TABLE` — cómo eliminarla (con cuidado)

### DML — Manipulación de datos
- [ ] `INSERT INTO tabla (col1, col2) VALUES (val1, val2)`
- [ ] `SELECT * FROM tabla`
- [ ] `SELECT col1, col2 FROM tabla WHERE condicion`
- [ ] `UPDATE tabla SET columna = valor WHERE condicion`
- [ ] `DELETE FROM tabla WHERE condicion`
- [ ] Por qué nunca hacer `DELETE` o `UPDATE` sin `WHERE`

### Consultas avanzadas
- [ ] `ORDER BY columna ASC/DESC`
- [ ] `LIMIT n` — para paginar resultados
- [ ] `COUNT(*)`, `SUM()`, `AVG()`, `MAX()`, `MIN()` — funciones de agregación
- [ ] `GROUP BY` — agrupar resultados por categoría
- [ ] `JOIN`: cómo conectar dos tablas — `INNER JOIN`, `LEFT JOIN`
- [ ] Subqueries básicas

### Python + SQLite
- [ ] Cómo usar el módulo `sqlite3` de Python (sin instalar nada)
- [ ] `conn = sqlite3.connect('archivo.db')` — crear/abrir la base
- [ ] `cursor = conn.cursor()` — qué es un cursor y para qué sirve
- [ ] `cursor.execute("SQL...")` — ejecutar una query
- [ ] `conn.commit()` — por qué es necesario confirmar cambios
- [ ] `cursor.fetchall()` / `cursor.fetchone()` — leer resultados
- [ ] Qué son los parámetros `?` en queries y por qué previenen SQL injection

---

## FASE 5 — MySQL

### Diferencias con SQLite
- [ ] SQLite vs MySQL: cuándo usar cada uno y por qué
- [ ] Qué es un servidor de base de datos y cómo conectarse a él
- [ ] Cómo instalar MySQL y MySQL Workbench
- [ ] Cómo crear usuarios y otorgar permisos (`GRANT`)

### Python + MySQL
- [ ] Instalar `mysql-connector-python` o `PyMySQL`
- [ ] Cómo conectarse desde Python: `host`, `user`, `password`, `database`
- [ ] Por qué guardar credenciales en variables de entorno (`.env`) y nunca en el código
- [ ] Qué es `python-dotenv` y cómo cargarlo

### Conceptos de producción
- [ ] Índices: qué son, cuándo crearlos y por qué aceleran las búsquedas
- [ ] Transacciones: `BEGIN`, `COMMIT`, `ROLLBACK`
- [ ] Qué es un ORM (SQLAlchemy) y cuándo usarlo en lugar de SQL directo

---

## FASE 6 — Análisis de datos con Python y R

### Python — pandas
- [ ] Qué es un DataFrame y cómo crearlo desde una lista, dict o SQL
- [ ] `pd.read_sql()` — leer una query directamente en un DataFrame
- [ ] Operaciones básicas: `.head()`, `.info()`, `.describe()`, `.shape`
- [ ] Filtrado: `df[df['columna'] == valor]`
- [ ] Agrupación: `df.groupby('columna').agg({'otra': 'sum'})`
- [ ] `pd.to_datetime()` — trabajar con fechas
- [ ] Exportar: `df.to_csv()`, `df.to_excel()`

### Python — matplotlib / seaborn
- [ ] Gráfico de barras, líneas y dispersión básicos
- [ ] Cómo personalizar ejes, títulos y colores
- [ ] Cuándo usar `seaborn` vs `matplotlib`

### R — ggplot2
- [ ] Gramática de gráficos: `ggplot(data, aes(x, y)) + geom_*()`
- [ ] `geom_bar()`, `geom_line()`, `geom_point()`, `geom_col()`
- [ ] `facet_wrap()` — múltiples paneles por categoría
- [ ] `scale_*` para personalizar ejes y colores
- [ ] `theme_minimal()` y personalización de temas
- [ ] Leer desde SQLite en R: paquete `DBI` + `RSQLite`

### Estadística aplicada al log de productividad
- [ ] Distribución de tareas completadas por día (histograma)
- [ ] Tendencia temporal (regresión lineal simple)
- [ ] Proporción de días con gatekeepers cumplidos
- [ ] Correlación entre hábitos y tareas de estudio completadas

---

## FASE 7 — Seguridad web

### Conceptos fundamentales
- [ ] Qué es la autenticación (¿quién sos?) vs autorización (¿qué podés hacer?)
- [ ] Por qué nunca guardar contraseñas en texto plano
- [ ] Qué es el hashing y cómo funciona `bcrypt`
- [ ] Qué es un token y por qué reemplaza a las sesiones clásicas

### JWT (JSON Web Tokens)
- [ ] Estructura de un JWT: header, payload, signature
- [ ] Cómo se genera, cómo se envía (Authorization header) y cómo se verifica
- [ ] Qué es el tiempo de expiración de un token
- [ ] Paquetes Python: `python-jose`, `passlib[bcrypt]`
- [ ] Cómo proteger un endpoint con `Depends()` en FastAPI

### Vulnerabilidades web básicas
- [ ] SQL Injection: qué es y cómo prevenirlo con parámetros
- [ ] XSS (Cross-Site Scripting): qué es y por qué no usar `innerHTML` con datos externos
- [ ] CSRF: qué es y cuándo importa
- [ ] HTTPS: qué cifra y por qué es obligatorio en producción
- [ ] CORS: configuración correcta para no dejar todo abierto

---

## FASE 8 — React

### Prerequisitos (necesario dominar primero)
- [ ] JS puro sólido: funciones, arrays, objetos, destructuring, spread operator
- [ ] Promises y async/await sin dudas
- [ ] Módulos JS: `import` / `export`

### Fundamentos de React
- [ ] Qué es un componente y por qué React organiza la UI en componentes
- [ ] JSX: HTML dentro de JS — qué es y cómo se transforma
- [ ] Props: cómo pasar datos de padre a hijo
- [ ] Estado con `useState`: qué es el estado y por qué React re-renderiza
- [ ] `useEffect`: cuándo y por qué ejecutar código en respuesta a cambios
- [ ] Cómo hacer `fetch()` dentro de un componente

### Patrones básicos
- [ ] Renderizado condicional: `{condicion && <Componente />}`
- [ ] Listas: `.map()` para renderizar arrays con `key`
- [ ] Manejo de formularios controlados
- [ ] Levantar el estado (`lifting state up`) entre componentes hermanos

---

## FASE 9 — Deploy y DevOps básico

### Docker
- [ ] Qué es un contenedor y por qué "funciona en mi máquina" deja de ser excusa
- [ ] Qué es una imagen Docker vs un contenedor
- [ ] `Dockerfile`: cómo construir la imagen de la app
- [ ] `docker-compose.yml`: orquestar app + base de datos juntas
- [ ] Variables de entorno en Docker: `ENV` y `-e`

### Deploy en VPS
- [ ] Qué es un VPS y cómo acceder por SSH
- [ ] Cómo copiar el proyecto al servidor (`git clone` o `scp`)
- [ ] Cómo levantar la app con Docker en el servidor
- [ ] Nginx como reverse proxy — qué hace y por qué es necesario
- [ ] Certificado SSL gratuito con Let's Encrypt

---

## Conceptos transversales (aplican a todas las fases)

### Git y GitHub
- [ ] `git init`, `git add`, `git commit`, `git push` — el ciclo básico
- [ ] Qué es un branch y por qué trabajar en ramas
- [ ] `git merge` vs `git rebase` — diferencias y cuándo usar cada uno
- [ ] `.gitignore` — qué nunca subir al repositorio (`.env`, `__pycache__`, `venv/`)
- [ ] Pull requests: cómo funciona el flujo de revisión de código
- [ ] Cómo escribir un buen `README.md`

### Herramientas de debugging
- [ ] DevTools del navegador: Console, Elements, Network, Sources
- [ ] Cómo leer un stack trace (error con número de línea)
- [ ] `print()` en Python / `console.log()` en JS como debugging básico
- [ ] Cómo usar el debugger de VS Code (breakpoints)

### Terminal y línea de comandos
- [ ] Navegar: `cd`, `ls`, `pwd`
- [ ] Crear y eliminar: `mkdir`, `touch`, `rm`
- [ ] Variables de entorno: `export VARIABLE=valor`, leer con `$VARIABLE`
- [ ] Procesos: `Ctrl+C`, `Ctrl+Z`, `kill`
- [ ] Pipe: `comando1 | comando2`

---

*Última actualización: 16/05/2026*
*Este documento es público y open source. Si llegaste acá por GitHub y te sirve, podés forkear el repo y adaptarlo a tus objetivos.*
