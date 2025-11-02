# 1. Alcance de Redes y Virtualización
## a) Clasificación y características de las redes según su alcance
1. **PAN (Personal Area Network) - Red de Área Personal**
   Tiene un alcance de unos pocos metros, aproximadamente de 1 a 10m.
    
    Ejemplos:
   - Conexión Blutooth entre el celular y los auriculares.
   - Comunicación entre smartwatch y celular.
   - Conexiones USB o infrarrojas.
    
    Características:
   - Están diseñadas para uso personal.
   - Son de baja potencia y corto alcance.
   - No requieren de infraestructura compleja.
2. **LAN (Local Area Network) — Red de Área Local**
    Tiene un alcance de unos cientos de metros o algunos kilómetros (por ejemplo, dentro de un edificio o campus).

    Ejemplos:
    - La red de computadores de una universidad o empresa.
    - Las red de una casa particular con su router Wi-Fi.

    Características:
    - Alta velocidad (100 Mbps - varios Gbps).
    - Administración local.
    - Puede ser cableada (Etherner) o inalámbrica (Wi-Fi).
3. **MAN (Metropolitan Area Network) - Red de Área Metropolitana**
    Tiene un alcance más amplio que una LAN, generalmente abarcando toda una ciudad.

    Ejemplos:
    - Red de proveedores de internet urbanos.
    - Las redes de televisión por cable disponibles en muchas ciudades.
    
    Características:
    - Conecta múltiples LAN dentro de una ciudad.
    - Usa fibra óptica, microondas o enlaces inalámbricos urbanos.
4. **WAN (Wide Area Network) - Red de Área Extensa**
    Son aquellas que abarcan una extensa área geográfica, como un país o continente.

    Ejemplos:
    - Internet.
    - La red privada de una empresa multinacional.
  
    Características:
    - Conecta muchas LAN, MAN, etc.
    - Usa infraestructuras públicas (telecomunicaciones, satélites, cables submarinos).
    - Latencia más alta y velocidades variables.
5. **GAN (Global Area Network) - Red de Alcance Global**
    Tienen un alcance global.

    Ejemplos:
    - Internet de redes corporativas interconectadas a nivel mundial.
    - Red global de satélites que da cobertura planetaria.
    
    Características:
    - Interconecta varias WAN.
    - Soporta comunicación global (incluso con movilidad internacional).
6. **VLAN (Virtual Local Area Networks)**

## b) Redes VLAN
Las redes VLAN son redes lógicas que dividen una LAN física en múltiples LAN lógicas independientes. Estas redes permiten 
segmentar y administrar grupos de dispositivos según criterios lógicos en lugar de criterios físicos. Las redes VLAN son 
esenciales para la segmentación y administración de dispositivos en una red, brindando flexibilidad y seguridad en la gestión de 
redes. Se basan en switches especialmente diseñados para este propósito y se identifican con colores o etiquetas.

Beneficios de las redes VLAN:
- Ofrecen flexibilidad en la configuración de la red.
- Permiten que la distribución del equipo de red no tenga que coincidir con la estructura física de la organización.

Ejemplo: En una empresa hay tres sectores
- Administración
- Recursos humanos
- Laboratorio

Todos están conectados al mismo switch físico, pero no se quiere que se puedan ver el tráfico entre sí (por seguridad y organización).

Entonces se crea:
- VLAN 10 para la administración
- VLAN 20 para recursos humanos
- VALN 30 para el laboraotorio
De esa forma, aunque físicamente estén conectados al mismo switch, lógicamente están aislados como si fueran redes separadas.
   
Clasificación:

1. Según la asignación (forma de identificar la VLAN)

|     Tipo de VLAN     | Descripción    |
|----------------------|-----------------|
| VLAN por puerto (Port-based VLAN) | Cada puerto del switch pertenece a una VLAN específica. Es la forma más común y fácil de configurar. |
| VLAN por dirección MAC | El switch asigna la VLAN según la dirección MAC del dispositivo. Si el dispositivo se mueve a otro puerto, sigue en su misma VLAN. |
| VLAN por protocolo | Se agrupan según el protocolo de capa 3 (por ejemplo, IPv4, IPv6, IPX, etc.). |
| VLAN por subred IP | Los dispositivos con direcciones IP dentro de una misma subred se asignan automáticamente a la misma VLAN. |
|VLAN dinámica (mediante VMPS o 802.1X)| La asignación se hace automáticamente mediante un servidor que reconoce al usuario o al dispositivo y lo asigna a su VLAN correspondiente.|

2. Según la función o tipo de tráfico

|     Tipo de VLAN     | Uso principal   |
|----------------------|-----------------|
| VLAN de datos (Data VLAN) | Transporta tráfico de usuarios normales (PCs, impresoras, etc.). |
| VLAN de voz (Voice VLAN) | Separada especialmente para tráfico de VoIP. Garantiza calidad de servicio (QoS). |
| VLAN nativa (Native VLAN) | Se usa para tráfico no etiquetado en enlaces troncales (por defecto suele ser la VLAN 1). |
| VLAN de administración (Management VLAN) | Dedicada al acceso de gestión del switch, routers, etc. |
| VLAN predeterminada (Default VLAN) | VLAN inicial del switch (también suele ser la VLAN 1). Todos los puertos pertenecen a ella hasta que se configuren manualmente. |

## c) Protocolo IEEE 802.1Q
El protocolo IEEE 802.1Q es el estándar que define cómo se implementan las VLANs en redes Ethernet. En otra palabras, es el 
protocolo que permite que varias VLAN viajen por el mismo enlace físico (como un cable entre dos switches, o entre un switch y un router) sin mezclarse.

## d) Tagging
El 802.1Q agrega una etiqueta (tag) dentro del encabezado Ethernet para indicar a qué VLAN pertenece cada trama.

Sin VLAN (Ethernet estándar):

```
[Dest MAC] [Src MAC] [Tipo/Longitud] [Datos] [FCS]
```
Con VLAN:

```
[Dest MAC] [Src MAC] [Tag 802.1Q] [Tipo/Longitud] [Datos] [FCS]
```

La etiqueta 802.1Q Tag ocupa 4 bytes adicionales insertados justo después de las direcciones MAC.

**Estructura del tag 802.1Q**

|     Campo     | Tamaño   | Descripción | 
|----------------------|-----------------| -----------------|
|     TPID (Tag Protocol Identifier)    | 16 bits   | Valor fijo 0x8100 que indica que el frame está etiquetado con 802.1Q. | 
|    PCP (Priority Code Point)     | 3 bits   | Prioridad (para QoS, útil por ejemplo en voz). | 
|     DEI (Drop Eligible Indicator)     | 1 bit   | Indica si el frame puede descartarse en congestión. | 
|     VID (VLAN Identifier)     | 12 bits   | Identificador de VLAN (de 1 a 4094). | 

# 2. Implementación de topología en Packet Tracer

En base a la consigna, realizamos la siguiente implementación en Packet Tracer e inicialmente solo configuramos el ruteo
de las PCs en base a la tabla de ruteo provista:

![topologia-inicial](img/topologia-inicial.png)

Configuración de PCs:

![ConfIP-PCA](img/ruteoPCA.png)
![ConfIP-PCB](img/ruteoPCB.png)

## a) Configuración de los switch (cambiar sus nombres)
![conf-nombre-sw1](img/cong-nombre-sw1.png)
![conf-nombre-sw2](img/conf-nombre-sw2.png)

## b) Asignar contraseñas privilegiadas, de consola y vty
![contra-sw1](img/contraseñas-sw1.png)
![contra-sw2](img/constraseñal-sw2.png)

## c) Encriptado de las contraseñas
![enciptado-contraseñas-switches](img/encriptado.png)

## d) Configuración IP en VLAN 1 según datos de la tabla
![confIP-VLAN](img/congIP-VLAN.png)

## e) Desconexión de terminales que no se están usando
Para el SW-1 solo Fa0/1 y Fa0/6 están en uso, esto se sabe de antemano por el armado de la topología:
![interfaces-del-SW1](img/interfaces-SW1.png)

Apagamos las demás interfaces que no se usan. Esta es una buena práctica para evitar conexiones no autorizadas o confusiones:
![deshabilitado-de-interfaces-que-no-se-usan-SW1](img/deshabilitado-interfaces-SW1.png)

Hacemos lo mismo para el SW-2, pero para este caso las interfaces en uso son Fa0/1 y Fa0/18:

![interfaces-del-SW2](img/interfaces-SW2.png)

Y apagamos las interfaces que no se usan:
![deshabilitado-de-interfaces-que-no-se-usan-SW2](img/deshabilitado-interfaces-SW2.png)

## f) Guardado de la configuración
![guardado-memoria-SW1](img/guardado-memoriaSW1.png)
![guardado-memoria-SW2](img/guardado-memoriaSW2.png)

## g) Testeo de comunicación
Verificamos la conexión entre los switeches. Si se recibe una repuesta con `!!!` la conexión entre los switches está funcionando correctamente.

![comunicacion](img/conectividad-entre-SWs.png)

## h) Creación de VLANs en los switches
![VLANs-en-los-switches](img/VLAN-en-ambos-SW.png)

Podemos verificar que se crearon correctamente:
![verificación-creación-VLANs](img/verificacion-VLANs.png)

## i) Visualizar lista de VLAN
En la captura del punto anterior donde se verifica que las VLAN se hayan creado correctamente se puede observar la lista de las VLAN utilizadas. **La VLAN por defecto es la 1**.

## j) Asignación de PC-A a VLAN Laboratorio
La PC-A está conectada al puerto Fa0/6 del switch SW-1. Para asignarla a la VLAN de Laboratorio tenemos que seleccionar la VLAN 10:
![PC-A-Laboratorio](img/PC-A-a-VLAN-Laboratorio.png)

## k) Configuración IP de Management
Se tiene configurado la IP de administración en VLAN 1, pero la VLAN 1 no se debe usar para administración. Vamos a mover
esta IP a la VLAN 99 que se creo con el nombre de Management:

![conf-management-IP](img/conf-managmnt.png)

## l) Estado de la VLAN
![estado-VLAN-SW1](img/estado-VLAN-SW1.png)

Comando `show vlan brief`:

| VLAN      | Nombre                              | Estado | Puertos asociados                               | Interpretación                                                                                                                                                                                |
| --------- | ----------------------------------- | ------ | ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1         | default                             | active | Fa0/1, Fa0/2–Fa0/5, Fa0/7–Fa0/24, Gig0/1–Gig0/2 | Esta es la **VLAN por defecto**. Todos los puertos aparecen listados aquí porque, aunque muchos estén administrativamente apagados, por defecto pertenecen a VLAN 1 mientras no se reasignen. |
| 10        | Laboratorio                         | active | Fa0/6                                           | Es la VLAN configurada para el **Laboratorio**, donde se conectó la PC-A. Su puerto asignado (Fa0/6) está **activo y operativo**.                                                             |
| 20        | Bar                                 | active | —                                               | VLAN creada correctamente pero **sin puertos asignados**, por eso no muestra interfaces asociadas.                                                                                            |
| 99        | Management                          | active | —                                               | VLAN de administración creada correctamente. No tiene puertos físicos asociados (sólo la interfaz VLAN99 lógica).                                                                             |

Las VLANs fueron creadas exitosamente (Laboratorio, Bar y Management).
Los puertos se encuentran correctamente asignados según las consignas:

Fa0/6 → VLAN10 (Laboratorio)

Resto → permanecen en VLAN1 (default).

Comando `show vlan brief`:

La mayoría de las interfaces FastEthernet (Fa0/2–Fa0/24) aparecen con el estado
administratively down, lo cual confirma que fueron correctamente deshabilitadas según el punto (e).

Las interfaces Fa0/1 y Fa0/6 están up/up, es decir habilitadas y con enlace físico activo.

- Fa0/1 está conectada al otro switch (SW-2).

- Fa0/6 está conectada a la PC-A.


| Interfaz | Dirección IP | Estado  | Interpretación                                                                                                                                    |
| -------- | ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| VLAN1    | unassigned   | up/up   | Interfaz VLAN por defecto sin IP asignada (fue deshabilitada su IP en el punto k).                                                                |
| VLAN99   | 192.168.1.11 | up/down | VLAN de **Management** correctamente configurada con su IP, pero **sin puertos activos asociados a la VLAN99**, por eso el protocolo está “down”. |


## m) Asignación de PC-B a VLAN Laboratorio del SW-2
![PC-B-Laboratorio](img/PC-B-a-VALN-Laboratorio.png)

*En el inciso k) ya se configuró el VLAN Management del SW-2.*

## n) Conectividad entre PC-A y PC-B

Se realizó una prueba de conectividad utilizando el comando `ping` desde la PC-A (192.168.10.3) hacia la PC-B (192.168.10.4) y desde
la PC-B hacia la PC-A. Nos dió como resultado tres respuesta "Request timed out", indicando que no existe comunicación entre
ambas computadoras:

![ping-entre-computadoras-no-funcionando](img/ping-no-funcionando.png)

Al verificar la configuración de los switches SW1 y SW2, se observó que las interfaces utilizadas para conectarlos entre si (FasrEthernet 0/1) no estaban configuradas como enlaces trunk. Esto significa que dichos puertos solo estaban permitiendo en tráfico de la VLAN nativa (VLAN 1), y por lo tanto todos los paquetes pertenecientes a la VLAN 10 (Laboratorio), en la cual se encuentran las PC-A y PC-B, no podían ser transmitidos entre los switches.

Para resolver este problema se configuraron los puertos FastEthernet 0/1 de ambos switches como enlaces trunk, mediante los siguientes comandos:

![configuracion-trunk-en-switches](img/configuracion-trunk.png)

Durante la configuración del enlace trunk, al establecer el modo trunk en SW-1 antes que en SW-2, se generaron mensajes de protocolo Spanning Tree (STP) en SW-2 indicando una inconsistencia de tipo de puerto. Esto ocurre porque el SW-1 comenzó a enviar tramas etiquetadas 802.1Q hacía un puerto del SW-2 que aún estaba en modo access.

Con esta configuración, el enlace entre los switches quedó habilitado para transportar tráfico de las VLAN 10 (Laboratorio) y 99 (Administración).

Se repitió el comando `ping` entre ambas PCs y se obtuvieron respuestas exitosas:

![ping-entre-PCs-funcionando](img/pings-funcionando.png)

Esto confirma que la comunicación entre las dos computadoras de la VLAN Laboratorio se estableció correctamente y que el enlace trunk está funcionando adecuadamente.


