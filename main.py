from flask import Flask, request, jsonify
from transcribe_endpoint import transcribe_audio
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/transcribe_file", methods=['POST'])
async def transcribe_file():
    data = json.dumps(request.json)
    file_url = data
    #transcipt = transcribe_audio(file_path)
    # Decodificar la cadena JSON
    enlace_json = json.loads(file_url)

    # Obtener el enlace
    enlace = enlace_json["file_url"]
    file_url = enlace
    print(file_url)
    transciption = transcribe_audio(file_url)
    return transciption


if __name__ == '__main__':
    from waitress import serve
    serve(app,host='0.0.0.0', port=5000)