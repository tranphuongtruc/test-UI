from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/image-to-image')
def image_to_image():
    return render_template('image-to-image.html')


@app.route('/text-to-image')
def text_to_image():
    return render_template('text-to-image.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the file to the 'uploads' folder
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        file_path = os.path.join(upload_folder, file.filename)
        file.save(file_path)
        return 'Successfully uploaded'

    return 'Failed to upload image.'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
