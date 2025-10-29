from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OCR_SPACE_API_KEY = "helloworld"  # You can use this free key for testing
OCR_URL = "https://api.ocr.space/parse/image"

@app.route('/')
def home():
    return {"message": "Historical Document OCR API is running!"}

@app.route('/analyze', methods=['POST'])
def analyze_document():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image_file = request.files['image']

    # Send image to OCR.Space API
    payload = {"apikey": OCR_SPACE_API_KEY, "language": "eng"}
    response = requests.post(OCR_URL, files={"file": image_file}, data=payload)

    result = response.json()
    try:
        extracted_text = result["ParsedResults"][0]["ParsedText"]
    except Exception:
        return jsonify({"error": "OCR failed", "details": result}), 500

    return jsonify({"text": extracted_text})

if __name__ == '__main__':
    app.run()
