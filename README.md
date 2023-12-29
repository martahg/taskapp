# Proyecto de Lista de Tareas con Angular y API REST Django

Este proyecto consiste en una aplicación web de lista de tareas desarrollada con Angular para el frontend y una API REST creada con Django para el backend. La aplicación permite a los usuarios crear, leer, actualizar estado y eliminar tareas.

## Características

- **Gestión de Tareas:** Permite al usuario crear nuevas tareas, marcarlas / desmarcarlas como completadas y eliminarlas.
- **Interfaz Amigable:** Interfaz de usuario intuitiva y fácil de usar, con un diseño minimalista para una mejor experiencia de usuario.

## Tecnologías Utilizadas

### Frontend (Angular)

- **Angular 17:** Utilización del framework Angular para el desarrollo del frontend.
- **Angualar Material:** Utilización del framework Angular Material para dar un mejor aspecto al frontend.
- **HTML/CSS/TypeScript:** Uso de estas tecnologías para la estructura, estilo y lógica del lado del cliente.
- **Angular CLI:** Herramienta de línea de comandos para facilitar la creación, administración y compilación del proyecto Angular.

### Backend (Django API REST)

- **Django:** Framework de desarrollo web en Python utilizado para construir la API REST.
- **Django REST Framework:** Biblioteca de Django para desarrollar API web de manera rápida y consistente.
- **Base de Datos:** Integración con una base de datos SQLite para almacenar las tareas y la información relacionada.

## Instrucciones de Uso

### Requisitos Previos

- **Node.js:** Asegúrate de tener Node.js instalado en tu máquina.
- **Angular CLI:** Instala Angular CLI globalmente ejecutando `npm install -g @angular/cli`.
- **Python y Django:** Asegúrate de tener instalado Python y Django en tu entorno de desarrollo.
- **Entorno Virtual (opcional pero recomendado):** Utiliza entornos virtuales de Python para aislar las dependencias del proyecto.

### Configuración del Proyecto

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/martahg/taskapp
   cd taskapp
2. **Instalar Dependencias del Frontend:**
     
   ```bash
   cd frontend
   npm install

4. **Configuración del Backend:**
   
  - Configura la base de datos en Django y establece las configuraciones necesarias en settings.py.
  - Ejecuta las migraciones:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. **Ejecución del Proyecto:**

   - Inicia el servidor de desarrollo de Angular:
  
     ```bash
     cd frontend
     ng serve
     
   - Inicia el servidor de desarrollo de Django:
     ```bash
     python manage.py runserver


5. **Acceder a la Aplicación:**

   Abre tu navegador web y visita http://localhost:4200 para acceder al frontend de Angular.

### Contacto
Para cualquier duda o sugerencia, no dudes en contactar a mhernandezgranado2@gmail.com.
