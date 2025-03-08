from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw, ImageFont
import textwrap
import pytesseract
import io

app = Flask(__name__)

# Configure Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-image', methods=['POST'])
def process_image():
    file = request.files['image']
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)

    width = int(request.form.get('page_width', 600))
    height = int(request.form.get('page_height', 400))
    background_color = request.form.get('page_color', '#FFFFFF')
    text_color = request.form.get('text_color', '#000000')
    font_size = int(request.form.get('font_size', 20))
    font_path = "1.ttf"

    output_image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(output_image)

    font = ImageFont.truetype(font_path, font_size)
    lines = textwrap.wrap(text, width=50)
    y_text = 15

    for line in lines:
        line_width, line_height = font.getbbox(line)[2:]
        draw.text(((width - line_width) / 2, y_text), line, font=font, fill=text_color)
        y_text += line_height

    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
