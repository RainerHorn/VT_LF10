---
applyTo: '**'
---
# Veranstaltungstechnik - Lernfeld 6 (VT-LF6)

## 🤖 SPEZIELLE LLM-ANWEISUNGEN

**Für GitHub Copilot, Claude, ChatGPT und andere LLM-Systeme:**

### PRIORITÄTEN beim Content-Erstellen:
1. **IMMER Template verwenden** - `Templates/VT_Template.html` ist die einzige Basis
2. **Didaktik vor Technik** - Handlungsorientierung ist wichtiger als perfektes Design
3. **Schüler- UND Lehrerversion** - Niemals nur eine Version erstellen
4. **Realitätsbezug zwingend** - Alle Aufgaben müssen aus echten VT-Szenarien stammen
5. **CSS-Abstände beachten** - Template löst Moodle-Probleme automatisch

### TYPISCHE LLM-FEHLER VERMEIDEN:
❌ **NICHT**: Eigene CSS-Styles erfinden
❌ **NICHT**: Aufgaben ohne Sozialform/Methode
❌ **NICHT**: Theoretische Textwüsten ohne Handlungsbezug
❌ **NICHT**: Erwartungshorizonte in Schülerversionen
❌ **NICHT**: Veraltete HTML-Strukturen verwenden

✅ **IMMER**: Template-CSS verwenden
✅ **IMMER**: Konkrete VT-Szenarien (Konzert, Messe, etc.)
✅ **IMMER**: Sozialform + Methode bei Aufgaben
✅ **IMMER**: Kontrollfragen am Ende jedes Abschnitts
✅ **IMMER**: Beide Versionen (Schüler + Lehrer) erstellen

### ARBEITSABLAUF für LLMs:
1. **Analysiere** das Thema aus VT-Sicht
2. **Wähle** realistisches Szenario (Veranstaltungstyp)
3. **Kopiere** VT_Template.html als Basis
4. **Strukturiere** nach handlungsorientiertem Schema
5. **Erstelle** Schülerversion (ohne Lösungen)
6. **Erstelle** Lehrerversion (mit Erwartungshorizonten)
7. **Prüfe** Qualitätskriterien (siehe Checkliste unten)

---

## LLM-Anweisungen für Content-Erstellung

Diese Datei enthält spezielle Anweisungen für LLM-basierte Content-Erstellung. Für die vollständige Projektdokumentation siehe README.md.

## Projektbeschreibung

Dieses Repository verwaltet HTML-basierte Lernmaterialien für einen Moodle-Kurs im Bereich Veranstaltungstechnik. Der Kurs richtet sich an Auszubildende zur Fachkraft für Veranstaltungstechnik und folgt den Prinzipien des handlungsorientierten Unterrichts gemäß der SchuCu-BBS Leitlinie 2024.

## Zielgruppe
- **Auszubildende**: Fachkraft für Veranstaltungstechnik 
- **Ausbildungsjahr**: Zweites Lehrjahr
- **Lernfeld**: LF6 (spezifische Inhalte je nach Curriculum)

## Struktur des Repositories

```
vt-lf6/
├── README.md                    # Hauptdokumentation und Fortschrittstracking
├── Seiten/                      # HTML-Seiten für den Moodle-Kurs
├── Templates/
│   ├── VT_Template.html         # Aktualisiertes Basis-Template (September 2025)
│   ├── Leitlinie_SchuCu-BBS_2024_07.pdf  # Didaktische Leitlinie
│   └── LF6 Plan.pdf            # Lehrplan für Lernfeld 6
└── .github/instructions/        # LLM-spezifische Anweisungen
```

## WICHTIGE LLM-REGELN für die Erstellung von Lernmaterialien

### 1. Template-Verwendung (AKTUALISIERT September 2025)

**IMMER** das bereitgestellte Template `Templates/VT_Template.html` als Basis verwenden:
- Das Template enthält OPTIMIERTE CSS-Styles mit minimalen Abständen
- JavaScript-Fallback für Moodle-Kompatibilität
- !important-Regeln für zuverlässige Style-Anwendung
- Integrierter Chatbot für Lernunterstützung (VT GPT) - automatisch geladen
- Responsive Design für verschiedene Bildschirmgrößen
- Interaktive Funktionen (Code kopieren, Erklärungen anfordern)

**Verfügbare CSS-Klassen (ERWEITERT):**
- `.section` - Hauptcontainer für Inhaltsblöcke
- `.task` - Aufgabenblöcke (grüner Hintergrund)
- `.question` - Frageblöcke (gelber Hintergrund)
- `.tech-specs` - Technische Spezifikationen (blauer Hintergrund)
- `.teacher-solution` - Erwartungshorizonte für Lehrerversionen (roter Hintergrund)
- `.intro` - Einführungstexte (grauer Hintergrund)
- `.phases` - Grid-Layout für Phasenübersichten
- `.phase` - Einzelne Phasen-Karten mit Hover-Effekten
- `.comparison-table` - Responsive Vergleichstabellen

### 2. CSS-Abstände (KRITISCHE ANFORDERUNG)

**PROBLEM GELÖST**: Moodle überschreibt Standard-CSS mit eigenen Abständen.
**LÖSUNG IMPLEMENTIERT**: Template enthält !important-Regeln und JavaScript-Fallback.

**Für Überschriften IMMER verwenden:**
- h2: margin-bottom: 0.1rem !important
- h3: margin-bottom: 0.1rem !important  
- h4: margin-bottom: 0.1rem !important

### 2. CSS-Abstände (KRITISCHE ANFORDERUNG)

**PROBLEM GELÖST**: Moodle überschreibt Standard-CSS mit eigenen Abständen.
**LÖSUNG IMPLEMENTIERT**: Template enthält !important-Regeln und JavaScript-Fallback.

**Für Überschriften IMMER verwenden:**
- h2: margin-bottom: 0.1rem !important
- h3: margin-bottom: 0.1rem !important  
- h4: margin-bottom: 0.1rem !important

**JavaScript-Fallback automatisch aktiv** - keine manuelle Anpassung nötig!

### 3. Handlungsorientierter Unterricht (PFLICHT)

Gemäß der SchuCu-BBS Leitlinie 2024 MÜSSEN alle Lernmaterialien folgende Prinzipien befolgen:

**a) Vollständige Handlung (6-Stufen-Modell):**
1. **Informieren** - Situation erfassen, Problemstellung verstehen
2. **Planen** - Lösungsweg entwickeln, Arbeitsschritte festlegen
3. **Entscheiden** - Beste Lösung auswählen, Begründung liefern
4. **Ausführen** - Praktische Umsetzung der geplanten Lösung
5. **Kontrollieren** - Ergebnis überprüfen, Qualität bewerten
6. **Bewerten** - Reflexion des Lernprozesses, Verbesserungsvorschläge

**b) Situationsbezug (PFLICHT):**
- Realitätsnahe Arbeitsaufträge aus der Veranstaltungstechnik
- Praxisrelevante Problemstellungen
- Berufstypische Handlungssituationen

**c) Kompetenzorientierung:**
- Fachkompetenz: Technisches Wissen und Fertigkeiten
- Methodenkompetenz: Problemlösungsstrategien
- Sozialkompetenz: Teamwork und Kommunikation
- Personalkompetenz: Selbstständigkeit und Verantwortung

### 4. Inhaltliche Gestaltung (QUALITÄTSKRITERIEN)

**Aufgabentypen erstellen:**
- **Situative Aufgaben**: Reale Szenarien aus Events, Konzerten, Messen
- **Projektaufgaben**: Komplexe, mehrstufige Problemstellungen
- **Fallstudien**: Analyse von Veranstaltungstechnik-Projekten
- **Theoretische Vertiefung**: Fachliche Grundlagen und Konzepte

**Sozialformen und Unterrichtsmethoden (IMMER variieren):**
- **Einzelarbeit**: Individuelle Reflexion, persönliche Lernprozesse
- **Tandemarbeit**: Partnerarbeit für Diskussion und Meinungsaustausch
- **Gruppenarbeit**: Teamaufgaben (3-4 Personen) für komplexe Problemstellungen
- **Plenum**: Klassengespräche, Präsentationen, gemeinsame Reflexion
- **Think-Pair-Share**: Erst einzeln denken, dann mit Partner besprechen, dann im Plenum
- **Expertenmethode**: Spezialisierung auf Teilthemen, dann Wissensvermittlung
- **Rollenspiele**: Kundengespräche, Beratungssituationen simulieren
- **Stationenlernen**: Verschiedene Aspekte an unterschiedlichen Arbeitsplätzen

**Berufsbezogene Kontexte (IMMER verwenden):**
- **Konzerte und Festivals**: Bühnentechnik, Live-Übertragung
- **Messen und Ausstellungen**: Präsentationstechnik, Medienwände
- **Firmenveranstaltungen**: Konferenztechnik, Streaming
- **Theater und Shows**: Bühnentechnik, Effekte
- **Sportereignisse**: Übertragungstechnik, Großbildleinwände
- **Hochzeiten und private Events**: Mobile Technik, Dokumentation

### 5. Strukturierung der Lerneinheiten (TEMPLATE)

```html
<div class="container">
    <div class="header">
        <h1>📽️ [Titel der Lerneinheit]</h1>
        <p>[Untertitel/Kontext]</p>
    </div>

    <div class="content">
        <div class="intro">
            <p><strong>Berufsbezogener Kontext:</strong> [Realistisches Szenario]</p>
        </div>

        <div class="section">
            <h2>[Hauptthema]</h2>
            
            <div class="task">
                <strong>Arbeitsauftrag [Nr.]: [Titel]</strong>
                <p><strong>Sozialform:</strong> [Einzelarbeit/Tandemarbeit/Gruppenarbeit/Plenum]</p>
                <p><strong>Methode:</strong> [z.B. Think-Pair-Share, Expertenmethode]</p>
                <p>[Konkrete Handlungsaufforderung]</p>
            </div>
            
            <!-- NUR FÜR LEHRERVERSIONEN -->
            <div class="teacher-solution">
                <h4>🎯 Erwartungshorizont</h4>
                <p>[Erwartete Antworten und Lösungsansätze]</p>
            </div>
            
            <div class="question">
                <strong>Kontrollfragen:</strong>
                <ol>
                    <li>[Verständnisfrage]</li>
                    <li>[Anwendungsfrage]</li>
                    <li>[Bewertungsfrage]</li>
                </ol>
            </div>
            
            <div class="tech-specs">
                <h4>🔧 Technische Hinweise</h4>
                <p>[Relevante Fachinfos und Spezifikationen]</p>
            </div>
        </div>
    </div>
</div>
```

### 6. Sprache und Stil (VERBINDLICH)

- **Direkte Ansprache**: "Sie" verwenden (förmlich)
- **Klare Arbeitsaufträge**: Handlungsverben nutzen (analysieren, entwickeln, bewerten)
- **Fachsprache**: Korrekte Verwendung veranstaltungstechnischer Begriffe
- **Verständlichkeit**: Komplexe Sachverhalte strukturiert erklären

### 7. Schüler- vs. Lehrerversionen (KRITISCH)

**SCHÜLERVERSION:**
- KEINE `.teacher-solution` Blöcke
- Reine Aufgabenstellungen ohne Lösungen
- Fokus auf Handlungsaufträge und Reflexion

**LEHRERVERSION:**
- MIT `.teacher-solution` Blöcken (rote Boxen)
- Erwartungshorizonte für alle Aufgaben
- Didaktische Hinweise und Lösungsansätze

### 8. Dateiorganisation (VERBINDLICH)

**Namenskonvention:**
- Schüler: `VT_LF6_[Thema]_[Nummer].html`
- Lehrer: `VT_LF6_[Thema]_[Nummer]_Lehrerversion.html`

**Ordnerstruktur:**
```
Seiten/
├── 00_Einfuehrung/
├── 01_Grundlagen/
├── 02_Signalarten/
├── 03_Signalueberragung/
└── [weitere Kapitel]/
```

### 9. Qualitätskriterien (CHECKLISTE)

Jede erstellte Lerneinheit MUSS enthalten:
- ✅ Berufsbezogenen Kontext (Veranstaltungsart spezifizieren)
- ✅ Realitätsbezogene Ausgangssituation
- ✅ Klar formulierte Arbeitsaufträge mit Sozialform und Methode
- ✅ Alle 6 Stufen der vollständigen Handlung
- ✅ Mindestens 3-5 Kontrollfragen pro Abschnitt
- ✅ Abwechslungsreiche Unterrichtsmethoden (min. 2 verschiedene pro Lerneinheit)
- ✅ Fachlich korrekte Inhalte
- ✅ Angemessene Schwierigkeit für Zielgruppe
- ✅ Reflexionselemente
- ✅ Responsive HTML-Struktur
- ✅ Korrekte CSS-Klassen aus aktuellem Template

### 10. Tests und Lernkontrollen

**Nach sinnvollen Kapiteln MÜSSEN Tests erstellt werden:**
- **Testformat**: Multiple Choice, Kurzantworten, Fallstudien
- **Testlänge**: 15-20 Fragen pro Test
- **Bewertung**: Punkte-System mit Feedback
- **Dateiname**: `VT_LF6_Test_[Thema]_[Nummer].html`

**Empfohlene Test-Intervalle:**
- Nach Grundlagen (DS 1-2)
- Nach Signalübertragung (DS 3-4) 
- Nach Videoübertragung (DS 5-6)
- Nach Codecs (DS 7-8)
- Nach Kamerasystemen (DS 9-11)
- Abschlusstest (DS 12-13)

### 11. Chatbot-Integration (AUTOMATISCH)

Der integrierte VT GPT Chatbot:
- **Automatische Initialisierung** beim Laden der Seite
- **Funktion**: Lernunterstützung, keine fertigen Lösungen
- **Rolle**: Fachexperte für Veranstaltungstechnik
- **Zielgruppe**: Fachkraft für Veranstaltungstechnik, 2. Ausbildungsjahr
- **Verhalten**: Erklärungen geben, Denkprozesse anregen

**Konfiguration (bereits im Template):**
- Host: dev.mm-bbs.de:8085
- Titel: "VT GPT" 
- Fachbereich: Veranstaltungstechnik
- Code-Erklärung auf Knopfdruck verfügbar

### 12. AKTUELLE ERKENNTNISSE (September 2025)

**CSS-Probleme gelöst:**
- ✅ Moodle-Kompatibilität durch !important-Regeln
- ✅ JavaScript-Fallback für zuverlässige Darstellung
- ✅ Minimale Abstände nach Überschriften (0.1rem)
- ✅ Responsive Design für alle Endgeräte

**Template aktualisiert:**
- ✅ Alle neuen CSS-Klassen verfügbar
- ✅ Automatische DOM-Manipulation
- ✅ Erweiterte Formatierungsoptionen

**Didaktische Optimierungen:**
- ✅ Strenge Trennung Schüler-/Lehrerversionen
- ✅ Handlungsorientierte Aufgabenstellungen
- ✅ Methodenvielfalt systematisch eingesetzt

---

## VERWENDUNG

1. **Template kopieren**: `VT_Template.html` als Basis
2. **Inhalt strukturieren**: Gemäß handlungsorientierter Didaktik
3. **CSS-Klassen verwenden**: Wie oben dokumentiert
4. **Zwei Versionen erstellen**: Schüler- und Lehrerversion
5. **Qualität prüfen**: Checkliste abarbeiten
6. **In Moodle testen**: Darstellung und Funktionalität

---

*Letzte Aktualisierung: 07. September 2025 - Template und CSS optimiert*

### 2. Handlungsorientierter Unterricht

Gemäß der SchuCu-BBS Leitlinie 2024 MÜSSEN alle Lernmaterialien folgende Prinzipien befolgen:

**a) Vollständige Handlung (6-Stufen-Modell):**
1. **Informieren** - Situation erfassen, Problemstellung verstehen
2. **Planen** - Lösungsweg entwickeln, Arbeitsschritte festlegen
3. **Entscheiden** - Beste Lösung auswählen, Begründung liefern
4. **Ausführen** - Praktische Umsetzung der geplanten Lösung
5. **Kontrollieren** - Ergebnis überprüfen, Qualität bewerten
6. **Bewerten** - Reflexion des Lernprozesses, Verbesserungsvorschläge

**b) Situationsbezug:**
- Realitätsnahe Arbeitsaufträge aus der Veranstaltungstechnik
- Praxisrelevante Problemstellungen
- Berufstypische Handlungssituationen

**c) Kompetenzorientierung:**
- Fachkompetenz: Technisches Wissen und Fertigkeiten
- Methodenkompetenz: Problemlösungsstrategien
- Sozialkompetenz: Teamwork und Kommunikation
- Personalkompetenz: Selbstständigkeit und Verantwortung

### 3. Inhaltliche Gestaltung

**Aufgabentypen erstellen:**
- **Situative Aufgaben**: Reale Szenarien aus Events, Konzerten, Messen
- **Projektaufgaben**: Komplexe, mehrstufige Problemstellungen
- **Fallstudien**: Analyse von Veranstaltungstechnik-Projekten
- **Theoretische Vertiefung**: Fachliche Grundlagen und Konzepte

**Sozialformen und Unterrichtsmethoden (IMMER variieren):**
- **Einzelarbeit**: Individuelle Reflexion, persönliche Lernprozesse
- **Tandemarbeit**: Partnerarbeit für Diskussion und Meinungsaustausch
- **Gruppenarbeit**: Teamaufgaben (3-4 Personen) für komplexe Problemstellungen
- **Plenum**: Klassengespräche, Präsentationen, gemeinsame Reflexion
- **Think-Pair-Share**: Erst einzeln denken, dann mit Partner besprechen, dann im Plenum
- **Expertenmethode**: Spezialisierung auf Teilthemen, dann Wissensvermittlung
- **Rollenspiele**: Kundengespräche, Beratungssituationen simulieren
- **Stationenlernen**: Verschiedene Aspekte an unterschiedlichen Arbeitsplätzen

**Berufsbezogene Kontexte (IMMER verwenden):**
- **Konzerte und Festivals**: Bühnentechnik, Live-Übertragung
- **Messen und Ausstellungen**: Präsentationstechnik, Medienwände
- **Firmenveranstaltungen**: Konferenztechnik, Streaming
- **Theater und Shows**: Bühnentechnik, Effekte
- **Sportereignisse**: Übertragungstechnik, Großbildleinwände
- **Hochzeiten und private Events**: Mobile Technik, Dokumentation

**Strukturierung der Lerneinheiten:**
```html
<div class="section">
    <h2>Berufsbezogener Kontext</h2>
    <!-- IMMER: Realistisches Szenario aus der Veranstaltungstechnik -->
    <!-- Beispiel: Konzert, Messe, Firmenveranstaltung, Theater etc. -->
    
    <h2>Situationsbeschreibung</h2>
    <!-- Detaillierte Beschreibung der Arbeitssituation -->
    
    <div class="task">
        <h3>Arbeitsauftrag</h3>
        <!-- Konkrete Handlungsaufforderung -->
        <!-- IMMER Sozialform angeben: Einzelarbeit/Tandem/Gruppe/Plenum -->
        <p><strong>Sozialform:</strong> [Einzelarbeit/Tandemarbeit/Gruppenarbeit (3-4 Personen)/Plenum]</p>
        <p><strong>Methode:</strong> [z.B. Think-Pair-Share, Expertenmethode, Rollenspiel, Stationenlernen]</p>
    </div>
    
    <div class="question">
        <h3>Kontrollfragen</h3>
        <!-- PFLICHT: Mindestens 3-5 Kontrollfragen pro Abschnitt -->
        <!-- Fragen zum Verständnis und zur Reflexion -->
        <!-- Verschiedene Sozialformen für Fragen nutzen -->
    </div>
    
    <div class="tech-specs">
        <h3>Technische Hinweise</h3>
        <!-- Relevante Fachinfos und Spezifikationen -->
    </div>
</div>
```

### 4. Sprache und Stil

- **Direkte Ansprache**: "Sie" verwenden (förmlich)
- **Klare Arbeitsaufträge**: Handlungsverben nutzen (analysieren, entwickeln, bewerten)
- **Fachsprache**: Korrekte Verwendung veranstaltungstechnischer Begriffe
- **Verständlichkeit**: Komplexe Sachverhalte strukturiert erklären

### 5. Chatbot-Integration

Der integrierte VT GPT Chatbot:
- **Funktion**: Lernunterstützung, keine fertigen Lösungen
- **Rolle**: Fachexperte für Veranstaltungstechnik
- **Zielgruppe**: Fachkraft für Veranstaltungstechnik, 2. Ausbildungsjahr
- **Verhalten**: Erklärungen geben, Denkprozesse anregen

**Wichtige Chatbot-Features:**
- Automatische Initialisierung beim Laden der Seite
- Code-Erklärung auf Knopfdruck (`explainCode()` Funktion)
- Copy-to-Clipboard Funktionalität
- Responsive Chat-Interface
- Kontextbezogene Hilfe basierend auf Seiteninhalt

### 6. Dateibenennung und Organisation

**Namenskonvention für HTML-Dateien:**
- Format: `VT_LF6_[Thema]_[Nummer].html`
- Beispiel: `VT_LF6_Beleuchtungstechnik_01.html`
- Keine Leerzeichen, Umlaute durch ae/oe/ue ersetzen

**Inhaltsverzeichnis in Seiten/:**
- Thematische Ordner erstellen
- Nummerierung für Reihenfolge verwenden
- Index-Dateien für Übersichtlichkeit

### 7. Qualitätskriterien

Jede erstellte Lerneinheit MUSS enthalten:
- [ ] Berufsbezogenen Kontext (Veranstaltungsart spezifizieren)
- [ ] Realitätsbezogene Ausgangssituation
- [ ] Klar formulierte Arbeitsaufträge mit Sozialform und Methode
- [ ] Alle 6 Stufen der vollständigen Handlung
- [ ] Mindestens 3-5 Kontrollfragen pro Abschnitt
- [ ] Abwechslungsreiche Unterrichtsmethoden (min. 2 verschiedene pro Lerneinheit)
- [ ] Fachlich korrekte Inhalte
- [ ] Angemessene Schwierigkeit für Zielgruppe
- [ ] Reflexionselemente
- [ ] Responsive HTML-Struktur

### 8. Tests und Lernkontrollen

**Nach sinnvollen Kapiteln MÜSSEN Tests erstellt werden:**
- **Testformat**: Multiple Choice, Kurzantworten, Fallstudien
- **Testlänge**: 15-20 Fragen pro Test
- **Bewertung**: Punkte-System mit Feedback
- **Dateiname**: `VT_LF6_Test_[Thema]_[Nummer].html`

**Test-Struktur:**
```html
<div class="section">
    <h2>Test: [Themenbereich]</h2>
    
    <div class="question">
        <h3>Frage 1</h3>
        <!-- Multiple Choice oder offene Frage -->
    </div>
    
    <div class="tech-specs">
        <h3>Auswertung</h3>
        <!-- Musterlösung und Erklärung -->
    </div>
</div>
```

**Empfohlene Test-Intervalle:**
- Nach Grundlagen (DS 1-2)
- Nach Signalübertragung (DS 3-4) 
- Nach Videoübertragung (DS 5-6)
- Nach Codecs (DS 7-8)
- Nach Kamerasystemen (DS 9-11)
- Abschlusstest (DS 12-13)

### 8. Technische Anforderungen

- **HTML5-Standard** einhalten
- **Responsive Design** für mobile Nutzung
- **Barrierefreiheit** berücksichtigen
- **Moodle-Kompatibilität** sicherstellen
- **Chatbot-Funktionalität** automatisch integriert - kein manueller Eingriff nötig
- **Chatbot-Konfiguration**: 
  - Host: dev.mm-bbs.de:8085
  - Titel: "VT GPT" 
  - Fachbereich: Veranstaltungstechnik
  - Zielgruppe: 2. Ausbildungsjahr

### 9. Chatbot-Nutzung in Lerneinheiten

**Bei der Erstellung von Lernmaterialien beachten:**
- Chatbot steht automatisch für Rückfragen zur Verfügung
- Lernende können Code-Snippets zur Erklärung an den Bot senden
- Interaktive Elemente fördern selbstständiges Lernen
- Bot unterstützt bei komplexen technischen Fragestellungen
- **Wichtig**: Bot gibt keine fertigen Lösungen, sondern Denkanstöße

### 12. Kontrollfragen-Gestaltung

**PFLICHT: Abwechslungsreiche Unterrichtsmethoden verwenden**

**Methodenauswahl je nach Lernziel:**
- **Think-Pair-Share**: Für komplexe Fragestellungen und Meinungsbildung
- **Expertenmethode**: Bei umfangreichen Themenbereichen (z.B. verschiedene Kameratypen)
- **Rollenspiele**: Für Kundengespräche und Beratungssituationen
- **Stationenlernen**: Bei technischen Spezifikationen und Gerätevergleichen
- **Fallstudien-Analyse**: Für reale Projektbeispiele
- **Diskussionsrunden**: Für Bewertung und Reflexion
- **Präsentationen**: Für Ergebnissicherung und Wissenstransfer

**Sozialformen strategisch einsetzen:**
- **Einzelarbeit**: Reflexion, individuelle Problemanalyse, Lernstandsüberprüfung
- **Tandemarbeit**: Fachgespräche, gegenseitiges Erklären, Peer-Learning
- **Gruppenarbeit**: Komplexe Projekte, arbeitsteilige Problemlösung, Teamkompetenzen
- **Plenum**: Ergebnispräsentation, Diskussion, gemeinsame Reflexion

**Beispiel-Methodenkombinationen:**
```html
<div class="task">
    <h3>Arbeitsauftrag: Kameraauswahl für Konzertaufzeichnung</h3>
    <p><strong>Phase 1 (Einzelarbeit):</strong> Analysieren Sie die Anforderungen (5 Min.)</p>
    <p><strong>Phase 2 (Tandemarbeit):</strong> Diskutieren Sie Ihre Einschätzungen (10 Min.)</p>
    <p><strong>Phase 3 (Plenum):</strong> Präsentieren Sie Ihre Lösung (15 Min.)</p>
    <p><strong>Methode:</strong> Think-Pair-Share mit abschließender Expertendiskussion</p>
</div>
```

**PFLICHT: Jeder Abschnitt benötigt Kontrollfragen**
- **Anzahl**: Mindestens 3-5 Fragen pro Abschnitt
- **Typen**: 
  - Verständnisfragen (Was ist...?)
  - Anwendungsfragen (Wie würden Sie...?)
  - Analysefragen (Warum ist...?)
  - Bewertungsfragen (Welche Lösung ist besser und warum?)

**Beispiel-Kontrollfragen:**
```html
<div class="question">
    <h3>Kontrollfragen</h3>
    <ol>
        <li>Erklären Sie den Unterschied zwischen analogen und digitalen Signalen in der Veranstaltungstechnik.</li>
        <li>In welcher Situation würden Sie analoge Übertragung bevorzugen?</li>
        <li>Analysieren Sie die Vor- und Nachteile digitaler Signalverarbeitung bei Live-Events.</li>
        <li>Bewerten Sie die Qualitätsunterschiede verschiedener Übertragungsverfahren.</li>
        <li>Wie würden Sie einem Kunden die Wahl der Übertragungstechnik erklären?</li>
    </ol>
</div>
```

## Verwendung

1. Neue HTML-Seite auf Basis von `VT_Template.html` erstellen
2. Inhalt gemäß handlungsorientierter Didaktik strukturieren
3. In entsprechenden Ordner unter `Seiten/` ablegen
4. In Moodle-Kurs einbinden

## Mitwirkende

- Entwicklung und Pflege durch Lehrkräfte der Multi-Media BBS
- Fachberatung Veranstaltungstechnik
- Didaktische Konzeption nach SchuCu-BBS Leitlinie

---

*Letzte Aktualisierung: September 2025*