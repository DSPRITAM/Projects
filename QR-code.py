import qrcode
import qrcode.constants 


def generate_QR_code(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "blue", back_color = "white")
    img.save("QR_code.png")


url = input("Enter Your URL: ")
generate_QR_code(url)