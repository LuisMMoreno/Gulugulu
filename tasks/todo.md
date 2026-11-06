# Plan Maestro de Modernización y Calidad - Gulugulu

## Fase 1: Cambios Visuales Prioritarios
- [x] **Header Modernizado**:
  - [x] Eliminar logo gráfico y espacio reservado en todos los templates.
  - [x] Reemplazar tipografía y color actuales por texto limpio `Gulugulu` en fuente `Suez One`.
  - [x] Garantizar carga y renderizado correcto de `suez-one.css` y `suez-one.woff2` en todas las vistas.
  - [x] Sin imágenes, iconos ni mascotas junto al nombre.
- [x] **Iconografía Lucide**:
  - [x] Mapear y sustituir todos los iconos `material-symbols-outlined` y otros iconos UI de la plataforma por iconos oficiales Lucide (`data-lucide` y helper SVG).
  - [x] Asegurar que `lucide.js` contenga todas las definiciones requeridas para los iconos de la plataforma (76 iconos integrados localmente).
  - [x] Mantener consistencia en tamaños, trazos (stroke-width: 2), alineación y colores.
  - [x] Verificar funcionamiento offline completo de Lucide (0 referencias externas, 0 llamadas a CDNs).

## Fase 2: Limpieza y Auditoría
- [x] Inspeccionar archivos pesados: analizar directorios `USB` (2.56 GB) y `storage` (1.18 GB), `.venv`, temporales y duplicados.
- [x] Identificar y eliminar scripts obsoletos / temporales (`cookies.txt`, `cookies_final.txt`, `stitch_variant*.html`, `fix_*.ps1`, `update_index.*`).
- [x] Resolver conflictos de fusión Git pendientes en `templates/admin_dashboard.html`.
- [x] Verificar dependencias en `requirements.txt` y depurar librerías no utilizadas.
- [x] Analizar seguridad: secretos en código, sanitización de entradas, subida de archivos y prevención de directory traversal.
- [x] Redactar `AUDIT_REPORT.md` en español y sin emojis.

## Fase 3: Refactorización
- [x] Modularizar y asegurar backend Flask (`app.py`, clave de sesión configurable vía entorno).
- [x] Optimizar SQLite con modo WAL y timeout de conexión de 15 segundos.
- [x] Sanitizar rutas en entrega de archivos para bloquear Directory Traversal (`/files/<path:filename>`).
- [x] Agregar validación de extensiones permitidas en subida de recursos (`upload_file`).
- [x] Crear manejadores de error 404 y 500 adaptables para API y navegación web.
- [x] Corregir discrepancia de extensión `.jpg` en `search_engine.py`.
- [x] Preservar funcionamiento local y fuera de línea al 100%.

## Fase 4: Pruebas
- [x] Configurar suite de pruebas automatizadas con `unittest` (compatible con `pytest`).
- [x] Pruebas unitarias de motor de búsqueda (`tests/test_search_engine.py`).
- [x] Pruebas de motor de búsqueda V2 y grafo de conocimiento (`tests/test_search_engine_v2.py`).
- [x] Pruebas de rutas HTTP, seguridad y verificación visual de Header e iconos (`tests/test_routes.py`).
- [x] Pruebas de autenticación, control de acceso por roles y ciclo de vida de sesión (`tests/test_auth.py`).
- [x] Ejecutar la suite completa (22 pruebas pasando con 100% de éxito).

## Fase 5: Documentación y GitHub
- [x] Crear `.gitignore` exhaustivo para Python, ejecutables, distribución USB, temporales y SO.
- [x] Crear `README.md` profesional en español sin emojis.
- [x] Crear `ARCHITECTURE.md` en español sin emojis.
- [x] Crear `CONTRIBUTING.md` en español sin emojis.
- [x] Crear `SECURITY.md` en español sin emojis.
- [x] Crear `FINAL_AUDIT_REPORT.md` documentando el estado final verificado.
