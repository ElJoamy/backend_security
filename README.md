# 🔐 Security Backend (FastAPI + SQLAlchemy + JWT + OAuth2)

Este es un backend moderno en FastAPI que implementa autenticación segura con JWT, validaciones robustas, subida de imagen de perfil, y estructura escalable.

---

## 🧱 Estructura del Proyecto

```
src/
├── config/              # Configuración general y .env
├── middleware/          # Middlewares globales (errores, sesiones)
├── models/              # Modelos SQLAlchemy generados por tabla
├── routes/              # Endpoints organizados por versión
├── schema/              # Pydantic Schemas (requests, responses)
├── security/            # JWT, auth y dependencias de seguridad
├── services/            # Lógica de negocio
├── utils/               # Validaciones, logs, generadores, etc.
app.py                   # Punto de entrada de FastAPI
```

---

## ⚙️ Requisitos

```bash
pip install -r requirements.txt
```

---

## 🗄️ Generar modelos por tabla automáticamente

1. Instala los paquetes necesarios:

```bash
pip install sqlacodegen pymysql
```

2. Genera todos los modelos en un solo archivo:

```bash
sqlacodegen mysql+pymysql://<usuario>:<contraseña>@<host>/<nombre_db> --outfile all_models.py
```

Ejemplo:

```bash
sqlacodegen mysql+pymysql://root:root@localhost/dbsecurity --outfile all_models.py
```

3. Divide los modelos en archivos individuales por tabla:

```bash
python split_models.py
```

Esto generará un archivo por tabla dentro de `src/models/` con nombres como `user_model.py`, `session_model.py`, etc.

---

## 🔐 Funcionalidades

- Registro de usuarios con validación de correo, teléfono y contraseña segura
- Login seguro con JWT + OAuth2
- Middleware para sesiones vía Cookie
- Edición de perfil con subida de imagen (almacenada como `LONGBLOB`)
- Acceso restringido a la imagen de perfil (solo el usuario puede acceder)
- Validación contra correos temporales desde un archivo `invalid_email_domains.txt`
- Manejo global de errores con logs coloreados

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

## 🧪 Tests y seguridad

- El sistema restringe acceso a recursos sensibles como fotos y datos personales
- Se valida que los uploads no contengan archivos maliciosos
- La API impide ataques de directory traversal o SQL Injection

