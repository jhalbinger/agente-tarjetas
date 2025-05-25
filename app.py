from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/respuesta-tarjetas', methods=["GET"])
def responder():
    return jsonify({
        "respuesta": "Respuesta desde el agente de tarjetas."
    })

if __name__ == '__main__':
    app.run()
