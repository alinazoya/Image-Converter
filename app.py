from flask import Flask, render_template, request, send_file, url_for
from filters import apply_filter
from PIL import Image
import io
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'static/processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        selected_filter = request.form['filter']

        if file:
            image = Image.open(file)
            processed_image = apply_filter(image, selected_filter)

            filename = f"{uuid.uuid4().hex}.png"
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            processed_image.save(file_path)

            return render_template('index.html', download_link=url_for('static', filename=f'processed/{filename}'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
