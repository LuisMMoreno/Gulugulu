# Politica de Seguridad - Gulugulu

La seguridad y confiabilidad de Gulugulu es fundamental para proteger los entornos educativos y la informacion institucional en las escuelas donde opera.

## 1. Versiones Compatibles
Unicamente se ofrece soporte de seguridad y parches para la rama principal activa:

| Version | Soportada |
|---|---|
| 2.x (Actual) | Si |
| 1.x (Heredada) | No |

## 2. Reporte Responsable de Vulnerabilidades
Si descubre un posible problema o fallo de seguridad en Gulugulu, le solicitamos no divulgarlo publicamente a traves de issues publicos en GitHub.

Por favor, reporte el hallazgo al equipo coordinador del proyecto a traves de correo electronico o mediante los canales de seguridad privada de GitHub. Incluya:
- Tipo de vulnerabilidad identificada (por ejemplo, Directory Traversal, Cross-Site Scripting, denegacion de servicio local).
- Descripcion paso a paso para reproducir la vulnerabilidad.
- Prueba de concepto o codigo de demostracion.
- Impacto potencial en el entorno educativo.

El equipo acusara recibo en un plazo no superior a 48 horas habiles y trabajara en una mitigacion antes de cualquier publicacion.

## 3. Practicas de Seguridad Implementadas en el Codigo

1. **Almacenamiento Seguro de Credenciales**:
   - Las contraseñas de usuarios administradores y maestros nunca se guardan en texto claro. Se utiliza el algoritmo de derivacion de claves PBKDF2 con SHA-256 (`werkzeug.security.generate_password_hash`).

2. **Control de Acceso Basado en Roles (RBAC)**:
   - Los endpoints sensibles (`/admin/dashboard`, `/admin/upload`, `/admin/delete`, `/admin/create_user`, `/admin/backup/*`) validan de forma estricta la existencia de una sesion activa y el rol requerido (`admin` o `maestro`).

3. **Prevencion de Escape de Directorios (Path Traversal)**:
   - La funcion de entrega de archivos estaticos y pedagogicos (`serve_file`) normaliza las rutas recibidas (`os.path.normpath`) y bloquea de manera explicita cualquier patron que contenga navegacion hacia directorios superiores (`..`).

4. **Validacion de Carga de Archivos**:
   - El formulario de carga de recursos valida una lista blanca de extensiones autorizadas (`ALLOWED_EXTENSIONS`), impidiendo la subida de ejecutables, scripts de shell o codigo interpretable al servidor.

5. **Parametrizacion de Consultas SQL**:
   - Todas las consultas ejecutadas contra SQLite hacen uso de marcadores de posicion (`?`), neutralizando intentos de inyeccion SQL.

6. **Proteccion de Cookies de Sesion**:
   - No se almacenan volcados de cookies en el directorio de trabajo del proyecto y se ignoran mediante `.gitignore` cualquier archivo temporal derivado de herramientas de pruebas.

