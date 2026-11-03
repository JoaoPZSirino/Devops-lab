import os
import socket
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

# Chave da API do TheCatAPI (lida de variável de ambiente)
CAT_API_KEY = os.getenv("CAT_API_KEY")

# HTML simples embutido com CSS bonito e botão para gerar novo gatinho
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Projeto Devops</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1a1a2e;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
        }
        .card {
            background-color: #16213e;
            padding: 24px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
            max-width: 500px;
            width: 90%;
        }
        img {
            max-width: 100%;
            height: 350px;
            object-fit: cover;
            border-radius: 8px;
            margin: 16px 0;
        }
        button {
            background-color: #e94560;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            transition: 0.2s;
        }
        button:hover {
            background-color: #ff5773;
            transform: scale(1.05);
        }
        .footer {
            margin-top: 15px;
            font-size: 12px;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Projeto Devops</h1>
        <img src="{{ image_url }}" alt="Foto de gato">
        <div>
            <button onclick="window.location.reload();">Novo Gato</button>
        </div>
        <div class="footer">
            Atendido pelo Pod: <strong>{{ hostname }}</strong>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    """Busca uma foto aleatória na TheCatAPI e exibe na página."""
    image_url = "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg" # fallback
    try:
        headers = {"x-api-key": CAT_API_KEY}
        response = requests.get(
            "https://api.thecatapi.com/v1/images/search", 
            headers=headers, 
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()        
            image_url = data[0]["url"]
    except Exception as e:
        print(f"Erro ao buscar foto: {e}")

    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, image_url=image_url, hostname=hostname)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)