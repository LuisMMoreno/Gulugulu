# Guia de Contribucion - Gulugulu

Agradecemos el interes en contribuir al proyecto Gulugulu. Esta plataforma tiene como proposito cerrar la brecha digital y pedagogica en escuelas rurales sin acceso a Internet. Para garantizar la calidad y estabilidad del codigo, solicitamos seguir las siguientes directrices.

## 1. Principios Fundamentales de Desarrollo

1. **Operatividad Fuera de Linea Absoluta**:
   - Queda estrictamente prohibido enlazar recursos externos mediante CDN (Google Fonts, Unpkg, Cloudflare, cdnjs, etc.).
   - Todo recurso estatico (fuentes tipograficas, librerias JavaScript, estilos CSS e imagenes) debe servirse localmente desde el directorio `static/`.

2. **Identidad Visual Consistente**:
   - El encabezado de la plataforma utiliza de manera exclusiva la tipografia local `Suez One` en formato solido, sin logotipos graficos ni mascotas anexas.
   - Toda la iconografia de la aplicacion debe emplear la libreria `Lucide` integrada en `static/js/lucide/lucide.js`. No se deben introducir fuentes de iconos externas.

3. **Seguridad y Calidad de Codigo**:
   - Todas las consultas SQL deben estar parametrizadas mediante tuplas para evitar inyecciones SQL.
   - Las rutas de archivos recibidas desde el cliente deben pasar por validacion y sanitizacion estricta contra Directory Traversal.
   - Toda nueva funcionalidad debe estar acompanada por pruebas automatizadas correspondientes.

## 2. Flujo de Trabajo con Git

1. Bifurcar (fork) el repositorio oficial en su cuenta de GitHub.
2. Clonar su bifurcacion localmente:
   ```bash
   git clone https://github.com/su-usuario/gulugulu.git
   cd gulugulu
   ```
3. Crear una rama especifica para su cambio:
   ```bash
   git checkout -b mejora-o-correccion
   ```
4. Realizar los cambios correspondientes asegurandose de respetar los estandares de codificacion PEP 8.
5. Ejecutar la suite completa de pruebas antes de realizar cualquier confirmacion:
   ```bash
   python -m unittest discover tests -v
   ```
   No se admitiran solicitudes de extraccion con pruebas fallidas.
6. Realizar confirmaciones claras y descriptivas en espanol:
   ```bash
   git commit -m "Correccion: sanitizacion de rutas en carga de archivos"
   ```
7. Enviar su rama al repositorio remoto:
   ```bash
   git push origin mejora-o-correccion
   ```
8. Abrir una solicitud de extraccion (Pull Request) hacia la rama principal del repositorio base.

## 3. Estructura de Pruebas
Los archivos de pruebas se ubican en la carpeta `tests/`:
- `test_search_engine.py`: Pruebas del motor en memoria V1.
- `test_search_engine_v2.py`: Pruebas del motor FTS5, expansion de consultas y grafo de conocimiento.
- `test_routes.py`: Pruebas de rutas HTTP, respuestas JSON, seguridad y consistencia de encabezados.
- `test_auth.py`: Pruebas de autenticacion, control de roles y gestion de sesiones.

## 4. Reporte de Errores
Si identifica un fallo en la plataforma, por favor abra un Issue en GitHub detallando:
- Descripcion concisa del comportamiento observado.
- Pasos exactos para reproducir el fallo.
- Entorno de ejecucion (sistema operativo, version de Python).
- Registros de consola o trazas de error relevantes.

