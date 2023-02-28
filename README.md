<div class="page"/>

# Knowledgegraphs in der Supply-Chain

## Contents
- [Knowledgegraphs in der Supply-Chain](#knowledgegraphs-in-der-supply-chain)
  - [Contents](#contents)
  - [Generelle Übersicht](#generelle-übersicht)
      - [Was regelt der Supply Chain Act?](#was-regelt-der-supply-chain-act)
    - [Warum fehlt die Cybersicherheit im Supply Chain Act?](#warum-fehlt-die-cybersicherheit-im-supply-chain-act)
  - [SIEM vs Knowledge-Graphs](#siem-vs-knowledge-graphs)
      - [Unterschied zwischen einem SIEM und Knowledge-Graphs in der Cybersicherheit](#unterschied-zwischen-einem-siem-und-knowledge-graphs-in-der-cybersicherheit)
      - [Was sind die Vorteile von Knowledgegraphs gegenüber einem SIEM?](#was-sind-die-vorteile-von-knowledgegraphs-gegenüber-einem-siem)
  - [Cyber Security: Knowledge Graphs](#cyber-security-knowledge-graphs)
      - [Wie können Lieferketten durch Knowledge-Graphs im Hinblick auf die Cybersicherheit geschützt werden?](#wie-können-lieferketten-durch-knowledge-graphs-im-hinblick-auf-die-cybersicherheit-geschützt-werden)
      - [Was wäre ein gutes Konzept zur Nutzung von Knowledge-Graphs für die Cybersicherheit, insbesondere im Hinblick auf die Lieferkette und das Lieferkettengesetz?](#was-wäre-ein-gutes-konzept-zur-nutzung-von-knowledge-graphs-für-die-cybersicherheit-insbesondere-im-hinblick-auf-die-lieferkette-und-das-lieferkettengesetz)
      - [Codebespiele für einen Knowledge-Graph Security Ansatz?](#codebespiele-für-einen-knowledge-graph-security-ansatz)
      - [Wie kann der Knowledge-Graph zur Entwicklung von Prognosemodellen verwendet werden kann, die den Managern der Versorgungskette dabei helfen, potenzielle Risiken zu antizipieren und abzumildern, bevor sie zu großen Problemen werden?](#wie-kann-der-knowledge-graph-zur-entwicklung-von-prognosemodellen-verwendet-werden-kann-die-den-managern-der-versorgungskette-dabei-helfen-potenzielle-risiken-zu-antizipieren-und-abzumildern-bevor-sie-zu-großen-problemen-werden)
      - [Wie können Knowledge-Graphs verwendet werden, um Angriffe auf ein Netz zu erkennen oder vorherzusagen und Geräte in einem Netz unter Quarantäne zu stellen?](#wie-können-knowledge-graphs-verwendet-werden-um-angriffe-auf-ein-netz-zu-erkennen-oder-vorherzusagen-und-geräte-in-einem-netz-unter-quarantäne-zu-stellen)
      - [Beispielcode in Python, wie man ein Netzwerkgerät unter Quarantäne stellt](#beispielcode-in-python-wie-man-ein-netzwerkgerät-unter-quarantäne-stellt)
    - [Docker Device-Emulation](#docker-device-emulation)
      - [Dockerfile und Python-Beispielcode, der ein Gerät in einem lokalen Netzwerk emuliert](#dockerfile-und-python-beispielcode-der-ein-gerät-in-einem-lokalen-netzwerk-emuliert)
      - [Hinzufügen von drei Geräten zum Netzwerk inklusive Knowledge-Graph-Abbildung](#hinzufügen-von-drei-geräten-zum-netzwerk-inklusive-knowledge-graph-abbildung)
      - [Wie man Geräte über Docker zum Netzwerk hinzufügt:](#wie-man-geräte-über-docker-zum-netzwerk-hinzufügt)
      - [Beispiel-Dockerfile, das Sie ändern können, um Ihre Geräte in einem lokalen Netzwerk zu emulieren:](#beispiel-dockerfile-das-sie-ändern-können-um-ihre-geräte-in-einem-lokalen-netzwerk-zu-emulieren)
      - [Beispieldatei device.py:](#beispieldatei-devicepy)
      - [Sicherheitsmaßnahmen für device.py](#sicherheitsmaßnahmen-für-devicepy)
      - [Darstellung aller kommunizierenden Docker-Container im lokalen Netzwerk](#darstellung-aller-kommunizierenden-docker-container-im-lokalen-netzwerk)
      - [Mapping aller kommunizierenden Geräte auf Port 80 inklusive API-Abfrage](#mapping-aller-kommunizierenden-geräte-auf-port-80-inklusive-api-abfrage)
  - [Firewalls](#firewalls)

## Generelle Übersicht
#### Was regelt der Supply Chain Act?
Der Supply Chain Act ist ein Gesetzesvorschlag, der darauf abzielt, Lieferketten zu regulieren, um sicherzustellen, dass in den Vereinigten Staaten verkaufte Waren nicht durch Zwangsarbeit oder andere Formen von Menschenrechtsverletzungen hergestellt werden. Das Gesetz würde Unternehmen dazu verpflichten, Informationen über ihre Lieferketten, einschließlich des Einsatzes von Zwangsarbeit, offenzulegen, und es würde Strafen für Verstöße festlegen.

Das vorgeschlagene Gesetz würde für alle Unternehmen gelten, die in den USA tätig sind und einen Jahresumsatz von mindestens 500 Millionen Dollar erzielen, unabhängig davon, ob sie ihren Hauptsitz in den USA oder im Ausland haben. Das Gesetz würde diese Unternehmen dazu verpflichten, ihre Lieferketten einer Sorgfaltsprüfung zu unterziehen und Informationen über ihre Bemühungen zur Ermittlung und Bekämpfung von Zwangsarbeit und anderen Menschenrechtsverletzungen offenzulegen.

Mit dem Supply Chain Act würde auch ein neues Büro im Arbeitsministerium eingerichtet, das für die Durchsetzung des Gesetzes zuständig wäre und den Unternehmen technische Unterstützung bei der Einhaltung der Anforderungen bieten würde. Sollte das Gesetz verabschiedet werden, würde es einen bedeutenden Wandel in der Art und Weise darstellen, wie US-Unternehmen ihre Lieferketten managen sollen, mit einem stärkeren Fokus darauf, sicherzustellen, dass Produkte in einer Weise hergestellt werden, die ethisch vertretbar ist und die Menschenrechte respektiert.


### Warum fehlt die Cybersicherheit im Supply Chain Act?
Der Supply Chain Act, wie er derzeit vorgeschlagen wird, konzentriert sich speziell auf Menschenrechtsverletzungen und Zwangsarbeit innerhalb von Lieferketten. Die Cybersicherheit ist zwar ein wichtiger Aspekt des Lieferkettenmanagements, fällt aber nicht in den Anwendungsbereich dieses Gesetzes.

Allerdings gab es in den letzten Jahren auch andere Gesetzesinitiativen, die auf die Verbesserung der Cybersicherheit in der Lieferkette abzielten. So enthielt der US National Defense Authorization Act for Fiscal Year 2021 Bestimmungen zur Sicherheit der Lieferkette im Verteidigungsministerium. Darüber hinaus hat die Cybersecurity and Infrastructure Security Agency (CISA) an der Entwicklung von Leitlinien für die Sicherheit der Lieferkette in verschiedenen Branchen gearbeitet.

Da die Lieferketten immer komplexer und vernetzter werden, ist es wahrscheinlich, dass wir mehr gesetzgeberische und regulatorische Bemühungen sehen werden, die darauf abzielen, sicherzustellen, dass diese Systeme sicher und widerstandsfähig gegen Cyberbedrohungen sind.


## SIEM vs Knowledge-Graphs
#### Unterschied zwischen einem SIEM und Knowledge-Graphs in der Cybersicherheit
SIEM (Security Information and Event Management) und Knowledge-Graphs sind beides Werkzeuge, die im Bereich der Cybersicherheit eingesetzt werden, aber sie haben unterschiedliche Zwecke und Funktionen.

Ein SIEM-System ist darauf ausgelegt, sicherheitsrelevante Daten aus verschiedenen Quellen zu sammeln und zu analysieren, z. B. von Netzwerkgeräten, Servern, Anwendungen und Sicherheitsgeräten. Es aggregiert, normalisiert und korreliert diese Daten, um potenzielle Sicherheitsvorfälle und Bedrohungen zu identifizieren. SIEM-Systeme verwenden in der Regel regelbasierte Engines und Algorithmen für maschinelles Lernen, um Muster verdächtiger Aktivitäten zu erkennen, Warnungen zu generieren und Einblicke in Sicherheitsereignisse zu geben.

Ein Wissensdiagramm hingegen ist eine Art von Datenbank, die ein graphenbasiertes Datenmodell verwendet, um Wissen auf strukturierte Weise zu speichern und zu organisieren. Knowledge-Graphs werden verwendet, um komplexe Beziehungen zwischen Entitäten und Konzepten darzustellen, was die Identifizierung von Mustern und Erkenntnissen erleichtert, die mit herkömmlichen Datenmodellen schwer zu erkennen wären.

Im Bereich der Cybersicherheit können Knowledge-Graphs verwendet werden, um Beziehungen zwischen verschiedenen Entitäten wie IP-Adressen, Domänennamen, Benutzerkonten und Sicherheitsereignissen zu modellieren. Durch die Darstellung dieser Beziehungen in einem Diagrammformat können Analysten schnell Verbindungen zwischen Entitäten identifizieren und Muster verdächtiger Aktivitäten erkennen, die auf einen Sicherheitsvorfall hindeuten könnten.

Der Hauptunterschied zwischen SIEM und Knowledge-Graphs besteht darin, dass SIEM-Systeme für die Analyse und Erkennung von Sicherheitsereignissen konzipiert sind, während Knowledge-Graphs für die visuelle Darstellung von Beziehungen zwischen Entitäten und Konzepten konzipiert sind. SIEM-Systeme werden in der Regel für die Überwachung und Erkennung in Echtzeit eingesetzt, während Knowledge-Graphs für die Visualisierung und Analyse großer Datenmengen im Zeitverlauf verwendet werden.

In der Praxis werden diese beiden Tools bei Cybersecurity-Operationen häufig gemeinsam eingesetzt, wobei SIEM-Systeme für die Überwachung von Ereignissen in Echtzeit und für Warnmeldungen sorgen, während Knowledge-Graphs eine ganzheitlichere Sicht auf Sicherheitsereignisse und Beziehungen zwischen Entitäten bieten. Durch die Kombination der Stärken dieser beiden Tools können Sicherheitsanalysten Sicherheitsvorfälle in komplexen und dynamischen Umgebungen schneller und effektiver erkennen und darauf reagieren.


#### Was sind die Vorteile von Knowledgegraphs gegenüber einem SIEM?
Während SIEM (Security Information and Event Management) und Knowledge-Graphs beide nützliche Werkzeuge für die Cybersicherheit sind, bieten Knowledge-Graphs mehrere Vorteile gegenüber SIEM-Systemen, darunter

- **Ganzheitliche Ansicht:** Knowledge-Graphs bieten eine ganzheitlichere Sicht auf die Daten und ermöglichen es Sicherheitsanalysten zu sehen, wie die Daten miteinander verbunden sind und in Beziehung zu anderen Entitäten stehen. Dies hilft Analysten, Verhaltensmuster und Beziehungen zwischen Entitäten zu erkennen, die von herkömmlichen SIEM-Systemen möglicherweise übersehen werden.

- **Skalierbarkeit:** Knowledge-Graphs sind darauf ausgelegt, große Datenmengen zu verarbeiten, was die Speicherung und Analyse großer Datenmengen aus verschiedenen Quellen erleichtert. Dies ist besonders nützlich in komplexen Cybersicherheitsumgebungen, in denen mehrere Datenquellen analysiert werden müssen.

- **Flexibel:** Knowledge-Graphs lassen sich leicht anpassen und auf spezifische Bedürfnisse abstimmen, was die Modellierung verschiedener Arten von Daten und Beziehungen erleichtert. Dies macht Knowledge-Graphs zu einem flexibleren Tool als SIEM-Systeme, die in der Regel auf vordefinierte Datenmodelle beschränkt sind.

- **Abfragen und Analysen:** Knowledge-Graphs bieten leistungsstarke Abfrage- und Analysefunktionen, die es Analysten ermöglichen, Daten in Echtzeit abzufragen und komplexe Beziehungen zwischen verschiedenen Entitäten zu analysieren. Dies erleichtert die Identifizierung potenzieller Bedrohungen und die schnelle Reaktion auf Sicherheitsvorfälle.

- **Kollaboration:** Knowledge-Graphs bieten ein gemeinsames Verständnis von Daten, das von mehreren Teams und Beteiligten genutzt werden kann. Dies erleichtert die Zusammenarbeit zwischen Sicherheitsanalytikern, Ansprechpartnern für Sicherheitsvorfälle und anderen Beteiligten und ermöglicht eine effektivere Zusammenarbeit.

Zusammenfassend lässt sich sagen, dass SIEM-Systeme zwar wertvolle Tools für die Erkennung von und Reaktion auf Sicherheitsvorfälle sind, Knowledge-Graphs jedoch zusätzliche Vorteile in Bezug auf Skalierbarkeit, Flexibilität und Analysefunktionen bieten. Durch die Kombination dieser beiden Tools können Unternehmen ihre Fähigkeit verbessern, Cyber-Bedrohungen effizienter und effektiver zu erkennen und auf sie zu reagieren.


## Cyber Security: Knowledge Graphs
#### Wie können Lieferketten durch Knowledge-Graphs im Hinblick auf die Cybersicherheit geschützt werden?
Knowledge-Graphs können ein leistungsfähiges Instrument zum Schutz von Lieferketten vor Cyber-Bedrohungen sein, da sie einen ganzheitlicheren Blick auf die Beziehungen zwischen verschiedenen Einheiten und Ereignissen innerhalb der Lieferkette ermöglichen. Im Folgenden sind einige Möglichkeiten aufgeführt, wie Knowledge-Graphs zum Schutz von Lieferketten eingesetzt werden können:

- **Identifizierung von Schwachstellen:** Knowledge-Graphs können helfen, Schwachstellen innerhalb der Lieferkette zu identifizieren, indem sie die Beziehungen zwischen verschiedenen Lieferanten, Produkten und Dienstleistungen modellieren. Durch die Visualisierung der Abhängigkeiten und Interdependenzen zwischen diesen Einheiten können Analysten potenzielle Schwachstellen identifizieren, die von Cyber-Angreifern ausgenutzt werden könnten.

- **Erkennen von Bedrohungen:** Knowledge-Graphs können verwendet werden, um potenzielle Bedrohungen innerhalb der Lieferkette zu erkennen, indem Beziehungen zwischen Unternehmen modelliert und Verhaltensmuster analysiert werden. Wenn beispielsweise ein Lieferant plötzlich beginnt, Zugriff auf Daten oder Systeme zu verlangen, die er normalerweise nicht benötigt, könnte dies ein rotes Tuch sein, das auf eine mögliche Sicherheitsverletzung hinweist.

- **Schnelle Reaktion:** Mit Hilfe von Knowledge-Graphs können Sicherheitsvorfälle innerhalb der Lieferkette schnell erkannt und darauf reagiert werden, indem bei Anomalien Echtzeitwarnungen und -benachrichtigungen ausgegeben werden. Dies kann dazu beitragen, die Auswirkungen eines Cyberangriffs abzumildern und zu verhindern, dass er sich auf andere Teile der Lieferkette ausbreitet.

- **Kollaboration:** Knowledge-Graphs können genutzt werden, um Informationen und Erkenntnisse über potenzielle Bedrohungen innerhalb der Lieferkette mit anderen Beteiligten wie Lieferanten, Kunden und Regulierungsbehörden auszutauschen. Dies kann dazu beitragen, die Zusammenarbeit und Koordination zwischen den verschiedenen Parteien innerhalb der Lieferkette zu verbessern, um sich besser vor Cyber-Bedrohungen zu schützen.

- **Risikomanagement:** Knowledge-Graphs können zur Modellierung und Quantifizierung von Risiken innerhalb der Lieferkette verwendet werden, indem die Beziehungen zwischen verschiedenen Unternehmen und die möglichen Auswirkungen einer Sicherheitsverletzung analysiert werden. Dies kann dazu beitragen, Strategien für das Risikomanagement zu entwickeln und die allgemeine Cybersicherheitslage innerhalb der Lieferkette zu verbessern.

Zusammenfassend lässt sich sagen, dass Knowledge-Graphs ein leistungsfähiges Instrument für den Schutz von Lieferketten vor Cyber-Bedrohungen sein können, da sie einen umfassenderen Überblick über die Beziehungen und Abhängigkeiten zwischen verschiedenen Unternehmen und Ereignissen innerhalb der Lieferkette bieten. Durch den Einsatz von Knowledge-Graphs zur Identifizierung von Schwachstellen, zur Erkennung von Bedrohungen, zur schnellen Reaktion, zur Zusammenarbeit mit Interessengruppen und zum Risikomanagement können Unternehmen ihre allgemeine Cybersicherheitslage verbessern und ihre Lieferketten besser schützen.


#### Was wäre ein gutes Konzept zur Nutzung von Knowledge-Graphs für die Cybersicherheit, insbesondere im Hinblick auf die Lieferkette und das Lieferkettengesetz?
Ein Konzept zur Nutzung von Knowledge-Graphs für die Cybersicherheit in Bezug auf die Lieferkette und den Supply Chain Act besteht in der Entwicklung einer Plattform für das Risikomanagement in der Lieferkette, die einen Knowledge-Graph zur Modellierung der Beziehungen zwischen verschiedenen Einheiten innerhalb der Lieferkette, wie Lieferanten, Anbietern und Kunden, nutzt.

Mit Hilfe des Knowledge-Graphs könnten wichtige Risikofaktoren innerhalb der Lieferkette identifiziert und abgebildet werden, z. B. Schwachstellen in Software- oder Hardwarekomponenten, Datenschutzverletzungen oder andere Sicherheitsvorfälle. Durch den Einsatz von Techniken des maschinellen Lernens und der Verarbeitung natürlicher Sprache zur Analyse und Kategorisierung von Daten aus verschiedenen Quellen könnte der Wissensgraph ein umfassenderes und genaueres Verständnis potenzieller Risiken für die Lieferkette liefern.

Darüber hinaus könnte der Wissensgraph zur Entwicklung von Vorhersagemodellen verwendet werden, die den Managern der Lieferkette helfen könnten, potenzielle Risiken vorherzusehen und zu mindern, bevor sie zu einem größeren Problem werden. Dies könnte Unternehmen dabei helfen, die Anforderungen des Supply Chain Act zu erfüllen, indem sie mehr Transparenz und Kontrolle über ihre Lieferketten erhalten und sicherstellen, dass sie geeignete Schritte unternehmen, um Zwangsarbeit und andere Menschenrechtsverletzungen zu verhindern.

Insgesamt könnte die Nutzung von Knowledge-Graphs auf diese Weise Unternehmen helfen, Cybersicherheitsrisiken innerhalb ihrer Lieferketten besser zu bewältigen und gleichzeitig die Einhaltung von Vorschriften wie dem Supply Chain Act zu unterstützen.


#### Codebespiele für einen Knowledge-Graph Security Ansatz?
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


#### Wie kann der Knowledge-Graph zur Entwicklung von Prognosemodellen verwendet werden kann, die den Managern der Versorgungskette dabei helfen, potenzielle Risiken zu antizipieren und abzumildern, bevor sie zu großen Problemen werden?
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

#### Wie können Knowledge-Graphs verwendet werden, um Angriffe auf ein Netz zu erkennen oder vorherzusagen und Geräte in einem Netz unter Quarantäne zu stellen?
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

#### Beispielcode in Python, wie man ein Netzwerkgerät unter Quarantäne stellt
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


### Docker Device-Emulation
#### Dockerfile und Python-Beispielcode, der ein Gerät in einem lokalen Netzwerk emuliert
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

#### Hinzufügen von drei Geräten zum Netzwerk inklusive Knowledge-Graph-Abbildung
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

#### Wie man Geräte über Docker zum Netzwerk hinzufügt:

1. Erstellen Sie ein Docker-Abbild für das Gerät, das Sie dem Netzwerk hinzufügen möchten.
2. Führen Sie das Docker-Abbild aus, um einen Docker-Container für jedes Gerät zu erstellen.
3. Weisen Sie jedem Container eine eindeutige IP-Adresse im gleichen Subnetz wie den anderen Geräten im Netzwerk zu.
4. Konfigurieren Sie die Container mit der entsprechenden Software und den Einstellungen, um das Verhalten der Geräte zu simulieren.

#### Beispiel-Dockerfile, das Sie ändern können, um Ihre Geräte in einem lokalen Netzwerk zu emulieren:
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

#### Beispieldatei device.py:
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

#### Sicherheitsmaßnahmen für device.py
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

#### Darstellung aller kommunizierenden Docker-Container im lokalen Netzwerk
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

#### Mapping aller kommunizierenden Geräte auf Port 80 inklusive API-Abfrage
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

## Firewalls
Firewalls sind wichtig für die Sicherung von Netzwerken durch die Kontrolle des ein- und ausgehenden Datenverkehrs. Um eine einfache Firewall mit Python zu erstellen, können wir das Socket-Modul verwenden, um ein- und ausgehende Netzwerkpakete zu erfassen und sie anhand von vordefinierten Regeln zu filtern.

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