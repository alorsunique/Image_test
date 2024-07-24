from flask import Flask, render_template, send_from_directory, request
from pathlib import Path
import json

import time
from datetime import datetime

app = Flask(__name__)





def image_list_segment(raw_image_list):
    print("Here")

    raw_length = len(raw_image_list)

    if raw_length % 3 == 0:
        total_rows = raw_length / 3
    else:
        total_rows = (raw_length / 3) + 1

    reverse_raw = raw_image_list.copy()
    reverse_raw.reverse()
    print(reverse_raw)

    image_row_list = []


    total_count = 0
    count = 0

    while count < total_rows:
        
        print("Inside")

        in_count = 0

        inner_image_row_list = []

        while in_count < 3 and total_count < raw_length:

            inner_image_row_list.append(reverse_raw[(count*3)+in_count])
            in_count += 1
            total_count += 1

        image_row_list.append(inner_image_row_list)

        count += 1
        print(count)

    return image_row_list

@app.route('/')
def home():

    image_list = []

    for file in image_folder_directory.iterdir():
        image_list.append(file.name)

    print(len(image_list))
    image_row_list = image_list_segment(image_list)
    print(len(image_row_list))

    print(image_row_list)

    return render_template('index.html', row_list=image_row_list)

@app.route('/<filename>')
def image_show(filename):
    return send_from_directory(image_folder_directory, filename)


@app.route('/data', methods=['POST'])
def data_show():
    data = request.get_json()
    print(data)
    print(type(data))

    print(data["title"])
    print(len(data["title"]))
    print(data['clicked_image'])

    image_list = data['clicked_image']

    time_filter = datetime.now()
    time_filter = time_filter.strftime("%Y%m%d_%H%M%S")
    
    if not len(data['title']) == 0:
        output_name = f"{data['title']}_{time_filter}"
    else:
        output_name = time_filter



    print(output_name)

    for entry in image_list:
        print(entry)

    with open(f"{output_name}.json","w") as content:
        json.dump(data, content)

    return data


@app.route('/test')
def test_page():
    return render_template('test.html')

if __name__ == "__main__":
    image_folder_directory = Path("D:\Projects\Recovery\IVE\Eleven")
    #image_folder_directory = Path(str(input(f"Path: ")).replace('"', ''))
    
    print(f"Directory: {image_folder_directory}")

    app.run(debug=True)
    