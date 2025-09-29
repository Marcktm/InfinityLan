# 1. La IEEE y su rol protagónico en el proceso de normalización y estandarización de las tecnologías.
## a) IEEE 802.3 y 802.11 
La **IEEE** (Institute of Electrical and Electronics Engineers) es una organización internacional sin fines de lucro que reune ingenieros, cinetíficos, y profesionales de la tecnología. Nació en 1963 de la fusión del AIEE (American Institute of Electrical Engineers) y el IRE (Institute of Radio Engineers).
Su rol en la estandarización de las tecnologías: a través de cómites técnicos, como el IEEE Standar Association, **define normas que permiten quye tecnologías de distintos fabricantes sean compatibles entre si**. Es decir, asegura ***interoperabilidad*** y ***uniformidad*** en telecomunicaciones, redes, electrónica, software y mucho más.

### IEEE 802.3 (Ethernet)
Nació en 1983 como el estandar oficial para **Ethernet**, que originalmente había sido desarrollado por Xerox, DEC e Intel en los años 70. Fue pensado como un protocolo de red local basado en cable coaxial, pero con el tiempo se adaptó al par trenzado (UTP) y la fibra óptica.
- Campo de aplicación:
  - Define como transmitir datos en redes cableadas.
  - Incluye la forma en que se estructuran las tramas, las tasas de transmisión (desde 10 Mbps en los 80 hasta 400 Gbps en la actualidad), y la forma en que las estaciones detectan y gestionan colisiones (CSMA/CD, aunque ya está en desuso con los switches).

Se convirtió en el estandar dominantes en LAN cableadas, si hablamos de "*Ethernet*" estamos hablando de IEEE 802.3.

### IEEE 802.11 (Wi-Fi)
El estándar original salió en 1997 y permitía velocidades de 1 a 2 Mbps. Desde entonces evolucionó y se introdujeron mejoras en la velocidad y eficiencia del espectro: 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax (Wi-Fi 6) y 802.11be (Wi-Fi 7).
- Campo de aplicación:
  - Define las redes inalámbricas de área local (WLAN).
  - Se usa en hogares, empresas, universidades, aeropuertos y prácticamente en cualquier lugar donde haya Wi-Fi.
  - Opera principalmente en las bandas de 2.4 GHz y 5 GHz, aunque ya hay desarrollo en 6GHz (Wi-Fi 6E).

Esta estandarización permitió la movilidad en entornos que antes dependían de cables, y abrió la puerta a tecnologías como IoT, smart homes y oficinas totalmente inalámbricas.

## b) Conexión a una red abierta de la facultad


## c) Red Wi-Fi y dispositivo con diferentes protocolos
Si una red Wi-Fi opera con un determinado protocolo y una notebook vieja utiliza una NIC (tarjeta de red inalámbrica) que no soporta dicho protocolo entonces no va a poder conectarse a la red Wi-Fi.
*Ejemplo*: Si el router está configurado solo en Wi-Fi 6 (802.11ax) y la notebook solo soporta hasta Wi-Fi 4 (802.11n), directamente no va a ver la red o no podrá autenticarse. Si el router soporta modos mixtos (por ejemplo AX + N + AC), entonces la notebook podrá conectarse usando el protocolo más antiguo que entienda, pero sacrificando velocidad y eficiencia de la red.
En resumen, ***no hay compatibilidad hacia adelante***, un dispositivo viejo no entiende protocolos más nuevos. ***Si puede haber compatibilidad hacia atrás***, pero depende de que el router esté configurado para soportar esos estándares antiguos.

## d) Relación entre el protocolo utilizado y la seguridad de la red
La versión del protocolo Wi-Fi (802.11) está muy ligada a la seguridad de la red, porque cada evolución del estándar fue corrigiendo vulnerabilidades y añadiendo mecanismos de cifrado más robustos. Vemos los siguientes:
- WEP (Wired Equivalent Privacy):
  - Uno de los primeros estándares de seguridad. Actualmente obsoleto, se descubrió que era muy inseguro (se rompe en minutos).
  - Protocolos compatibles: 802.11a, 802.11b, 802.11g.
- WPA (Wi-Fi Protected Access):
  - Introducido como una mejora temporal sobre WEP. utiliza TKIP (Temporal Key Integrity Protocol).
  - Protocolos compatibles: 802.11a, 802.11b, 802.11g, 802.11n.
- WPA2 (Wi-Fi Protected Access 2)
  - Utiliza AES (Advances Encryption Standard), mucho más seguro que sus predecesores. Se ha convertido en el estándar de seguridad predominante.
  - Protocolos compatibles: 802.11a, 802.11g, 802.11n, 802.11ac.
- WPA3 (Wi-Fi Protected Access 3)
  - Mejora la protección contra ataques de diccionario (offline dictionary attack) y ofrece un cifrado más fuerte. Introducido con Wi-Fi 6, pero compatible con versiones anteriores.
  - Protocolos compatibles: 802.11n, 802.11ac, 802.11ax.


## e) Investigación de los protocolos más recientes
|        | Wi-Fi 5         | Wi-Fi 6         | Wi-Fi 7         |
|----------------------|-----------------|-----------------|-----------------|
| Versión IEEE         |802.ac           |802.11ax         |802.11be         |
| Tasa de datos máxima |6,9 Gbps         |9,6 Gbps         |46 Gbps          |
| Banda(s)             |5 Ghz            |2,4 Ghz y 5 Ghz  |2,4 Ghz, 5 Ghz y 6 Ghz|
| Ancho de Banda       |20, 40, 80 y 160 [MHz]|20, 40, 80 y 160 [MHz]|20, 40, 80, 160 y 320 [MHz]|
| Modulación           |256-QAM          |1024-QAM         |4096-QAM         |
| Sistema de Seguridad |WPA2             |WPA3             |WPA3 (y mejoras futuras)|


# 3. Protocolos de comunicación inalámbrica
## a) Lista de algunos de los protocolos más comunes
| Protocolo | ¿Está estandarizado? Si/No | Si aplica: ¿Cuál(es) estándares? (si tiene varios mencionar la última versión) |
|-----------|-----------------------------|--------------------------------------------------------------------------------|
| Wi-Fi     |             Si           |IEEE 802.11        |
| Bluetooth |             Si           |IEEE 802.15.3      |
| ZigBee    |             Si           |IEEE 802.15.4      |
| NFC       |             Si           |ISO/IEC 18092      |
| LTE       |             Si           |3GPP Release 17    |
| GSM       |             Si           |3GPP TS 02.xx       |
| 5G (3GPP) |             Si           |3GPP Release 17 y 18 |
| LoRa      |             No           |                     |
| NB-IoT    |             Si           |3GPP Release 13 (mejoras en Release 17)|
| SigFox    |             No                |                                                                                |
| Z-Wave    |             Si                |  ITU-T G.9959 (desde 2019, antes propietario)  |

## b) Relación de algunos protocolos entre el alcance y su data rate
![grafico-distancia-data-rate](../img/distancia-datarate.png)

## c) Características de distintos medios de transmición
| Característica                | UTP | Fibra Óptica | Wi-Fi 802.11be | Bluetooth 5.4 | 5G |
|-------------------------------|-----|--------------|----------------|----------------|----|
| Ancho de banda                |100 [Mbps] - 10 [Gbps]|10 [Gbps] - 100 [Gbps]|Hasta 40 [Gbps]|2 [Mbps]|Hasta 10 [Gbps]|
| Distancias                    |~ 100 [m]|~ 80 [km]|~ 100 [m]|~ 50 [m]|~ 1 [km]|
| Inmunidad a EMI / RFI         |Baja|Alta|Baja|Media|Media|
| Costos de medios/conectores/dispositivos |Bajo|Medio|Medio|Bajo|Alto|
| ¿Disponible en Packet Tracer? |Si|No|Si|No|No|

