# Checklist de Regresión - Sistema de Gestión Full Stack

Este checklist permite validar rápidamente que las funcionalidades principales del sistema continúan funcionando luego de cambios o actualizaciones.

---

## Login

- [x] La página de login carga correctamente.
- [x] El usuario administrador puede iniciar sesión.
- [x] El sistema redirige al dashboard luego del login.

---

## Dashboard

- [x] El dashboard carga sin errores.
- [x] Se muestran métricas principales.
- [x] Se actualizan datos relacionados a productos, clientes y ventas.

---

## Productos

- [x] Se puede crear un producto.
- [x] Se puede editar un producto.
- [x] Se puede modificar el stock.
- [x] Los productos se listan correctamente.

---

## Clientes

- [x] Se puede crear un cliente.
- [x] El cliente aparece como activo.
- [x] Los clientes se listan correctamente.

---

## Ventas

- [x] Se puede seleccionar un cliente.
- [x] Se puede seleccionar un producto.
- [x] Se puede agregar cantidad.
- [x] Se puede confirmar una venta.
- [x] La venta aparece en el historial.

---

## Stock

- [x] El stock se visualiza correctamente.
- [x] El stock disminuye luego de una venta.
- [x] Se muestran productos con stock disponible.
- [x] Se identifican productos con stock bajo o sin stock.

---

## Reportes

- [x] Se muestran ventas del período.
- [x] Se muestran ingresos.
- [x] Se muestra producto más vendido.
- [x] Se muestra cliente con más compras.

---

## Asistente IA local

- [x] El módulo carga correctamente.
- [x] Responde sobre stock bajo.
- [x] Responde sobre resumen de ventas.
- [x] Responde sobre clientes destacados.
- [x] Responde sobre productos importantes.
- [x] Responde consejos de gestión.

---

## Pruebas automatizadas

- [x] Test API health-check aprobado.
- [x] Test E2E login aprobado.
- [x] Reporte HTML generado correctamente.

---

## Resultado general

Estado de regresión: **Aprobado**.