## 9. DMX (XLR 5-polig) – Die Lichtsteuer-Schnittstelle der Veranstaltungstechnik

Der DMX-Standard (Digital Multiplex) hat sich seit den 1980er-Jahren als internationale Norm zur Steuerung von Lichtsystemen etabliert. DMX512 wurde ursprünglich vom USITT (United States Institute for Theatre Technology) definiert und ist heute nach ANSI E1.11 standardisiert. Die typische physikalische Verbindung erfolgt über XLR-Steckverbinder mit 5 Polen – obwohl in der Praxis auch oft 3-polige Varianten verwendet werden, was technisch nicht normkonform, aber verbreitet ist.

DMX512 überträgt digitale Steuerdaten seriell mit 250 kbit/s. Ein sogenanntes Universum umfasst 512 Kanäle, die jeweils einen 8-Bit-Wert (0–255) tragen – genug, um z. B. Dimmer, Farbe, Pan/Tilt, Gobos oder Strobo-Effekte eines Scheinwerfers zu steuern. Geräte werden „adressiert“, um ihre Kanäle eindeutig im Datenstrom zu finden.

**Typische Komponenten:**
- Lichtpult oder Software mit DMX-Ausgang
- Interface (USB → DMX oder ArtNet → DMX)
- XLR-5-Pol-Kabel, oft durchgeschleift (Daisy Chain)
- Abschlusswiderstand am letzten Gerät (120 Ohm)

Die elektrische Übertragung erfolgt als symmetrisches Signal nach dem RS-485-Standard. Damit sind Kabellängen bis etwa 300 m möglich. Wichtig ist die Verwendung hochwertiger DMX-Kabel mit passender Impedanz (120 Ohm), da Mikrofonkabel nicht geeignet sind und Reflektionen verursachen können.

**XLR-Belegung nach DMX512:**
- Pin 1: Masse (Shield)
- Pin 2: Daten (-)
- Pin 3: Daten (+)
- Pin 4 & 5: Reserve (für zukünftige Protokolle oder RDM)

DMX ist ein unidirektionales Protokoll – das Lichtpult sendet, Geräte empfangen. Für bidirektionale Kommunikation (z. B. zur Statusabfrage) wurde RDM (Remote Device Management) eingeführt, das die selben Kabel nutzt.

**Fehlerquellen in der Praxis:**
- Keine Terminierung am Ende der Leitung
- Einsatz von Audio-XLR-Kabeln statt DMX-Kabeln
- 3-Pol-XLR-Stecker in nicht normgerechten Systemen
- Adressierungskonflikte oder falsche DMX-Kanäle

DMX ist trotz seiner Einfachheit sehr leistungsfähig und wird durch Protokolle wie ArtNet (DMX über Ethernet) oder sACN (Streaming ACN) ergänzt. In der modernen Veranstaltungstechnik ist DMX nach wie vor der Standard zur Steuerung von Scheinwerfern, LED-Panels, Nebelmaschinen, Lasern und vielem mehr.

**Quellen:**
- [Wikipedia – DMX512](https://de.wikipedia.org/wiki/DMX512)
- [USITT – DMX-Standards](https://www.usitt.org)
- [Artistic Licence – DMX Explained](https://artisticlicence.com/)
- [Enttec – DMX Grundlagen](https://www.enttec.com/)
