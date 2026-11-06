# Gulugulu - Plataforma Educativa y Buscador Escolar Fuera de Linea

## Descripcion General
Gulugulu es una plataforma web educativa desarrollada en Flask y SQLite, disenada especificamente para operar de manera autonoma y eficiente en instituciones educativas que carecen de conexion a Internet. Proporciona un entorno integrado de busqueda semantica de recursos educativos (guias, cuadernillos, videos, audios e ilustraciones), un modulo interactivo de minijuegos para los cinco grados de primaria y un panel administrativo para la gestion docente y preservacion de contenidos.

## Caracteristicas Principales

### 1. Buscador Escolar Hibrido (V1 y V2)
- Motor de busqueda FTS5 con ponderacion BM25 (prioridad a titulos y materias).
- Expansion automatica de consultas mediante diccionario y tokens de sinonimos (`synonyms.json` y tabla `search_tokens`).
- Tokenizador especializado con soporte para digitos individuales y terminos pedagogicos.
- Autocompletado dinamico en tiempo real.
- Filtrado por grado escolar (Primero a Quinto), materia academica y categoria de medio (documentos, imagenes, videos, audios).
- Previsualizacion de cuadernillos y recursos mediante miniaturas en formato WebP.

### 2. Modulo de Minijuegos Educativos
- Conjunto de actividades didacticas organizadas curricularmente de primer a quinto grado.
- Motor de animaciones SVG reactivo basado en Vue.js y GSAP, con funcionamiento 100% local.
- Navegacion fluida basada en arquitectura Single Page Application (SPA) para transiciones sin recargas de pagina ni perdida del modo pantalla completa.

### 3. Panel de Control y Administracion Docente
- Autenticacion robusta con hash de contraseñas mediante Werkzeug (`pbkdf2:sha256`).
- Control de acceso basado en roles (`admin` y `maestro`).
- Carga de nuevos recursos educativos con validacion de extensiones permitidas.
- Metadatos por archivo (grado, materia, autor y fecha de publicacion).
- Sistema de copias de seguridad manuales y programadas de la base de datos y archivos.
- Procedimiento de restauracion de emergencia en caso de inconsistencia en la base de datos.

### 4. Identidad Visual e Iconografia Unificada
- Encabezado minimalista con tipografia Suez One cargada localmente en formato WOFF2.
- Iconografia estandarizada mediante la libreria oficial Lucide (64+ definiciones vectoriales integradas localmente).
- Ausencia total de solicitudes a redes de distribucion externas (CDN), garantizando soberania operativa fuera de linea.

## Requisitos del Sistema
- Python 3.10 o superior (compatible y probado en Python 3.14).
- Sistema Operativo: Windows, Linux o macOS.
- Espacio en disco: Minimo 2 GB si se conservan los recursos pedagogicos locales.
- Dependencias de Python especificadas en `requirements.txt`.

## Instalacion y Puesta en Marcha

### 1. Clonar el repositorio
```bash
git clone https://github.com/usuario/gulugulu.git
cd gulugulu
```

### 2. Crear y activar un entorno virtual
En Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En Linux o macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Inicializar la base de datos (opcional si no existe)
```bash
python init_db.py
```
Credenciales administrativas iniciales:
- Usuario: `admin`
- Contraseña: `admon123*`

### 5. Iniciar la aplicacion
```bash
python app.py
```
El servidor estara disponible en `http://localhost:5000` con recarga automatica en desarrollo.

## Ejecucion de Pruebas Automatizadas
El proyecto cuenta con una suite completa de pruebas unitarias y de integracion:
```bash
python -m unittest discover tests -v
```

## Estructura del Proyecto
```
GULUGULU/
├── app.py                  # Servidor central Flask y rutas HTTP/API
├── search_engine.py        # Motor de busqueda en memoria (V1)
├── init_db.py              # Script de inicializacion y seeding de la BD
├── database.db             # Base de datos SQLite (FTS5, usuarios, grafos)
├── requirements.txt        # Dependencias oficiales del proyecto
├── synonyms.json           # Diccionario de sinonimos pedagogicos
├── core/                   # Modulos de arquitectura y logica de negocio
│   ├── database/           # Acceso y configuracion de base de datos V2
│   ├── knowledge/          # Grafo de conocimiento y recomendaciones
│   ├── migrations/         # Esquemas SQL de migracion
│   ├── pipeline/           # Procesamiento de recursos y extractores
│   ├── search/             # Motor de busqueda FTS5 V2 y expansor
│   └── utils/              # Formateadores de texto y utilidades
├── storage/                # Almacenamiento canonical de recursos educativos
│   ├── documents/          # Cuadernillos y lecturas en PDF
│   ├── videos/             # Videos educativos en MP4
│   ├── images/             # Fotografias e ilustraciones
│   └── thumbnails/         # Miniaturas WebP optimizadas
├── templates/              # Plantillas HTML con motor Jinja2
│   ├── index.html          # Pagina principal del buscador
│   ├── results.html        # Vista de resultados y filtros
│   ├── minijuegos.html     # Portal de seleccion de grados
│   ├── admin_login.html    # Acceso administrativo
│   ├── admin_dashboard.html# Panel de gestion de maestros y archivos
│   ├── db_error.html       # Interfaz de contingencia y recuperacion
│   └── juegos/             # Motores de juego por cada grado escolar
├── static/                 # Recursos estaticos del cliente
│   ├── css/                # Hojas de estilo y fuentes locales (Suez One, Plus Jakarta)
│   ├── js/                 # Logica de cliente, Vue.js, Lucide y fullscreen SPA
│   ├── images/             # Iconografia y recursos graficos
│   └── videos/             # Video y animaciones de fondo
└── tests/                  # Suite de pruebas automatizadas
    ├── test_search_engine.py
    ├── test_search_engine_v2.py
    ├── test_routes.py
    └── test_auth.py
```

## Licencia
Este proyecto es software libre para fines educativos bajo los terminos de la Universidad de Cundinamarca (UDEC).

