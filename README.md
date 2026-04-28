
<img width="1920" height="1080" alt="Black and Gray Minimalist Creative Portfolio Presentation (1)" src="https://github.com/user-attachments/assets/de11ba45-e0d0-48bd-888e-27721cf7c980" />


Repositorio dedicado al proceso de testing del proyecto **Sistema de Gestión Full Stack**.

El objetivo es documentar y ejecutar pruebas manuales y automatizadas sobre un sistema web desarrollado con **React**, **FastAPI**, **PostgreSQL** y **Docker**.

---

## Proyecto testeado

Repositorio principal:  
https://github.com/joagonzalez26/sistema-gestion-fullstack

Aplicación local:

- Frontend: http://localhost:5173
- Backend: http://localhost:8000

---

## Objetivo

Validar el correcto funcionamiento de los módulos principales del sistema:

- Login
- Dashboard
- Productos
- Clientes
- Ventas
- Stock
- Reportes
- Asistente IA local

---

## Etapas de prueba

### Etapa 1 - Pruebas manuales

Se realizaron pruebas manuales sobre los módulos principales del sistema, interactuando directamente con la aplicación desde el navegador.

Se verificó:

- Inicio de sesión.
- Visualización del dashboard.
- Creación y edición de productos.
- Creación de clientes.
- Registro de ventas.
- Descuento automático de stock.
- Visualización de reportes.
- Funcionamiento del asistente IA local.

Estado: **completado**.

### Etapa 2 - Pruebas automatizadas

Se implementaron pruebas automatizadas iniciales con **Python**, **Pytest**, **Requests** y **Selenium**.

Pruebas realizadas:

- Health-check del backend.
- Carga de la página de login con Selenium.

Resultado actual: **2 passed**.

---

## Herramientas utilizadas

- Python
- Pytest
- Requests
- Selenium
- WebDriver Manager
- Pytest HTML
- Google Chrome

---

## Estructura del repositorio

- `docs/`
  - `plan-de-pruebas.md`
  - `casos-de-prueba.md`
  - `checklist-regresion.md`
  - `reporte-de-bugs.md`

- `evidencias/`
  - `capturas/`
  - `reportes/`

- `tests/`
  - `api/test_health_check.py`
  - `e2e/test_login.py`
  - `manual/`

- `README.md`
- `requirements.txt`
- `.gitignore`

---

## Instalación

### Crear entorno virtual

Ejecutar:

`python3 -m venv .venv`

Activar entorno virtual en macOS/Linux:

`source .venv/bin/activate`

### Instalar dependencias

Ejecutar:

`pip install -r requirements.txt`

---

## Ejecución de pruebas

Antes de ejecutar las pruebas, el sistema principal debe estar corriendo con Docker.

### Levantar el sistema principal

Desde el proyecto `sistema-gestion`:

`cd ~/Desktop/sistema-gestion`

`docker-compose up -d`

### Ejecutar pruebas

Desde este repositorio:

`pytest`

---

## Reporte HTML

### Generar reporte

`pytest --html=evidencias/reportes/reporte-testing.html`

### Ubicación del reporte

`evidencias/reportes/reporte-testing.html`

---

## Estado actual

- Pruebas manuales principales realizadas.
- Test API health-check aprobado.
- Test E2E login aprobado.
- Reporte HTML generado correctamente.

---

## Autor

Testing realizado por **Joaquín González** 
