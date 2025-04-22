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

<style>
:root {
    --green-htb: #20c997;
    --blue-link: #1e88e5;
    --background: #2f2f2f;
    --card-bg: #3d3d3d;
    --text: #eeeeee;
    --background-tarjeta: #2f2f2f;
}

[data-theme="light"] {
    --green-htb: #0d8c6e;
    --blue-link: #0d47a1;
    --background: #f5f5f5;
    --card-bg: #ffffff;
    --text: #333333;
}

body {
    font-family: 'Roboto', sans-serif;
    margin: 0;
    padding: 2rem;
    background-color: var(--background);
    color: var(--text);
}

.member {
    background: var(--background-tarjeta);
    padding: 1rem;
    margin: 1rem;
    border-radius: 10px;
    max-width: 300px;
    box-shadow: 0 0 15px rgba(32, 201, 151, 0.2);
    text-align: center;
    border: 1px solid var(--green-htb);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.member:hover {
    transform: translateY(-20px);
    box-shadow: 0 12px 20px rgba(32, 201, 151, 0.3);
}

.member img {
    border-radius: 50%;
    border: 2px solid var(--green-htb);
}

.badges img {
    margin: 0.25rem;
}

ul {
    text-align: left;
    font-size: 0.9em;
}

a {
    text-decoration: none;
    color: var(--green-htb);
}

h1, h2, h3 {
    color: var(--green-htb);
}
</style>

<table>
  <section class="team" style="margin-bottom: 3rem; text-align: center;">
    <h2>👥 Nuestro Equipo</h2>
    <div class="container" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px;">
      <div class="member">
        <img src="https://avatars.githubusercontent.com/u/68487005?v=4" width="100" height="100" alt="Joseph" loading="lazy">
        <h3>Joseph Anthony Meneses Salguero</h3>
        <p><strong>IT Operations</strong> at <a href="https://www.linkedin.com/company/seagull-ai/">Seagull Software</a></p>
        <p style="font-size: 0.85em;">IT Operations @Seagull | Hack The Box Ambassador | Junior Cybersecurity | Red Team | Python Mid | Ethical Hacking | SysAdmin | DevOps | Backend & AI Dev | DBA</p>
        <h4>🚀 Algunos Proyectos:</h4>
        <p style="font-size: 0.75em; color: #888; margin-top: -0.5rem; margin-bottom: 1rem;">
          (Haz clic en los títulos para ver más detalles)
        </p>
        <ul style="line-height: 1.8;">
          <li><a href="https://medium.com/saturdays-ai/diagn%C3%B3sticos-de-x-rays-con-neumon%C3%ADa-en-ni%C3%B1os-entre-0-a-5-a%C3%B1os-con-machine-learning-1b4c575bb2b4">Diagnóstico de X-Rays con IA</a> — Modelo para detectar neumonía infantil.</li>
          <li><a href="https://github.com/ElJoamy/Asistente-virtual-AI">Asistente virtual en Telegram</a> — Bot con OpenAI, spaCy y base de datos.</li>
          <li><a href="https://github.com/ElJoamy/mysql-course">Curso completo de SQL</a> — Teoría, práctica y proyecto final en MySQL.</li>
        </ul>
        <div class="badges">
          <a href="https://github.com/ElJoamy" target="_blank">
            <img src="https://img.shields.io/badge/-GitHub-black?style=flat&logo=github" />
          </a>          
          <a href="https://linkedin.com/in/joamy5902"><img src="https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=linkedin"></a>
          <a href="https://www.linkedin.com/in/joamy5902/details/certifications/"><img src="https://img.shields.io/badge/-Certificaciones-grey?style=flat&logo=googlechrome"></a>
        </div>
      </div>
    </div>
  </section>
</table>