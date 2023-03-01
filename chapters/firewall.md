# Firewalls
- [Firewalls](#firewalls)
  - [Definition](#definition)
  - [Erstellen einer einfachen Firewall in Python](#erstellen-einer-einfachen-firewall-in-python)
    - [Docker-Container mit Firewall verbinden](#docker-container-mit-firewall-verbinden)
    - [Traffic über Firewall-Container](#traffic-über-firewall-container)

<br>
<hr>
<br>

## Definition
Firewalls sind wichtig für die Sicherung von Netzwerken durch die Kontrolle des ein- und ausgehenden Datenverkehrs. Um eine einfache Firewall mit Python zu erstellen, können wir das Socket-Modul verwenden, um ein- und ausgehende Netzwerkpakete zu erfassen und sie anhand von vordefinierten Regeln zu filtern.

<br>

## Erstellen einer einfachen Firewall in Python
Hier ein Beispiel für Python-Code für eine einfache Firewall, mit der der eingehende Datenverkehr auf Port 80 blockiert werden kann:
```python
import socket

HOST = ''
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
```

Um diesen Python-Code zu dockerisieren, können wir ein Dockerfile mit folgendem Inhalt erstellen:
```Dockerfile
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "firewall.py"]
```

Dieses Dockerfile verwendet das offizielle Python 3.8-Image als Basis-Image, kopiert unseren Python-Code und die Anforderungsdatei in das Image, installiert die Anforderungen und führt dann unseren Python-Code aus, wenn der Container startet.

Um den Docker-Container zu erstellen und auszuführen, können wir die folgenden Befehle verwenden:
```command
docker build -t my-firewall .
docker run --name my-firewall-container -p 80:80 -d my-firewall
```
Der erste Befehl erstellt das Docker-Abbild und versieht es mit dem Namen "my-firewall". Der zweite Befehl führt einen Container mit diesem Image aus, bindet den Port 80 des Containers an den Port 80 des Host-Rechners und führt den Container im Detached-Modus aus.

Beachten Sie, dass dies ein einfaches Beispiel ist und eine echte Firewall viel mehr Regeln und Funktionen hat. Außerdem ist es wichtig zu bedenken, dass die Erstellung einer Firewall ein tiefes Verständnis von Netzwerken und Sicherheit erfordert, und dieser Code sollte nicht in einer Produktionsumgebung ohne umfangreiche Tests und Validierung verwendet werden.

<br>

### Docker-Container mit Firewall verbinden
Um Docker-Container mit der Firewall zu verbinden, können Sie ein Docker-Netzwerk erstellen und die Container mit diesem Netzwerk verbinden. Anschließend können Sie die Container so konfigurieren, dass sie die Firewall als Standard-Gateway verwenden.

Dazu ein Beispiel:

1. Ein Docker-Netzwerk erstellen:
```command
docker network create my-network
```
<br>

2. Starten des Firewall-Containers und Verbindung mit dem Netzwerk:
```command
docker run --name firewall --network my-network firewall-image
```

>(`firewall-image` durch den Namen des Firewall-Docker-Images ersetzen)

<br>

3. Starten der anderen Container und Verbindung mit demselben Netzwerk:
```command
docker run --name app1 --network my-network app1-image
docker run --name app2 --network my-network app2-image
```
>Ersetzen von `app1-image` und `app2-image` durch die Namen der Docker-Images der Anwendung.

<br>

4. Konfiguration der Container sodass sie die Firewall als Standard-Gateway verwenden:
```command
docker network connect --ip 172.18.0.2 my-network firewall
docker network connect --ip 172.18.0.3 my-network app1
docker network connect --ip 172.18.0.4 my-network app2
```

In diesem Beispiel haben wir den einzelnen Containern im `my-network`-Netzwerk IP-Adressen zugewiesen. Die IP-Adresse der Firewall ist `172.18.0.2`, und die IP-Adressen der Anwendungscontainer sind `172.18.0.3` und `172.18.0.4`. Diese Adressen müssen an die eigene Netzwerkkonfiguration angepasst werden.

Das Standard-Gateway jedes Containers wie folgt auf die IP-Adresse der Firewall einstellen:
```command
docker exec app1 route add default gw 172.18.0.2
docker exec app2 route add default gw 172.18.0.2
```
Dadurch wird der gesamte Netzwerkverkehr von den Anwendungscontainern durch den Firewall-Container geleitet. Der Firewall-Container kann dann den Verkehr analysieren und ihn auf der Grundlage Ihrer Firewall-Regeln entweder zulassen oder blockieren.

<br>

### Traffic über Firewall-Container
Um den Datenverkehr über die Firewall des Docker-Containers zu den mit ihm verbundenen Containern zu leiten, können Sie die Netzwerkfunktionen von Docker nutzen.

Hier ist ein Beispiel:

1. Erstellen eines Docker-Netzwerks:
```command
docker network create my-network
```
2. Starten des Firewall-Containers mit der Option `--network`, um ihn mit dem Netzwerk zu verbinden:
```command
docker run --name firewall --network my-network -d firewall-image
```
3. Starten des/der Anwendungscontainer(s) mit der Option `--network`, um ihn/sie mit dem Netzwerk zu verbinden:
```command
docker run --name app --network my-network -d app-image
```
4. Konfigurieren der Firewall sodass sie den Datenverkehr zwischen dem/den Anwendungscontainer(n) und der Außenwelt leitet:
```command
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination app:80
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

Dadurch wird der über Port 80 eingehende Datenverkehr an den App-Container im Docker-Netzwerk my-network umgeleitet und NAT auf den vom App-Container ausgehenden Datenverkehr nach außen angewendet.

Beachten Sie, dass die spezifischen iptables-Regeln, die Sie anwenden müssen, von den Anforderungen Ihrer Firewall-Anwendung abhängen.