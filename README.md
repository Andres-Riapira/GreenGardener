# GreenGardener 🌱

Aplicación móvil y web para la gestión de tareas de jardinería.  
Permite administrar plantas, calendario de riego, fertilización y control de actividades.

## 🚀 Tecnologías
- Backend: Flask + SQLAlchemy + Marshmallow
- Frontend: React Native
- Base de datos: PostgreSQL
- Autenticación: JWT

## 📂 Estructura del proyecto
- `src/` → Código principal del backend
- `tests/` → Pruebas unitarias con Pytest
- `migrations/` → Migraciones de base de datos
- `utils/` → Utilidades (auth, helpers, etc.)

## ⚙️ Instalación
```bash
git clone https://github.com/Andres-Riapira/GreenGardener.git
cd GreenGardener
pip install -r requirements.txt
flask db upgrade
flask run
