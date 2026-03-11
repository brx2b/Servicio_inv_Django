# Actividad fullstack clase 1

## Integrantes:

Brian Aravena Quezada Andrés

## Análisis del problema:

Explicar brevemente:

- cuál es el problema del sistema presentado en el caso
- por qué el sistema monolítico presenta dificultades
- qué problema específico busca resolver el microservicio diseñado

Debido al rápido crecimiento y popularización de la plataforma, la infraestructura actual monolítica presenta diversos problemas que afectan de forma negativa a los usuarios.

## Problema clave identificado:

Gestión de inventario: 

- El sistema carece de sincronización eficiente.
- Productos marcados como disponibles no se encuentran disponibles en el inventario real
- Necesita escalar para futuro crecimiento de nuevos almacenes

**Un sistema monolítico siempre presenta problemas y limitaciones técnicas en su capacidad de manejar muchas peticiones y información de los usuarios lo que puede causar caídas y mal funcionamiento de el sistema completo causando mal funcionamiento, alta latencia, pobre optimización ya que en un entorno de mucha demanda como una plataforma popular en este caso ShopSmart, se requiere un sistema mejor capacitado y óptimo para uso masivo como un sistema con una arquitectura de microservicios.**

### **3. Arquitectura elegida**

### Microservicios

**Una nueva plataforma en base a una arquitectura de microservicios mejorará de una forma mayor a la actual utilizada (monolítica) permitiendo una mejor escalabilidad, experiencia de usuario, menor riesgo de caídas/errores en el sistema completo, entre más mejoras como la implementación de nuevos sistemas a medida que la plataforma avanza.**

### **4. Diseño del microservicio**

Describir el microservicio creado:

Servicio inventario:

Servicio encargado en la información de disponibilidad en la plataforma

- Encargado en mantener actualizado el inventario de la plataforma de forma sincronizada con el inventario real disponible dejando atrás el problema de compras sin stock disponible, este servicio permite que el usuario pueda visualizar el stock disponible y comprarlo sin problemas relacionados a la demora de actualización del inventario disponible ofreciendo una mejor experiencia.

### **5. Endpoints implementados**

GET /productos

- Devuelve información como nombre, valor, y stock disponible.
<img width="1440" height="581" alt="image" src="https://github.com/user-attachments/assets/68674f36-66d3-4269-a751-56fed6479b06" />



POST /productos

- Permite agregar un nuevo producto al inventario agregando información como nombre, valor y stock disponible.

<img width="1529" height="431" alt="image 1" src="https://github.com/user-attachments/assets/08b54331-410d-453f-936a-f20d9970b5ba" />


<img width="1444" height="701" alt="image 2" src="https://github.com/user-attachments/assets/b802dabc-25fb-4c14-9704-ee02832605df" />


Se visualiza el nuevo producto agregado (id 2).

URL RENDER: https://servicioinvdjango.onrender.com/api/productos/
