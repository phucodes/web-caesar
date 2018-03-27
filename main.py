from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="/caesar" method="post">
            <label for="encrypt_caesar">
                    Rotate By:
                    <input type="text" name="rot" value="0"/>
                    <textarea type="textarea" name="text" />{0}</textarea>
            </label>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""

@app.route("/caesar", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = request.form['rot']
    input_text = str(text)
    input_rot = int(rot)
    encrypt_message = rotate_string(input_text, input_rot)
    return form.format(encrypt_message)

@app.route("/")
def index():
    return form.format("")

app.run()