# Knowledgegraphs in der Supply-Chain
![Supply Chains](./pictures/chapters/supply_chains_steampunk.png)
<hr>

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
  - [Codebeispiele](#codebeispiele)
  - [Docker Device Emulation](#docker-device-emulation)
  - [Scanner](#scanner)
  - [Spoofing](#spoofing)

<br>
<hr>
<br>
<div style="page-break-after: always;"></div>

## Generelle Übersicht
<br>

### Was regelt der Supply Chain Act?
Der Supply Chain Act ist ein Gesetzesvorschlag, der darauf abzielt, Lieferketten zu regulieren, um sicherzustellen, dass in den Vereinigten Staaten verkaufte Waren nicht durch Zwangsarbeit oder andere Formen von Menschenrechtsverletzungen hergestellt werden. Das Gesetz würde Unternehmen dazu verpflichten, Informationen über ihre Lieferketten, einschließlich des Einsatzes von Zwangsarbeit, offenzulegen, und es würde Strafen für Verstöße festlegen.

Das vorgeschlagene Gesetz würde für alle Unternehmen gelten, die in den USA tätig sind und einen Jahresumsatz von mindestens 500 Millionen Dollar erzielen, unabhängig davon, ob sie ihren Hauptsitz in den USA oder im Ausland haben. Das Gesetz würde diese Unternehmen dazu verpflichten, ihre Lieferketten einer Sorgfaltsprüfung zu unterziehen und Informationen über ihre Bemühungen zur Ermittlung und Bekämpfung von Zwangsarbeit und anderen Menschenrechtsverletzungen offenzulegen.

Mit dem Supply Chain Act würde auch ein neues Büro im Arbeitsministerium eingerichtet, das für die Durchsetzung des Gesetzes zuständig wäre und den Unternehmen technische Unterstützung bei der Einhaltung der Anforderungen bieten würde. Sollte das Gesetz verabschiedet werden, würde es einen bedeutenden Wandel in der Art und Weise darstellen, wie US-Unternehmen ihre Lieferketten managen sollen, mit einem stärkeren Fokus darauf, sicherzustellen, dass Produkte in einer Weise hergestellt werden, die ethisch vertretbar ist und die Menschenrechte respektiert.

<br>

### Warum fehlt die Cybersicherheit im Supply Chain Act?
Der Supply Chain Act, wie er derzeit vorgeschlagen wird, konzentriert sich speziell auf Menschenrechtsverletzungen und Zwangsarbeit innerhalb von Lieferketten. Die Cybersicherheit ist zwar ein wichtiger Aspekt des Lieferkettenmanagements, fällt aber nicht in den Anwendungsbereich dieses Gesetzes.

Allerdings gab es in den letzten Jahren auch andere Gesetzesinitiativen, die auf die Verbesserung der Cybersicherheit in der Lieferkette abzielten. So enthielt der US National Defense Authorization Act for Fiscal Year 2021 Bestimmungen zur Sicherheit der Lieferkette im Verteidigungsministerium. Darüber hinaus hat die Cybersecurity and Infrastructure Security Agency (CISA) an der Entwicklung von Leitlinien für die Sicherheit der Lieferkette in verschiedenen Branchen gearbeitet.

Da die Lieferketten immer komplexer und vernetzter werden, ist es wahrscheinlich, dass wir mehr gesetzgeberische und regulatorische Bemühungen sehen werden, die darauf abzielen, sicherzustellen, dass diese Systeme sicher und widerstandsfähig gegen Cyberbedrohungen sind.

<br>
<br>
<div style="page-break-after: always;"></div>

## SIEM vs Knowledge-Graphs
### Unterschied zwischen einem SIEM und Knowledge-Graphs in der Cybersicherheit
SIEM (Security Information and Event Management) und Knowledge-Graphs sind beides Werkzeuge, die im Bereich der Cybersicherheit eingesetzt werden, aber sie haben unterschiedliche Zwecke und Funktionen.

Ein SIEM-System ist darauf ausgelegt, sicherheitsrelevante Daten aus verschiedenen Quellen zu sammeln und zu analysieren, z. B. von Netzwerkgeräten, Servern, Anwendungen und Sicherheitsgeräten. Es aggregiert, normalisiert und korreliert diese Daten, um potenzielle Sicherheitsvorfälle und Bedrohungen zu identifizieren. SIEM-Systeme verwenden in der Regel regelbasierte Engines und Algorithmen für maschinelles Lernen, um Muster verdächtiger Aktivitäten zu erkennen, Warnungen zu generieren und Einblicke in Sicherheitsereignisse zu geben.

Ein Wissensdiagramm hingegen ist eine Art von Datenbank, die ein graphenbasiertes Datenmodell verwendet, um Wissen auf strukturierte Weise zu speichern und zu organisieren. Knowledge-Graphs werden verwendet, um komplexe Beziehungen zwischen Entitäten und Konzepten darzustellen, was die Identifizierung von Mustern und Erkenntnissen erleichtert, die mit herkömmlichen Datenmodellen schwer zu erkennen wären.

Im Bereich der Cybersicherheit können Knowledge-Graphs verwendet werden, um Beziehungen zwischen verschiedenen Entitäten wie IP-Adressen, Domänennamen, Benutzerkonten und Sicherheitsereignissen zu modellieren. Durch die Darstellung dieser Beziehungen in einem Diagrammformat können Analysten schnell Verbindungen zwischen Entitäten identifizieren und Muster verdächtiger Aktivitäten erkennen, die auf einen Sicherheitsvorfall hindeuten könnten.

Der Hauptunterschied zwischen SIEM und Knowledge-Graphs besteht darin, dass SIEM-Systeme für die Analyse und Erkennung von Sicherheitsereignissen konzipiert sind, während Knowledge-Graphs für die visuelle Darstellung von Beziehungen zwischen Entitäten und Konzepten konzipiert sind. SIEM-Systeme werden in der Regel für die Überwachung und Erkennung in Echtzeit eingesetzt, während Knowledge-Graphs für die Visualisierung und Analyse großer Datenmengen im Zeitverlauf verwendet werden.

In der Praxis werden diese beiden Tools bei Cybersecurity-Operationen häufig gemeinsam eingesetzt, wobei SIEM-Systeme für die Überwachung von Ereignissen in Echtzeit und für Warnmeldungen sorgen, während Knowledge-Graphs eine ganzheitlichere Sicht auf Sicherheitsereignisse und Beziehungen zwischen Entitäten bieten. Durch die Kombination der Stärken dieser beiden Tools können Sicherheitsanalysten Sicherheitsvorfälle in komplexen und dynamischen Umgebungen schneller und effektiver erkennen und darauf reagieren.

<br>

### Was sind die Vorteile von Knowledgegraphs gegenüber einem SIEM?
Während SIEM (Security Information and Event Management) und Knowledge-Graphs beide nützliche Werkzeuge für die Cybersicherheit sind, bieten Knowledge-Graphs mehrere Vorteile gegenüber SIEM-Systemen, darunter

- **Ganzheitliche Ansicht:** Knowledge-Graphs bieten eine ganzheitlichere Sicht auf die Daten und ermöglichen es Sicherheitsanalysten zu sehen, wie die Daten miteinander verbunden sind und in Beziehung zu anderen Entitäten stehen. Dies hilft Analysten, Verhaltensmuster und Beziehungen zwischen Entitäten zu erkennen, die von herkömmlichen SIEM-Systemen möglicherweise übersehen werden.

- **Skalierbarkeit:** Knowledge-Graphs sind darauf ausgelegt, große Datenmengen zu verarbeiten, was die Speicherung und Analyse großer Datenmengen aus verschiedenen Quellen erleichtert. Dies ist besonders nützlich in komplexen Cybersicherheitsumgebungen, in denen mehrere Datenquellen analysiert werden müssen.

- **Flexibel:** Knowledge-Graphs lassen sich leicht anpassen und auf spezifische Bedürfnisse abstimmen, was die Modellierung verschiedener Arten von Daten und Beziehungen erleichtert. Dies macht Knowledge-Graphs zu einem flexibleren Tool als SIEM-Systeme, die in der Regel auf vordefinierte Datenmodelle beschränkt sind.

- **Abfragen und Analysen:** Knowledge-Graphs bieten leistungsstarke Abfrage- und Analysefunktionen, die es Analysten ermöglichen, Daten in Echtzeit abzufragen und komplexe Beziehungen zwischen verschiedenen Entitäten zu analysieren. Dies erleichtert die Identifizierung potenzieller Bedrohungen und die schnelle Reaktion auf Sicherheitsvorfälle.

- **Kollaboration:** Knowledge-Graphs bieten ein gemeinsames Verständnis von Daten, das von mehreren Teams und Beteiligten genutzt werden kann. Dies erleichtert die Zusammenarbeit zwischen Sicherheitsanalytikern, Ansprechpartnern für Sicherheitsvorfälle und anderen Beteiligten und ermöglicht eine effektivere Zusammenarbeit.

Zusammenfassend lässt sich sagen, dass SIEM-Systeme zwar wertvolle Tools für die Erkennung von und Reaktion auf Sicherheitsvorfälle sind, Knowledge-Graphs jedoch zusätzliche Vorteile in Bezug auf Skalierbarkeit, Flexibilität und Analysefunktionen bieten. Durch die Kombination dieser beiden Tools können Unternehmen ihre Fähigkeit verbessern, Cyber-Bedrohungen effizienter und effektiver zu erkennen und auf sie zu reagieren.

<br>
<br>

## Cyber Security: Knowledge Graphs
### Wie können Lieferketten durch Knowledge-Graphs im Hinblick auf die Cybersicherheit geschützt werden?
Knowledge-Graphs können ein leistungsfähiges Instrument zum Schutz von Lieferketten vor Cyber-Bedrohungen sein, da sie einen ganzheitlicheren Blick auf die Beziehungen zwischen verschiedenen Einheiten und Ereignissen innerhalb der Lieferkette ermöglichen. Im Folgenden sind einige Möglichkeiten aufgeführt, wie Knowledge-Graphs zum Schutz von Lieferketten eingesetzt werden können:

- **Identifizierung von Schwachstellen:** Knowledge-Graphs können helfen, Schwachstellen innerhalb der Lieferkette zu identifizieren, indem sie die Beziehungen zwischen verschiedenen Lieferanten, Produkten und Dienstleistungen modellieren. Durch die Visualisierung der Abhängigkeiten und Interdependenzen zwischen diesen Einheiten können Analysten potenzielle Schwachstellen identifizieren, die von Cyber-Angreifern ausgenutzt werden könnten.

- **Erkennen von Bedrohungen:** Knowledge-Graphs können verwendet werden, um potenzielle Bedrohungen innerhalb der Lieferkette zu erkennen, indem Beziehungen zwischen Unternehmen modelliert und Verhaltensmuster analysiert werden. Wenn beispielsweise ein Lieferant plötzlich beginnt, Zugriff auf Daten oder Systeme zu verlangen, die er normalerweise nicht benötigt, könnte dies ein rotes Tuch sein, das auf eine mögliche Sicherheitsverletzung hinweist.

- **Schnelle Reaktion:** Mit Hilfe von Knowledge-Graphs können Sicherheitsvorfälle innerhalb der Lieferkette schnell erkannt und darauf reagiert werden, indem bei Anomalien Echtzeitwarnungen und -benachrichtigungen ausgegeben werden. Dies kann dazu beitragen, die Auswirkungen eines Cyberangriffs abzumildern und zu verhindern, dass er sich auf andere Teile der Lieferkette ausbreitet.

- **Kollaboration:** Knowledge-Graphs können genutzt werden, um Informationen und Erkenntnisse über potenzielle Bedrohungen innerhalb der Lieferkette mit anderen Beteiligten wie Lieferanten, Kunden und Regulierungsbehörden auszutauschen. Dies kann dazu beitragen, die Zusammenarbeit und Koordination zwischen den verschiedenen Parteien innerhalb der Lieferkette zu verbessern, um sich besser vor Cyber-Bedrohungen zu schützen.

- **Risikomanagement:** Knowledge-Graphs können zur Modellierung und Quantifizierung von Risiken innerhalb der Lieferkette verwendet werden, indem die Beziehungen zwischen verschiedenen Unternehmen und die möglichen Auswirkungen einer Sicherheitsverletzung analysiert werden. Dies kann dazu beitragen, Strategien für das Risikomanagement zu entwickeln und die allgemeine Cybersicherheitslage innerhalb der Lieferkette zu verbessern.

Zusammenfassend lässt sich sagen, dass Knowledge-Graphs ein leistungsfähiges Instrument für den Schutz von Lieferketten vor Cyber-Bedrohungen sein können, da sie einen umfassenderen Überblick über die Beziehungen und Abhängigkeiten zwischen verschiedenen Unternehmen und Ereignissen innerhalb der Lieferkette bieten. Durch den Einsatz von Knowledge-Graphs zur Identifizierung von Schwachstellen, zur Erkennung von Bedrohungen, zur schnellen Reaktion, zur Zusammenarbeit mit Interessengruppen und zum Risikomanagement können Unternehmen ihre allgemeine Cybersicherheitslage verbessern und ihre Lieferketten besser schützen.

<br>

### Was wäre ein gutes Konzept zur Nutzung von Knowledge-Graphs für die Cybersicherheit, insbesondere im Hinblick auf die Lieferkette und das Lieferkettengesetz?
Ein Konzept zur Nutzung von Knowledge-Graphs für die Cybersicherheit in Bezug auf die Lieferkette und den Supply Chain Act besteht in der Entwicklung einer Plattform für das Risikomanagement in der Lieferkette, die einen Knowledge-Graph zur Modellierung der Beziehungen zwischen verschiedenen Einheiten innerhalb der Lieferkette, wie Lieferanten, Anbietern und Kunden, nutzt.

Mit Hilfe des Knowledge-Graphs könnten wichtige Risikofaktoren innerhalb der Lieferkette identifiziert und abgebildet werden, z. B. Schwachstellen in Software- oder Hardwarekomponenten, Datenschutzverletzungen oder andere Sicherheitsvorfälle. Durch den Einsatz von Techniken des maschinellen Lernens und der Verarbeitung natürlicher Sprache zur Analyse und Kategorisierung von Daten aus verschiedenen Quellen könnte der Wissensgraph ein umfassenderes und genaueres Verständnis potenzieller Risiken für die Lieferkette liefern.

Darüber hinaus könnte der Wissensgraph zur Entwicklung von Vorhersagemodellen verwendet werden, die den Managern der Lieferkette helfen könnten, potenzielle Risiken vorherzusehen und zu mindern, bevor sie zu einem größeren Problem werden. Dies könnte Unternehmen dabei helfen, die Anforderungen des Supply Chain Act zu erfüllen, indem sie mehr Transparenz und Kontrolle über ihre Lieferketten erhalten und sicherstellen, dass sie geeignete Schritte unternehmen, um Zwangsarbeit und andere Menschenrechtsverletzungen zu verhindern.

Insgesamt könnte die Nutzung von Knowledge-Graphs auf diese Weise Unternehmen helfen, Cybersicherheitsrisiken innerhalb ihrer Lieferketten besser zu bewältigen und gleichzeitig die Einhaltung von Vorschriften wie dem Supply Chain Act zu unterstützen.

<br>

## Codebeispiele
Codebeispiele für Security, Prognosen und Quarantäne von Geräten sind in [diesem](./chapters/codesamples/codesamples.md) Kapitel erklärt.

<br>

## Docker Device Emulation
Die Device-Emulation in Docker wird in [diesem](./chapters/docker-device-emulation/docker-device-emulation.md) Kapitel erklärt.

<br>

## Scanner
Scanner werden in [diesem](./chapters/scanner/scanner.md) Kapitel erklärt.

<br>

## Spoofing
Spoofing wird in [diesem](./chapters/spoofing/spoofing.md) Kapitel erklärt.