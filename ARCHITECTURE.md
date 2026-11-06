# Arquitectura del Sistema - Gulugulu

## 1. Vision General
Gulugulu esta disenado siguiendo un patron arquitectonico modular, ligero y desacoplado, optimizado para ejecutarse en hardware modesto de escuelas rurales sin conexion a Internet. La solucion combina un backend en Python con Flask y SQLite, con un frontend dinamico basado en un enrutador SPA sin dependencias externas y componentes reactivos en Vue.js.

## 2. Diagrama de Capas

```
+-------------------------------------------------------------------+
|                        CAPA DE PRESENTACION                       |
|  - HTML5 Semantico + Jinja2                                       |
|  - Suez One (Tipografia Encabezado) + Plus Jakarta Sans           |
|  - Lucide Icons (Libreria Vectorial Offline)                      |
|  - Vue.js 3 (Modulos Didacticos Reactivos)                        |
|  - Enrutador SPA Persistente (fullscreen.js)                      |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|                      CAPA DE CONTROLADOR (Flask)                  |
|  - Enrutamiento HTTP / API REST (/search, /autocomplete, /admin)  |
|  - Autenticacion y Control de Acceso por Roles (RBAC)             |
|  - Proteccion contra Directory Traversal en Descarga de Archivos  |
|  - Manejo Centralizado de Excepciones y Respuestas de Error       |
+-------------------------------------------------------------------+
             |                                    |
             v                                    v
+-----------------------------+      +------------------------------+
|     MOTOR DE BUSQUEDA       |      |     GRAFO DE CONOCIMIENTO    |
|  - SearchEngineV2 (FTS5)    |      |  - KnowledgeGraphEngine      |
|  - Ponderacion BM25         |      |  - RecommendationEngine      |
|  - QueryExpander (Sinonimos)|      |  - PathBuilder (Rutas)       |
|  - Filtros Multicriterio    |      |                              |
+-----------------------------+      +------------------------------+
             \                                    /
              \                                  /
               v                                v
+-------------------------------------------------------------------+
|                  CAPA DE DATOS Y ALMACENAMIENTO                   |
|  - SQLite (database.db) con modo WAL (Write-Ahead Logging)        |
|  - Tablas FTS5 (indice de texto completo virtual)                 |
|  - Sistema de Archivos Local (storage/):                          |
|      * storage/documents/   * storage/videos/                     |
|      * storage/images/      * storage/thumbnails/                 |
|  - Tarea en Segundo Plano de Copias de Seguridad (backups/)       |
+-------------------------------------------------------------------+
```

## 3. Componentes del Frontend

### 3.1. Enrutador SPA y Modo Pantalla Completa (`fullscreen.js`)
Para evitar recargas completas de pagina que rompan la experiencia de pantalla completa en tabletas y computadores de aula, se implemento un interceptor de navegacion asincrono (`navigateSpa`). Este componente:
1. Intercepta clics en enlaces internos y envios de formularios GET.
2. Solicita el HTML de destino mediante la API Fetch.
3. Extrae y reemplaza el contenido del cuerpo (`document.body`) y sincroniza los estilos dinamicos.
4. Re-ejecuta ordenadamente los scripts necesarios.
5. Invoca automaticamente `lucide.createIcons()` para instanciar la iconografia en el nuevo DOM.
6. Mantiene el estado de pantalla completa en el almacenamiento local (`localStorage`).

### 3.2. Iconografia Vectorial Integrada (`static/js/lucide/lucide.js`)
En lugar de depender de fuentes web como Material Symbols (cuyos glifos no cargaban de forma consistente sin red), se desarrollo una version autocontenida de Lucide:
- 76 trazados SVG oficiales optimizados para tamanos de 16px, 18px, 20px y 24px con grosor de trazo uniforme (`stroke-width="2"`).
- API estandar compatible con atributos `data-lucide`, `data-size` y `data-stroke-width`.
- Metodo generador `lucide.createIcon(name, attrs)` para inyeccion dinamica en plantillas JavaScript.

### 3.3. Motores de Juego Didactico (`static/js/juegos/`)
Cada grado escolar cuenta con 20 desafios disenados por competencias:
- Grado 1: Memoria, reconocimiento fonetico, figuras y comparacion visual.
- Grado 2: Operaciones aritmeticas iniciales, series numericas y desafios logicos.
- Grado 3: Comprension lectora, vocabulario contextual y geometria basica.
- Grado 4: Geografia, recursos naturales y fraccionarios.
- Grado 5: Metodo cientifico, sistemas biologicos y problemas cuantitativos avanzados.

## 4. Componentes del Backend

### 4.1. Motor de Busqueda V2 (`core/search/search_engine.py`)
Utiliza la extension FTS5 de SQLite para realizar busquedas textuales ultra-rapidas:
- Ponderacion diferencial en la funcion BM25: Titulo (100.0), Materia (20.0).
- Expansion de sinonimos (`QueryExpander`): Traduce terminos comunes y consultas infantiles hacia conceptos curriculares formales.
- Tokenizacion tolerante: Mantiene digitos individuales para permitir busquedas directas de grados escolares (por ejemplo, "matematicas 1").
- Subconsultas SQL optimizadas para el filtrado simultaneo por grado, materia y tipo de medio.

### 4.2. Grafo de Conocimiento y Recomendaciones (`core/knowledge/`)
- Mapea prerrequisitos conceptuales entre diferentes objetos de aprendizaje.
- Genera sugerencias de navegacion pedagogica para que el estudiante avance gradualmente de temas basicos a complejos.

### 4.3. Servidor Seguro de Archivos (`serve_file`)
- Normaliza las rutas de acceso entrantes mediante `os.path.normpath` para neutralizar ataques de escape de directorio (`../`).
- Prioriza el almacenamiento estructurado V2 (`storage/`) e implementa contingencia transparente hacia el directorio de origen (`BD/`).

## 5. Esquema de Base de Datos
- `roles`: Definicion de roles del sistema (`admin`, `maestro`).
- `users`: Cédula, nombre, nombre de usuario y hash de contraseña.
- `file_metadata`: Metadatos academicos de archivos subidos (grado, materia, docente autor, fecha).
- `learning_objects`: Registro maestro de unidades pedagogicas.
- `search_tokens`: Tabla de sinonimos, alias y expansion de vocabulario.
- `fts_learning_objects`: Tabla virtual FTS5 para indexacion de alta velocidad.
- `concepts` y `concept_relationships`: Nodos y aristas del grafo de conocimiento.

## 6. Mecanismos de Resiliencia y Respaldo
- Conexiones SQLite con tiempo de espera de 15 segundos y modo de registro WAL (`Write-Ahead Logging`) para permitir lecturas concurrentes sin bloqueos de contencion.
- Hilo demonio en segundo plano (`weekly_backup_task`) que genera copias automatizadas de la base de datos y los archivos los domingos.
- Rutas administrativas manuales (`/admin/backup/create` y `/admin/backup/restore`) con desempaquetado atomico.

