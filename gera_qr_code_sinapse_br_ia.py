import qrcode

# Link do seu repositório corrigido
url = "https://github.com/neirivon/rubrica.sinapse-br-ia"

# Configuração do QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Criando a imagem (Você pode mudar 'black' para 'darkgreen' ou 'darkred')
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code_github_sinapse_br_ia.png")
