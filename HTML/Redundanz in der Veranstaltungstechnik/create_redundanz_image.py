#!/usr/bin/env python3
"""
Erstellt ein ansprechendes Header-Bild für das Redundanz-Thema
im Stil der bestehenden Projektbilder
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_redundanz_image():
    # Bildgröße definieren (ähnlich wie andere Header-Bilder)
    width, height = 1200, 400
    
    # Hauptfarben definieren (passend zum blauen Design der Website)
    bg_color = (30, 42, 74)  # Dunkelblau
    primary_blue = (37, 99, 235)  # Hauptblau
    light_blue = (59, 130, 246)  # Hellblau
    accent_blue = (147, 197, 253)  # Akzentblau
    white = (255, 255, 255)
    gray = (156, 163, 175)
    
    # Bild erstellen
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Hintergrund-Gradient simulieren mit Rechtecken
    for i in range(height):
        # Gradient von dunkelblau zu etwas heller
        ratio = i / height
        r = int(bg_color[0] + (primary_blue[0] - bg_color[0]) * ratio * 0.3)
        g = int(bg_color[1] + (primary_blue[1] - bg_color[1]) * ratio * 0.3)
        b = int(bg_color[2] + (primary_blue[2] - bg_color[2]) * ratio * 0.3)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Netzwerk-Knoten als Kreise zeichnen (Redundanz-Konzept)
    nodes = [
        {'pos': (200, 150), 'size': 40, 'color': light_blue, 'label': 'A'},
        {'pos': (400, 100), 'size': 40, 'color': light_blue, 'label': 'B'},
        {'pos': (600, 150), 'size': 40, 'color': light_blue, 'label': 'C'},
        {'pos': (800, 100), 'size': 40, 'color': light_blue, 'label': 'D'},
        {'pos': (1000, 150), 'size': 40, 'color': light_blue, 'label': 'E'},
        {'pos': (400, 250), 'size': 35, 'color': accent_blue, 'label': 'F'},
        {'pos': (600, 300), 'size': 35, 'color': accent_blue, 'label': 'G'},
        {'pos': (800, 250), 'size': 35, 'color': accent_blue, 'label': 'H'}
    ]
    
    # Verbindungslinien zeichnen (redundante Pfade)
    connections = [
        # Hauptpfad
        (nodes[0]['pos'], nodes[1]['pos'], light_blue, 3),
        (nodes[1]['pos'], nodes[2]['pos'], light_blue, 3),
        (nodes[2]['pos'], nodes[3]['pos'], light_blue, 3),
        (nodes[3]['pos'], nodes[4]['pos'], light_blue, 3),
        
        # Redundante Pfade
        (nodes[0]['pos'], nodes[5]['pos'], accent_blue, 2),
        (nodes[1]['pos'], nodes[5]['pos'], accent_blue, 2),
        (nodes[2]['pos'], nodes[6]['pos'], accent_blue, 2),
        (nodes[5]['pos'], nodes[6]['pos'], accent_blue, 2),
        (nodes[6]['pos'], nodes[7]['pos'], accent_blue, 2),
        (nodes[3]['pos'], nodes[7]['pos'], accent_blue, 2),
        (nodes[7]['pos'], nodes[4]['pos'], accent_blue, 2),
        
        # Kreuzverbindungen für höhere Redundanz
        (nodes[0]['pos'], nodes[2]['pos'], gray, 1),
        (nodes[2]['pos'], nodes[4]['pos'], gray, 1),
        (nodes[1]['pos'], nodes[3]['pos'], gray, 1)
    ]
    
    # Verbindungen zeichnen
    for start, end, color, width in connections:
        draw.line([start, end], fill=color, width=width)
    
    # Knoten zeichnen
    for node in nodes:
        x, y = node['pos']
        size = node['size']
        color = node['color']
        
        # Äußerer Kreis (Glow-Effekt)
        draw.ellipse([x-size-3, y-size-3, x+size+3, y+size+3], fill=color, outline=white, width=1)
        # Hauptkreis
        draw.ellipse([x-size, y-size, x+size, y+size], fill=color, outline=white, width=2)
        # Innerer Kreis
        draw.ellipse([x-size+8, y-size+8, x+size-8, y+size-8], fill=white, outline=color, width=1)
    
    # Titel hinzufügen
    try:
        # Versuche eine schöne Schrift zu verwenden
        title_font = ImageFont.truetype("arial.ttf", 48)
        subtitle_font = ImageFont.truetype("arial.ttf", 24)
    except:
        # Fallback auf Standard-Schrift
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    # Haupttitel
    title = "REDUNDANZ IN DER NETZWERKTECHNIK"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    
    # Titel mit Schatten-Effekt
    draw.text((title_x + 2, 32), title, fill=(0, 0, 0), font=title_font)  # Schatten
    draw.text((title_x, 30), title, fill=white, font=title_font)  # Haupttext
    
    # Untertitel
    subtitle = "Ausfallsichere Netzwerkarchitekturen für Veranstaltungstechnik"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    
    draw.text((subtitle_x + 1, 91), subtitle, fill=(0, 0, 0), font=subtitle_font)  # Schatten
    draw.text((subtitle_x, 90), subtitle, fill=accent_blue, font=subtitle_font)  # Haupttext
    
    # Redundanz-Symbole hinzufügen
    # Pfeil-Symbole für Failover
    arrow_points = [
        # Pfeil 1 (Failover-Richtung)
        [(350, 180), (370, 170), (370, 175), (380, 175), (380, 185), (370, 185), (370, 190)],
        # Pfeil 2 (Backup-Pfad)
        [(650, 200), (670, 190), (670, 195), (680, 195), (680, 205), (670, 205), (670, 210)]
    ]
    
    for arrow in arrow_points:
        draw.polygon(arrow, fill=white, outline=light_blue)
    
    # Redundanz-Indikator Texte
    draw.text((320, 195), "Failover", fill=white, font=subtitle_font)
    draw.text((620, 215), "Backup", fill=white, font=subtitle_font)
    
    # Speichern
    output_path = os.path.join(os.path.dirname(__file__), "Redundanz_Netzwerktechnik.webp")
    img.save(output_path, "WEBP", quality=85, optimize=True)
    print(f"Bild erfolgreich erstellt: {output_path}")
    
    return output_path

if __name__ == "__main__":
    create_redundanz_image()
