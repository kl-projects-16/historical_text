from flask import Flask, request, jsonify
from text_extractor import extract_text_from_image
import tempfile

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Historical Document OCR API is running!"})

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Save uploaded file temporarily
    file = request.files['image']
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        file.save(temp.name)
        text = extract_text_from_image(temp.name)

    return jsonify({"extracted_text": text})

if __name__ == '__main__':
    app.run(debug=True)
