import qrcode

def generate_qr(url, filename="qrcode.png"):
    # Initialize the QRCode object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add the URL data
    qr.add_data(url)
    qr.make(fit=True)

    # Create the image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the file
    img.save(filename)
    print(f"Success! QR Code saved as {filename}")

if __name__ == "__main__":
    user_url = input("Enter the URL to convert: ")
    generate_qr(user_url)
