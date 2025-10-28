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