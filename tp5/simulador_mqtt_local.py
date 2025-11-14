"""
Simulador Local de MQTT - TP5
Simula comunicación Pub/Sub sin necesidad de broker externo
"""
import threading
import time
from collections import defaultdict
from datetime import datetime

class BrokerMQTTLocal:
    """Broker MQTT simulado en memoria"""
    
    def __init__(self):
        self.suscriptores = defaultdict(list)  # {topico: [callbacks]}
        self.mensajes_log = []
        self.lock = threading.Lock()
    
    def subscribe(self, topico, callback):
        """Suscribirse a un tópico"""
        with self.lock:
            self.suscriptores[topico].append(callback)
            timestamp = datetime.now().strftime("%H:%M:%S")
            log = f"[{timestamp}] 📢 Cliente suscrito a: {topico}"
            self.mensajes_log.append(log)
            print(log)
    
    def publish(self, topico, mensaje):
        """Publicar mensaje en un tópico"""
        with self.lock:
            timestamp = datetime.now().strftime("%H:%M:%S")
            log = f"[{timestamp}] 📤 Publicado en '{topico}': {mensaje}"
            self.mensajes_log.append(log)
            print(log)
            
            # Entregar mensaje a suscriptores
            if topico in self.suscriptores:
                for callback in self.suscriptores[topico]:
                    callback(topico, mensaje)
    
    def mostrar_log(self):
        """Mostrar historial de mensajes"""
        print("\n" + "="*60)
        print("HISTORIAL DE MENSAJES")
        print("="*60)
        for msg in self.mensajes_log:
            print(msg)
        print("="*60 + "\n")


# Crear broker local
broker = BrokerMQTTLocal()


class DispositivoA:
    """Dispositivo A - Publicador"""
    
    def __init__(self, broker):
        self.broker = broker
        self.nombre = "Dispositivo A"
    
    def publicar_estado(self):
        """Publica mensajes de estado"""
        print(f"\n🔹 {self.nombre} iniciado\n")
        
        for i in range(3):
            mensaje = f"Dispositivo A activo - Mensaje {i+1}"
            self.broker.publish("lan/deviceA/status", mensaje)
            time.sleep(2)
        
        print(f"\n🔹 {self.nombre} finalizó transmisión\n")


class DispositivoB:
    """Dispositivo B - Suscriptor"""
    
    def __init__(self, broker):
        self.broker = broker
        self.nombre = "Dispositivo B"
        self.mensajes_recibidos = []
    
    def conectar(self):
        """Suscribirse al tópico"""
        print(f"\n🔹 {self.nombre} iniciado\n")
        self.broker.subscribe("lan/deviceA/status", self.on_mensaje)
    
    def on_mensaje(self, topico, mensaje):
        """Callback cuando llega un mensaje"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.mensajes_recibidos.append((timestamp, topico, mensaje))
        print(f"[{timestamp}] 🔔 {self.nombre} recibió: '{mensaje}'")
    
    def mostrar_resumen(self):
        """Mostrar resumen de mensajes recibidos"""
        print(f"\n{'='*60}")
        print(f"RESUMEN - {self.nombre}")
        print(f"{'='*60}")
        print(f"Total de mensajes recibidos: {len(self.mensajes_recibidos)}")
        for ts, topico, msg in self.mensajes_recibidos:
            print(f"  [{ts}] {topico}: {msg}")
        print(f"{'='*60}\n")


def main():
    """Programa principal"""
    print("\n" + "="*60)
    print("SIMULACIÓN DE RED LOCAL MQTT")
    print("TP5 - Comunicación Pub/Sub")
    print("="*60 + "\n")
    
    # Crear dispositivos
    deviceA = DispositivoA(broker)
    deviceB = DispositivoB(broker)
    
    # Conectar Dispositivo B (suscriptor)
    deviceB.conectar()
    
    # Esperar un momento
    time.sleep(1)
    
    # Dispositivo A publica mensajes
    deviceA.publicar_estado()
    
    # Esperar a que se procesen todos los mensajes
    time.sleep(1)
    
    # Mostrar resúmenes
    deviceB.mostrar_resumen()
    broker.mostrar_log()
    
    print("✅ Simulación completada exitosamente\n")


if __name__ == "__main__":
    main()
