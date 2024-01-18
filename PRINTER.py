import csv
from PIL import Image, ImageDraw, ImageFont

def create_centered_image(csv_file, output_image_path):
    # Legge il contenuto del file CSV nel path
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        data_rows = list(reader)

    # Imposta il font e la dimensione del font

    # font = ImageFont.load_default()
    font_size = 30
    font_path = './Roboto-Bold.ttf'
    font = ImageFont.truetype(font_path, font_size)

    # Calcola le dimensioni dell'immagine
    cell_padding = 80
    cell_widths = [max(font.getbbox(header, anchor="lt")[2], max(font.getbbox(row[i], anchor="lt")[2] for row in data_rows)) + cell_padding for i, header in enumerate(headers)]
    cell_height = font.getbbox(headers[0], anchor="lt")[3] + cell_padding

    image_width = sum(cell_widths)
    image_height = (len(data_rows) + 1) * cell_height  # +1 for the header

    # Crea un'immagine con sfondo bianco
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Scrive gli header
    x_offset = 0
    for i, header in enumerate(headers):
        draw.text((x_offset + cell_padding // 2, cell_padding // 2), header, font=font, fill="black")
        x_offset += cell_widths[i]

    # Write data rows
    for i, row in enumerate(data_rows, start=1):
        x_offset = 0
        for j, value in enumerate(row):
            draw.text((x_offset + cell_padding // 2, i * cell_height + cell_padding // 2), value, font=font, fill="black")
            x_offset += cell_widths[j]

    # Salva l'immagine nel path di output
    image.save(output_image_path)


csv_file_path = './encoded-fogliotest.csv'
output_image_path = 'pescetto_completo.png'
create_centered_image(csv_file_path, output_image_path)
