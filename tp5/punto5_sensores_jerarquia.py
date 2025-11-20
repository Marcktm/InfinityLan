"""
TP5 - Punto 5: Jerarquía de Tópicos con Sensores
Implementa:
  lan/sala1/sensor/temp
  lan/sala1/sensor/hum
  lan/sala2/sensor/temp

5a) Sensores generan datos aleatorios cada 500ms y publican en sus tópicos
5b) Cliente "central" (gateway) se suscribe y recopila datos en archivos locales
5c) Mediante broadvasting enviar al menos dos mensajes de comando a los clientes: comenzar la simulación de datos y apagarse
5d) Capturar un paquete usando un sniffer y realizar un análisis simple
"""
import threading
import time
import random
from datetime import datetime
from collections import defaultdict
import csv
import os


class BrokerLocal:
    """Broker MQTT simulado con soporte para wildcards"""
    def __init__(self):
        self.suscriptores = defaultdict(list)
        self.lock = threading.Lock()
    
    def subscribe(self, topico, callback):
        with self.lock:
            self.suscriptores[topico].append(callback)
            print(f"✅ Suscripción registrada: {topico}")
    
    def publish(self, topico, mensaje):
        with self.lock:
            # --- SIMULACIÓN DE CAPTURA DE PAQUETE MQTT (consiga e) ---
            paquete_simulado = {
                "Tipo": "PUBLISH",
                "Topic": topico,
                "Payload": mensaje,
                "QoS": 0,
                "Retain": False,
                "Longitud_payload": len(mensaje)
            }
            # Cada vez que un sensor publique un dato o el gateway envíe un comando, se imprimirá...
            print(f"\n📦 [CAPTURA SIMULADA MQTT]")
            print(f"   ├─ Tipo: {paquete_simulado['Tipo']}")
            print(f"   ├─ Tópico: {paquete_simulado['Topic']}")
            print(f"   ├─ Payload: {paquete_simulado['Payload']}")
            print(f"   ├─ QoS: {paquete_simulado['QoS']}")
            print(f"   └─ Longitud: {paquete_simulado['Longitud_payload']} bytes\n")
            # ----------------------------------------------
            # Entregar a suscriptores exactos
            if topico in self.suscriptores:
                for callback in self.suscriptores[topico]:
                    callback(topico, mensaje)
            
            # Entregar a suscriptores con wildcard #
            for suscripcion, callbacks in self.suscriptores.items():
                if suscripcion.endswith('/#'):
                    prefijo = suscripcion[:-2]
                    if topico.startswith(prefijo):
                        for callback in callbacks:
                            callback(topico, mensaje)
                
                # Wildcard + (un nivel)
                elif '+' in suscripcion:
                    partes_suscripcion = suscripcion.split('/')
                    partes_topico = topico.split('/')
                    
                    if len(partes_suscripcion) == len(partes_topico):
                        match = True
                        for s, t in zip(partes_suscripcion, partes_topico):
                            if s != '+' and s != t:
                                match = False
                                break
                        
                        if match:
                            for callback in callbacks:
                                callback(topico, mensaje)


# Broker compartido
broker = BrokerLocal()


class Sensor(threading.Thread):
    """Sensor que genera lecturas aleatorias"""
    def __init__(self, nombre, topico, tipo, min_val, max_val, unidad):
        super().__init__()
        self.nombre = nombre
        self.topico = topico
        self.tipo = tipo
        self.min_val = min_val
        self.max_val = max_val
        self.unidad = unidad
        self.activo = True
        self.daemon = True
        self.lecturas_enviadas = 0
        broker.subscribe("lan/comandos", self.on_comando)

    
    def generar_lectura(self):
        """Genera una lectura aleatoria"""
        valor = round(random.uniform(self.min_val, self.max_val), 2)
        return valor
    
    def run(self):
        print(f"🌡️  {self.nombre} iniciado → Publicando en: {self.topico}")
        
        while True:
            if self.activo:
                lectura = self.generar_lectura()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            
                mensaje = f"{lectura}{self.unidad}"
                broker.publish(self.topico, mensaje)
                self.lecturas_enviadas += 1    
                print(f"[{timestamp}] 📊 {self.nombre}: {mensaje}")
            time.sleep(0.5)  # 500ms
    
    def detener(self):
        self.activo = False
    
    # Función que maneja los mensajes de comandos (punto d)
    def on_comando(self, topico, mensaje):
        if mensaje.lower() == "start":
            if not self.activo:
                print(f"▶️  {self.nombre} recibió START → activando")
                self.activo = True
        elif mensaje.lower() == "stop":
            if self.activo:
                print(f"⏹️  {self.nombre} recibió STOP → deteniendo")
                self.activo = False
                

class GatewayCentral:
    """Cliente Central que recopila y almacena datos de sensores"""
    def __init__(self):
        self.datos = defaultdict(list)
        self.lock = threading.Lock()
        self.carpeta_datos = "datos_sensores"
        
        # Crear carpeta si no existe
        if not os.path.exists(self.carpeta_datos):
            os.makedirs(self.carpeta_datos)
            print(f"📁 Carpeta creada: {self.carpeta_datos}/\n")
    
    def conectar(self):
        """Suscribirse a todos los sensores"""
        print("="*70)
        print("🌐 GATEWAY CENTRAL - RECOLECTOR DE DATOS")
        print("="*70)
        
        # Suscribirse a todos los sensores con wildcard
        broker.subscribe("lan/#", self.on_mensaje)
        
        print("\n✅ Gateway suscrito a: lan/#")
        print("   Esto captura TODOS los sensores de TODAS las salas\n")
    
    def on_mensaje(self, topico, mensaje):
        """Callback cuando llega un mensaje de sensor"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        with self.lock:
            self.datos[topico].append({
                'timestamp': timestamp,
                'valor': mensaje
            })
    
    def guardar_datos(self):
        """Guardar datos en archivos CSV"""
        print("\n" + "="*70)
        print("💾 GUARDANDO DATOS EN ARCHIVOS")
        print("="*70 + "\n")
        
        with self.lock:
            for topico, lecturas in self.datos.items():
                # Crear nombre de archivo basado en el tópico
                nombre_archivo = topico.replace('/', '_') + '.csv'
                ruta_completa = os.path.join(self.carpeta_datos, nombre_archivo)
                
                # Guardar en CSV
                with open(ruta_completa, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Timestamp', 'Valor'])
                    
                    for lectura in lecturas:
                        writer.writerow([lectura['timestamp'], lectura['valor']])
                
                print(f"✅ {nombre_archivo} → {len(lecturas)} lecturas guardadas")
        
        print(f"\n📂 Archivos guardados en: ./{self.carpeta_datos}/\n")
    
    def mostrar_resumen(self):
        """Mostrar resumen de datos recopilados"""
        print("="*70)
        print("📊 RESUMEN DE DATOS RECOPILADOS")
        print("="*70 + "\n")
        
        with self.lock:
            total_lecturas = 0
            for topico, lecturas in sorted(self.datos.items()):
                print(f"📍 {topico}")
                print(f"   ├─ Total de lecturas: {len(lecturas)}")
                
                if lecturas:
                    # Extraer valores numéricos
                    valores = []
                    for l in lecturas:
                        try:
                            val_str = l['valor'].rstrip('°C%')
                            valores.append(float(val_str))
                        except:
                            pass
                    
                    if valores:
                        print(f"   ├─ Valor mínimo: {min(valores)}")
                        print(f"   ├─ Valor máximo: {max(valores)}")
                        print(f"   └─ Promedio: {sum(valores)/len(valores):.2f}")
                
                print()
                total_lecturas += len(lecturas)
            
            print(f"🎯 Total de lecturas recopiladas: {total_lecturas}")
        
        print("="*70 + "\n")

    ## Función para enviar los comandos (consigna d)
    def enviar_comandos(self, comando):
        print(f"\n📢 Enviando comando BROADCAST: '{comando}'\n")
        broker.publish("lan/comandos", comando)


def main():
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  TP5 - PUNTO 5: JERARQUÍA DE TÓPICOS CON SENSORES".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")
    
    # Crear Gateway Central
    gateway = GatewayCentral()
    gateway.conectar()
    
    time.sleep(1)
    
    print("="*70)
    print("🌡️  INICIANDO SENSORES")
    print("="*70 + "\n")
    
    # Crear sensores según la jerarquía
    sensor1 = Sensor(
        nombre="Sensor Temp Sala 1",
        topico="lan/sala1/sensor/temp",
        tipo="temperatura",
        min_val=18.0,
        max_val=28.0,
        unidad="°C"
    )
    
    sensor2 = Sensor(
        nombre="Sensor Hum Sala 1",
        topico="lan/sala1/sensor/hum",
        tipo="humedad",
        min_val=40.0,
        max_val=70.0,
        unidad="%"
    )
    
    sensor3 = Sensor(
        nombre="Sensor Temp Sala 2",
        topico="lan/sala2/sensor/temp",
        tipo="temperatura",
        min_val=19.0,
        max_val=26.0,
        unidad="°C"
    )
    
    # Iniciar sensores
    sensores = [sensor1, sensor2, sensor3]
    for sensor in sensores:
        sensor.start()
    
    print("\n✅ 3 sensores activos generando datos cada 500ms\n")
    print("="*70)
    print("📡 TRANSMISIÓN DE DATOS EN TIEMPO REAL")
    print("="*70 + "\n")
    
    gateway.enviar_comandos("start") 
    
    # Dejar correr por 10 segundos (20 lecturas por sensor)
    try:
        time.sleep(10)
    except KeyboardInterrupt:
        print("\n⚠️  Deteniendo sensores...\n")
    
    # Detener sensores
    # for sensor in sensores:
    #    sensor.detener()
    
     # --- 🔴 Fin de simulación mediante BROADCAST ---
    gateway.enviar_comandos("stop")
    print("\n⏹️  Simulación detenida\n")
    time.sleep(1) # Damos tiempo para que todos los hilos terminen de procesar
    
    # Guardar datos y mostrar resumen
    gateway.guardar_datos()
    gateway.mostrar_resumen()
    
    print("="*70)
    print("📈 ESTADÍSTICAS DE SENSORES")
    print("="*70)
    for sensor in sensores:
        print(f"  • {sensor.nombre}: {sensor.lecturas_enviadas} lecturas enviadas")
    print("="*70 + "\n")
    
    ## 5. a)
    #print("✅ PUNTO 5a COMPLETADO\n")
    #print("💡 Los datos fueron guardados en archivos CSV para análisis posterior")
    #print("   Puedes abrirlos con Excel o cualquier editor de texto\n")

    ## 5. d)
    print("✅ PUNTO 5d COMPLETADO\n")
    print("💡 Los sensores fueron controlados mediante comandos broadcast (start/stop)")
    print("   y los datos se guardaron en archivos CSV para análisis posterior\n")

if __name__ == "__main__":
    main()
