# 📝 Test-Übersicht: Netzwerktechnik (Kapitel 2 - Aufgaben 4* & 5*)

**Themen:** Switches, Router, VLANs  
**Anzahl Fragen:** 25 (davon 7 mit SVG-Grafiken)  
**Zielgruppe:** Fachkraft für Veranstaltungstechnik, 3. Ausbildungsjahr  
**Erstellt:** Februar 2026

---

## **Teil A: Switches und Router (10 Fragen)**

### Frage 1 ⭐ Leicht
**Typ:** multichoice (single)  
**Punkte:** 1-2

**Frage:**  
Was ist der Hauptunterschied zwischen einem Switch und einem Router?

**Antwortmöglichkeiten:**
- [ ] Ein Switch arbeitet auf Layer 3, ein Router auf Layer 2
- [x] Ein Switch verbindet Geräte innerhalb eines Netzwerks, ein Router verbindet verschiedene Netzwerke
- [ ] Ein Switch ist schneller als ein Router
- [ ] Ein Switch nutzt IP-Adressen, ein Router nutzt MAC-Adressen

---

### Frage 2 ⭐⭐ Mittel
**Typ:** ddmatch (Zuordnung)  
**Punkte:** 3-4

**Frage:**  
Ordnen Sie die folgenden Begriffe den richtigen Definitionen zu:

**Links (Begriffe):**
- MAC-Adresse
- IP-Adresse
- Layer 2
- Layer 3
- Broadcast-Domain
- Collision-Domain

**Rechts (Definitionen):**
- Physische Adresse einer Netzwerkkarte (Hardware-Adresse)
- Logische Adresse zur Identifikation in einem Netzwerk
- Sicherungsschicht im OSI-Modell (Switches arbeiten hier)
- Vermittlungsschicht im OSI-Modell (Router arbeiten hier)
- Bereich, in dem Broadcast-Pakete alle Geräte erreichen
- Bereich, in dem Kollisionen auftreten können (bei Hubs)

---

### Frage 3 ⭐ Leicht
**Typ:** ddwtos (Lückentext mit Drag-and-Drop)  
**Punkte:** 2

**Frage:**  
Ein Switch lernt MAC-Adressen durch Analyse der [[1]]-Adresse eingehender Frames und speichert diese in der [[2]].

**Begriffe zum Einsetzen:**
- Gruppe 1: Quell, Ziel, IP
- Gruppe 2: MAC-Address-Table, Routing-Tabelle, ARP-Cache

**Lösung:** Quell, MAC-Address-Table

---

### Frage 4 ⭐⭐⭐ Schwer
**Typ:** essay (Freitext)  
**Punkte:** 5-6

**Frage:**  
Beschreiben Sie den Paketfluss, wenn ein Gerät mit IP 192.168.1.10 ein Paket an 10.0.0.50 sendet und beide Netze durch einen Router verbunden sind.

**Erwartungshorizont:**
- Gerät erkennt, dass Ziel-IP in anderem Netzwerk liegt
- Paket wird an Gateway (Router) gesendet
- Router empfängt Paket, prüft Routing-Tabelle
- Router ändert MAC-Adressen (Source und Destination)
- Router leitet Paket ins Zielnetzwerk weiter
- TTL wird dekrementiert

---

### Frage 5 ⭐⭐ Mittel
**Typ:** multichoice (multi) - 3 richtig aus 6  
**Punkte:** 3-4

**Frage:**  
Welche Aussagen zu Switches sind korrekt? (Mehrfachauswahl)

**Antwortmöglichkeiten:**
- [x] Switches lernen MAC-Adressen dynamisch
- [x] Switches reduzieren Kollisionen durch separate Collision-Domains
- [ ] Switches können verschiedene Netzwerke miteinander verbinden
- [x] Switches arbeiten standardmäßig auf Layer 2 des OSI-Modells
- [ ] Switches nutzen die Routing-Tabelle zur Weiterleitung
- [ ] Switches erhöhen Broadcasts im gesamten Netzwerk

**Punkteverteilung:** Jede richtige = +33%, jede falsche = -17%

---

### Frage 6 ⭐ Leicht
**Typ:** shortanswer  
**Punkte:** 1

**Frage:**  
Auf welcher OSI-Schicht arbeitet ein Standard-Switch?

**Akzeptierte Antworten:**
- Layer 2
- Schicht 2
- Sicherungsschicht
- Data Link Layer

---

### Frage 7 ⭐⭐ Mittel
**Typ:** ddmatch (Zuordnung)  
**Punkte:** 3

**Frage:**  
Ordnen Sie die Port-Geschwindigkeiten den passenden Anwendungsfällen in der Veranstaltungstechnik zu:

**Links (Geschwindigkeiten):**
- 100 Mbit/s (Fast Ethernet)
- 1 Gbit/s (Gigabit Ethernet)
- 10 Gbit/s (10GbE)

**Rechts (Anwendungen):**
- DMX-Steuerung, einfache Netzwerkgeräte
- Dante-Audio (64 Kanäle), HD-Video-Streaming
- 4K-Video, Backbone-Verbindungen, NDI-HX3

---

### Frage 8 ⭐ Leicht
**Typ:** multichoice (multi)  
**Punkte:** 2

**Frage:**  
Welche der folgenden Angaben finden Sie typischerweise in einem Switch-Datenblatt?

**Antwortmöglichkeiten:**
- [x] Anzahl der Ports
- [x] Port-Geschwindigkeiten (z.B. 1 Gbit/s)
- [x] Switching-Kapazität (z.B. 52 Gbps)
- [x] VLAN-Unterstützung
- [ ] CPU-Taktrate des Switches
- [x] PoE-Leistung pro Port

---

### Frage 9 ⭐⭐ Mittel 🎨 MIT SVG
**Typ:** ddimageortext (Drag-Drop auf SVG-Grafik)  
### Frage 11 ⭐ Leicht

**Frage:**  
Ordnen Sie die Netzwerkkomponenten den nummerierten Positionen im Diagramm zu.

**SVG-Diagramm:** Netzwerktopologie mit Switch und Router

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400" viewBox="0 0 600 400">
  <defs>
    <style>
      .device-box { fill: #e3f2fd; stroke: #1976d2; stroke-width: 2; }
      .router-box { fill: #fff3e0; stroke: #f57c00; stroke-width: 2; }
      .line { stroke: #333; stroke-width: 2; }
      .text { font-family: Arial; font-size: 12px; fill: #333; }
      .label-circle { fill: #c00; stroke: #fff; stroke-width: 1.5; }
      .label-text { font-family: Arial; font-size: 11px; fill: #fff; font-weight: bold; }
    </style>
  </defs>
  
  <!-- Netzwerk A (links) -->
  <text x="50" y="30" class="text" font-weight="bold">Netzwerk A: 192.168.1.0/24</text>
  
  <!-- Switch -->
  <rect x="70" y="80" width="120" height="80" class="device-box" rx="5"/>
  <text x="130" y="115" class="text" text-anchor="middle" font-weight="bold">Switch</text>
  <text x="130" y="135" class="text" text-anchor="middle" font-size="10">Layer 2</text>
  
  <!-- Position 1: Switch -->
  <circle cx="20" cy="120" r="11" class="label-circle"/>
  <text x="20" y="124" class="label-text" text-anchor="middle">1</text>
  
  <!-- Geräte an Switch -->
  <rect x="70" y="200" width="80" height="40" class="device-box" rx="3"/>
  <text x="110" y="225" class="text" text-anchor="middle" font-size="10">PC 1</text>
  
  <rect x="70" y="260" width="80" height="40" class="device-box" rx="3"/>
  <text x="110" y="285" class="text" text-anchor="middle" font-size="10">PC 2</text>
  
  <!-- Verbindungen -->
  <line x1="130" y1="160" x2="110" y2="200" class="line"/>
  <line x1="130" y1="160" x2="110" y2="260" class="line"/>
  
  <!-- Netzwerk B (rechts) -->
  <text x="380" y="30" class="text" font-weight="bold">Netzwerk B: 10.0.0.0/24</text>
  
  <!-- Router in der Mitte -->
  <rect x="260" y="100" width="100" height="60" class="router-box" rx="5"/>
  <text x="310" y="128" class="text" text-anchor="middle" font-weight="bold">Router</text>
  <text x="310" y="145" class="text" text-anchor="middle" font-size="10">Layer 3</text>
  
  <!-- Position 2: Router -->
  <circle cx="580" cy="130" r="11" class="label-circle"/>
  <text x="580" y="134" class="label-text" text-anchor="middle">2</text>
  
  <!-- Verbindung Switch-Router -->
  <line x1="190" y1="120" x2="260" y2="130" class="line"/>
  <text x="225" y="115" class="text" font-size="9">eth0</text>
  
  <!-- Server im Netzwerk B -->
  <rect x="420" y="110" width="80" height="40" class="device-box" rx="3"/>
  <text x="460" y="135" class="text" text-anchor="middle" font-size="10">Server</text>
  
  <!-- Verbindung Router-Server -->
  <line x1="360" y1="130" x2="420" y2="130" class="line"/>
  <text x="390" y="120" class="text" font-size="9">eth1</text>
  
  <!-- MAC vs IP Labels -->
  <rect x="80" y="330" width="160" height="50" fill="#f0f0f0" stroke="#666" stroke-width="1" rx="3"/>
  <text x="160" y="350" class="text" text-anchor="middle" font-size="10" font-weight="bold">Position 3:</text>
  <text x="160" y="365" class="text" text-anchor="middle" font-size="9">Arbeitet mit</text>
  <text x="160" y="378" class="text" text-anchor="middle" font-size="9">MAC-Adressen</text>
  
  <circle cx="569" cy="355" r="11" class="label-circle"/>
  <text x="569" y="359" class="label-text" text-anchor="middle">3</text>
  
  <rect x="360" y="330" width="160" height="50" fill="#f0f0f0" stroke="#666" stroke-width="1" rx="3"/>
  <text x="440" y="350" class="text" text-anchor="middle" font-size="10" font-weight="bold">Position 4:</text>
  <text x="440" y="365" class="text" text-anchor="middle" font-size="9">Arbeitet mit</text>
  <text x="440" y="378" class="text" text-anchor="middle" font-size="9">IP-Adressen</text>
  
  <circle cx="20" cy="355" r="11" class="label-circle"/>
  <text x="20" y="359" class="label-text" text-anchor="middle">4</text>
</svg>
```

**Drag-Items (Begriffe zum Zuordnen):**
1. Switch (Layer 2 Gerät)
2. Router (Layer 3 Gerät)
3. MAC-Address-Table
4. Routing-Tabelle
5. Hub (Distractor)
6. Modem (Distractor)

**Drop-Zonen (Koordinaten):**
- Position 1 (Switch-Label): xleft=9, ytop=109
- Position 2 (Router-Label): xleft=569, ytop=119
- Position 3 (MAC-Box): xleft=558, ytop=344
- Position 4 (IP-Box): xleft=9, ytop=344

**Hinweis:** Es gibt 2 zusätzliche Begriffe, die nicht passen.

**Lösung:**
- Position 1 → Switch (Layer 2 Gerät)
- Position 2 → Router (Layer 3 Gerät)
- Position 3 → MAC-Address-Table
- Position 4 → Routing-Tabelle

**Template:** `template-ddimageortext-drag-auf-svg.xml`

---

### Frage 10 ⭐⭐ Mittel 🎨 MIT SVG
**Typ:** multichoice (single) mit SVG-Diagramm  
**Punkte:** 3

**Frage:**  
Betrachten Sie das OSI-Modell-Diagramm. Auf welcher Schicht arbeitet ein Standard-Switch?

**SVG-Diagramm:** OSI-Schichten-Modell

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="400" height="320" viewBox="0 0 400 320">
  <defs>
    <style>
      .layer { fill: #e3f2fd; stroke: #1976d2; stroke-width: 2; }
      .layer-highlight { fill: #ffeb3b; stroke: #f57c00; stroke-width: 3; }
      .layer-text { font-family: Arial; font-size: 14px; fill: #333; font-weight: bold; }
      .layer-desc { font-family: Arial; font-size: 10px; fill: #666; }
    </style>
  </defs>
  
  <!-- Layer 7 -->
  <rect x="50" y="20" width="300" height="35" class="layer" rx="3"/>
  <text x="200" y="40" class="layer-text" text-anchor="middle">7. Anwendungsschicht</text>
  
  <!-- Layer 6 -->
  <rect x="50" y="60" width="300" height="35" class="layer" rx="3"/>
  <text x="200" y="80" class="layer-text" text-anchor="middle">6. Darstellungsschicht</text>
  
  <!-- Layer 5 -->
  <rect x="50" y="100" width="300" height="35" class="layer" rx="3"/>
  <text x="200" y="120" class="layer-text" text-anchor="middle">5. Sitzungsschicht</text>
  
  <!-- Layer 4 -->
  <rect x="50" y="140" width="300" height="35" class="layer" rx="3"/>
  <text x="200" y="160" class="layer-text" text-anchor="middle">4. Transportschicht</text>
  
  <!-- Layer 3 - Router -->
  <rect x="50" y="180" width="300" height="35" class="layer" rx="3"/>
  <text x="140" y="200" class="layer-text" text-anchor="middle">3. Vermittlungsschicht</text>
  <text x="280" y="200" class="layer-desc" text-anchor="middle" fill="#f57c00">(Router)</text>
  
  <!-- Layer 2 - Switch (HIGHLIGHTED) -->
  <rect x="50" y="220" width="300" height="35" class="layer-highlight" rx="3"/>
  <text x="140" y="240" class="layer-text" text-anchor="middle">2. Sicherungsschicht</text>
  <text x="280" y="240" class="layer-desc" text-anchor="middle" fill="#f57c00">(Switch)</text>
  
  <!-- Layer 1 -->
  <rect x="50" y="260" width="300" height="35" class="layer" rx="3"/>
  <text x="200" y="280" class="layer-text" text-anchor="middle">1. Bitübertragungsschicht</text>
</svg>
```

**Antwortmöglichkeiten:**
- [ ] Layer 1 (Bitübertragungsschicht)
- [x] Layer 2 (Sicherungsschicht)
- [ ] Layer 3 (Vermittlungsschicht)
- [ ] Layer 4 (Transportschicht)

**Template:** `template-multichoice-mit-svg.xml`

---

## **Teil B: VLANs - Grundlagen (8 Fragen)**

### Frage 9 ⭐ Leicht
**Typ:** shortanswer  
**Punkte:** 1

**Frage:**  
Was bedeutet die Abkürzung VLAN?

**Akzeptierte Antworten:**
- Virtual Local Area Network
- Virtuelles lokales Netzwerk

---

### Frage 12 ⭐⭐ Mittel
**Typ:** ddmatch (Zuordnung)  
**Punkte:** 4

**Frage:**  
Ordnen Sie die Vorteile von VLANs den richtigen Kategorien zu:

**Links (Vorteile):**
- Trennung von Gäste-WLAN und Produktivnetz
- Broadcast-Kontrolle durch Segmentierung
- Geräte können logisch gruppiert werden (unabhängig vom Standort)
- Vereinfachte Fehlersuche in einzelnen Segmenten
- Netzwerkverkehr zwischen VLANs kann kontrolliert werden
- Neue Geräte durch Port-Konfiguration zuweisen

**Rechts (Kategorien):**
- Sicherheit
- Performance
- Flexibilität
- Verwaltung

---

### Frage 13 ⭐⭐ Mittel
**Typ:** cloze (eingebettete Antworten)  
**Punkte:** 3

**Frage:**  
VLANs basieren auf dem Standard {1:SHORTANSWER:=IEEE 802.1Q~=802.1Q}. Jedes VLAN erhält eine eindeutige ID im Bereich von {1:NUMERICAL:=1:0} bis {1:NUMERICAL:=4094:0}.

---

### Frage 14 ⭐⭐ Mittel
**Typ:** essay (Freitext)  
**Punkte:** 3-4

**Frage:**  
Erklären Sie, warum es sinnvoll ist, Dante-Audio in einem separaten VLAN zu betreiben.

**Erwartungshorizont:**
- Dante benötigt geringe Latenz (< 1 ms typisch)
- Isolation von anderem Netzwerkverkehr (Broadcasts, Video-Traffic)
- Quality of Service (QoS) kann gezielt für Audio-VLAN konfiguriert werden
- Vermeidung von Paketverlusten durch Priorisierung
- Sicherheit: Produktiv-Audio von Gäste-WLAN getrennt
- Broadcast-Kontrolle (Dante nutzt Multicast)

---

### Frage 15 ⭐⭐⭐ Schwer
**Typ:** multichoice (multi)  
**Punkte:** 5

**Frage:**  
Welche Aussagen zu Broadcast-Domains und VLANs sind richtig?

**Antwortmöglichkeiten:**
- [x] Jedes VLAN bildet eine eigene Broadcast-Domain
- [x] Broadcasts in VLAN 10 erreichen nicht VLAN 20
- [ ] Ein Switch ohne VLANs hat mehrere Broadcast-Domains
- [x] Art-Net-Broadcasts bleiben innerhalb des Licht-VLANs
- [ ] VLANs vergrößern die Broadcast-Domain
- [x] Durch VLAN-Segmentierung wird die Netzwerk-Performance verbessert

**Punkteverteilung:** 4 richtig, je 25% pro richtiger Antwort, -12% pro falscher

---

### Frage 16 ⭐⭐⭐ Schwer
**Typ:** ordering ⚠️ (Plugin benötigt)  
**Punkte:** 5

**Frage:**  
Bringen Sie die Schritte beim VLAN-Tagging in die richtige Reihenfolge:

**Richtige Reihenfolge:**
1. Switch empfängt untagged Frame von Endgerät
2. Switch identifiziert das VLAN anhand des Access-Ports
3. Switch fügt 802.1Q-Tag mit VLAN-ID in Frame ein
4. Frame wird über Trunk-Port zum nächsten Switch gesendet
5. Empfangender Switch liest VLAN-Tag aus Frame
6. Switch entfernt Tag vor Weitersendung an Endgerät über Access-Port

---

### Frage 17 ⭐⭐ Mittel 🎨 MIT SVG
**Typ:** ddwtos (Lückentext mit SVG-Prozessdiagramm)  
### Frage 19 ⭐⭐ Mittel

**Frage:**  
Ergänzen Sie die Lücken im Text zum VLAN-Tagging-Prozess.

**SVG-Diagramm:** VLAN-Tagging-Prozess

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200" viewBox="0 0 600 200">
  <defs>
    <style>
      .process-box { fill: #e3f2fd; stroke: #1976d2; stroke-width: 2; }
      .arrow { fill: none; stroke: #333; stroke-width: 2; marker-end: url(#arrowhead); }
      .text { font-family: Arial; font-size: 11px; fill: #333; }
      .title { font-family: Arial; font-size: 12px; fill: #333; font-weight: bold; }
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Schritt 1: Eingabe -->
  <rect x="20" y="60" width="100" height="60" class="process-box" rx="5"/>
  <text x="70" y="85" class="title" text-anchor="middle">Endgerät</text>
  <text x="70" y="102" class="text" text-anchor="middle">sendet Frame</text>
  <text x=20 ⭐⭐ Mittel
**Typ:** cloze (eingebettete Antworten)  
**Punkte:** 3

**Frage:**  
Ein {1:SHORTANSWER:=Access~=Access-Port}-Port überträgt Daten nur für ein einziges VLAN, während ein {1:SHORTANSWER:=Trunk~=Trunk-Port}-Port mehrere VLANs gleichzeitig transportieren kann. Traffic auf Access-Ports ist {1:MULTICHOICE:=untagged~tagged}.

---

### Frage 21 ⭐⭐ Mittel 🎨 MIT SVG
**Typ:** ddmatch mit SVG-Diagramm  
**Punkte:** 4

**Frage:**  
Ordnen Sie die Port-Konfigurationen im Diagramm den Beschreibungen zu.

**SVG-Diagramm:** Switch-Port-Konfiguration

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="500" height="280" viewBox="0 0 500 280">
  <defs>
    <style>
      .switch-body { fill: #e3f2fd; stroke: #1976d24 Fragen)**

### Frage 23trunk { fill: #ff9800; stroke: #e65100; stroke-width: 2; }
      .device { fill: white; stroke: #333; stroke-width: 1.5; }
      .line-vlan10 { stroke: #ffeb3b; stroke-width: 3; }
      .line-vlan20 { stroke: #4caf50; stroke-width: 3; }
      .line-trunk { stroke: #ff9800; stroke-width: 3; }
      .text { font-family: Arial; font-size: 10px; fill: #333; }
      .label { font-family: Arial; font-size: 12px; fill: #333; font-weight: bold; }
    </style>
  </defs>
  
  <!-- Switch -->
  <rect x="180" y="100" width="140" height="80" class="switch-body" rx="5"/>
  <text x="250" y="130" class="label" text-anchor="middle">Switch SW-01</text>
  <text x="250" y="148" class="text" text-anchor="middle">Cisco SG350</text>
  
  <!-- Port 1 - Access VLAN 10 -->
  <rect x="185" y="120" width="25" height="12" class="port-access" rx="2"/>
  <text x=24 ⭐⭐ Mittel
**Typ:** multichoice (multi)  
**Punkte:** 3

**Frage:**  
Welche Geräte sind für Inter-VLAN-Routing geeignet?

**Antwortmöglichkeiten:**
- [ ] Layer-2-Switch (unmanaged)
- [x] Layer-3-Switch (Multilayer-Switch)
- [x] Router
- [ ] Hub
- [x] Firewall mit Routing-Funktionen
- [ ] Access Point

**Punkteverteilung:** 3 richtig, je 33,33%

---

### Frage 25 ⭐⭐⭐ Schwer 🎨 MIT SVG
**Typ:** ddimageortext (Drag-Drop auf SVG) + essay  
**Punkte:** 6

**Frage:**  
**Teil A:** Ordnen Sie im Diagramm die richtigen Gateway-Adressen den VLANs zu.  
**Teil B:** Beschreiben Sie, wie ein Paket von PC1 (VLAN 10) zu PC2 (VLAN 20) geroutet wird.

**SVG-Diagramm:** Inter-VLAN-Routing mit Layer-3-Switch

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="550" height="380" viewBox="0 0 550 380">
  <defs>
    <style>
      .vlan-box { fill-opacity: 0.2; stroke-width: 2; }
      .vlan10-box { fill: #ffeb3b; stroke: #f57f17; }
      .vlan20-box { fill: #4caf50; stroke: #2e7d32; }
      .l3switch { fill: #f3e5f5; stroke: #7b1fa2; stroke-width: 2; }
      .device { fill: white; stroke: #333; stroke-width: 1.5; }
      .gateway { fill: #fff3e0; stroke: #e65100; stroke-width: 2; }
      .text { font-family: Arial; font-size: 10px; fill: #333; }
      .label { font-family: Arial; font-size: 12px; fill: #333; font-weight: bold; }
      .label-circle { fill: #c00; stroke: #fff; stroke-width: 1.5; }
      .label-text { font-family: Arial; font-size: 11px; fill: #fff; font-weight: bold; }
    </style>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
  
  <!-- Layer-3-Switch in der Mitte -->
  <rect x="200" y="150" width="150" height="80" class="l3switch" rx="5"/>
  <text x="275" y="175" class="label" text-anchor="middle">Layer-3-Switch</text>
  <text x="275" y="192" class="text" text-anchor="middle">Inter-VLAN-Routing</text>
  <text x="275" y="210" class="text" text-anchor="middle" font-size="9">VLAN 10: 10.10.10.0/24</text>
  <text x="275" y="222" class="text" text-anchor="middle" font-size="9">VLAN 20: 10.10.20.0/24</text>
  
  <!-- VLAN 10 oben links -->
  <rect x="30" y="30" width="140" height="100" class="vlan-box vlan10-box" rx="5"/>
  <text x="100" y="50" class="label" text-anchor="middle">VLAN 10 - Audio</text>
  <text x="100" y="65" class="text" text-anchor="middle" font-size="9">10.10.10.0/24</text>
  
  <rect x="50" y="80" width="100" height="35" class="device" rx="3"/>
  <text x="100" y="95" class="text" text-anchor="middle" font-weight="bold">PC1</text>
  <text x="100" y="107" class="text" text-anchor="middle" font-size="9">IP: 10.10.10.10</text>
  
  <!-- Gateway-Box VLAN 10 -->
  <rect x="220" y="50" width="110" height="30" class="gateway" rx="3"/>
  <text x="275" y="65" class="text" text-anchor="middle" font-weight="bold">Gateway VLAN 10:</text>
  <text x="275" y="77" class="text" text-anchor="middle" font-size="9">Position 1</text>
  <circle cx="569" cy="65"23%)
- **⭐⭐ Mittel:** 15 Fragen (58%)
- **⭐⭐⭐ Schwer:** 5 Fragen (19%)
- **Gesamt:** 26 Fragen

### Fragetyp-Verteilung
| Fragetyp | Anzahl | Prozent | Mit SVG |
|----------|--------|---------|---------|
| multichoice | 6 | 23% | 1 🎨 |
| ddmatch | 5 | 19% | 1 🎨 |
| essay | 4 | 15% | - |
| ddimageortext | 2 | 8% | 2 🎨 |
| cloze | 3 | 12% | 1 🎨 |
| shortanswer | 2 | 8% | - |
| ddwtos | 2 | 8% | 1 🎨 |
| truefalse | 1 | 4% | - |
| ordering ⚠️ | 1 | 4% | - |
| **Mit SVG-Grafik** | **7** | **27%** | ✅ |

### Punkteverteilung
- **Leichte Fragen:** 1-2 Punkte
- **Mittlere Fragen:** 3-4 Punkte
- **Schwere Fragen:** 5-6 Punkte
- **Gesamt:** ca. 90 Punkte

### Bestehensgrenze (Vorschlag)
- **100%:** 90 Punkte (Note 1,0)
- **92%:** 83 Punkte (Note 1,5)
- **81%:** 73 Punkte (Note 2,0)
- **67%:** 60 Punkte (Note 3,0)
- **50%:** 45 Punkte (Note 4,0 - Bestanden)
- **< 50%:** < 45 Punkte (Note 5,0 - Nicht bestanden)

### SVG-Fragen Übersicht
| Frage | Typ | Thema | SVG-Inhalt |
|-------|-----|-------|------------|

**Standard-Templates:**
- `template-multichoice-mehrfachauswahl.xml`
- `template-ddmatch-zuordnung.xml`
- `template-essay-freitext.xml`
- `template-cloze-eingebettete-antworten.xml`
- `template-ddwtos-lueckentext.xml`
- `template-shortanswer-kurzantwort.xml`
- `template-truefalse-wahr-falsch.xml`
- `template-ordering-anordnung.xml` ⚠️ (Plugin benötigt)

**SVG-erweiterte Templates:** 🎨
- `template-ddimageortext-drag-auf-svg.xml` (Fragen 9, 25)
- `template-multichoice-mit-svg.xml` (Frage 10)
- `template-ddwtos-lueckentext-mit-svg.xml` (Frage 17)
- `template-cloze-mit-svg.xml` (Frage 18)
- `template-ddmatch-zuordnung-mit-svg.xml` (Frage 21
```
 - inkl. SVG-Topologie & OSI-Modell
2. **Teil B:** VLAN-Konzepte - inkl. SVG zu Tagging & Broadcast-Domains
3. **Teil C:** VLAN-Konfiguration - inkl. SVG zu Port-Typen
4. **Teil D:** Komplexe Anwendungsszenarien - inkl. SVG zu Inter-VLAN-Routing

### Besondere Merkmale
✅ **7 Fragen mit SVG-Grafiken** für visuelles Lernen  
✅ **Interaktive Drag-Drop-Aufgaben** auf Netzwerkdiagrammen  
✅ **Praxisbezug** durch VT-spezifische Szenarien (Dante, Art-Net, Festival)  
✅ **Kombination** aus Wissensabfrage und Anwendung  
✅ **Skalierbare Vektorgrafiken** ohne Qualitätsverluste

### SVG-Vorteile im Test
- **Visuelles Verständnis:** Netzwerktopologien und Datenflüsse werden sichtbar
- **Realitätsnähe:** Diagramme entsprechen professionellen Netzwerkplänen
- **Interaktivität:** Drag-Drop direkt auf Netzwerkkomponenten
- **Barrierefreiheit:** SVG-Text ist skalierbar und screenreader-kompatibel

---

**Stand:** Februar 2026  
**Autor:** Erstellt für VT-LF10 Netzwerktechnik  
**Basis:** Kapitel 2, Aufgaben 4, 4.1, 5, 5a  
**Besonderheit:** Enthält 7 SVG-basierte Fragen für visuell-interaktives Lernenp=274

**Lösung Teil A:**
- Position 1 → 10.10.10.1
- Position 2 → 10.10.20.1

**Teil B - Essay-Frage:**  
Beschreiben Sie den Routing-Pfad eines Pakets von PC1 (10.10.10.10) zu PC2 (10.10.20.10).

**Erwartungshorizont Teil B:**
1. PC1 erkennt: Ziel-IP (10.10.20.10) liegt in anderem Subnetz
2. PC1 sendet Paket an sein Gateway (10.10.10.1 = VLAN-Interface des L3-Switch)
3. Layer-3-Switch empfängt Paket in VLAN 10
4. Switch prüft Routing-Tabelle: 10.10.20.0/24 → VLAN 20
5. Switch leitet Paket intern an VLAN-Interface 10.10.20.1 weiter
6. Switch sendet Paket über Access-Port in VLAN 20
7. PC2 empfängt Paket
8. TTL wird dekrementiert, MAC-Adressen werden geändert

**Bonus-Punkte:** Erwähnung von ARP-Requests für MAC-Adressauflösung

**Template:** `template-ddimageortext-drag-auf-svg.xml` + essay-Ergänzung

---

### Frage 26
  <rect x="70" y="145" width="60" height="25" class="device" rx="3"/>
  <text x="100" y="162" class="text" text-anchor="middle" font-size="9">Audio</text>
  <text x="100" y="168" class="text" text-anchor="middle" font-size="6">VLAN 10</text>
  <line x1="130" y1="157" x2="185" y2="147" class="line-vlan10"/>
  
  <rect x="70" y="175" width="60" height="25" class="device" rx="3"/>
  <text x="100" y="192" class="text" text-anchor="middle" font-size="9">Lichtpult</text>
  <text x="100" y="198" class="text" text-anchor="middle" font-size="6">VLAN 20</text>
  <line x1="130" y1="187" x2="185" y2="167" class="line-vlan20"/>
  
  <!-- Switch rechts (Trunk) -->
  <rect x="370" y="120" width="70" height="40" class="switch-body" rx="3"/>
  <text x="405" y="140" class="text" text-anchor="middle" font-weight="bold">SW-02</text>
  <text x="405" y="152" class="text" text-anchor="middle" font-size="8">Core Switch</text>
  <line x1="315" y1="145" x2="370" y2="145" class="line-trunk"/>
  <text x="342" y="140" class="text" text-anchor="middle" font-size="8">VLAN 10+20</text>
  
  <!-- Legende -->
  <rect x="20" y="230" width="460" height="40" fill="#f5f5f5" stroke="#999" stroke-width="1" rx="3"/>
  <rect x="30" y="238" width="15" height="8" class="port-access"/>
  <text x="50" y="245" class="text" font-size="9">= Access-Port (untagged, 1 VLAN)</text>
  
  <rect x="30" y="254" width="15" height="12" class="port-trunk"/>
  <text x="50" y="263" class="text" font-size="9">= Trunk-Port (tagged, mehrere VLANs)</text>
</svg>
```

**Zuordnung:**
- Port 1
- Port 2
- Port 3
- Port 4

**Definitionen:**
- Access-Port für VLAN 10
- Access-Port für VLAN 20
- Trunk-Port für Switch-Verbindung
- Ungenutzter Port (Distractor)

**Lösung:**
- Port 1 → Access-Port für VLAN 10
- Port 2 → Access-Port für VLAN 10
- Port 3 → Access-Port für VLAN 20
- Port 4 → Trunk-Port für Switch-Verbindung

**Template:** `template-ddmatch-zuordnung-mit-svg.xml`

---

### Frage 2220" y="102" class="text" text-anchor="middle">fügt 802.1Q</text>
  <text x="220" y="115" class="text" text-anchor="middle">Tag hinzu</text>
  
  <!-- Pfeil 2 -->
  <path d="M 270 90 L 330 90" class="arrow"/>
  <text x="300" y="85" class="text" text-anchor="middle" font-size="9">Trunk-Port</text>
  
  <!-- Schritt 3: Transport -->
  <rect x="330" y="60" width="100" height="60" class="process-box" rx="5"/>
  <text x="380" y="85" class="title" text-anchor="middle">Netzwerk</text>
  <text x="380" y="102" class="text" text-anchor="middle">Frame mit</text>
  <text x="380" y="115" class="text" text-anchor="middle" fill="#d84315">VLAN-Tag</text>
  
  <!-- Pfeil 3 -->
  <path d="M 430 90 L 480 90" class="arrow"/>
  
  <!-- Schritt 4: Ausgabe -->
  <rect x="480" y="60" width="100" height="60" class="process-box" rx="5"/>
  <text x="530" y="85" class="title" text-anchor="middle">Switch 2</text>
  <text x="530" y="102" class="text" text-anchor="middle">entfernt Tag</text>
  <text x="530" y="115" class="text" text-anchor="middle">→ untagged</text>
  
  <!-- Legende -->
  <rect x="20" y="150" width="560" height="35" fill="#f5f5f5" stroke="#999" stroke-width="1" rx="3"/>
  <text x="300" y="170" class="text" text-anchor="middle" font-weight="bold">802.1Q-Tagging zwischen Switches über Trunk-Ports</text>
</svg>
```

**Lückentext:**  
Ein Frame wird von einem Endgerät an einen [[1]]-Port gesendet. Der Switch fügt einen [[2]]-Tag mit der VLAN-ID hinzu. Der Frame wird über einen [[3]]-Port weitergeleitet. Beim Empfang über einen Access-Port wird der Tag [[4]].

**Begriffe zum Einsetzen:**
- Gruppe 1: Access, Trunk, Management
- Gruppe 2: 802.1Q, 802.3, QoS
- Gruppe 3: Trunk, Access, Uplink
- Gruppe 4: entfernt, verdoppelt, weitergeleitet

**Lösung:** Access, 802.1Q, Trunk, entfernt

**Template:** `template-ddwtos-lueckentext-mit-svg.xml`

---

### Frage 18 ⭐⭐ Mittel 🎨 MIT SVG
**Typ:** cloze mit SVG-Diagramm  
**Punkte:** 4

**Frage:**  
Analysieren Sie das Broadcast-Domain-Diagramm und beantworten Sie die Fragen.

**SVG-Diagramm:** Broadcast-Domains in VLANs

```xml
<svg xmlns="http://www.w3.org/2000/svg" width="500" height="300" viewBox="0 0 500 300">
  <defs>
    <style>
      .vlan-area { fill-opacity: 0.3; stroke-width: 3; stroke-dasharray: 5,5; }
      .vlan10 { fill: #ffeb3b; stroke: #f57f17; }
      .vlan20 { fill: #4caf50; stroke: #2e7d32; }
      .device { fill: white; stroke: #333; stroke-width: 2; }
      .switch { fill: #e3f2fd; stroke: #1976d2; stroke-width: 2; }
      .text { font-family: Arial; font-size: 11px; fill: #333; }
      .label { font-family: Arial; font-size: 13px; fill: #333; font-weight: bold; }
    </style>
  </defs>
  
  <!-- VLAN 10 (gelb) -->
  <ellipse cx="130" cy="100" rx="110" ry="80" class="vlan-area vlan10"/>
  <text x="130" y="30" class="label" text-anchor="middle">VLAN 10 - Audio</text>
  
  <rect x="80" y="70" width="50" height="30" class="device" rx="3"/>
  <text x="105" y="90" class="text" text-anchor="middle" font-size="9">Mischpult</text>
  
  <rect x="80" y="120" width="50" height="30" class="device" rx="3"/>
  <text x="105" y="140" class="text" text-anchor="middle" font-size="9">Dante I/O</text>
  
  <rect x="150" y="70" width="50" height="30" class="device" rx="3"/>
  <text x="175" y="90" class="text" text-anchor="middle" font-size="9">Stage Box</text>
  
  <!-- VLAN 20 (grün) -->
  <ellipse cx="370" cy="100" rx="110" ry="80" class="vlan-area vlan20"/>
  <text x="370" y="30" class="label" text-anchor="middle">VLAN 20 - Licht</text>
  
  <rect x="320" y="70" width="50" height="30" class="device" rx="3"/>
  <text x="345" y="90" class="text" text-anchor="middle" font-size="9">Lichtpult</text>
  
  <rect x="320" y="120" width="50" height="30" class="device" rx="3"/>
  <text x="345" y="140" class="text" text-anchor="middle" font-size="9">Moving</text>
  <text x="345" y="148" class="text" text-anchor="middle" font-size="7">Heads</text>
  
  <rect x="390" y="70" width="50" height="30" class="device" rx="3"/>
  <text x="415" y="90" class="text" text-anchor="middle" font-size="9">artNET</text>
  <text x="415" y="98" class="text" text-anchor="middle" font-size="7">Node</text>
  
  <!-- Switch in der Mitte -->
  <rect x="215" y="200" width="70" height="50" class="switch" rx="5"/>
  <text x="250" y="220" class="label" text-anchor="middle">Switch</text>
  <text x="250" y="235" class="text" text-anchor="middle" font-size="9">VLAN-fähig</text>
  
  <!-- Verbindungen zu Switch -->
  <line x1="130" y1="150" x2="240" y2="200" stroke="#f57f17" stroke-width="2"/>
  <line x1="370" y1="150" x2="260" y2="200" stroke="#2e7d32" stroke-width="2"/>
  
  <!-- Hinweistext -->
  <text x="250" y="280" class="text" text-anchor="middle" font-size="10" fill="#d32f2f">Broadcasts bleiben im VLAN!</text>
</svg>
```

**Cloze-Frage:**  
Ein Switch ohne VLANs hat {1:NUMERICAL:=1:0} Broadcast-Domain(s). Mit zwei VLANs hat derselbe Switch {1:NUMERICAL:=2:0} Broadcast-Domain(s). Broadcasts in VLAN 10 {1:MULTICHOICE:=erreichen nicht~erreichen} VLAN 20.

**Template:** `template-cloze-mit-svg.xml`

---

## **Teil C: VLANs - Port-Typen (4 Fragen)**

### Frage 15 ⭐⭐ Mittel
**Typ:** ddmatch (Zuordnung)  
**Punkte:** 4

**Frage:**  
Ordnen Sie die Eigenschaften den Port-Typen zu:

**Links (Eigenschaften):**
- Überträgt nur ein VLAN
- Überträgt mehrere VLANs gleichzeitig
- Traffic ist untagged
- Traffic ist tagged (802.1Q)
- Für Endgeräte verwendet
- Verbindet Switches untereinander

**Rechts (Port-Typen):**
- Access-Port
- Trunk-Port

**Zuordnung:**
- Access-Port: Nur ein VLAN, untagged, für Endgeräte
- Trunk-Port: Mehrere VLANs, tagged, verbindet Switches

---

### Frage 16 ⭐⭐ Mittel
**Typ:** cloze (eingebettete Antworten)  
**Punkte:** 3

**Frage:**  
Ein {1:SHORTANSWER:=Access~=Access-Port}-Port überträgt Daten nur für ein einziges VLAN, während ein {1:SHORTANSWER:=Trunk~=Trunk-Port}-Port mehrere VLANs gleichzeitig transportieren kann. Traffic auf Access-Ports ist {1:MULTICHOICE:=untagged~tagged}.

---

### Frage 17 ⭐⭐ Mittel
**Typ:** truefalse  
**Punkte:** 2

**Frage:**  
Wahr oder Falsch: Das Native VLAN auf einem Trunk-Port sollte aus Sicherheitsgründen NICHT VLAN 1 sein.

**Antwort:** Wahr

**Begründung:** VLAN 1 ist Standard-Native-VLAN und anfällig für VLAN-Hopping-Angriffe. Best Practice: Native VLAN ändern.

---

## **Teil D: Inter-VLAN-Routing & Praxisanwendung (3 Fragen)**

### Frage 18 ⭐⭐ Mittel
**Typ:** essay (Freitext)  
**Punkte:** 3-4

**Frage:**  
Warum können Geräte in unterschiedlichen VLANs standardmäßig nicht miteinander kommunizieren?

**Erwartungshorizont:**
- VLANs sind logisch getrennte Netzwerke
- Jedes VLAN ist eine eigene Broadcast-Domain
- Layer-2-Switches arbeiten nur innerhalb eines VLANs
- VLANs haben unterschiedliche IP-Subnetze
- Kommunikation zwischen Subnetzen erfordert Layer-3-Routing
- Sicherheitskonzept: Isolation als Standard

---

### Frage 19 ⭐⭐ Mittel
**Typ:** multichoice (multi)  
**Punkte:** 3

**Frage:**  
Welche Geräte sind für Inter-VLAN-Routing geeignet?

**Antwortmöglichkeiten:**
- [ ] Layer-2-Switch (unmanaged)
- [x] Layer-3-Switch (Multilayer-Switch)
- [x] Router
- [ ] Hub
- [x] Firewall mit Routing-Funktionen
- [ ] Access Point

**Punkteverteilung:** 3 richtig, je 33,33%

---

### Frage 20 ⭐⭐⭐ Schwer
**Typ:** essay (Freitext)  
**Punkte:** 6

**Frage:**  
**Praxisaufgabe:** Sie planen ein Festival-Netzwerk mit folgenden VLANs:
- **VLAN 10:** Licht (10.10.10.0/24)
- **VLAN 20:** Audio (10.10.20.0/24)
- **VLAN 30:** Video (10.10.30.0/24)
- **VLAN 50:** Gäste-WLAN (10.10.50.0/24)

Welche VLANs sollten miteinander kommunizieren dürfen? Begründen Sie Ihre Entscheidungen aus Sicherheits- und Performance-Sicht.

**Erwartungshorizont:**

**Empfohlene Konfiguration:**

✅ **Erlaubte Kommunikation:**
- Management-VLAN → Alle VLANs (für Monitoring und Konfiguration)
- Video-VLAN ↔ Audio-VLAN (für multimediale Produktion, Synchronisation)

❌ **Isolation (keine Kommunikation):**
- Gäste-WLAN (VLAN 50) → Keine technischen VLANs (Sicherheit!)
- Licht-VLAN (VLAN 10) → Isoliert (Art-Net braucht keine externe Kommunikation)

**Begründungen:**

**Sicherheit:**
- Gäste-WLAN MUSS isoliert sein → Schutz vor unbefugtem Zugriff
- Produktivsysteme (Licht, Audio, Video) von öffentlichem WLAN trennen
- Management-Zugang über separates, geschütztes VLAN

**Performance:**
- Art-Net (Licht-VLAN) produziert viele Broadcasts → Isolation verhindert Überlastung anderer VLANs
- Dante-Audio hat strenge Latenzanforderungen → Eigenes VLAN ohne Störungen
- Video-Streaming benötigt hohe Bandbreite → Keine Konkurrenz durch andere Dienste

**ACL-Regeln (erweitert):**
```
VLAN 50 (Gäste) → Internet: Erlaubt
VLAN 50 (Gäste) → VLAN 10, 20, 30: Verweigert
VLAN 30 (Video) → VLAN 20 (Audio): Erlaubt (für Sync)
VLAN 10 (Licht) → Alle anderen: Verweigert (vollständig isoliert)
```

---

## 📊 Zusammenfassung

### Schwierigkeitsverteilung
- **⭐ Leicht:** 6 Fragen (30%)
- **⭐⭐ Mittel:** 10 Fragen (50%)
- **⭐⭐⭐ Schwer:** 4 Fragen (20%)

### Fragetyp-Verteilung
| Fragetyp | Anzahl | Prozent |
|----------|--------|---------|
| multichoice | 5 | 25% |
| ddmatch | 4 | 20% |
| essay | 4 | 20% |
| cloze | 2 | 10% |
| shortanswer | 2 | 10% |
| ddwtos | 1 | 5% |
| truefalse | 1 | 5% |
| ordering ⚠️ | 1 | 5% |

### Punkteverteilung
- **Leichte Fragen:** 1-2 Punkte
- **Mittlere Fragen:** 3-4 Punkte
- **Schwere Fragen:** 5-6 Punkte
- **Gesamt:** ca. 65 Punkte

### Bestehensgrenze (Vorschlag)
- **100%:** 65 Punkte (Note 1,0)
- **92%:** 60 Punkte (Note 1,5)
- **81%:** 53 Punkte (Note 2,0)
- **67%:** 44 Punkte (Note 3,0)
- **50%:** 33 Punkte (Note 4,0 - Bestanden)
- **< 50%:** < 33 Punkte (Note 5,0 - Nicht bestanden)

---

## 💡 Hinweise zur Umsetzung

### Templates verwenden
Alle Fragen können mit den Templates aus `HTML/fragen/templates/` erstellt werden:
- `template-multichoice-mehrfachauswahl.xml`
- `template-ddmatch-zuordnung.xml`
- `template-essay-freitext.xml`
- `template-cloze-eingebettete-antworten.xml`
- `template-ddwtos-lueckentext.xml`
- `template-shortanswer-kurzantwort.xml`
- `template-truefalse-wahr-falsch.xml`
- `template-ordering-anordnung.xml` ⚠️ (Plugin benötigt)

### Praxisbezug
Alle Fragen sind auf die Veranstaltungstechnik ausgerichtet:
- Dante-Audio
- DMX/Art-Net Lichtsteuerung
- NDI-Video
- Festival-Szenarien
- Hybridveranstaltungen

### Didaktische Progression
1. **Teil A:** Grundlagen (Switches vs. Router)
2. **Teil B:** VLAN-Konzepte
3. **Teil C:** VLAN-Konfiguration
4. **Teil D:** Komplexe Anwendungsszenarien

---

**Stand:** Februar 2026  
**Autor:** Erstellt für VT-LF10 Netzwerktechnik  
**Basis:** Kapitel 2, Aufgaben 4, 4.1, 5, 5a
