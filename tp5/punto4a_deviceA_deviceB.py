"""
TP5 - Punto 4a: Comunicación Directa Dispositivo A → Dispositivo B
Dispositivo A publica en lan/deviceA/status
Dispositivo B se suscribe y muestra mensajes recibidos
"""
import threading
import time
from datetime import datetime
from collections import defaultdict


class BrokerLocal:
    """Broker MQTT simulado"""
    def __init__(self):
        self.suscriptores = defaultdict(list)
        self.lock = threading.Lock()
    
    def subscribe(self, topico, callback):
        with self.lock:
            self.suscriptores[topico].append(callback)
    
    def publish(self, topico, mensaje):
        with self.lock:
            if topico in self.suscriptores:
                for callback in self.suscriptores[topico]:
                    callback(topico, mensaje)


# Broker compartido
broker = BrokerLocal()


class DispositivoA(threading.Thread):
    """Dispositivo A - PUBLICADOR"""
    def __init__(self):
        super().__init__()
        self.daemon = True
    
    def run(self):
        print("\n" + "="*70)
        print("📤 DISPOSITIVO A - PUBLICADOR")
        print("="*70)
        print("Tópico: lan/deviceA/status")
        print("Acción: Publicar mensajes de estado\n")
        
        time.sleep(2)  # Esperar a que B se suscriba
        
        mensajes = [
            "Dispositivo A activo",
            "Temperatura: 25°C",
            "Batería: 85%",
            "Estado: Operativo"
        ]
        
        for i, msg in enumerate(mensajes, 1):
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] 📤 Dispositivo A publicó: '{msg}'")
            broker.publish("lan/deviceA/status", msg)
            time.sleep(1.5)
        
        print(f"\n✅ Dispositivo A finalizó transmisión\n")


class DispositivoB:
    """Dispositivo B - SUSCRIPTOR"""
    def __init__(self):
        self.mensajes_recibidos = []
    
    def conectar(self):
        print("\n" + "="*70)
        print("📢 DISPOSITIVO B - SUSCRIPTOR")
        print("="*70)
        print("Tópico suscrito: lan/deviceA/status")
        print("Acción: Esperando mensajes de Dispositivo A...\n")
        
        broker.subscribe("lan/deviceA/status", self.on_mensaje)
    
    def on_mensaje(self, topico, mensaje):
        """Callback cuando llega un mensaje"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.mensajes_recibidos.append({
            'timestamp': timestamp,
            'topico': topico,
            'mensaje': mensaje
        })
        print(f"[{timestamp}] 🔔 Dispositivo B recibió: '{mensaje}'")
    
    def mostrar_resumen(self):
        print("\n" + "="*70)
        print("📊 RESUMEN DE COMUNICACIÓN - DISPOSITIVO B")
        print("="*70)
        print(f"Total de mensajes recibidos: {len(self.mensajes_recibidos)}\n")
        
        for i, msg in enumerate(self.mensajes_recibidos, 1):
            print(f"  Mensaje {i}:")
            print(f"    ├─ Timestamp: {msg['timestamp']}")
            print(f"    ├─ Tópico: {msg['topico']}")
            print(f"    └─ Contenido: {msg['mensaje']}")
        
        print("="*70 + "\n")


def main():
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  TP5 - PUNTO 4a: COMUNICACIÓN DIRECTA A → B".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")
    
    # Crear Dispositivo B y suscribirlo
    deviceB = DispositivoB()
    deviceB.conectar()
    
    # Iniciar Dispositivo A en thread separado
    deviceA = DispositivoA()
    deviceA.start()
    
    # Esperar a que A termine
    deviceA.join()
    
    # Esperar un poco más para procesar mensajes
    time.sleep(1)
    
    # Mostrar resumen
    deviceB.mostrar_resumen()
    
    print("✅ PUNTO 4a COMPLETADO\n")


if __name__ == "__main__":
    main()
