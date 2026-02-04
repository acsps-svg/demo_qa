from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    # Serve o seu arquivo HTML estático
    return send_file("index.html")

if __name__ == "__main__":
    # Importante para o CI: host 0.0.0.0 ou 127.0.0.1
    app.run(host="127.0.0.1", port=5000)