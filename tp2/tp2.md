






---

## Consigna 2
![punto2](../tp2/img/img-consig2.png)

### a) ¿Qué fenómeno físico se está representando en la Figura? ¿Cuáles son las características principales del mismo?

En la figura podemos ver el fenómeno de la interferencia electromagnética (también conocido como _ruido_). La interferencia es una señal eléctrica no deseada que se suma a la señal principal, y la podemos ver representada en la figura como una alteración en la propagación de la onda entre la torre y el smartphone. Los orígenes de las interferencias pueden ser internos (producidos por el propio sistema) o externas (provenientes de dispositivos ajenos) que es el caso de la figura, en ella podemos ver que un taladro mecánico produce la interferencia. 
Las principales características de la interferencia son:
- Superposición de ondas: La base de la interferencia es el principio de superposición, cuando dos o más ondas electromagnéticas coinciden en el espacio y tiempo, sus campos eléctricos y magnéticos se suman. Esto puede producir zonas de refuerzo (constructiva) o de cancelación (destructiva). En la práctica suele haber una combinación de ambas.
- La interferencia depende de la frecuencia de onda.
- Ondas con la misma frecuencia pueden interferir más fácilmente, por ejemplo dos routers en el mismo canal de 2.4 GHz.
- Puede ser constante en el tiempo si las fuentes son coherentes, como dos láseres con la misma frecuencia estable.
- O variable/aleatoria si las fuentes son incoherentes, como ruidos eléctricos.

### b) Recordando las bandas de transmisión vistas en el TP01, investigar: ¿A qué tipos de transmisión afecta este fenómeno? ¿Cuáles son más resilientes al mismo?

Las transmisiones que operan en bandas de alta frecuencia son las más vulnerables al ruido, ya que presentan una mayor sensibilidad frente a obstáculos físicos y condiciones atmosféricas. Por ejemplo, hoy en día es normal que los ISP ofrezcan routers con dos bandas de frecuencias Wi-Fi, una de 5 GHz la cuál tiene la ventaja de ser más rápida pero es muy susceptible a las interferencias y obstáculos físicos. Y la otra señal que ofrece está en una banda de frecuencia más baja (2.4 GHz) pero es más resistente a las interferencias. 

### c) ¿Qué es la SNR? ¿Tiene algo que ver con el concepto de BER que vimos en el TP01?

La SNR (_Signal-to-Noise Ratio_) es una medida que compara la potencia de la señal útil con respecto a la potencia del ruido presente en el mismo canal o medio de transmisión.
- Un mayor SNR significa una señal más fuerte en relación al ruido, lo que implica una mejor calidad en la transmición de la señal.
El BER (Bit-Error-Rate) es la tasa de error de bits, es decir, la proporción de bits transmitidos que se reciben de forma incorrecta debido a interferencias.
- A medida que disminuye el SNR el BER aumenta lo que significa que más bits se reciben de manera errónea.

## Consigna 3
### a) ¿Qué es el Ethernet? ¿Cuáles son sus características principales? ¿Cómo se conforma una trama de datos de Ethernet? ¿Qué diferencias hay entre Ethernet, Fast Ethernet y Gigabit Ethernet?
Ethernet es una tecnología de red de área local (LAN) que define como se transmiten los datos entre dispositivos dentro de una misma red cableada. 
**Características principales de Ethernet**
- Topología: Originalmente en bus, pero actualmente se usa en estrella (_switches_).
- Medio físico: Cables de par trenzado (UTP, STP), fibra óptica o coaxial.
- Método de acceso: Usa el protocolo CSMA/CD (_Carrier Sense Multiple Access with Collision Detection_) en redes half-duplex.
- Velocidades: Comenzó con 10Mbps, pero evolucionó a 100M bps (Fast Ethernet), 1 Gbps (Gigabit Ethernet), 10 Gbps e incluso más.
- Direcciones física: Cada dispositivo tiene una dirección MAC única (48 bits).

Una trama Ethernet es la unidad de transmisión. Sus campos principales son:

- Preamble (7 bytes) + Start Frame Delimiter (1 byte). Sincronización.
- Dirección MAC de destino (6 bytes). A quién va dirigido.
- Dirección MAC de origen (6 bytes). Quién envía.
- Tipo / Longitud (2 bytes), indica si es un tipo de protocolo (ej: IPv4, IPv6, ARP) o la longitud de datos.
- Datos (46 a 1500 bytes), carga útil (payload), lo que realmente se quiere transmitir.
- CRC / FCS (4 bytes): código de verificación para detectar errores.

### b) ¿Qué es un cable UTP? ¿Qué relación tiene la construcción de este cable con los conceptos vistos en el ítem 2) de este trabajo? ¿Qué diferencias hay entre un cable UTP "derecho" y uno "cruzado"?
UTP significa Unshielded Twisted Pair. Es el tipo de cable más usado en redes Ethernet. Está compuesto por 4 pares de hilos de cobre trenzados entre sí, sin recubrimiento metálico extra (de este viene el _unshielded_).
**Relación entre la construcción UTP y la interferencia**:
- Cada par transmite señales diferenciales (la señal va por un hilo y la inversa por el otro).
- Al trenzarlos, las interferencias externas afectan de manera similar a ambos hilos, y el receptos puede resetearlas. Esto se conoce como cancelación de ruido común o CMRR.
- Cada par tiene un número de giros diferentes por metro, para que no se acople demasiado la interferencia entre pares (crosstalk).
Por eso es que aunque no tengan blindaje metálico, los UTP pueden funcionar muy bien hasta altas frecuencias.
**Diferencias enrte cable UTP "derecho" y "cruzado"**
- Cable derecho:
  - Los pines de ambos extremos siguen el mismo orden de colores (por ejemplo T568B en ambos lados).
  - Se utiliza para conectar dispositivos diferentes: PC con switch, PC con router, switch con router.
- Cable cruzado:
  - Los pares de transmisión y recepción se invierten en un extremo.
  - Se usa para conectar dos dispositivos iguales entre sí, como dos switches por ejemplo.



