# Kurztest Netzwerktechnik – Kapitel 1-3
**Maximale Punktzahl: 100 Punkte**  
**Bearbeitungszeit: 45 Minuten**

---

## Aufgabe 1: Zahlensysteme in der Netzwerktechnik (20 Punkte)

**a)** (6 Punkte) Erklären Sie, warum in der Netzwerktechnik das Binärsystem verwendet wird. Gehen Sie dabei auf die technische Funktionsweise digitaler Geräte ein.

**b)** (7 Punkte) Eine IP-Adresse wird sowohl in dezimaler als auch in binärer Form dargestellt. Beschreiben Sie, welche Vorteile die dezimale Schreibweise für Menschen hat und in welchen Situationen die binäre Darstellung wichtig ist.

**c)** (7 Punkte) MAC-Adressen werden in hexadezimaler Schreibweise angegeben (z. B. `00:1A:2B:FF:6C:90`). Erklären Sie, warum die hexadezimale Darstellung gegenüber der binären Schreibweise praktischer ist.

---

## Aufgabe 2: IP-Adressen und Netzwerkstruktur (20 Punkte)

Sie planen das Netzwerk für eine große Veranstaltung mit folgenden Gerätekategorien:
- **Audio-Netzwerk**: Dante-Geräte, Mikrofone, Stageboxen
- **Video-Netzwerk**: Kameras, Medienserver, LED-Controller
- **Licht-Netzwerk**: DMX-Nodes, Art-Net-Geräte
- **Management-Netzwerk**: Switches, Router, Monitoring-Systeme

**a)** (8 Punkte) Begründen Sie ausführlich, warum eine Trennung dieser Gerätekategorien in verschiedene Netzwerksegmente sinnvoll ist. Nennen Sie mindestens drei technische oder organisatorische Vorteile.

**b)** (6 Punkte) Beschreiben Sie, welche Rolle die Subnetzmaske bei der Kommunikation zwischen Geräten spielt. Erklären Sie, wie ein Gerät mithilfe der Subnetzmaske entscheidet, ob ein anderes Gerät im gleichen Netzwerk liegt.

**c)** (6 Punkte) Erklären Sie die Begriffe "Netzwerkadresse" und "Broadcastadresse". Warum können diese Adressen nicht an einzelne Geräte vergeben werden?

---

## Aufgabe 3: IP-Pakete und MTU (20 Punkte)

Bei einer Livestream-Übertragung treten regelmäßig Bildstörungen auf.

**a)** (7 Punkte) Beschreiben Sie den grundsätzlichen Aufbau eines IP-Pakets. Welche Informationen enthält der IP-Header und wozu werden diese benötigt?

**b)** (7 Punkte) Erklären Sie den Begriff "MTU" (Maximum Transmission Unit) und dessen Bedeutung für die Netzwerkübertragung. Was passiert, wenn ein Paket größer ist als die MTU?

**c)** (6 Punkte) Erläutern Sie, warum Fragmentierung bei Live-Videostreaming oder Audiosystemen wie Dante besonders problematisch sein kann. Gehen Sie auf die zeitkritischen Aspekte ein.

---

## Aufgabe 4: TCP vs. UDP in der Veranstaltungspraxis (20 Punkte)

**a)** (8 Punkte) Erklären Sie die grundlegenden Unterschiede zwischen TCP und UDP. Gehen Sie dabei auf folgende Aspekte ein:
   - Verbindungsaufbau
   - Fehlerbehandlung
   - Geschwindigkeit und Latenz

**b)** (12 Punkte) Ordnen Sie den folgenden vier Anwendungsfällen das geeignete Transportprotokoll (TCP oder UDP) zu und begründen Sie Ihre Entscheidung jeweils ausführlich:
   - Firmware-Update für ein digitales Mischpult über die Weboberfläche
   - Dante-Audio-Übertragung von 48 Mikrofon-Kanälen zur FOH-Konsole
   - Steuerung einer LED-Wand über Art-Net-Protokoll
   - Dateitransfer einer Projektdatei zum Medienserver

---

## Aufgabe 5: Fehleranalyse und Problemlösung (20 Punkte)

Bei einem Festival treten folgende Probleme auf:

**Problem 1:** Das Dante-Audionetzwerk hat gelegentliche Knackser und Aussetzer, obwohl alle Kabel und Steckverbindungen überprüft wurden.

**Problem 2:** Ein Medienserver kann nicht mit einem LED-Controller kommunizieren, obwohl beide eingeschaltet sind und Link-LEDs an den Netzwerkanschlüssen leuchten.

**Problem 3:** Der Livestream wird instabil, sobald mehr als 50 Kameras gleichzeitig aktiv sind.

**a)** (7 Punkte) Nennen Sie für Problem 1 mindestens drei mögliche netzwerktechnische Ursachen. Erklären Sie zu jeder Ursache, wie diese zu Audiostörungen führen kann.

**b)** (7 Punkte) Analysieren Sie Problem 2: Welche grundlegenden Konfigurationsparameter müssen bei beiden Geräten überprüft werden, damit sie miteinander kommunizieren können? Nennen Sie mindestens vier Aspekte.

**c)** (6 Punkte) Schlagen Sie für Problem 3 eine konkrete Lösungsstrategie vor. Erklären Sie, wie eine bessere Netzwerkstruktur oder -segmentierung das Problem beheben könnte.

---

## Bewertungshinweise für Lehrkräfte

- **Aufgabe 1:** Verständnis der Zahlensysteme und deren praktische Bedeutung
- **Aufgabe 2:** Konzeptionelles Verständnis von Netzwerkstrukturen und IP-Adressierung
- **Aufgabe 3:** Verständnis von Paketstruktur und MTU-Problematik
- **Aufgabe 4:** Protokollverständnis und praxisgerechte Anwendung
- **Aufgabe 5:** Problemlösungskompetenz und Transfer auf reale Situationen

**Punkteverteilung:**
- 90-100 Punkte: Sehr gut (1)
- 75-89 Punkte: Gut (2)
- 60-74 Punkte: Befriedigend (3)
- 45-59 Punkte: Ausreichend (4)
- 0-44 Punkte: Mangelhaft (5)
