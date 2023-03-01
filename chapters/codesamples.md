# Codebeispiele
- [Codebeispiele](#codebeispiele)
  - [Security](#security)
    - [Codebespiele für einen Knowledge-Graph Security Ansatz](#codebespiele-für-einen-knowledge-graph-security-ansatz)
  - [Prognose](#prognose)
    - [Wie kann der Knowledge-Graph zur Entwicklung von Prognosemodellen verwendet werden kann, die den Managern der Versorgungskette dabei helfen, potenzielle Risiken zu antizipieren und abzumildern, bevor sie zu großen Problemen werden?](#wie-kann-der-knowledge-graph-zur-entwicklung-von-prognosemodellen-verwendet-werden-kann-die-den-managern-der-versorgungskette-dabei-helfen-potenzielle-risiken-zu-antizipieren-und-abzumildern-bevor-sie-zu-großen-problemen-werden)
    - [Wie können Knowledge-Graphs verwendet werden, um Angriffe auf ein Netz zu erkennen oder vorherzusagen und Geräte in einem Netz unter Quarantäne zu stellen?](#wie-können-knowledge-graphs-verwendet-werden-um-angriffe-auf-ein-netz-zu-erkennen-oder-vorherzusagen-und-geräte-in-einem-netz-unter-quarantäne-zu-stellen)
  - [Quarantäne](#quarantäne)
    - [Beispielcode in Python, wie man ein Netzwerkgerät unter Quarantäne stellt](#beispielcode-in-python-wie-man-ein-netzwerkgerät-unter-quarantäne-stellt)


<br>
<hr>
<br>

## Security
### Codebespiele für einen Knowledge-Graph Security Ansatz
Der Schutz von Lieferketten mithilfe von Knowledge-Graphs umfasst mehrere Schritte, darunter die Datenerfassung, die Erkennung von Entitäten, die Extraktion von Beziehungen, die Erstellung von Knowledge-Graphs und die Analyse. Hier ein Beispiel dafür, wie dies mit Python und der Bibliothek Natural Language Toolkit (NLTK) geschehen könnte:

1. Datenerfassung: Sammeln Sie Daten aus verschiedenen Quellen innerhalb der Lieferkette, z. B. Produktbeschreibungen, Lieferanteninformationen und Transaktionsdaten.
```python
import pandas as pd
import requests

# Collect supplier information
suppliers = pd.read_csv('suppliers.csv')

# Collect transaction data
response = requests.get('https://api.example.com/transactions')
transactions = pd.DataFrame(response.json())
```

2. Erkennung von Entitäten: Verwenden Sie Techniken zur Verarbeitung natürlicher Sprache, um Entitäten aus den erfassten Daten zu extrahieren, z. B. Lieferantennamen, Produktnamen und Transaktionsbeträge.
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# Extract supplier names
def extract_suppliers(text):
  words = word_tokenize(text)
  tags = pos_tag(words)
  return [word for word, tag in tags if tag == 'NNP']

suppliers['entities'] = suppliers['description'].apply(extract_suppliers)

# Extract product names
def extract_products(text):
  words = word_tokenize(text)
  tags = pos_tag(words)
  return [word for word, tag in tags if tag == 'NN']

transactions['entities'] = transactions['description'].apply(extract_products)
```

3. Extraktion von Beziehungen: Verwenden Sie Techniken zur Verarbeitung natürlicher Sprache, um Beziehungen zwischen Entitäten zu extrahieren, z. B. Lieferanten-Produkt-Beziehungen und Transaktionsbeziehungen.
```python
from nltk import ne_chunk
from nltk.tree import Tree

# Extract supplier-product relationships
def extract_supplier_products(text):
  chunked = ne_chunk(pos_tag(word_tokenize(text)))
  supplier_products = []
  for subtree in chunked.subtrees(filter=lambda t: t.label() == 'ORGANIZATION'):
    supplier = subtree.leaves()[0][0]
    product = ' '.join([leaf[0] for leaf in subtree.leaves()[1:]])
    supplier_products.append((supplier, product))
  return supplier_products

suppliers['relationships'] = suppliers['description'].apply(extract_supplier_products)

# Extract transaction relationships
def extract_transactions(text):
  chunked = ne_chunk(pos_tag(word_tokenize(text)))
  transactions = []
  for subtree in chunked.subtrees(filter=lambda t: t.label() == 'MONEY'):
    transaction = subtree.leaves()[0][0]
    transactions.append(transaction)
  return transactions

transactions['relationships'] = transactions['description'].apply(extract_transactions)
```

4. Konstruktion eines Knowledge-Graphs: Verwenden Sie die extrahierten Entitäten und Beziehungen, um einen Knowledge-Graphs zu konstruieren, der die Beziehungen zwischen verschiedenen Entitäten innerhalb der Lieferkette darstellt.
```python
import networkx as nx

# Construct knowledge graph
graph = nx.Graph()
for index, row in suppliers.iterrows():
  for supplier in row['entities']:
    for product in row['relationships']:
      graph.add_edge(supplier, product)

for index, row in transactions.iterrows():
  for entity in row['entities']:
    for transaction in row['relationships']:
      graph.add_edge(entity, transaction)
```

5. Analyse: Verwenden Sie den konstruierten Knowledge-Graphs, um die Beziehungen zwischen verschiedenen Einheiten innerhalb der Lieferkette zu analysieren und potenzielle Schwachstellen oder Bedrohungen zu ermitteln.
```python
# Analyze graph
import matplotlib.pyplot as plt

# Visualize graph
pos = nx.spring_layout(graph)
nx.draw(graph, pos=pos, with_labels=True)
plt.show()

# Identify vulnerabilities
vulnerabilities = []
for supplier in suppliers['entities']:
  for product in graph.neighbors(supplier):
    if len(graph.neighbors(product)) == 1:
      vulnerabilities.append((supplier, product))

print(vulnerabilities)
```

Dies ist nur ein Beispiel dafür, wie Knowledge-Graphs zum Schutz von Lieferketten vor Cyber-Bedrohungen eingesetzt werden können. Durch die Erstellung eines Knowledge-Graphs, der die Beziehungen zwischen verschiedenen Einheiten innerhalb der Lieferkette darstellt, wird es einfacher, potenzielle Schwachstellen oder Bedrohungen zu erkennen. Der obige Beispielcode zeigt, wie der Wissensgraph dazu verwendet werden kann, Schwachstellen in der Lieferkette zu erkennen, z. B. Lieferanten, die nur ein einziges Produkt liefern, oder Produkte, die nur einen einzigen Lieferanten haben.

Durch den Einsatz von Knowledge-Graphs in Kombination mit anderen Cybersicherheitsmaßnahmen wie Firewalls, Intrusion-Detection-Systemen und Zugangskontrollen können Unternehmen ihre Lieferketten besser vor Cyberbedrohungen schützen. Knowledge-Graphs bieten eine ganzheitliche Sicht auf die Lieferkette, die Unternehmen dabei helfen kann, potenzielle Bedrohungen und Schwachstellen zu erkennen und Erkenntnisse darüber zu gewinnen, wie die Lieferkette optimiert werden kann, um ihre Effizienz und Widerstandsfähigkeit zu erhöhen.

<br>

## Prognose
### Wie kann der Knowledge-Graph zur Entwicklung von Prognosemodellen verwendet werden kann, die den Managern der Versorgungskette dabei helfen, potenzielle Risiken zu antizipieren und abzumildern, bevor sie zu großen Problemen werden?
Knowledge-Graphs können zur Entwicklung von Vorhersagemodellen verwendet werden, indem maschinelle Lernverfahren zur Analyse und Kategorisierung von Daten aus verschiedenen Quellen innerhalb der Lieferkette eingesetzt werden. Das Wissensdiagramm kann dann verwendet werden, um Muster und Trends zu erkennen, die auf potenzielle Risiken hinweisen, und um Vorhersagen über zukünftige Risikoereignisse zu erstellen.

Der folgende Python-Codeausschnitt zeigt, wie Knowledge-Graphs zur Entwicklung eines einfachen Vorhersagemodells verwendet werden können:
```python
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data into a pandas DataFrame
data = pd.read_csv('suppliers.csv')

# Create a knowledge graph
knowledge_graph = {}

# Iterate through the data and add nodes to the knowledge graph
for index, row in data.iterrows():
    supplier_id = row['supplier_id']
    vendor_id = row['vendor_id']
    supplier_score = row['supplier_score']
    vendor_score = row['vendor_score']
    
    # Add supplier node to the knowledge graph
    if supplier_id not in knowledge_graph:
        knowledge_graph[supplier_id] = {'score': supplier_score, 'connected_vendors': [vendor_id]}
    else:
        knowledge_graph[supplier_id]['score'] = supplier_score
        knowledge_graph[supplier_id]['connected_vendors'].append(vendor_id)
    
    # Add vendor node to the knowledge graph
    if vendor_id not in knowledge_graph:
        knowledge_graph[vendor_id] = {'score': vendor_score, 'connected_suppliers': [supplier_id]}
    else:
        knowledge_graph[vendor_id]['score'] = vendor_score
        knowledge_graph[vendor_id]['connected_suppliers'].append(supplier_id)

# Define a function to predict the risk level of a supplier
def predict_supplier_risk(supplier_id):
    supplier_node = knowledge_graph[supplier_id]
    connected_vendors = supplier_node['connected_vendors']
    
    vendor_scores = []
    for vendor_id in connected_vendors:
        vendor_node = knowledge_graph[vendor_id]
        vendor_scores.append(vendor_node['score'])
    
    average_vendor_score = sum(vendor_scores) / len(vendor_scores)
    
    if supplier_node['score'] < average_vendor_score:
        return 'high'
    else:
        return 'low'

# Split data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Train a logistic regression model on the training data
X_train = train_data.drop(['supplier_id', 'vendor_id', 'supplier_score'], axis=1)
y_train = train_data['supplier_score']
model = LogisticRegression()
model.fit(X_train, y_train)

# Generate predictions on the test data using the logistic regression model
X_test = test_data.drop(['supplier_id', 'vendor_id', 'supplier_score'], axis=1)
y_test = test_data['supplier_score']
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Model accuracy:', accuracy)

# Generate predictions for supplier risk using the knowledge graph
supplier_id = 'supplier_1'
risk_level = predict_supplier_risk(supplier_id)
print('Risk level for supplier', supplier_id, 'is:', risk_level)
```

In diesem Beispiel laden wir zunächst Daten aus einer Datei suppliers.csv in einen Pandas DataFrame. Anschließend erstellen wir einen Knowledge-Graphs, indem wir die Daten iterativ durchgehen und Knoten für jeden Lieferanten und Anbieter hinzufügen. Jeder Knoten im Knowledge-Graphs enthält Informationen über die Punktzahl für die betreffende Entität sowie über alle Verbindungen zu anderen Lieferanten oder Anbietern.

Anschließend definieren wir eine Funktion zur Vorhersage des Risikoniveaus eines Lieferanten auf der Grundlage der Punktzahlen der mit ihm verbundenen Lieferanten.

Um mit dem Code-Beispiel fortzufahren, können wir nun ein Vorhersagemodell unter Verwendung der Knowledge-Graphs-Daten erstellen. Eine Möglichkeit, dies zu tun, ist die Verwendung eines Algorithmus für maschinelles Lernen, wie logistische Regression oder Entscheidungsbäume, um die Wahrscheinlichkeit vorherzusagen, dass ein Lieferant ein Sicherheitsrisiko darstellt.

Hier ein Beispiel für die Implementierung eines logistischen Regressionsmodells in Python mit scikit-learn:
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load data
suppliers = pd.read_csv('suppliers.csv')

# Define features and target variable
features = suppliers[['location', 'certification', 'past_security_incidents']]
target = suppliers['security_risk']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

# Fit logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Predict on test set
y_pred = lr.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model accuracy:", accuracy)
```

In diesem Beispiel laden wir die Lieferantendaten aus der Datei `suppliers.csv` und definieren die Merkmale und die Zielvariable. Anschließend werden die Daten mit der Funktion `train_test_split()` in Trainings- und Testdatensätze aufgeteilt. Als Nächstes passen wir ein logistisches Regressionsmodell an die Trainingsdaten an und machen Vorhersagen für den Testsatz. Schließlich wird die Genauigkeit des Modells mit der Funktion `accuracy_score()` bewertet.

Die Verwendung eines Knowledge-Graphs zur Entwicklung von Vorhersagemodellen kann Managern in der Lieferkette dabei helfen, potenzielle Risiken vorherzusehen und abzumildern, bevor sie zu größeren Problemen werden. Durch die Analyse von Lieferantendaten und die Identifizierung von Mustern und Trends können Manager proaktive Schritte unternehmen, um potenzielle Sicherheitsrisiken in ihren Lieferketten zu mindern.

<br>

### Wie können Knowledge-Graphs verwendet werden, um Angriffe auf ein Netz zu erkennen oder vorherzusagen und Geräte in einem Netz unter Quarantäne zu stellen?
Knowledge-Graphs können zur Erkennung und Vorhersage von Angriffen auf ein Netzwerk verwendet werden, indem Netzwerkdaten analysiert und Muster und Anomalien identifiziert werden, die auf einen Angriff hindeuten könnten. Sobald ein Angriff identifiziert ist, kann der Wissensgraph verwendet werden, um betroffene Geräte unter Quarantäne zu stellen und die Ausbreitung des Angriffs zu verhindern.

Hier ein Beispiel für die Verwendung eines Knowledge-Graphs zur Erkennung und Vorhersage von Angriffen auf ein Netzwerk und zur Quarantäne von Geräten in Python:
```python
import pandas as pd
import networkx as nx

# Load network data
network_data = pd.read_csv('network_data.csv')

# Create knowledge graph
kg = nx.Graph()

# Add nodes for devices
for device in network_data['device']:
    kg.add_node(device)

# Add edges for device connections
for _, row in network_data.iterrows():
    device1 = row['device']
    device2 = row['connected_device']
    kg.add_edge(device1, device2)

# Analyze network data and identify anomalies
anomalies = []
for device in network_data['device']:
    neighbors = list(kg.neighbors(device))
    if len(neighbors) < 3:
        anomalies.append(device)

# Quarantine affected devices
for device in anomalies:
    print("Quarantining device:", device)
    # Code to quarantine device goes here...
```

In diesem Beispiel laden wir zunächst die Netzwerkdaten aus der Datei `network_data.csv` und erstellen einen Knowledge-Graph mithilfe der `networkx`-Bibliothek. Wir fügen Knoten für jedes Gerät und Kanten für jede Geräteverbindung hinzu.

Anschließend analysieren wir die Netzwerkdaten und identifizieren Anomalien anhand einer einfachen Regel, die besagt, dass jedes Gerät mit weniger als drei Verbindungen als anomal gilt. In einem realen Szenario könnten komplexere Algorithmen zur Erkennung von Anomalien verwendet werden. Schließlich stellen wir alle betroffenen Geräte unter Quarantäne, indem wir eine Meldung ausgeben und einen Code ausführen, der das Gerät unter Quarantäne stellt. In der Praxis können Quarantäneverfahren die Deaktivierung des Netzwerkzugangs, die Blockierung des Netzwerkverkehrs oder sogar die physische Isolierung des Geräts beinhalten.

Durch die Verwendung eines Knowledge-Graphs zur Erkennung und Vorhersage von Angriffen auf ein Netzwerk und zur Quarantäne betroffener Geräte können Unternehmen das Risiko verringern, dass sich Cyberangriffe in ihren Netzwerken ausbreiten und weitreichende Schäden verursachen.

<br>

## Quarantäne
### Beispielcode in Python, wie man ein Netzwerkgerät unter Quarantäne stellt
Die Quarantäne eines Netzwerkgeräts beinhaltet in der Regel das Entfernen des Geräts aus dem Netzwerk, um eine weitere Verbreitung des Angriffs zu verhindern. Hier ist ein Beispiel dafür, wie man mit Python den Netzwerkzugang für ein Gerät durch Hinzufügen einer Firewall-Regel sperrt:

```python
import subprocess

# Define the IP address of the device to be quarantined
ip_address = '192.168.0.10'

# Disable network access for the device by adding a firewall rule
subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'])
```

In diesem Beispiel verwenden wir das Modul `subprocess`, um den Befehl `iptables` mit Root-Rechten (`sudo`) auszuführen und eine Firewall-Regel hinzuzufügen, die den gesamten eingehenden Datenverkehr von der angegebenen IP-Adresse (`ip_address`) unterbindet. Dadurch wird das Gerät effektiv unter Quarantäne gestellt, indem jeglicher Netzwerkzugriff von dem Gerät blockiert wird.

Beachten Sie, dass der spezifische Befehl, der zur Quarantäne eines Geräts verwendet wird, je nach Netzwerkumgebung und Sicherheitsrichtlinien variieren kann. Unternehmen sollten klare Verfahren für die Isolierung und Quarantäne von Geräten im Falle eines Sicherheitsvorfalls entwickeln und sicherstellen, dass alle Mitarbeiter in diesen Verfahren geschult sind.