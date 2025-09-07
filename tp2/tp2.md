# INFORME TP1 - GRUPO InfinityLAN

### INTEGRANTES:

* Reyeros, Marcos Agustín
* Brezzo, Benjamin
* Castillo, Dario
---
## Consigna 1
![punto1](../tp2/img/conssigna1tp2.png)
---

---

### a) ¿Qué fenómeno físico se representa en la figura?

Se representa la **propagación de ondas electromagnéticas** desde un satélite hacia una embarcación en el océano. Lo que ocurre es que al comunicarse estos 2 medios a ciertas distancia y en movimiento produce lo que causa el llamado "Efecto dopler" cuando el satelita o barco se acercan en movimiento la frecuencia recibida se incrementa como se ve en la imagen y si se alejan la frecuencia disminuye. Esto afecta las comunicaciones satelitales donde el desplazamiento puede ser de algunos khz. Debido a esto los receptores deben ser capaz de poder ajustar dinamicamente la freciencia para mantener la misma señal

**Características principales de propagacion**

- No requiere medio físico, puede propagarse en el vacío.
- frecuencia y longitud de onda como parametros a analizar.
- Atenuación y dispersión. La señal puede debilitarse por distancia, clima o interferencias.

---

### b) ¿Qué tipos de transmisión afecta más este fenómeno? ¿Cuáles son más sensibles?

las transmisiones afectadas pueden ser:

- **Satelital :** Con nivel de sensibilidad alto al efecto dopler, el satelite se mueve rapido respecto al receptor, generando desvios de frecuencia significativos
- **Aeronautica, ADS-B y Radares:** con sensibilidad alta. Las velocidades involucradas son grandes, y el efecto dopler se para estimar la posicion y velocidad del avion.
- **Movil o terrestre 4G/5G:** con sensibilidad media al efecto, el usuario del dispositivo en movimiento genera variaciones de frecuencia que deben compensarse.
- **WI-FI y Bluetooth :**  con sensibilidad baja al efecto en distancias coras y velocidades bajas, el efecto es menor pero puede influir en entornos moviles
- **Cableada, fibraoptica o ethernet :** sensibilidad nula. No tiene propagacon por aire ni movimiento relativo.
---

###  c) ¿Por qué no se debe encender el celular en un avión? ¿Tiene relación con lo anterior?

El poner "modo avion" en los celulares es obligatorio en despegues y aterrizajes por razones tecnicas.

Ocurre lo que es la interferencia electromagnetica, debido a que los celulares transmiten señales en bandas similares a las usadas por los aviones VHF, radar, ILS. Como son muchos pasajeros activos pueden generar ruido o falsas alertas.

Los sistemas criticos durante despegue o aterrizaje, los pilotos dependen de la presicion de sus instrumentos, Una interderencia puede provocar errores en lectura de altitud, presion o aproximacion son visibilidad por clima. 

Por lo que los dispositivos moviles en movimiento cuado el celular intenta conectarse a torres terrestres a gran velocidad y altitud, se generan multiples intentos de conexion que satura las redes del avion, 

---

# punto 3 c)
inicializar wireshark en la interfaz activa WI-FI

# comando cmd : ipconfig

![punto3](../tp2/img/ipconfig.png)

# copiar la direccion ip
---

# filtrado por la direccion ip:

ip.addr == 192.168.1.61


![punto3](../tp2/img/filtadosinping.png)



# haciendo ping hacia una red externa para ver trafico a google

![punto3](../tp2/img/pinggoogle.png)

# ping localmente 

![punto3](../tp2/img/pinglocal.png)

# filtrado para ver ping al router local mediante comando icmp

![punto3](../tp2/img/visualizacionyfiltradodepingalrouter.png)

# visualizacion de un paquete 

## hexa:

![punto3](../tp2/img/hexa.png)

# datos del paquete:

![punto3](../tp2/img/datosdepaquete.png)

# analisis de datos paquete :

![punto3](../tp2/img/analisispaquete.png)



---

**Ethernet II**  
Es la capa de enlace. Muestra las direcciones MAC de origen y destino. En este caso,(`Tp-LinkT_7d:44:6f`) está enviando datos al router (`SichuanUnifi_f1:3e:40`).

**IPv4**  
Es la capa de red. Indica que el paquete va desde la IP local `192.168.0.103` hacia el gateway `192.168.0.1`. Usa el protocolo TCP.

**TCP (Transmission Control Protocol)**  
Es la capa de transporte. Este paquete tiene el flag **SYN**, lo que significa que está iniciando una conexión TCP. Es el primer paso del "handshake" que se usa para establecer comunicación confiable entre dos dispositivos.

**Puerto origen: 49270**  
Es un puerto dinámico asignado por tu sistema.

**Puerto destino: 80**  
Indica que el paquete va hacia un servidor web (HTTP).

**Número de secuencia: 0**  
Como es el primer paquete, comienza en cero.

**Tamaño de ventana: 64240**  
Define cuántos bytes puede recibir el dispositivo antes de enviar una confirmación.

**Opciones TCP**  
Incluye parámetros como MSS (tamaño máximo de segmento), SACK (reconocimiento selectivo), escalado de ventana y timestamps. Sirven para optimizar la conexión.

---

