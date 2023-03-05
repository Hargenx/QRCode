import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=10,
                   border=4)
entrada = str(input('Digite o link: '))
qr.add_data(entrada)
qr.make(fit=True)

imagem = qr.make_image(fill_color='black', back_color='white')

imagem.save('qrcode.png')
