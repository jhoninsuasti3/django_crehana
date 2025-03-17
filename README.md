# 🚀 Task Management API - Django + GraphQL

Bienvenido a **Task Management API**, un sistema basado en **Django y GraphQL con Strawberry** para la gestión de tareas. Este proyecto sigue una arquitectura **hexagonal** y aplica principios **SOLID** y **Clean Code** para garantizar escalabilidad y mantenibilidad.

## 📂 Estructura del Proyecto

```
django_crehana/
├── config/                  # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
├── tasks/                   # Aplicación de gestión de tareas
│   ├── application/         # Capa de Aplicación (Casos de Uso)
│   ├── domain/              # Capa de Dominio (Modelos y Entidades)
│   ├── infrastructure/      # Capa de Infraestructura (Repositorios, DB)
│   ├── presentation/        # Capa de Presentación (GraphQL API)
│   ├── tests/               # Pruebas unitarias e integración
├── manage.py                # Comando de gestión de Django
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 📌 Arquitectura del Proyecto

Esta API sigue una **arquitectura hexagonal**, separando capas de la siguiente manera:

- **`config/`** → Configuración global de Django.
- **`tasks/presentation/`** → Maneja la API GraphQL con Strawberry.
- **`tasks/application/`** → Contiene la lógica de negocio.
- **`tasks/domain/`** → Define los modelos de datos.
- **`tasks/infrastructure/`** → Implementa los repositorios de persistencia.
- **`tasks/tests/`** → Pruebas unitarias e integración con `pytest`.

Esta separación permite una mayor **mantenibilidad**, facilitando el testing y la escalabilidad.

---

## 🚀 **Configuración Inicial**

### **1️⃣ Instalar Dependencias**
Asegúrate de tener **Python 3.9+** y ejecuta:

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2️⃣ Aplicar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ Iniciar el Servidor
```bash
python manage.py runserver
```
📌 **GraphQL Playground:** http://127.0.0.1:8000/graphql/

---

# 🐳 Ejecutar la Aplicación con Docker

### 1️⃣ Construir la imagen
```bash
docker build -t django-graphql-app .
```

### 2️⃣ Ejecutar el contenedor
```bash
docker run -p 8000:8000 django-graphql-app
```

# 🐳 Ejecutar con docker-compose

Si prefieres levantar la API con docker-compose:
```bash
docker-compose up --build
```

---

# ✅ Ejecutar Pruebas
```bash
pytest --disable-warnings
```

Si quieres ver detalles de cada prueba:
```bash
pytest -v
```

---

# 📌 Pruebas de la API

Puedes probar los endpoints en GraphQL Playground o con curl:

### Obtener todas las tareas
```graphql
{
  tasks {
    id
    title
    description
    completed
  }
}
```

### Crear una tarea
```graphql
mutation {
  createTask(title: "Nueva tarea", description: "Descripción", completed: false) {
    id
    title
    description
    completed
  }
}
```

### Obtener una tarea por ID
```graphql
{
  task(id: 1) {
    id
    title
    description
    completed
  }
}
```

### Actualizar una tarea
```graphql
mutation {
  updateTask(id: 1, title: "Tarea actualizada", description: "Nueva descripción", completed: true) {
    id
    title
    description
    completed
  }
}
```

### Eliminar una tarea
```graphql
mutation {
  deleteTask(id: 1)
}
```

---

# 📌 Pruebas Automáticas
Para verificar que todo el código cumple con los estándares:
```bash
pytest --disable-warnings
```

---

### **📌 Resumen**
- ✅ **Incluimos la descripción del proyecto y arquitectura hexagonal**.
- ✅ **Añadimos instrucciones para configurar el entorno local**.
- ✅ **Incluimos pasos para ejecutar la API con Docker**.
- ✅ **Añadimos instrucciones para ejecutar pruebas unitarias e integración**.
- ✅ **Proporcionamos ejemplos de consultas GraphQL**.

🚀 **¡Este proyecto está listo para producción!** 🎯🔥
