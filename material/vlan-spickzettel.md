# Spickzettel: VLAN-Design in der Veranstaltungstechnik

- Trenne mindestens nach „Gewerken“: eigenes VLAN für Audio (Dante/Q-SYS), eines für Video/AVoIP, eines für Licht/Steuerung (MA/sACN/Art-Net) und eines für Office/Internet.
- Dante: Trenne nach Möglichkeit Control-/Management-Traffic und Audiostreams (z. B. VLAN Dante-Audio, VLAN Control), vor allem bei gemischten Netzen mit anderen Protokollen.
- Für Dante-Redundanz (Primary/Secondary) besser physisch getrennte Switches/Verkabelung nutzen; VLAN-Redundanz auf demselben Switch ist nur eine logische Trennung.
- AV-Switches (z. B. Netgear AV Line) bieten oft fertige Profile, die VLAN-IDs, QoS und IGMP-Snooping passend für Audio/Video vorkonfigurieren – nutze diese Templates statt alles „from scratch“ zu bauen.
- Uplinks zwischen FOH, Bühne, Regie etc. immer als Trunks konfigurieren und alle benötigten VLANs getaggt transportieren; Endgeräteports dagegen untagged in genau einem VLAN.
- Inter-VLAN-Routing nur dort erlauben, wo es wirklich nötig ist (z. B. FOH-PC soll Dante-Controller für das Audio-VLAN bedienen, aber nicht direkt ins Video-VLAN); Zugriff sauber über Firewall/ACLs begrenzen.
- DHCP pro VLAN sauber planen (oder bewusst nur statische IPs im Audio-VLAN), damit keine „falschen“ Server in Broadcast-Domänen funken und dein Dante/AVoIP-Netz stören.
- Default-VLAN (oft VLAN 1) möglichst nicht für produktiven AV-Traffic verwenden, sondern nur Management oder gar nichts; produktive Netze immer mit eigenen VLAN-IDs dokumentiert anlegen.
