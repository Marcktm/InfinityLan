# 3

## ESQUEMA TOPOLOGICO:


![ESQUEMATOPOLOGICO](img/topo.jpeg)



## ESQUEMA FISICO:


![ESQUEMATOPOLOGICO](img/fisico.jpeg)






## FONDO :


![ESQUEMATOPOLOGICO](img/background.jpeg)


## CONFIGURACION DE ROUTER AIRCRAF 
 ```
 enable
conf t
! Trunk hacia el switch
interface GigabitEthernet0/0/0
 no shutdown
!
interface GigabitEthernet0/0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0
 ip nat inside
 ip access-group BLOQ_TURISTA in
!
interface GigabitEthernet0/0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ip nat inside
!
interface GigabitEthernet0/0/0.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ip nat inside
!
interface GigabitEthernet0/0/0.40
 encapsulation dot1Q 40
 ip address 192.168.40.1 255.255.255.0
 ip nat inside
!
! Hacia ISP
interface GigabitEthernet0/0/1
 ip address 200.0.0.1 255.255.255.252
 ip nat outside
 no shutdown
!
! NAT PAT
ip access-list standard NAT_INSIDE
 permit 192.168.0.0 0.0.255.255
ip nat inside source list NAT_INSIDE interface GigabitEthernet0/0/1 overload
!
! Ruta por defecto
ip route 0.0.0.0 0.0.0.0 200.0.0.2
!
! DHCP (DNS = servidor 192.168.40.10)
ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp excluded-address 192.168.20.1 192.168.20.20
ip dhcp excluded-address 192.168.30.1 192.168.30.20
ip dhcp excluded-address 192.168.40.1 192.168.40.20

ip dhcp pool TURISTAS
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.40.10

ip dhcp pool BUSINESS
 network 192.168.20.0 255.255.255.0
 default-router 192.168.20.1
 dns-server 192.168.40.10

ip dhcp pool ADMIN
 network 192.168.30.0 255.255.255.0
 default-router 192.168.30.1
 dns-server 192.168.40.10

ip dhcp pool SERVIDORES
 network 192.168.40.0 255.255.255.0
 default-router 192.168.40.1
 dns-server 192.168.40.10
!
! ACL: Turista solo servidor local + DHCP/DNS/ICMP
ip access-list extended BLOQ_TURISTA
 10 permit udp 192.168.10.0 0.0.0.255 eq 68 any eq 67
 20 permit udp any eq 67 192.168.10.0 0.0.0.255 eq 68
 30 permit udp 192.168.10.0 0.0.0.255 host 192.168.40.10 eq 53
 31 permit tcp 192.168.10.0 0.0.0.255 host 192.168.40.10 eq 53
 40 permit icmp 192.168.10.0 0.0.0.255 host 192.168.10.1
 50 permit icmp 192.168.10.0 0.0.0.255 host 192.168.40.10
 60 permit tcp  192.168.10.0 0.0.0.255 host 192.168.40.10 eq 80
 61 permit tcp  192.168.10.0 0.0.0.255 host 192.168.40.10 eq 443
 70 deny   ip   192.168.10.0 0.0.0.255 any
 80 permit ip any any
end

 ```



## CONFIGURACION DE ROUTER ISP (PROVEDOR DE SERVICIOS DE INTERNET) 
 ```
enable
conf t
interface GigabitEthernet0/0/0
 ip address 200.0.0.2 255.255.255.252
 no shutdown
!
interface Loopback0
 ip address 8.8.8.8 255.255.255.255
!
ip route 192.168.0.0 255.255.0.0 200.0.0.1
end
 ```


## CONFIGURACION DE SWITCH
 ```
enable
conf t
vlan 10 name Turistas
vlan 20 name Business
vlan 30 name Admin
vlan 40 name Servidores

interface range fa0/1-3
 switchport mode access
 switchport access vlan 10
 spanning-tree portfast

interface range fa0/4-5
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast

interface fa0/6
 switchport mode access
 switchport access vlan 30
 spanning-tree portfast

interface fa0/7
 switchport mode access
 switchport access vlan 40
 spanning-tree portfast

interface fa0/8
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40
end
 ```
 En vlan nos debe aparecer las clases diferenciadas. 10 para turista, 20 para business y 30 para admin:
 ![ESQUEMATOPOLOGICO](img/vlan.PNG)

 ## CONFIGURACION DE SERVIDOR "ENTRETENIMIENTO":
 Configuramos como estatico la direccion ip4 mascara gateway y dns 
![ESQUEMATOPOLOGICO](img/SERVER.PNG)

Habilitar HTTP Y EN DNS cambiamos las url:
![ESQUEMATOPOLOGICO](img/url.PNG)

en index.html crear pagina. Por defecto viene la de packet tracer

![ESQUEMATOPOLOGICO](img/index.jpeg)

 ```
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Entretenimiento a bordo</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
    :root{--bg:#0c1222;--fg:#eaf0ff;--mut:#9fb0c8;--tur:#2e86ff;--biz:#00b894;--adm:#c56cf0;--card:#121a2c}
    *{box-sizing:border-box} body{margin:0;background:linear-gradient(#0b1328,#0e1530);color:var(--fg);font:16px/1.5 system-ui,Segoe UI,Roboto,Arial}
    header{padding:42px 16px;text-align:center}
    h1{margin:0;font-size:36px}
    .sub{color:var(--mut);margin-top:6px}
    .wrap{max-width:900px;margin:18px auto;padding:0 16px}
    .panel{display:none;background:linear-gradient(180deg,var(--card),#0f182a);border:1px solid #243353;border-radius:14px;padding:18px;box-shadow:0 10px 30px rgba(0,0,0,.25)}
    .badge{display:inline-block;padding:6px 10px;border-radius:999px;font-weight:700;letter-spacing:.4px;text-transform:uppercase;margin-bottom:10px}
    .tur .badge{background:color-mix(in srgb,var(--tur) 25%, #000);color:#cfe1ff;border:1px solid color-mix(in srgb,var(--tur) 60%, #000)}
    .biz .badge{background:color-mix(in srgb,var(--biz) 25%, #000);color:#d9fff3;border:1px solid color-mix(in srgb,var(--biz) 60%, #000)}
    .adm .badge{background:color-mix(in srgb,var(--adm) 25%, #000);color:#f3e3ff;border:1px solid color-mix(in srgb,var(--adm) 60%, #000)}
    h2{margin:4px 0 8px}
    ul{margin:8px 0 0 18px;color:var(--mut)}
    .active{display:block}
    .hint{margin-top:10px;color:#7f8aa6;font-size:13px}
  </style>
</head>
<body>
  <header>
    <h1>Entretenimiento a bordo</h1>
    <div class="sub">Contenido y conectividad según tu clase.</div>
  </header>

  <div class="wrap">
    <section id="turista" class="panel tur">
      <span class="badge">Clase Turista</span>
      <h2 style="color:var(--tur)">Plan Esencial</h2>
      <ul>
        <li>Películas y series en SD</li>
        <li>Música y podcasts</li>
        <li>Juegos básicos</li>
        <li>Acceso al portal local (Internet bloqueado por política)</li>
      </ul>
    </section>

    <section id="business" class="panel biz">
      <span class="badge">Clase Business</span>
      <h2 style="color:var(--biz)">Plan Premium</h2>
      <ul>
        <li>Películas y series en HD</li>
        <li>Wi‑Fi con prioridad de ancho de banda</li>
        <li>Videollamadas y trabajo online</li>
        <li>Acceso completo al portal y servidor local</li>
      </ul>
    </section>

    <section id="admin" class="panel adm">
      <span class="badge">Clase Admin</span>
      <h2 style="color:var(--adm)">Acceso Total</h2>
      <ul>
        <li>Todo el contenido (SD/HD/4K)</li>
        <li>Herramientas de monitoreo y diagnóstico</li>
        <li>Gestión de red y soporte</li>
        <li>Salida completa a Internet</li>
      </ul>
    </section>

    <p class="hint">Abrí: turista.vuelo, business.vuelo o admin.vuelo (o usa ?clase=turista|business|admin).</p>
  </div>

  <script>
    function getClase(){
      const q = new URLSearchParams(location.search).get('clase');
      if (q) return q.toLowerCase();
      const h = location.hostname.toLowerCase();
      if (h.includes('business')) return 'business';
      if (h.includes('admin')) return 'admin';
      return 'turista';
    }
    const clase = getClase();
    const id = {turista:'turista', business:'business', admin:'admin'}[clase] || 'turista';
    document.getElementById(id).classList.add('active');
    document.title = `Entretenimiento - ${id[0].toUpperCase()+id.slice(1)}`;
  </script>
</body>
</html>
 ```




 ## CONFIGURACION DE LAPTOPS TURISTA, BUSINESS Y ADMIN
![ESQUEMATOPOLOGICO](img/LAPTOPS.PNG)


 ## COMPROBACION DE PING TURISTA
![ESQUEMATOPOLOGICO](img/PINGT.JPEG)

 ## COMPROBACION DE PING BUSINESS
![ESQUEMATOPOLOGICO](img/PINGB.JPEG)


 ## COMPROBACION DE PING ADMIN
![ESQUEMATOPOLOGICO](img/PINGADMIN.JPEG)



 ## SIMULACION
![ESQUEMATOPOLOGICO](img/SIMULACION.JPEG)



 ## ACCESO A WEB DE LAS CLASES
![ESQUEMATOPOLOGICO](img/WEBCLASES.JPEG)

## CONCLUSION

- Se logró la segmentación por VLAN (Turista/Business/Admin/Servidor) y el enrutamiento VLAN con router.
- DHCP y DNS operativos; los clientes obtienen IP/GW correctos y resuelven los hostnames del portal.
NAT y ruta por defecto en AIRCRAF permiten salida a Internet; Business y Admin navegan, Turista queda bloqueado por ACL.
- El servidor de entretenimiento responde por HTTP y muestra la vista según la clase; las pruebas de ping/HTTP coinciden con la matriz del TP.
- La topología quedó clara, reproducible y escalable para agregar más redes o políticas.