# 1. Protocolo MQTT

MQTT es un protocolo de comunicación ligero diseñado específicamente para dispositivos IoT y aplicaciones que requieren una transmisión eficiente de mensajes en redes con ancho de banda limitado. A diferencia de los modelos cliente-servidor tradicionales, MQTT utiliza un patrón Publish/Subscribe que permite comunicación desacoplada entre dispositivos.

---

##  Características del Protocolo MQTT

- **Protocolo Ligero:** Overhead mínimo (solo 8 bytes en la cabecera fija), ideal para dispositivos con recursos limitados.
- **Basado en TCP/IP:** Utiliza conexiones TCP para garantizar la entrega de mensajes.
- **Broker-Centric:** Todos los mensajes pasan por un broker central que actúa como intermediario entre publicadores y suscriptores.
- **Topicos Jerárquicos:** Los mensajes se organizan en temas usando separadores `/` (ej: `casa/salon/temperatura`, `auto/velocidad`).
- **Credentials Simples:** Soporta autenticación básica con usuario y contraseña.

---

##  Ventajas de MQTT

1. **Bajo Consumo de Ancho de Banda:** Ideal para redes con limitaciones (celular, IoT, satelital).
2. **Comunicación Asincrónica:** Publicadores y suscriptores no necesitan estar conectados simultáneamente.
3. **Escalabilidad:** Un broker puede manejar miles de clientes sin problemas.
4. **Desacoplamiento:** Los publicadores no necesitan conocer a los suscriptores y viceversa.
5. **Bajo Acoplamiento Temporal:** Perfecto para sistemas distribuidos y dispositivos móviles.

---

##  Desventajas de MQTT

1. **Dependencia del Broker:** Si el broker cae, la comunicación se interrumpe.
2. **Seguridad Limitada:** La autenticación básica requiere capas adicionales (TLS/SSL) para producción.
3. **No es Compatible con HTTP:** Requiere clientes y servidores específicos para MQTT.
4. **Complejidad en Sistemas Grandes:** Configurar clustering y alta disponibilidad requiere soluciones avanzadas.

---

## El Patrón Publish/Subscribe (Pub/Sub)
El patrón Pub/Sub es un modelo de comunicación basado en **eventos** donde:

- **Publicadores:** Envían mensajes a un tema específico sin saber quién los recibe.
- **Suscriptores:** Se registran en temas de interés y reciben automáticamente los mensajes publicados.
- **Broker:** Actúa como intermediario, almacenando temas y enrutando mensajes.

###  Diferencia con Modelo Cliente-Servidor Tradicional

| Aspecto | Modelo Cliente-Servidor | Modelo Pub/Sub |
|--------|------------------------|-----------------|
| **Acoplamiento** | Fuerte (cliente conoce servidor) | Débil (desacoplado) |
| **Comunicación** | Sincrónica  | Asincrónica |
| **Escalabilidad** | Uno-a-Uno | Muchos-a-Muchos |
| **Intermediario** | No (contacto directo) | Sí (broker obligatorio) |
| **Flexibilidad** | Baja | Alta |

---

# 2. Desplego de un broker MQTT

Trabajaremos con HiveMQ Cloud, ya que se puede trabajar en la nube sin instalar nada. Ingresamos a: https://www.hivemq.cloud/


Creación de cuenta, y luego creación del cruster:

---
![](img/newcluster.png)

---

 ![](img/hivemq.png)

---

![](img/infocluster.png)

---

# 3.
---
 ```
cd "c:\Users\dario\OneDrive\Desktop\comDatosTP\tp5"
python simulador_mqtt_local.py
 ```
---
![](img/conexionlocal.png)

---


# 4.

### a)
 ```
cd "c:\Users\dario\OneDrive\Desktop\comDatosTP\tp5"
python punto4a_deviceA_deviceB.py
 ```
---
![](img/5a1.png)
![](img/5a2.png)

---

### b)

 ```
python punto4b_broadcasting.py
 ```
---
![](img/5b1.png)
![](img/5b2.png)
![](img/5b3.png)
--
# 5.
Para realizar esta consignas (y las anidadas) se desarrolló un programa en Python que se puede encontrar en este repositorio bajo el nombre de:

 ```
python punto5_sensores_jerarquia.py   
 ```
 ---

El objetivo es simular una red local con varios clientes (sensores) comunicándose mediante el protocolo **MQTT**, organizados en
una jerarquía de tópicos que represente distintas salas y tipos de sensores.

Cada sensor se comporta como un cliente publicador, enviando sus datos a un broker local simulado, mientras que una gateway central actúa como suscriptor y recolector de datos.
Posteriormente, se incorporó la funcionalidad de broadcast de comandos, para iniciar y detener remotamente los sensores, y una captura simbólica de los paquetes MQTT para su análisis.

### a) Simulación de sensores con generación de datos aleatorios
Se crearon tres instancias de la clase `Sensor`, cada una asociada a un tópico diferente dentro de la jerarquía:

```
lan/sala1/sensor/temp
lan/sala1/sensor/hum
lan/sala2/sensor/temp
```
Cada sensor ejecuta un hilo independiente (`threading.Thread`) que, cada 500 ms, genera una lectura aleatoria mediante `random.uniform(min_val, max_val)`.

Ejemplo de configuración:
```
sensor1 = Sensor(
    nombre="Sensor Temp Sala 1",
    topico="lan/sala1/sensor/temp",
    tipo="temperatura",
    min_val=18.0,
    max_val=28.0,
    unidad="°C"
)
```

Cada lectura se envía al broker mediante:
```
broker.publish(self.topico, mensaje)
```

El broker simulado (`BrokerLocal`) se encarga de distribuir el mensaje a todos los clientes suscritos.

Resultado de ejecución:

![](img/c1.png)
![](img/c2.png)
![](img/c3.png)
![](img/c4.png)
![](img/c5.png)


---

### b) Gateway Central – Recolección y almacenamiento de datos

Ahora nuestro cliente “central” (gateway) se suscribirá y recopilará los datos generados por los sensores en archivos locales (texto, CSV, serializado o base de datos).

La clase `GatewayCental` representa al cliente central del sistema. Al conectarse, se suscribe al tópico `"lan/#"` utilizando:
```
broker.subscribe("lan/#", self.on_mensaje)
```

Cada mensaje recibido se almacena en un diccionario `defaultdict(list)` con la siguiente estructura:
```
self.datos[topico].append({
    'timestamp': timestamp,
    'valor': mensaje
})
```

Al finalizar la simulación, los datos se exportan a archivos CSV mediante el método `guardar_datos()`:
```
with open(ruta_completa, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Valor'])
    ...
```

Cada tópico genera su propio archivo, por ejemplo:

```
datos_sensores/lan_sala1_sensor_temp.csv
datos_sensores/lan_sala2_sensor_temp.csv
```

Al concluir la ejecución, se muestran estadísticas con el número de lecturas y los valores mínimo, máximo y promedio por sensor.
Los archivos CSV generados pueden abrirse en Excel o cualquier editor de texto.

### d) Broadcast de comandos (start / stop)

Mediante broadcasting deberemos poder enviar al menos dos mensajes de comando a los clientes (ahora sensores): comenzar la simulación de datos y apagarse.

Se agregó un tópico especial de control llamado `"lan/comandos"`, al cual se suscriben todos los sensores:

```
broker.subscribe("lan/comandos", self.on_comando)
```

Cada sensor implementa el método `on_comando()` que interpreta los mensajes `"start"` y `"stop"`:
```
def on_comando(self, topico, mensaje):
    if mensaje.lower() == "start":
        self.activo = True
    elif mensaje.lower() == "stop":
        self.activo = False
```

El Gateway Cental puede enviar estos comandos a todos los sensores mediante:
```
def enviar_comandos(self, comando):
    broker.publish("lan/comandos", comando)
```
Los sensores comienzan a generar datos al recibir el comando start y detienen sus lecturas con stop, sin necesidad de finalizar el programa.

### e) Captura y análisis de un paquete (sniffer simulado)

Como se trata de un entorno de simulación sin comunicación TCP/IP real, se implementó una captura simbólica dentro del método `publish()` de la clase `BrokerLocal`.
Cada vez que se publica un mensaje, el broker imprime la estructura básica de un paquete MQTT:
```
paquete_simulado = {
    "Tipo": "PUBLISH",
    "Topic": topico,
    "Payload": mensaje,
    "QoS": 0,
    "Retain": False,
    "Longitud_payload": len(mensaje)
}
```

Salida de consola:
```
📦 [CAPTURA SIMULADA MQTT]
   ├─ Tipo: PUBLISH
   ├─ Tópico: lan/sala1/sensor/temp
   ├─ Payload: 24.3°C
   ├─ QoS: 0
   └─ Longitud: 6 bytes
```
Un paquete MQTT PUBLISH real contiene las siguientes secciones:

1. Fixed Header:
- Tipo de mensaje: PUBLISH (0x30)
- Flags y longitud variable del mensaje.

2. Variable Header:
- Nombre del tópico (lan/sala1/sensor/temp).
- Identificador del mensaje (si QoS > 0).

3. Payload:
- Contiene el dato publicado (por ejemplo "24.3°C").

Aunque en esta simulación no se utiliza una pila TCP/IP real, el formato presentado reproduce fielmente la estructura lógica de un paquete MQTT que circularía por la red.


## Preguntas

### a) ¿Sobre qué protocolos de capa de transporte están trabajando en esta actividad?

En esta actividad se utiliza principalmente el protocolo TCP en la capa de transporte, ya que MQTT funciona sobre TCP para garantizar la entrega ordenada y confiable de los mensajes entre clientes y el broker.

### b) ¿Qué pueden decir sobre la garantía de Integridad, Confidencialidad y Disponibilidad en esta arquitectura?

Integridad: TCP y MQTT aseguran que los mensajes lleguen completos y sin alteraciones, pero no protegen contra modificaciones maliciosas si no se usa cifrado.
Confidencialidad: Por defecto, los mensajes MQTT no están cifrados; para garantizar confidencialidad se debe usar TLS/SSL.
Disponibilidad: Depende de la estabilidad del broker y la red. Si el broker central falla, la comunicación se interrumpe.

### c) ¿Qué rol juegan los niveles de QoS en la fiabilidad de los mensajes?
Los niveles de QoS (Quality of Service) en MQTT determinan la garantía de entrega:

QoS 0: Entrega “al menos una vez”, sin confirmación.
QoS 1: Entrega “al menos una vez”, con confirmación.
QoS 2: Entrega “exactamente una vez”, con doble confirmación.
Esto permite ajustar la fiabilidad según la importancia del mensaje.

### d) ¿Qué ventajas ofrece el modelo pub/sub frente al modelo cliente-servidor?

Desacopla emisores y receptores (no necesitan conocerse).
Permite escalabilidad y flexibilidad.
Facilita la comunicación de muchos a muchos.
Reduce la carga en los clientes, centralizando la gestión en el broker.

### e) ¿Qué limitaciones tiene MQTT respecto a una red LAN real?

Depende de un broker central, lo que puede ser un punto único de fallo.
No está diseñado para transmisión de grandes volúmenes de datos.
Puede tener latencia adicional por el paso por el broker.
Requiere configuración y mantenimiento del broker.

### f) ¿Qué implicaciones tiene depender de un broker central para la comunicación?

Si el broker falla, toda la comunicación se detiene.
Puede ser un objetivo de ataques o sobrecarga.
Es necesario asegurar alta disponibilidad y respaldo del broker.
Centraliza la gestión y control de los mensajes, lo que puede ser ventajoso para monitoreo, pero riesgoso si no se gestiona bien.
