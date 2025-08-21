
# generate a code qr
import qrcode
import requests
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from QR_code.settings import BASE_DIR,MEDIA_URL



def generate_qrcode(output):
    img = qrcode.make("https://www.example.com/okeokf/ffkfoekf/efkoAXS")
    img.save(output)









def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip






def get_geo_from_ip(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    data = response.json()
    return data.get('latitude'), data.get('longitude')






# INSERT THE QR AT THE BOTTOM OF EACH PDF'S PAGE
def insert_qr_pdf(original_pdf,id):
    # Création d’un overlay avec le QR code
    qr_width = 100
    output_pdf = f"media/outputs/output_{original_pdf}{id}.pdf"
    qr_image = f"media/qrcodes/{original_pdf+id}{id}.png"
    print(
        f"""
            {original_pdf}
            {output_pdf}
            {qr_image}
        """
    )
    original_pdf=f"media/inputs/{original_pdf}.pdf"
    generate_qrcode(qr_image)
    page_width,page_height = letter
    x = (page_width - qr_width) / 2
    y = 50

    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawImage(qr_image, x=x, y=y, width=50, height=50)  # position et taille du QR
    can.save()
    packet.seek(0)
    
    # Lire le PDF original
    existing_pdf = PdfReader(original_pdf)
    output = PdfWriter()
    
    overlay_pdf = PdfReader(packet)
    overlay_page = overlay_pdf.pages[0]
    
    for page in existing_pdf.pages:
        page.merge_page(overlay_page)
        output.add_page(page)
    
    with open(output_pdf, "wb") as f:
        output.write(f)
    return output_pdf



# insert_qr_pdf("input.pdf","qrcode.png","done.pdf")

generate_qrcode("media/qrcodes/ubuntupocketguide-v1-1.png")