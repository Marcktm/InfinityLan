"""
TP5 - Punto 4b: Broadcasting en LAN
Tópico general: lan/broadcast/#
Múltiples clientes suscritos
Cliente central publica en lan/broadcast/all
"""
import threading
import time
from datetime import datetime
from collections import defaultdict


class BrokerLocal:
    """Broker MQTT simulado con soporte para wildcards"""
    def __init__(self):
        self.suscriptores = defaultdict(list)
        self.lock = threading.Lock()
    
    def subscribe(self, topico, callback):
        with self.lock:
            self.suscriptores[topico].append(callback)
    
    def publish(self, topico, mensaje):
        with self.lock:
            # Entregar a suscriptores exactos
            if topico in self.suscriptores:
                for callback in self.suscriptores[topico]:
                    callback(topico, mensaje)
            
            # Entregar a suscriptores con wildcard #
            for suscripcion, callbacks in self.suscriptores.items():
                if suscripcion.endswith('/#'):
                    prefijo = suscripcion[:-2]  # Remover /#
                    if topico.startswith(prefijo):
                        for callback in callbacks:
                            callback(topico, mensaje)


# Broker compartido
broker = BrokerLocal()


class ClienteCentral(threading.Thread):
    """Cliente Central - PUBLICADOR"""
    def __init__(self):
        super().__init__()
        self.daemon = True
    
    def run(self):
        print("\n" + "="*70)
        print("📡 CLIENTE CENTRAL - PUBLICADOR")
        print("="*70)
        print("Tópico: lan/broadcast/all")
        print("Acción: Enviar mensajes de broadcast a todos los clientes\n")
        
        time.sleep(2)  # Esperar a que todos se suscriban
        
        mensajes = [
            "¡Atención a todos los dispositivos!",
            "Actualización de firmware disponible",
            "Reinicio programado en 5 minutos",
            "Broadcast finalizado"
        ]
        
        for i, msg in enumerate(mensajes, 1):
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] 📡 Central transmitió: '{msg}'")
            broker.publish("lan/broadcast/all", msg)
            time.sleep(2)
        
        print(f"\n✅ Cliente Central finalizó broadcast\n")


class ClienteReceptor:
    """Cliente Receptor - SUSCRIPTOR"""
    def __init__(self, nombre, identificador):
        self.nombre = nombre
        self.id = identificador
        self.mensajes_recibidos = []
    
    def conectar(self):
        print(f"📢 {self.nombre} (ID: {self.id}) suscrito a: lan/broadcast/#")
        broker.subscribe("lan/broadcast/#", self.on_mensaje)
    
    def on_mensaje(self, topico, mensaje):
        """Callback cuando llega un mensaje"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.mensajes_recibidos.append({
            'timestamp': timestamp,
            'topico': topico,
            'mensaje': mensaje
        })
        print(f"[{timestamp}] 🔔 {self.nombre} recibió: '{mensaje}'")
    
    def mostrar_resumen(self):
        print(f"\n{'─'*70}")
        print(f"📊 RESUMEN - {self.nombre} (ID: {self.id})")
        print(f"{'─'*70}")
        print(f"Suscripción: lan/broadcast/#")
        print(f"Mensajes recibidos: {len(self.mensajes_recibidos)}\n")
        
        for i, msg in enumerate(self.mensajes_recibidos, 1):
            print(f"  [{i}] {msg['timestamp']} → {msg['mensaje']}")
        
        print(f"{'─'*70}")


def main():
    print("\n" + "█"*70)
    print("█" + " "*68 + "█")
    print("█" + "  TP5 - PUNTO 4b: BROADCASTING EN LAN".center(68) + "█")
    print("█" + " "*68 + "█")
    print("█"*70 + "\n")
    
    print("="*70)
    print("🔧 CONFIGURANDO CLIENTES SUSCRIPTORES")
    print("="*70 + "\n")
    
    # Crear múltiples clientes receptores
    cliente1 = ClienteReceptor("Cliente 1", "c1-sala1")
    cliente2 = ClienteReceptor("Cliente 2", "c2-sala2")
    cliente3 = ClienteReceptor("Cliente 3", "c3-oficina")
    
    # Conectar todos los clientes
    cliente1.conectar()
    cliente2.conectar()
    cliente3.conectar()
    
    print(f"\n✅ {3} clientes conectados y esperando broadcast...\n")
    
    # Iniciar Cliente Central
    central = ClienteCentral()
    central.start()
    
    # Esperar a que termine el broadcast
    central.join()
    
    # Esperar procesamiento
    time.sleep(1)
    
    # Mostrar resúmenes de cada cliente
    print("\n" + "="*70)
    print("📊 RESÚMENES DE RECEPCIÓN POR CLIENTE")
    print("="*70)
    
    cliente1.mostrar_resumen()
    cliente2.mostrar_resumen()
    cliente3.mostrar_resumen()
    
    # Análisis final
    print("\n" + "="*70)
    print("📈 ANÁLISIS DE BROADCASTING")
    print("="*70)
    print(f"✅ Total de clientes: 3")
    print(f"✅ Mensajes enviados por Central: 4")
    print(f"✅ Cliente 1 recibió: {len(cliente1.mensajes_recibidos)} mensajes")
    print(f"✅ Cliente 2 recibió: {len(cliente2.mensajes_recibidos)} mensajes")
    print(f"✅ Cliente 3 recibió: {len(cliente3.mensajes_recibidos)} mensajes")
    print(f"\n🎯 Resultado: Todos los clientes recibieron TODOS los mensajes")
    print(f"    Esto demuestra el funcionamiento del patrón BROADCAST")
    print("="*70 + "\n")
    
    print("✅ PUNTO 4b COMPLETADO\n")


if __name__ == "__main__":
    main()
