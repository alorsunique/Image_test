from flask import Flask, render_template, send_from_directory
from pathlib import Path

app = Flask(__name__)


image_list = []

@app.route('/')
def home():
    return render_template('index.html', image_list=image_list)


image_folder_directory = Path("D:\Projects\Recovery\Aespa\Savage")

@app.route('/<filename>')
def image_show(filename):
    return send_from_directory(image_folder_directory, filename)

if __name__ == "__main__":

    print("Hello World")

    for file in image_folder_directory.iterdir():
        print(file)
        image_list.append(file.name)

    



    app.run(debug=True)