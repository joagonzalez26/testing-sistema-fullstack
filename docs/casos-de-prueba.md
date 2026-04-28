# Casos de Prueba - Sistema de Gestión Full Stack

Documento con los casos de prueba principales realizados sobre el sistema.

---

## CP-001 - Inicio de sesión correcto

**Módulo:** Login  
**Tipo:** Manual  
**Estado:** Aprobado  

### Precondición

El sistema debe estar corriendo en `http://localhost:5173`.

### Pasos

1. Ingresar a la página de login.
2. Escribir el email del usuario administrador.
3. Escribir la contraseña.
4. Presionar el botón para iniciar sesión.

### Resultado esperado

El sistema permite el acceso y redirige al dashboard principal.

### Resultado obtenido

El usuario pudo iniciar sesión correctamente.

---

## CP-002 - Visualización del dashboard

**Módulo:** Dashboard  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Iniciar sesión.
2. Acceder al panel principal.
3. Observar las métricas del sistema.

### Resultado esperado

El dashboard muestra métricas de productos, clientes, ventas, ingresos, stock y últimos registros.

### Resultado obtenido

El dashboard cargó correctamente y mostró información del sistema.

---

## CP-003 - Crear producto

**Módulo:** Productos  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Ingresar al módulo Productos.
2. Presionar la opción para crear un nuevo producto.
3. Completar nombre, descripción, precio y stock.
4. Guardar el producto.

### Resultado esperado

El producto se guarda correctamente y aparece en el listado.

### Resultado obtenido

El producto fue creado y visualizado correctamente.

---

## CP-004 - Editar stock de producto

**Módulo:** Productos / Stock  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Ingresar al módulo Productos.
2. Seleccionar un producto existente.
3. Modificar la cantidad de stock.
4. Guardar los cambios.
5. Verificar el módulo Stock.

### Resultado esperado

El stock del producto se actualiza correctamente.

### Resultado obtenido

El stock fue modificado y reflejado correctamente en el sistema.

---

## CP-005 - Crear cliente

**Módulo:** Clientes  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Ingresar al módulo Clientes.
2. Crear un nuevo cliente.
3. Completar los datos solicitados.
4. Guardar.

### Resultado esperado

El cliente se registra correctamente y aparece como activo.

### Resultado obtenido

El cliente fue creado correctamente y quedó marcado como activo.

---

## CP-006 - Registrar venta

**Módulo:** Ventas  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Ingresar al módulo Ventas.
2. Seleccionar un cliente.
3. Seleccionar un producto.
4. Indicar la cantidad.
5. Confirmar la venta.

### Resultado esperado

La venta se registra correctamente y aparece en el historial.

### Resultado obtenido

La venta fue cargada correctamente en el sistema.

---

## CP-007 - Descuento automático de stock

**Módulo:** Ventas / Stock  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Verificar el stock inicial de un producto.
2. Registrar una venta de ese producto.
3. Volver al módulo Stock.
4. Comparar el stock anterior con el stock actual.

### Resultado esperado

El stock disminuye según la cantidad vendida.

### Resultado obtenido

El stock se descontó correctamente luego de registrar la venta.

---

## CP-008 - Visualización de reportes

**Módulo:** Reportes  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Registrar al menos una venta.
2. Ingresar al módulo Reportes.
3. Revisar las métricas comerciales.

### Resultado esperado

El sistema muestra ventas, ingresos, producto más vendido y cliente con más compras.

### Resultado obtenido

Los reportes reflejaron correctamente los datos reales del sistema.

---

## CP-009 - Asistente IA local

**Módulo:** Asistente IA  
**Tipo:** Manual  
**Estado:** Aprobado  

### Pasos

1. Ingresar al módulo Asistente IA.
2. Enviar consultas como:
   - Analizar stock bajo.
   - Resumen de ventas.
   - Clientes destacados.
   - Productos más importantes.
   - Ideas para mejorar el negocio.
   - Consejos de gestión.

### Resultado esperado

El asistente responde en modo local con información relacionada al sistema.

### Resultado obtenido

El asistente respondió correctamente a las consultas principales.

---

## CP-010 - Health-check del backend

**Módulo:** API  
**Tipo:** Automatizado  
**Archivo:** `tests/api/test_health_check.py`  
**Estado:** Aprobado  

### Descripción

Validar que el backend responda correctamente en la ruta de health-check.

### Resultado esperado

La API responde con status code `200` y JSON `true`.

### Resultado obtenido

La prueba automatizada finalizó correctamente.

---

## CP-011 - Carga de página de login

**Módulo:** Login  
**Tipo:** Automatizado E2E  
**Archivo:** `tests/e2e/test_login.py`  
**Estado:** Aprobado  

### Descripción

Validar con Selenium que la página de login carga correctamente en el navegador.

### Resultado esperado

El navegador abre correctamente la página de login.

### Resultado obtenido

La prueba automatizada finalizó correctamente.

---

## Resultado general

Los casos de prueba principales fueron ejecutados correctamente.

**Estado general:** Aprobado.
