import qrcode

# Link da sua aplicação no Streamlit
url = "https://rubrica-sinapse-br-ia.streamlit.app"

# Configurações do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicionando o link
qr.add_data(url)
qr.make(fit=True)

# Criando a imagem (Cores: Preto no fundo Branco)
img = qr.make_image(fill_color="black", back_color="white")

# Salvando o arquivo
img.save("qrcode_sinapse_br_ia.png")

print("QR Code gerado com sucesso: qrcode_sinapse_br_ia.png")
