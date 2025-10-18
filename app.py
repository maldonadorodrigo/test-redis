import os
import redis
from flask import Flask, render_template_string

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# HTML simples
HTML_TEMPLATE = """
<!doctype html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Teste Redis</title>
    <style>
      body { font-family: Arial; text-align: center; margin-top: 50px; }
      .status { font-size: 24px; font-weight: bold; }
      .conectado { color: green; }
      .falha { color: red; }
    </style>
  </head>
  <body>
    <div class="status {{ classe }}">{{ mensagem }}</div>
  </body>
</html>
"""

@app.route("/")
def teste_redis():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()
        mensagem = f"✅ Conectado ao Redis em {REDIS_HOST}:{REDIS_PORT}"
        classe = "conectado"
    except redis.ConnectionError as e:
        mensagem = f"❌ Falha na conexão: {e}"
        classe = "falha"
    return render_template_string(HTML_TEMPLATE, mensagem=mensagem, classe=classe)

if __name__ == "__main__":
    # Escuta na porta 5000 e aceita conexões externas
    app.run(host="0.0.0.0", port=5000)
