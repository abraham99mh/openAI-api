from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import openai

app = Flask(__name__)

CORS(app, origins='http://localhost:5173')

# Establecer la clave de API de OpenAI
openai.api_key = "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"

# Lista de preprompts preestablecidos
preprompts = {
    1: "Contesta como alienígena: ",
    2: "Contesta como fan de Cristiano Ronaldo: ",
    3: "Contesta como poeta del siglo XVIII: ",
    4: "Contesta como científico loco: "
}


@app.route('/api/v1/open_ai_respuesta', methods=['POST'])
def generar_respuesta():
    print("Generando respuesta...")

    prompt = request.form.get('prompt')
    preprompt = int(request.form.get('preprompt'))

    # Obtener el preprompt correspondiente al valor numérico
    preprompt = preprompts.get(preprompt)
    print(preprompt)

    # Generar la respuesta utilizando la API de OpenAI
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt=preprompt + prompt,
        max_tokens=100,
        temperature=1.0
    )
    respuesta = completion.choices[0].text

    # Devolver la respuesta en formato JSON
    return jsonify({'respuesta': respuesta})


@app.route('/api/v1/open_ai_respuesta', methods=['GET'])
def index():
    return ("My OpenAI API")


if __name__ == '__main__':
    app.run(port=8080, debug=True)
