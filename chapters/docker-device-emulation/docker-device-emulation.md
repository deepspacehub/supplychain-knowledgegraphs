# Docker Device-Emulation

- [Docker Device-Emulation](#docker-device-emulation)
  - [Dockerfiles](#dockerfiles)
    - [Dockerfile und Python-Beispielcode, der ein Gerät in einem lokalen Netzwerk emuliert](#dockerfile-und-python-beispielcode-der-ein-gerät-in-einem-lokalen-netzwerk-emuliert)
    - [Hinzufügen von drei Geräten zum Netzwerk inklusive Knowledge-Graph-Abbildung](#hinzufügen-von-drei-geräten-zum-netzwerk-inklusive-knowledge-graph-abbildung)
    - [Wie man Geräte über Docker zum Netzwerk hinzufügt:](#wie-man-geräte-über-docker-zum-netzwerk-hinzufügt)
    - [Beispiel-Dockerfile, das Sie ändern können, um Ihre Geräte in einem lokalen Netzwerk zu emulieren:](#beispiel-dockerfile-das-sie-ändern-können-um-ihre-geräte-in-einem-lokalen-netzwerk-zu-emulieren)
    - [Beispieldatei device.py:](#beispieldatei-devicepy)
    - [Sicherheitsmaßnahmen für device.py](#sicherheitsmaßnahmen-für-devicepy)
    - [Darstellung aller kommunizierenden Docker-Container im lokalen Netzwerk](#darstellung-aller-kommunizierenden-docker-container-im-lokalen-netzwerk)
    - [Mapping aller kommunizierenden Geräte auf Port 80 inklusive API-Abfrage](#mapping-aller-kommunizierenden-geräte-auf-port-80-inklusive-api-abfrage)


<br>
<hr>
<br>

## Dockerfiles
### Dockerfile und Python-Beispielcode, der ein Gerät in einem lokalen Netzwerk emuliert
Hier ein Beispiel für ein Dockerfile und Python-Code, das ein Gerät in einem lokalen Netzwerk emuliert:

Dockerfile:
```Dockerfile
FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY device.py .

CMD ["python", "device.py"]
```

requirements.txt
```text
Flask==2.1.0
```

device.py:
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Device emulation running.'

@app.route('/data')
def data():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

Dieses Dockerfile richtet eine Python-Umgebung ein, installiert Flask (ein leichtgewichtiges Web-Framework) und kopiert das Skript `device.py` in den Container. Das Skript erstellt einen Webserver, der auf Port 80 lauscht und auf Anfragen an den Endpunkt `/data` mit einer JSON-Nutzlast antwortet, die Statusinformationen enthält.

Um das Docker-Image zu erstellen, muss ein Verzeichnis mit den oben genannten Dateien erstellet folgenden Befehl in diesem Verzeichnis ausgeführt werden:
```console
docker build -t device-emulator .
```
Dadurch wird ein Docker-Image namens `device-emulator` erstellt, das mit dem folgenden Befehl ausgeführt werden kann:
```console
docker run -p 80:80 device-emulator
```

Dadurch wird der Container gestartet und Port 80 im Container auf Port 80 auf dem Host abgebildet, so dass Sie auf den Geräteemulator zugreifen können, indem Sie in einem Webbrowser auf dem Host zu `http://localhost/data` navigieren.

Beachten Sie, dass dieses Beispiel nur zu Demonstrationszwecken dient und keine Sicherheitsmaßnahmen enthält. In einem realen Szenario sollte ein Geräteemulator angemessene Sicherheitskontrollen enthalten, um unbefugten Zugriff zu verhindern und vor potenziellen Schwachstellen zu schützen.

<br>

### Hinzufügen von drei Geräten zum Netzwerk inklusive Knowledge-Graph-Abbildung
Hier ist ein Beispiel für Python-Code, der drei emulierte Geräte in einem Knowledge-Graphs unter Verwendung der `rdflib`-Bibliothek abbildet:
```python
from rdflib import Graph, Namespace, RDF, Literal
from rdflib.tools.rdf2dot import rdf2dot
import sys

# Define namespaces
SCHEMA = Namespace("http://schema.org/")
EXAMPLE = Namespace("http://example.com/")

# Create a new graph
g = Graph()

# Define devices
device1 = EXAMPLE['device1']
device2 = EXAMPLE['device2']
device3 = EXAMPLE['device3']

# Define device types
laptop = SCHEMA['Laptop']
server = SCHEMA['Server']
printer = SCHEMA['Printer']

# Add devices and types to the graph
g.add((device1, RDF.type, laptop))
g.add((device2, RDF.type, server))
g.add((device3, RDF.type, printer))

# Define properties
locatedIn = EXAMPLE['located']
hasIP = EXAMPLE['hasIP']
manufacturer = SCHEMA['manufacturer']
model = SCHEMA['model']

# Add properties to the graph
g.add((device1, locatedIn, Literal('Room A')))
g.add((device2, locatedIn, Literal('Room B')))
g.add((device3, locatedIn, Literal('Room C')))
g.add((device1, hasIP, Literal('192.168.1.1')))
g.add((device2, hasIP, Literal('192.168.1.2')))
g.add((device3, hasIP, Literal('192.168.1.3')))
g.add((device1, manufacturer, Literal('Dell')))
g.add((device2, manufacturer, Literal('HP')))
g.add((device3, manufacturer, Literal('Canon')))
g.add((device1, model, Literal('Latitude')))
g.add((device2, model, Literal('Proliant')))
g.add((device3, model, Literal('Pixma')))

# Set up security controls
g.add((EXAMPLE['network'], RDF.type, SCHEMA['Network']))
g.add((EXAMPLE['network'], SCHEMA['hasPart'], device1))
g.add((EXAMPLE['network'], SCHEMA['hasPart'], device2))
g.add((EXAMPLE['network'], SCHEMA['hasPart'], device3))
g.add((EXAMPLE['network'], EXAMPLE['hasFirewall'], EXAMPLE['firewall']))
g.add((EXAMPLE['firewall'], RDF.type, EXAMPLE['Firewall']))
g.add((EXAMPLE['firewall'], EXAMPLE['hasRule'], EXAMPLE['allow_incoming_tcp']))
g.add((EXAMPLE['allow_incoming_tcp'], RDF.type, EXAMPLE['Rule']))
g.add((EXAMPLE['allow_incoming_tcp'], EXAMPLE['protocol'], Literal('TCP')))
g.add((EXAMPLE['allow_incoming_tcp'], EXAMPLE['port'], Literal(80)))

# Print the graph
print(g.serialize(format='turtle'))
```

Dieser Code definiert drei Geräte (`device1`, `device2` und `device3`) mit ihren jeweiligen Typen (`laptop`, `server` und `printer`). Er definiert auch mehrere Eigenschaften für jedes Gerät, wie z. B. `locatedIn`, `hasIP`, `manufacturer` und `model`. Der Code fügt dann diese Geräte und Eigenschaften zu einem neuen RDF-Graphen hinzu und gibt den resultierenden Graphen im Turtle-Format aus.

Um die emulierten Geräte auf den Knowledge-Graphs abzubilden, müssten Sie den Code ändern, um Informationen von den Geräten abzurufen und sie dynamisch zum Graphen hinzuzufügen. Sie könnten zum Beispiel die `requests`-Bibliothek verwenden, um HTTP-Anforderungen an die emulierten Geräte zu senden und die Antworten zu analysieren, um relevante Informationen zu extrahieren. Auf diese Weise ließe sich eine umfassendere und aktuellere Darstellung des Netzwerks und seiner Geräte im Knowledge-Graphs erstellen.

```python
import io
import pydotplus
from IPython.display import display, Image
from rdflib.tools.rdf2dot import rdf2dot

def visualize(g):
    stream = io.StringIO()
    rdf2dot(g, stream, opts = {display})
    dg = pydotplus.graph_from_dot_data(stream.getvalue())
    png = dg.create_png()
    display(Image(png))

visualize(g)
```

Dieser Python-Code definiert eine Funktion namens `visualize()`, die einen RDFLib-Graph `g` als Eingabe nimmt und eine PNG-Bildvisualisierung des Graphen mit Graphviz und Pydotplus erzeugt.

Die Funktion beginnt mit dem Import der notwendigen Bibliotheken: `io`, `pydotplus`, `IPython.display` und `rdflib.tools.rdf2dot`.

Dann wird die Funktion `visualize()` definiert, die einen RDFLib-Graph `g` als Eingabe erhält. Innerhalb der Funktion wird ein StringIO-Objekt `stream` erstellt, das zur Erfassung der Ausgabe der Funktion `rdf2dot()` verwendet wird. Die Funktion `rdf2dot()` ist ein Werkzeug in der RDFLib, das einen RDF-Graphen in das DOT-Format von Graphviz konvertiert, das eine reine Textdarstellung eines Graphen ist. Die Funktion wird mit den Parametern `g`, `stream` und `opts` aufgerufen. Der Parameter `opts` ist ein Wörterbuch mit Optionen, die an den Graphviz-Befehl `dot` übergeben werden, wenn die DOT-Datei gerendert wird. In diesem Fall ist `opts` auf `{display}` gesetzt, was eine Abkürzung ist, um Graphviz anzuweisen, den Graphen mit einem Standardlayout zu rendern und auf dem Bildschirm anzuzeigen.

Als nächstes verwendet die Funktion Pydotplus, um ein Diagrammobjekt `dg` aus den in `stream` gespeicherten DOT-Daten zu erstellen. Die Funktion `graph_from_dot_data()` nimmt die DOT-Daten als Eingabe und gibt ein Pydotplus-Diagrammobjekt zurück.

Schließlich wird das Pydotplus-Grafikobjekt `dg` verwendet, um mit der Methode `create_png()` ein PNG-Bild png zu erstellen. Die PNG-Bilddaten werden dann im IPython-Notebook mit der Funktion `display()` aus der `IPython.display`-Bibliothek angezeigt.

Die Funktion wird mit `g` als Eingabe aufgerufen, um den RDFLib-Graphen zu visualisieren.

<br>

### Wie man Geräte über Docker zum Netzwerk hinzufügt:
1. Erstellen Sie ein Docker-Abbild für das Gerät, das Sie dem Netzwerk hinzufügen möchten.
2. Führen Sie das Docker-Abbild aus, um einen Docker-Container für jedes Gerät zu erstellen.
3. Weisen Sie jedem Container eine eindeutige IP-Adresse im gleichen Subnetz wie den anderen Geräten im Netzwerk zu.
4. Konfigurieren Sie die Container mit der entsprechenden Software und den Einstellungen, um das Verhalten der Geräte zu simulieren.

<br>

### Beispiel-Dockerfile, das Sie ändern können, um Ihre Geräte in einem lokalen Netzwerk zu emulieren:
```Dockerfile
FROM python:3.9

# Install any necessary dependencies
RUN pip install some-package

# Copy device file to container
COPY device1.py /app/device1.py
COPY device2.py /app/device2.py
COPY device3.py /app/device3.py

# Set the working directory to /app
WORKDIR /app

# Expose port for incoming traffic
EXPOSE 80

# Run devices
CMD ["python", "device1.py"]
CMD ["python", "device2.py"]
CMD ["python", "device3.py"]
```

Diese Dockerdatei setzt voraus, dass Sie Gerätedateien mit den Namen `device1.py`, `device2.py` und `device3.py` erstellt und alle erforderlichen Abhängigkeiten installiert haben, damit sie ordnungsgemäß funktionieren. Sobald Sie die Dockerdatei an Ihre Bedürfnisse angepasst haben, können Sie die Container mit Docker-Befehlen wie docker build und docker run erstellen und ausführen.

<br>

### Beispieldatei device.py:
```python
import socket

# Set up socket connection
HOST = '0.0.0.0'
PORT = 80
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

<br>

### Sicherheitsmaßnahmen für device.py
Um die Sicherheit des `device.py`-Codes zu verbessern, können Sie die folgenden Maßnahmen in Betracht ziehen:

Verwenden Sie HTTPS anstelle von HTTP: HTTPS verschlüsselt die Daten bei der Übertragung zwischen Client und Server, wodurch es für Angreifer schwieriger wird, die Daten abzufangen oder zu manipulieren. Sie können eine Bibliothek wie `ssl` in Python verwenden, um eine sichere Socket-Schicht für den Server einzurichten.

Eingabedaten säubern: Der aktuelle Code sendet alle Daten, die er vom Client erhält, blind zurück, was ihn anfällig für Injektionsangriffe machen kann. Sie können eine Eingabevalidierung und -sanitisierung hinzufügen, um zu verhindern, dass bösartige Eingaben verarbeitet werden. So können Sie beispielsweise überprüfen, ob die Eingabedaten einem bestimmten Format oder Schema entsprechen, und sie zurückweisen, wenn dies nicht der Fall ist.

Begrenzen Sie den Geltungsbereich des Servers: Indem Sie den Server an `0.0.0.0` binden, erlauben Sie ihm, alle Netzwerkschnittstellen abzuhören, auch die externen. Dies kann den Server für Angriffe aus dem Internet anfällig machen. Stattdessen können Sie den Server an eine bestimmte IP-Adresse binden, die nur über das lokale Netzwerk erreichbar ist.

Verwenden Sie eine Firewall: Eine Firewall kann dazu beitragen, dass nicht autorisierter Datenverkehr den Server nicht erreicht, wodurch die Angriffsfläche verringert wird. Sie können eine Firewall wie `iptables` verwenden, um den Zugriff auf den Server von bestimmten IP-Adressen oder Ports aus zu beschränken.

Verwenden Sie sichere Kodierungsverfahren: Sie können sichere Kodierungspraktiken verwenden, um das Risiko von Schwachstellen im Code zu verringern. So können Sie beispielsweise die Verwendung veralteter oder unsicherer Funktionen vermeiden, Benutzereingaben bereinigen und Ein- und Ausgaben validieren.

Hier ein Beispiel dafür, wie Sie den device.py-Code ändern können, um einige dieser Maßnahmen zu implementieren:

```python
import socket
import ssl

# Set up socket connection
HOST = '192.168.0.1'  # replace with actual IP address of the server
PORT = 443  # use HTTPS port
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')  # use a self-signed certificate or obtain one from a trusted authority

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn, context.wrap_socket(conn, server_side=True) as secure_conn:
        print('Connected by', addr)
        while True:
            data = secure_conn.recv(1024)
            if not data:
                break
            # sanitize and validate input data
            processed_data = process_data(data)
            secure_conn.sendall(processed_data)
```

Dieser Code bindet den Server an eine bestimmte IP-Adresse (`192.168.0.1`) und verwendet den HTTPS-Port (`443`). Außerdem verwendet er ein selbstsigniertes Zertifikat, um die HTTPS-Verschlüsselung zu aktivieren. Die Eingabedaten werden bereinigt und überprüft, bevor sie verarbeitet werden.

<br>

### Darstellung aller kommunizierenden Docker-Container im lokalen Netzwerk
Um alle kommunizierenden emulierten Docker-Geräte im lokalen Netzwerk zu finden und sie in einem Diagramm darzustellen, können Sie das Docker SDK für Python und die NetworkX-Bibliothek verwenden. Hier ist ein Beispielcode:

```python
import docker
import networkx as nx
import matplotlib.pyplot as plt

# Set up Docker client
client = docker.from_env()

# Get all containers
containers = client.containers.list()

# Create empty graph
G = nx.Graph()

# Iterate through containers
for container in containers:
    # Get container info
    container_info = container.attrs

    # Get container name and IP address
    container_name = container_info['Name'].lstrip('/')
    container_ip = container_info['NetworkSettings']['Networks']['bridge']['IPAddress']

    # Add container to graph
    G.add_node(container_name, ip=container_ip)

    # Iterate through container ports
    for port in container_info['NetworkSettings']['Ports']:
        # Get port number and protocol
        port_number = int(port.split('/')[0])
        protocol = port.split('/')[1]

        # Get host IP address and port
        if port_number in container_info['HostConfig']['PortBindings']:
            host_ip = container_info['NetworkSettings']['IPAddress']
            host_port = container_info['HostConfig']['PortBindings'][port][0]['HostPort']
            host_address = f"{host_ip}:{host_port}"
            G.add_node(host_address, ip=host_ip)
            G.add_edge(container_name, host_address, protocol=protocol, port=port_number)

# Draw graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='black', font_size=10, node_size=1000)
edge_labels = nx.get_edge_attributes(G, 'protocol')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.show()
```

Dieser Code verwendet das Docker SDK für Python, um Informationen über alle Container zu erhalten, die auf der lokalen Docker-Instanz laufen. Für jeden Container werden sein Name und seine IP-Adresse extrahiert und als Knoten zum NetworkX-Graphen hinzugefügt. Außerdem durchläuft er die Container-Ports, extrahiert die Portnummer, das Protokoll sowie die IP-Adresse und den Port des Hosts und fügt sie als Knoten und Kanten zum Graphen hinzu.

Schließlich zeichnet der Code den Graphen mit Hilfe des Spring-Layout-Algorithmus, wobei die Knotenbeschriftungen die Container- und Host-IP-Adressen und die Kantenbeschriftungen das verwendete Protokoll anzeigen.

<br>

### Mapping aller kommunizierenden Geräte auf Port 80 inklusive API-Abfrage
Hinweis: Der folgende Code ist nur für Lehrzwecke gedacht. Es ist wichtig, eine ordnungsgemäße Autorisierung einzuholen, bevor Sie Netzwerke scannen oder API-Anfragen an Geräte stellen.

Hier ist ein Beispiel für Python-Code, der alle kommunizierenden Geräte an Port 80 im lokalen Netzwerk findet, sie in einem Diagramm abbildet und eine API-Anfrage an Geräte sendet, die eine offene API haben:
```python
import socket
import requests
import networkx as nx
import matplotlib.pyplot as plt

# Set up socket connection
HOST = '0.0.0.0'
PORT = 80

# Set up graph
G = nx.Graph()

# Scan network for devices on port 80
for i in range(1, 255):
    ip = f'192.168.1.{i}'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex((ip, PORT))
        if result == 0:
            print(f'{ip}: {PORT} is open')
            G.add_node(ip)

# Send API requests to devices that have an open API
for node in G.nodes():
    try:
        response = requests.get(f'http://{node}/api')
        if response.status_code == 200:
            print(f'{node} API response: {response.json()}')
    except:
        pass

# Draw graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
```

Dieser Code durchsucht die IP-Adressen `192.168.1.1` bis `192.168.1.254` nach Geräten mit einem offenen Port 80. Für jedes gefundene Gerät fügt er einen Knoten zu einem networkx-Graphen hinzu. Anschließend wird eine API-Anfrage an jeden Knoten gesendet, der dem Diagramm hinzugefügt wurde, und die Antwort wird ausgedruckt, wenn der Statuscode 200 lautet. Abschließend wird der Graph mit Hilfe des Spring-Layout-Algorithmus in networkx gezeichnet und mit matplotlib angezeigt.