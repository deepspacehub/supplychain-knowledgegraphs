# Scanner
![Scanner](./../../pictures/chapters/scanner_steampunk.png)
<hr>

- [Scanner](#scanner)
  - [Definition](#definition)
  - [Erstellen eines einfachen Scanners](#erstellen-eines-einfachen-scanners)

<br>
<hr>
<br>

## Definition
Netzwerk-Scanner sind Tools, mit denen die mit einem Netzwerk verbundenen Geräte und Dienste identifiziert und abgebildet werden können. Sie können nach offenen Ports, Schwachstellen und anderen Schwachstellen suchen, die von Angreifern ausgenutzt werden können.

Netzwerkscanner können eine Gefahr für die Lieferkette darstellen, wenn sie von Angreifern eingesetzt werden, um anfällige Geräte im Netzwerk eines Partners der Lieferkette zu identifizieren. Angreifer können diese Schwachstellen nutzen, um sich unbefugt Zugang zum Netzwerk zu verschaffen, sensible Daten zu stehlen oder andere Angriffe auf die Lieferkette zu starten.

Wenn beispielsweise das Netzwerk eines Zulieferers kompromittiert wird, können Angreifer den Zugang nutzen, um geistiges Eigentum zu stehlen, sich Zugang zu vertraulichen Daten zu verschaffen oder die Produktion zu unterbrechen. Dies kann erhebliche Auswirkungen auf die Abläufe in der gesamten Lieferkette haben und zu Rufschädigung, finanziellen Verlusten und rechtlichen Verpflichtungen führen.

<br>

## Erstellen eines einfachen Scanners
Um ein Python-Skript zu erstellen, das das Netzwerk nach Sicherheitslücken durchsucht, können wir verschiedene Open-Source-Tools wie Nmap, OpenVAS und andere verwenden. Hier ist ein Beispielskript, das Nmap verwendet, um das Netzwerk nach offenen Ports und Diensten zu scannen:

```python
import nmap

# Set up Nmap scanner
scanner = nmap.PortScanner()

# Define target IP range
target = '192.168.1.1/24'

# Perform Nmap scan
scanner.scan(hosts=target, arguments='-sS -sV')

# Iterate over scanned hosts
for host in scanner.all_hosts():
    # Print host and open ports
    print(f'Host: {host}')
    for port in scanner[host]['tcp']:
        state = scanner[host]['tcp'][port]['state']
        service = scanner[host]['tcp'][port]['name']
        print(f'  Port {port} ({service}): {state}')
```

Dieses Skript verwendet die `nmap`-Bibliothek, um einen TCP SYN-Scan (`-sS`) und eine Erkennung der Dienstversion (`-sV`) auf allen Hosts im angegebenen IP-Bereich durchzuführen. Anschließend durchläuft es jeden gescannten Host und gibt die offenen Ports und die zugehörigen Dienste aus.

Um dieses Skript zu dockerisieren, können wir ein Dockerfile erstellen, das die erforderlichen Abhängigkeiten installiert und das Skript in den Container kopiert:

```Dockerfile
FROM python:3.9

RUN apt-get update && apt-get install -y nmap

COPY scanner.py .

CMD ["python", "scanner.py"]
```

Dieses Dockerfile startet mit dem offiziellen Python 3.9-Image, installiert das `nmap`-Paket mit `apt-get`, kopiert das Skript `scanner.py` in den Container und setzt den Standardbefehl zur Ausführung des Skripts mit Python.

Um den Docker-Container zu starten und das Netzwerk zu scannen, können wir den Befehl `docker run` verwenden:

```command
docker run --rm --net=host my-scanner
```

Dieser Befehl führt den Container mit dem `my-scanner`-Image aus, setzt den Netzwerkmodus auf `host`, damit der Container auf die Netzwerkschnittstellen des Hosts zugreifen kann, und entfernt den Container beim Beenden mit der Option `--rm`. Das Skript `scanner.py` wird dann das Netzwerk scannen und die Ergebnisse ausdrucken.