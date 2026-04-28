# Plan de Pruebas - Sistema de Gestión Full Stack

## Objetivo

Validar el funcionamiento general del Sistema de Gestión Full Stack, comprobando sus módulos principales desde la perspectiva de un usuario final y mediante pruebas automatizadas iniciales.

## Alcance

Se probaron los siguientes módulos:

- Login
- Dashboard
- Productos
- Clientes
- Ventas
- Stock
- Reportes
- Asistente IA local

## Tipos de pruebas

### Etapa 1 - Pruebas manuales

Pruebas funcionales realizadas manualmente desde el navegador, simulando el uso real del sistema.

### Etapa 2 - Pruebas automatizadas

Pruebas iniciales implementadas con Python, Pytest, Requests y Selenium.

## Ambiente de prueba

- Sistema: Sistema de Gestión Full Stack
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- Base de datos: PostgreSQL en Docker
- Navegador: Google Chrome
- Sistema operativo: macOS

## Criterio de aprobación

Una prueba se considera aprobada cuando el resultado obtenido coincide con el resultado esperado, no se detectan errores funcionales o de conexión, y las pruebas automatizadas finalizan con estado `passed`.

## Estado general

El sistema fue probado manualmente en sus módulos principales y se ejecutaron pruebas automatizadas iniciales con resultado satisfactorio.
