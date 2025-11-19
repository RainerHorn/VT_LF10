# Kurztest: Netzwerktechnik Grundlagen (Kapitel 1-3) - Verständnisorientiert

Dieser Test prüft das technische Verständnis der Konzepte aus den Kapiteln 1-3, ohne dass komplexe Umrechnungen oder Subnetting-Berechnungen durchgeführt werden müssen.

---

## Frage 1: Aufbau von IP-Adressen (Zahlensysteme)
Ein Auszubildender versucht, einem Lichtpult die IP-Adresse `192.168.256.1` zuzuweisen. Das Gerät zeigt eine Fehlermeldung an und akzeptiert die Eingabe nicht.

Erklären Sie technisch begründet (unter Bezugnahme auf die Speicherung in Bits/Bytes), warum der Wert **256** in einem Block (Oktett) einer IPv4-Adresse nicht existieren kann.

---

## Frage 2: Funktion der Subnetzmaske (Routing-Entscheidung)
Ein Medienserver mit der IP `10.0.0.5` möchte Daten an einen Projektor mit der IP `10.0.1.20` senden.
Bevor das Datenpaket das Gerät verlässt, prüft der Medienserver seine eigene **Subnetzmaske**.

Beschreiben Sie die Aufgabe der Subnetzmaske in diesem Moment:
1. Was "sagt" die Subnetzmaske dem Medienserver über das Ziel?
2. Welche Entscheidung trifft der Medienserver basierend darauf: Sendet er das Paket direkt an den Projektor oder an den Standard-Gateway (Router)?

---

## Frage 3: Hardware- vs. Logische Adressen (MAC vs. IP)
Geräte in der Veranstaltungstechnik besitzen sowohl eine **MAC-Adresse** (oft als Aufkleber am Gehäuse) als auch eine **IP-Adresse** (im Menü einstellbar).

1. Worin liegt der grundlegende Unterschied zwischen diesen beiden Adressarten in Bezug auf ihre Veränderbarkeit?
2. Warum benötigen wir überhaupt IP-Adressen, wenn doch jedes Gerät schon eine weltweit eindeutige MAC-Adresse hat? (Denken Sie an die Strukturierung von großen Netzwerken).

---

## Frage 4: MTU und Fragmentierung (Konzept)
Die "Maximum Transmission Unit" (MTU) begrenzt die Größe eines Datenpakets im Netzwerk. Wenn ein Paket größer ist als die MTU, muss es "fragmentiert" (zerteilt) werden.

Erklären Sie, warum diese Fragmentierung gerade bei **Echtzeit-Anwendungen** (wie Live-Audio über Dante oder Live-Video) problematisch sein kann. Nennen Sie einen konkreten Nachteil, der durch das Zerteilen und Wiederzusammensetzen entsteht.

---

## Frage 5: Protokollwahl (TCP vs. UDP)
Vergleichen Sie die Protokolle TCP und UDP anhand eines Szenarios aus der Veranstaltungstechnik:

*   **Szenario A:** Übertragung von Steuerdaten für Moving Lights (Art-Net/sACN). Hier ist es wichtig, dass die Befehle sofort ausgeführt werden. Veraltete Befehle sind nutzlos.
*   **Szenario B:** Übertragung einer Show-Datei (Savegame) vom USB-Stick auf den internen Speicher des Pults über das Netzwerk.

Welches Protokoll (TCP oder UDP) eignet sich für welches Szenario besser? Begründen Sie Ihre Wahl kurz mit den Eigenschaften "Zuverlässigkeit" und "Geschwindigkeit".

---

# Lösungsvorschläge (für Dozenten)

**Zu Frage 1:**
*   Eine IPv4-Adresse besteht aus 4 Blöcken à 8 Bit (1 Byte).
*   Mit 8 Bit können maximal 256 Zustände dargestellt werden ($2^8$).
*   Da wir bei 0 anfangen zu zählen, ist der höchste mögliche Wert **255** (binär `11111111`). Die 256 passt nicht mehr in 8 Bit.

**Zu Frage 2:**
*   1. Die Subnetzmaske definiert, welcher Teil der IP-Adresse zum "Netzwerk" gehört und welcher zum "Gerät" (Host). Sie dient als Schablone zum Vergleich.
*   2. Der Server vergleicht sein eigenes Netz mit dem des Ziels.
    *   Wenn das Netz identisch ist -> Direktversand (ARP Request an Ziel).
    *   Wenn das Netz unterschiedlich ist -> Versand an das Gateway (Router).

**Zu Frage 3:**
*   1. **MAC-Adresse:** Physikalische Adresse, fest in die Hardware eingebrannt, weltweit eindeutig (wie eine Fahrgestellnummer).
    *   **IP-Adresse:** Logische Adresse, konfigurierbar, abhängig vom Netzwerkstandort (wie eine Wohnadresse).
*   2. IP-Adressen ermöglichen eine hierarchische Strukturierung (Subnetze) und Routing. Mit MAC-Adressen (die völlig chaotisch verteilt sind) wäre kein effizientes Routing im Internet möglich, da jeder Router jede MAC-Adresse der Welt kennen müsste.

**Zu Frage 4:**
*   Fragmentierung bedeutet, dass ein Paket in Teile zerlegt und beim Empfänger wieder zusammengesetzt werden muss.
*   **Nachteil:** Dies kostet Rechenzeit (Latenz). Wenn auch nur ein einziges Fragment verloren geht, ist das gesamte Paket ungültig und muss verworfen werden. Bei Live-Audio führt dies zu Aussetzern (Dropouts) oder erhöhter Verzögerung (Latenz), was im Live-Betrieb inakzeptabel ist.

**Zu Frage 5:**
*   **Szenario A (Lichtsteuerung): UDP.** Wir brauchen maximale Geschwindigkeit (Echtzeit). Wenn ein Paket verloren geht, ist das nicht schlimm, da sofort das nächste mit neuen Werten kommt. Wir wollen nicht auf eine Bestätigung warten.
*   **Szenario B (Dateiübertragung): TCP.** Hier ist Datenintegrität das Wichtigste. Die Datei darf keine Fehler haben. TCP garantiert, dass alle Pakete ankommen und in der richtigen Reihenfolge zusammengesetzt werden. Geschwindigkeit ist zweitrangig.
