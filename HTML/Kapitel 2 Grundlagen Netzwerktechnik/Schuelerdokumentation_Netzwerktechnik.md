# Schülerdokumentation: Grundlagen der Netzwerktechnik in der Veranstaltungstechnik

## Willkommen zur Lernsituation Netzwerktechnik

Sehr geehrte Auszubildende,

in dieser Unterrichtseinheit beschäftigen Sie sich mit den Grundlagen der Netzwerktechnik im Kontext der Veranstaltungstechnik. Sie werden lernen, wie moderne Veranstaltungen durch professionelle Netzwerkinfrastrukturen gesteuert werden und wie Sie selbst solche Systeme planen und konfigurieren können.

---

## 1. Ihre Aufgabe

### Das Szenario
Sie arbeiten bei der Veranstaltungsfirma "TechEvent GmbH" und sind mit der Planung der Netzwerkinfrastruktur für ein großes Musikfestival beauftragt worden. Das Festival umfasst mehrere Bühnen und verschiedene technische Bereiche, die alle miteinander vernetzt werden müssen.

### Ihre Rolle
Als angehende Fachkraft für Veranstaltungstechnik übernehmen Sie die Verantwortung für:
- Die Planung der IP-Adressierung
- Die Konfiguration von VLANs
- Die Auswahl geeigneter Netzwerkkomponenten
- Die Sicherstellung der Netzwerksicherheit

---

## 2. Lernziele

Nach erfolgreichem Abschluss dieser Lernsituation können Sie:

✅ **Zahlensysteme sicher anwenden**
- Zwischen Binär-, Dezimal- und Hexadezimalsystem konvertieren
- Diese Kenntnisse für IP-Adressberechnungen nutzen

✅ **IP-Netzwerke planen**
- Subnetzmasken berechnen und anwenden
- Netzwerk- und Broadcastadressen bestimmen
- Host-Bereiche definieren

✅ **Netzwerkkomponenten verstehen**
- Unterschiede zwischen Switches und Routern erklären
- Grundlegende Konfigurationen durchführen

✅ **VLANs implementieren**
- Netzwerke sinnvoll segmentieren
- Sicherheitsaspekte berücksichtigen

✅ **Netzwerkprobleme lösen**
- Systematisch Fehler analysieren
- Geeignete Tools verwenden

---

## 3. Vorbereitung und Grundverständnis

### 3.1 Was Sie bereits wissen sollten

Bevor Sie mit den praktischen Aufgaben beginnen, sollten Sie über folgende Grundkenntnisse verfügen:

**Aus vorherigen Lernfeldern:**
- Grundlagen der Digitaltechnik
- Elektrische Grundgrößen (Spannung, Strom, Widerstand)
- Grundverständnis für Datenübertragung

**Mathematische Grundlagen:**
- Grundrechenarten
- Potenzen und Logarithmen (für Subnetting)
- Binäres Zahlensystem (wird in Aufgabe 1 vertieft)

### 3.2 Lernstrategie für dieses Modul

**Empfohlene Herangehensweise:**

1. **Bearbeiten Sie die Aufgaben in der empfohlenen Reihenfolge** - jede Aufgabe baut auf der vorherigen auf
2. **Nutzen Sie die Simulationssoftware aktiv** - Theorie allein reicht nicht aus
3. **Dokumentieren Sie Ihre Lösungen ausführlich** - das hilft beim späteren Nachvollziehen
4. **Testen Sie Ihre Konfigurationen gründlich** - funktioniert alles wie geplant?
5. **Reflektieren Sie nach jeder Aufgabe** - was haben Sie gelernt, wo gab es Probleme?

### 3.3 Arbeitsumgebung vorbereiten

**Checkliste vor dem Start:**

✅ **Software installiert:**
- Cisco Packet Tracer (kostenlos über Cisco Networking Academy)
- Texteditor für Dokumentation
- PDF-Reader für Referenzmaterialien

✅ **Referenzmaterialien bereitgelegt:**
- Subnetzmasken-Tabelle (siehe Kapitel 7.2)
- Private IP-Bereiche
- Standard-Port-Liste

✅ **Arbeitsplatz organisiert:**
- Ausreichend Bildschirmfläche für Simulation und Dokumentation
- Notizbuch für Berechnungen
- Taschenrechner (optional)

**💡 Tipp:** Erstellen Sie einen eigenen Projektordner auf Ihrem Computer, in dem Sie alle Ihre Simulationsdateien, Dokumentationen und Screenshots organisiert ablegen.

---

## 4. Aufgabenübersicht und Lernweg

### 4.1 Aufgabe 1: Zahlensysteme 🔢

**Lernziel:** Sie erlernen die sichere Konvertierung zwischen verschiedenen Zahlensystemen, die in der Netzwerktechnik unerlässlich ist.

**Warum ist das wichtig?** 
In der Netzwerktechnik arbeiten Sie ständig mit verschiedenen Zahlensystemen. IP-Adressen werden zwar dezimal dargestellt, aber Computer arbeiten intern binär. Subnetzmasken müssen Sie oft in binärer Form verstehen, um Subnetting korrekt durchzuführen. MAC-Adressen werden hexadezimal dargestellt. Ein sicherer Umgang mit diesen Konvertierungen ist daher fundamental für jeden Netzwerktechniker.

**Was lernen Sie konkret?**
- Konvertierung von Dezimal zu Binär und umgekehrt
- Verständnis für Hexadezimalzahlen
- Anwendung der Zweierpotenzen
- Praktische Relevanz für IP-Adressberechnungen

**Vorbereitung:** Lernen Sie die Zweierpotenzen von 2⁰ bis 2⁷ auswendig. Diese benötigen Sie für jede Konvertierung.

**📋 [Link zur Aufgabe 1: Zahlensysteme](Aufgabe%201%20Zahlensysteme.html)**

---

### 4.2 Aufgabe 2: Netzwerkadressen 🌐

**Lernziel:** Sie planen die IP-Adressierung für ein komplexes Festivalnetzwerk und verstehen Subnetting in der Praxis.

**Warum ist das wichtig?**
Bei jeder Veranstaltung müssen verschiedene Bereiche (FOH, Monitor, Licht, Video) vernetzt werden. Ohne durchdachte IP-Planung entstehen Adresskonflikte, Sicherheitsprobleme und Kommunikationsstörungen. Subnetting ermöglicht es Ihnen, große Netzwerke effizient zu strukturieren und verschiedene Bereiche logisch zu trennen.

**Was lernen Sie konkret?**
- Berechnung der benötigten Host-Anzahl pro Bereich
- Auswahl geeigneter Subnetzmasken
- Bestimmung von Netzwerk- und Broadcastadressen
- Planung von IP-Bereichen ohne Überschneidungen
- Dokumentation von Netzwerkstrukturen

**Praxisbezug:** Sie verteilen das Netzwerk 10.50.0.0/16 auf verschiedene Festivalbereiche mit unterschiedlichen Anforderungen (FOH: 50 Geräte, Licht: 100 Geräte, Gäste-WLAN: 200 Geräte, etc.).

**📋 [Link zur Aufgabe 2: Netzwerkadressen](Aufgabe%202%20Netzwerkadressen.html)**

---

### 4.3 Aufgabe 3: Nutzgröße und Aufbau eines IP-Paketes 📦

**Lernziel:** Sie verstehen den internen Aufbau von IP-Paketen und können Overhead-Berechnungen für verschiedene Anwendungen durchführen.

**Warum ist das wichtig?**
In der Veranstaltungstechnik übertragen Sie verschiedenste Datentypen: Audio-Streams für Beschallung, Video-Streams für LED-Wände, Steuerdaten für Lichtanlagen. Jeder Datentyp hat unterschiedliche Overhead-Charakteristiken. Das Verständnis von IP-Paketen hilft Ihnen bei der Bandbreitenplanung und bei der Fehlersuche in Netzwerken.

**Was lernen Sie konkret?**
- Aufbau eines IPv4-Headers mit allen Feldern
- Berechnung des Protocol-Overheads (IP, UDP, TCP, RTP)
- Effizienzanalyse verschiedener Übertragungsarten
- Bandbreitenplanung für Audio- und Video-Streams
- Verständnis für Fragmentierung und MTU

**Praxisbeispiele:** 
- Audio-Streaming für Monitorsysteme
- Video-Übertragung für LED-Panels
- Steuerdaten für DMX-over-IP
- Web-Traffic für Management-Interfaces

**📋 [Link zur Aufgabe 3: IP-Paket-Aufbau](Aufgabe%203%20Nutzgröße%20und%20Aufbau%20eines%20IP%20Paketes.html)**

---

### 4.4 Aufgabe 4: Switches und Router ⚙️

**Lernziel:** Sie verstehen die fundamentalen Unterschiede zwischen Switches und Routern und können beide Gerätetypen grundlegend konfigurieren.

**Warum ist das wichtig?**
Switches und Router sind die zentralen Bausteine jeder Netzwerkinfrastruktur. In der Veranstaltungstechnik verbinden Switches die Geräte eines Bereichs (z.B. alle Lichtpulte im Lichtbereich), während Router verschiedene Bereiche miteinander verbinden und den Datenverkehr zwischen ihnen steuern. Das Verständnis ihrer Funktionsweise ist essentiell für jede Netzwerkplanung.

**Was lernen Sie konkret?**
- Layer-2 vs. Layer-3 Funktionalität
- MAC-Adress-Lernen bei Switches
- Routing-Tabellen und Next-Hop-Bestimmung
- Broadcast-Domänen und Collision-Domänen
- Grundlegende CLI-Befehle für Cisco-Geräte
- Konfiguration von Management-IPs

**Praktische Übungen:**
- Switch-Konfiguration mit 4 angeschlossenen Geräten
- Router-Setup für Inter-VLAN-Routing
- Konnektivitätstests mit Ping und Traceroute
- Fehlerdiagnose bei Verbindungsproblemen

**📋 [Link zur Aufgabe 4: Switches und Router](Aufgabe%204%20Switches%20und%20Router.html)**

---

### 4.5 Aufgabe 5: Praktische Anwendung 🎯

**Lernziel:** Sie setzen alle erlernten Konzepte in einem realistischen Festivalszenario um und erstellen ein vollständiges Netzwerkkonzept.

**Warum ist das wichtig?**
Diese Aufgabe simuliert eine echte Projektarbeit, wie Sie sie später im Berufsleben durchführen werden. Sie müssen verschiedene Anforderungen berücksichtigen, technische Entscheidungen treffen und diese dokumentieren. Das ist die Brücke zwischen Theorie und Praxis.

**Was lernen Sie konkret?**
- Anforderungsanalyse für Netzwerkprojekte
- Erstellung professioneller Netzwerkdiagramme
- Integration verschiedener Technologien
- Projektdokumentation und -präsentation
- Kosten-Nutzen-Abwägungen
- Redundanz- und Ausfallsicherheitsplanung

**Projektelemente:**
- Bedarfsanalyse für alle Festivalbereiche
- Topologie-Design mit redundanten Verbindungen
- Geräteauswahl und Dimensionierung
- Verkabelungsplanung
- Sicherheitskonzept
- Implementierungsplan

**📋 [Link zur Aufgabe 5: Praktische Anwendung](Aufgabe%205%20Anwendung.html)**

---

### 4.6 Aufgabe 7: VLAN-Konfiguration 🔐

**Lernziel:** Sie implementieren eine professionelle Netzwerksegmentierung mittels VLANs und verstehen deren Sicherheits- und Performance-Vorteile.

**Warum ist das wichtig?**
VLANs sind in der modernen Veranstaltungstechnik unerlässlich. Sie ermöglichen es, verschiedene Bereiche (FOH, Monitor, Licht, Video) logisch zu trennen, ohne separate physische Netzwerke aufbauen zu müssen. Das erhöht die Sicherheit, verbessert die Performance und reduziert Kosten. Besonders wichtig ist die Trennung von produktiven Systemen und Gäste-Netzwerken.

**Was lernen Sie konkret?**
- VLAN-Konzepte und -Vorteile
- Access-Ports vs. Trunk-Ports
- Inter-VLAN-Routing
- VLAN-Tagging (802.1Q)
- Sicherheitsaspekte der Netzwerksegmentierung
- Troubleshooting von VLAN-Konfigurationen

**Praxisszenarien:**
- Trennung von Produktions- und Gäste-Netzwerken
- Isolierung kritischer Systeme (Notbeleuchtung, Sicherheit)
- QoS-Implementierung für verschiedene Datentypen
- Bandbreitenverwaltung pro Bereich

**Sicherheitsaspekte:**
- Verhinderung von VLAN-Hopping-Angriffen
- Schutz vor Broadcast-Storms
- Kontrolle des Datenverkehrs zwischen VLANs

**📋 [Link zur Aufgabe 7: VLAN-Konfiguration](Aufgabe%207%20VLAN.html)**

---

## 4.7 Empfohlener Lernweg

**Für optimalen Lernerfolg empfehlen wir folgende Reihenfolge:**

1. **Woche 1:** Aufgabe 1 (Zahlensysteme) - Fundament legen
2. **Woche 2:** Aufgabe 2 (Netzwerkadressen) - IP-Planung verstehen
3. **Woche 3:** Aufgabe 3 (IP-Pakete) - Tieferes Verständnis entwickeln
4. **Woche 4:** Aufgabe 4 (Switches/Router) - Geräte kennenlernen
5. **Woche 5:** Aufgabe 7 (VLANs) - Segmentierung beherrschen
6. **Woche 6:** Aufgabe 5 (Praktische Anwendung) - Alles zusammenführen

**Zeitaufwand pro Aufgabe:** 60-90 Minuten  
**Gesamtaufwand:** Ca. 8-10 Stunden

**Lernkontrolle:** Nach jeder Aufgabe finden Sie Selbsttests und Reflexionsfragen zur Lernkontrolle.

---

## 5. Arbeitsorganisation und Lernweg

### 5.1 Zeitplanung für das Gesamtprojekt

**Gesamtdauer:** 6 Wochen (Selbststudium + Präsenzphasen)

#### Wochenplan:

**Woche 1: Fundamentals**
- Aufgabe 1: Zahlensysteme
- Selbststudium: 60-90 Minuten
- Präsenzphase: Kontrolle und Vertiefung (45 Min)

**Woche 2: Network Planning**
- Aufgabe 2: Netzwerkadressen und Subnetting
- Selbststudium: 90 Minuten
- Präsenzphase: Gemeinsame Übungen (90 Min)

**Woche 3: Deep Dive**
- Aufgabe 3: IP-Paket-Analyse
- Selbststudium: 60 Minuten
- Präsenzphase: Wireshark-Workshop (45 Min)

**Woche 4: Hardware**
- Aufgabe 4: Switches und Router
- Selbststudium: 90 Minuten
- Präsenzphase: Praktische Konfiguration (90 Min)

**Woche 5: Segmentation**
- Aufgabe 7: VLAN-Konfiguration
- Selbststudium: 75 Minuten
- Präsenzphase: VLAN-Labor (90 Min)

**Woche 6: Integration**
- Aufgabe 5: Praktische Anwendung
- Projektarbeit: 120 Minuten
- Präsenzphase: Präsentationen (90 Min)

### 5.2 Arbeitsformen und Methoden

**Blended Learning Ansatz:**
Dieses Lernmodul kombiniert Selbststudium mit Präsenzphasen für optimalen Lernerfolg.

#### Selbststudium (ca. 60% der Arbeitszeit)
- **Individuelle Bearbeitung** der HTML-Aufgaben in Ihrem eigenen Tempo
- **Nutzung der Simulationssoftware** für praktische Übungen
- **Selbstkontrolle** durch integrierte Tests und Checklisten
- **Dokumentation** Ihrer Lösungen und Erkenntnisse

#### Präsenzphasen (ca. 40% der Arbeitszeit)
- **Vertiefung** schwieriger Konzepte mit dem Lehrenden
- **Praktische Übungen** an echter Hardware
- **Gruppenarbeit** für komplexere Projekte
- **Peer-Learning** durch Erfahrungsaustausch

#### Unterstützungsangebote
- **Sprechstunden:** Mittwochs 14:00-15:00 Uhr
- **Online-Forum:** Für Fragen und Diskussionen
- **Lerngruppen:** Selbstorganisiert, Räume buchbar
- **Video-Tutorials:** Ergänzende Erklärungen zu komplexen Themen

---

## 6. Bewertung und Leistungsnachweise

### 6.1 Leistungsnachweise im Überblick

**Kontinuierliche Bewertung (60%)**
- Bearbeitung der Aufgaben 1-7 (jeweils 10 Punkte)
- Dokumentation und Reflexion (10 Punkte)
- Mitarbeit in Präsenzphasen (20 Punkte)

**Abschlussprojekt (40%)**
- Aufgabe 5: Praktische Anwendung (30 Punkte)
- Präsentation des Festivalnetzwerks (10 Punkte)

**Gesamtpunktzahl:** 100 Punkte

### 6.2 Was wird bewertet?

#### Fachliche Richtigkeit (50%)
- **Korrekte Berechnungen:** IP-Adressen, Subnetzmasken, Host-Bereiche
- **Funktionsfähige Konfiguration:** Switches, Router, VLANs
- **Logische Netzwerkstruktur:** Sinnvolle Segmentierung und Adressierung

#### Methodisches Vorgehen (25%)
- **Systematische Herangehensweise:** Strukturierte Problemlösung
- **Saubere Dokumentation:** Vollständige und nachvollziehbare Aufzeichnungen
- **Verwendung geeigneter Tools:** Effektiver Einsatz von Software und Hilfsmitteln

#### Kommunikation und Teamarbeit (25%)
- **Fachsprache:** Korrekte Verwendung technischer Begriffe
- **Kooperationsfähigkeit:** Konstruktive Zusammenarbeit in der Gruppe
- **Präsentationsqualität:** Verständliche Darstellung der Ergebnisse

### 6.3 Bewertungsraster für Einzelaufgaben

| Kriterium | Sehr gut (1) | Gut (2) | Befriedigend (3) | Ausreichend (4) |
|-----------|--------------|---------|------------------|-----------------|
| **Fachliche Richtigkeit** | Alle Berechnungen/Konfigurationen korrekt, innovative Lösungsansätze | Lösungen größtenteils korrekt, kleine Ungenauigkeiten | Grundlegende Lösungen korrekt, einige Fehler | Grundverständnis erkennbar, mehrere Fehler |
| **Dokumentation** | Vollständig, übersichtlich, professionell, nachvollziehbar | Vollständig und strukturiert | Weitgehend vollständig, teilweise unstrukturiert | Grundlegende Dokumentation vorhanden |
| **Reflexion** | Tiefgehende Analyse, kritische Bewertung, Transferleistung | Gute Reflexion, einige kritische Punkte | Oberflächliche Reflexion, wenig kritische Betrachtung | Minimale Reflexion |

### 6.4 Bewertung des Abschlussprojekts (Aufgabe 5)

**Technische Umsetzung (60%)**
- Vollständigkeit des Netzwerkdesigns
- Korrektheit der Konfigurationen
- Funktionsfähigkeit der Implementierung
- Berücksichtigung von Sicherheitsaspekten

**Projektdokumentation (25%)**
- Strukturierte Darstellung
- Nachvollziehbarkeit der Entscheidungen
- Professionalität der Dokumentation
- Vollständigkeit der Angaben

**Präsentation (15%)**
- Verständliche Erklärung technischer Zusammenhänge
- Souveräner Umgang mit Fragen
- Einhaltung der Zeitvorgaben
- Verwendung der Fachsprache

---

## 7. Lernunterstützung und Hilfsmittel

### 7.1 Empfohlene Software-Tools

**Für alle Aufgaben verfügbar:**

🔧 **Cisco Packet Tracer** (Kostenlos über Cisco Networking Academy)
- Netzwerksimulation für alle praktischen Übungen
- Umfangreiche Geräte-Bibliothek
- Integrierte Lernaktivitäten

🔧 **Advanced IP Scanner** (Kostenlos)
- Netzwerk-Scanning und -Analyse
- Erkennung aktiver Geräte
- Port-Scanning-Funktionen

🔧 **Wireshark** (Open Source)
- Professionelle Paketanalyse
- Protokoll-Dekodierung
- Netzwerk-Troubleshooting

🔧 **Online-Subnetting-Rechner**
- subnet-calculator.com
- Kontrolle Ihrer Berechnungen
- Visuelle Darstellung von Subnetzen

### 7.2 Referenzmaterialien und Dokumentation

**📚 Immer griffbereit:**

**Subnetzmasken-Referenz:**
```
CIDR  | Subnetzmaske      | Anzahl Hosts
------|-------------------|-------------
/24   | 255.255.255.0    | 254
/25   | 255.255.255.128  | 126
/26   | 255.255.255.192  | 62
/27   | 255.255.255.224  | 30
/28   | 255.255.255.240  | 14
/29   | 255.255.255.248  | 6
/30   | 255.255.255.252  | 2
```

**Standard-Ports (Auswahl):**
```
HTTP:    80      | HTTPS:   443
SSH:     22      | Telnet:  23
FTP:     21      | TFTP:    69
DNS:     53      | DHCP:    67/68
SNMP:    161     | POP3:    110
```

**Private IP-Bereiche:**
```
Klasse A: 10.0.0.0/8        (10.0.0.0 - 10.255.255.255)
Klasse B: 172.16.0.0/12     (172.16.0.0 - 172.31.255.255)
Klasse C: 192.168.0.0/16    (192.168.0.0 - 192.168.255.255)
```

### 7.3 Lernunterstützung bei Problemen

**🆘 Schnelle Hilfe:**

1. **FAQ-Sektion:** Häufige Fragen und Antworten zu jeder Aufgabe
2. **Video-Tutorials:** Schritt-für-Schritt Anleitungen für schwierige Konzepte
3. **Peer-Learning-Forum:** Austausch mit anderen Lernenden
4. **Sprechstunden:** Persönliche Beratung durch Lehrende

**🔍 Problemlösungs-Strategie:**
1. Problembeschreibung konkretisieren
2. Fehlermeldungen dokumentieren
3. Bisherige Lösungsversuche auflisten
4. Hilfe im Forum oder Sprechstunde suchen

---

## 8. Sicherheitshinweise

### Allgemeine Regeln
- **Passwort-Sicherheit:** Verwenden Sie sichere Passwörter für alle Netzwerkgeräte
- **Dokumentation:** Führen Sie ein Änderungsprotokoll für alle Konfigurationen
- **Backup:** Erstellen Sie Sicherungskopien aller Konfigurationsdateien

### Labor-Sicherheit
- **Isoliertes Netzwerk:** Arbeiten Sie nur im Labor-Netzwerk
- **Keine Produktivsysteme:** Konfigurieren Sie niemals echte Produktionsgeräte
- **Datenschutz:** Verwenden Sie keine echten Unternehmensdaten

---

## 9. Reflexionsfragen

Denken Sie nach dem Abschluss der Aufgaben über folgende Fragen nach:

### Technische Reflexion
1. Welche Herausforderungen hatten Sie beim Subnetting?
2. Wo lagen die Hauptschwierigkeiten bei der Gerätekonfiguration?
3. Welche Lösungsalternativen hätte es gegeben?

### Methodische Reflexion
1. Wie sind Sie bei der Problemlösung vorgegangen?
2. Welche Tools haben Ihnen am meisten geholfen?
3. Was würden Sie beim nächsten Mal anders machen?

### Übertragung in die Praxis
1. Wie könnten Sie diese Kenntnisse bei echten Veranstaltungen anwenden?
2. Welche zusätzlichen Aspekte sind in der Praxis zu beachten?
3. Welche Weiterbildungsmöglichkeiten interessieren Sie?

---

## 10. Weiterführende Ressourcen

### Online-Lernplattformen
- **Cisco Networking Academy** (netacad.com)
- **Subnetting.org** - Interaktive Übungen
- **GNS3 Academy** - Erweiterte Simulationen

### Fachbücher
- Tanenbaum: "Computernetzwerke" (Grundlagenwerk)
- Kurose/Ross: "Computernetzwerke" (Praxisorientiert)
- Cisco Press: "CCNA Study Guides" (Zertifizierungsvorbereitung)

### Praktische Vertiefung
- **Raspberry Pi Projekte:** Eigene Netzwerkdienste aufsetzen
- **Homelab:** Aufbau eines eigenen Testlabors
- **Zertifizierungen:** CCNA, CompTIA Network+

---

## Schlusswort

Herzlichen Glückwunsch! Sie haben erfolgreich die Grundlagen der Netzwerktechnik in der Veranstaltungstechnik erarbeitet. Diese Kenntnisse bilden das Fundament für viele weitere Themen in Ihrem Berufsfeld.

**Nächste Schritte:**
- Vertiefen Sie Ihre Kenntnisse durch praktische Projekte
- Bleiben Sie über neue Technologien informiert
- Nutzen Sie Gelegenheiten für Weiterbildungen

**Denken Sie daran:** Netzwerktechnik ist ein sich schnell entwickelndes Feld. Lebenslanges Lernen ist der Schlüssel zum Erfolg!

---

**Viel Erfolg bei Ihrer weiteren Ausbildung!**

*Multi-Media Berufsbildende Schulen*  
*Fachbereich Veranstaltungstechnik*
