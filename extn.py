from flask import Flask,request, jsonify
from flask_cors import CORS
import cap
from io import BytesIO
import base64
from PIL import Image


app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run():
    """
    Solve the captcha.
    """
    print('Running')
    arg = request.json.get('arg')
    img = Image.open(BytesIO(base64.b64decode(arg)))
    ans = cap.solve(img)
    return jsonify({'answer': ans})

if __name__ == '__main__':
    app.run(debug=True,port=5000)