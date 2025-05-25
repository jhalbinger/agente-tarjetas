from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/respuesta-tarjetas', methods=["POST"])
def responder():
    data = request.get_json()
    consulta_usuario = data.get("consulta", "No se recibió consulta")

    # Aquí podés poner lógica específica si querés personalizar la respuesta
    return jsonify({
        "respuesta": f"El agente de tarjetas recibió la consulta: '{consulta_usuario}' y está trabajando en una respuesta especializada."
    })

if __name__ == '__main__':
    app.run()

