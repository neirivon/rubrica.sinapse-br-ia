# pontos_rota.py
pontos = [
    (-18.9579529, -48.2299539, "Casa"),
    (-18.9586936, -48.2315737, "Abelardo_Pena_291"),
    (-18.9375088, -48.2299736, "Terminal_Santa_Luzia"),
    (-18.8850513, -48.2540238, "Terminal_Umuarama"),
    (-18.7645467, -48.2886511, "IFTM_Fazenda_Sobradinho")
]

# Gerar GPX
gpx = '''<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="VHSTVRIPPERS Route Exporter">
  <trk>
    <name>Rota IFTM - VHSTVRIPPERS04</name>
    <trkseg>
'''

for lat, lon, nome in pontos:
    gpx += f'      <trkpt lat="{lat}" lon="{lon}">\n'
    gpx += f'        <name>{nome}</name>\n'
    gpx += '      </trkpt>\n'

gpx += '''    </trkseg>
  </trk>
</gpx>'''

with open("rota_ifmt_vhstvrippers.gpx", "w") as f:
    f.write(gpx)

print("✅ Arquivo GPX salvo: rota_ifmt_vhstvrippers.gpx")
