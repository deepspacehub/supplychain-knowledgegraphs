# Load Balancer
![Load Balancer](./../../pictures/chapters/load_balancer_steampunk.png)
<hr>

- [Load Balancer](#load-balancer)
  - [Definition](#definition)
  - [Bau eines Load-Balancers in Python](#bau-eines-load-balancers-in-python)


<br>
<hr>
<br>

## Definition


<br>

## Bau eines Load-Balancers in Python
Um einen Load Balancer in Python zu erstellen, der in einem Docker-Container läuft, können Sie ein Python-Framework wie Flask oder Django verwenden, um einen Webserver zu erstellen, der auf eingehende Anfragen hört und sie auf der Grundlage eines Lastausgleichsalgorithmus auf Backend-Server verteilt. Im Folgenden wird beschrieben, wie Sie einen Load Balancer mit Flask implementieren können:

Erstellen Sie einen Flask-Webserver, der auf eingehende Anfragen an einem bestimmten Port wartet.

Definieren Sie einen Lastausgleichsalgorithmus, der die eingehenden Anfragen auf mehrere Backend-Server verteilt. Dies kann ein einfacher Round-Robin-Algorithmus oder ein ausgefeilterer Algorithmus sein, der die Serververfügbarkeit, Antwortzeiten oder andere Faktoren berücksichtigt.

Verbinden Sie den Load Balancer mit den Backend-Servern über HTTP-Anfragen. Sie können die `requests`-Bibliothek in Python verwenden, um HTTP-Anfragen an Backend-Server zu senden.

Konfigurieren Sie den Load Balancer so, dass er hohe Verkehrslasten und Failover-Szenarien bewältigen kann. Dies kann bedeuten, dass Sie die Anzahl der Backend-Server je nach Bedarf erhöhen oder verringern, den Zustand und die Leistung der Server überwachen und Serverausfälle ordnungsgemäß behandeln.

Erstellen Sie ein Docker-Image der Load-Balancer-Anwendung, und stellen Sie es in einem Docker-Container bereit.

Das folgende Codebeispiel zeigt, wie man einen einfachen Round-Robin-Load-Balancer mit Flask implementiert:

```python
from flask import Flask, request
import requests

app = Flask(__name__)

backend_servers = [
    "http://backend1:8080",
    "http://backend2:8080",
    "http://backend3:8080"
]

current_server_index = 0

@app.route('/')
def handle_request():
    global current_server_index
    backend_server = backend_servers[current_server_index]
    current_server_index = (current_server_index + 1) % len(backend_servers)
    response = requests.get(backend_server + request.path)
    return response.content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

In diesem Beispiel lauscht der Load Balancer auf eingehende Anfragen an Port 80 und verteilt sie an drei Backend-Server, die an Port 8080 laufen. Die Funktion `handle_request` implementiert einen einfachen Round-Robin-Algorithmus, der für jede eingehende Anforderung den nächsten Backend-Server in der Liste auswählt.

Um diesen Load Balancer in einem Docker-Container auszuführen, können Sie ein `Dockerfile` erstellen, das die erforderlichen Abhängigkeiten installiert und den Python-Code in den Container kopiert:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

Anschließend können Sie das Docker-Image erstellen und den Container mit den folgenden Befehlen ausführen:

```command
docker build -t my-load-balancer .
docker run -p 80:80 my-load-balancer
```

Dadurch wird der Load-Balancer-Container gestartet, der eingehende Anfragen an Port 80 abhört und sie an die Backend-Server verteilt.