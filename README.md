# 🔐 Security Backend (FastAPI + SQLAlchemy + JWT + OAuth2)

Este es un backend moderno y seguro construido con FastAPI, que implementa autenticación robusta basada en JWT, protección CSRF, limitación de intentos de acceso, validaciones exhaustivas, subida segura de imagen de perfil y arquitectura escalable.

---

## 🧱 Estructura del Proyecto

```
src/
├── config/              # Configuración general y carga del .env
├── middleware/          # Middlewares globales (errores, CSRF, sesiones)
├── models/              # Modelos SQLAlchemy generados por tabla
├── routes/              # Endpoints organizados por versión (api/v1)
├── schema/              # Esquemas Pydantic (requests y responses)
├── security/            # JWT, manejo de tokens, dependencias de seguridad
├── services/            # Lógica de negocio (auth, perfil, refresh)
├── utils/               # Validaciones, logs, generadores, controles de login
app.py                   # Punto de entrada principal de FastAPI
```

---

## ⚙️ Requisitos

```bash
pip install -r requirements.txt
```

---

## 📄 Generar modelos automáticamente

1. Instalar dependencias:
```bash
pip install sqlacodegen pymysql
```

2. Generar todos los modelos:
```bash
sqlacodegen mysql+pymysql://<usuario>:<contraseña>@<host>/<nombre_db> --outfile all_models.py
```

3. Dividir modelos en archivos individuales:
```bash
python split_models.py
```
Esto generará un archivo por tabla en `src/models/`.

---

## 🔐 Características de Seguridad

- ✅ Registro seguro con validación de email, teléfono y contraseña robusta
- ✅ Login con JWT firmado (access y refresh token)
- ✅ Middleware de sesión via cookies HttpOnly
- ✅ Protección CSRF: cookie + header personalizado
- ✅ Reintentos de login limitados a 3 (bloqueo por 15 min)
- ✅ Subida de imagen segura (validación de extensión, mime y peso)
- ✅ Revocación de tokens via jti y blacklist
- ✅ Rotación de refresh token (al usarse se invalida el anterior)
- ✅ Logout completo con invalidación de tokens
- ✅ Solo el usuario puede acceder a su propia foto de perfil
- ✅ Validación contra correos temporales (desde archivo `invalid_email_domains.txt`)
- ✅ Middleware CSRF configurable por método y ruta excluida

---

## 🔎 Swagger UI

La documentación automática está disponible en:
```
http://localhost:8000/docs
```

---

## 🚀 Ejecutar el servidor

```bash
uvicorn app:app --reload --port 8000
```

---

## 🧪 Seguridad Adicional Validada

| Mecanismo | Protección contra |
|----------|-------------------|
| JWT con expiración | Reutilización de tokens robados |
| Cookies HttpOnly + SameSite=strict | XSS y CSRF |
| Middleware CSRF | Acciones externas maliciosas (POST, PUT, DELETE) |
| Blacklist de tokens por JTI | Logout efectivo y rotación de tokens |
| Límite de intentos de login | Fuerza bruta y bots |
| Validación de imagen | Subida de archivos maliciosos |
| Acceso restringido a recursos | Suplantación de identidad |

---

## 📚 Próximas mejoras sugeridas

- 🔐 OAuth2 con Google/GitHub para login externo
- 📉 Auditoría de sesiones activas (IP, dispositivo, tiempo)
- 🚨 Alertas ante reintentos fallidos excesivos
- 🔢 Rate limit por IP o endpoint

---

## Autor

<table>
<tr>
    <td align="center">
        <a href="https://github.com/ElJoamy">
            <img src="https://avatars.githubusercontent.com/u/68487005?v=4" width="100;" alt="ElJoamy" style="border-radius: 50%;"/>
            <br />
            <sub><b>Joseph Anthony Meneses Salguero</b></sub>
        </a>
        <br />
        <a href="https://linkedin.com/in/joamy5902">
            <img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
        </a>
        <a href="https://github.com/ElJoamy">
            <img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
        </a>
        <br />
        <sub>Bckend and AI Developer | Security Specialist</sub>
    </td>
</tr>
</table>
