from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def show_readme():
    url = "https://raw.githubusercontent.com/RaDiTZz0/subdomain-takeover/refs/heads/main/README.md"
    r = requests.get(url)
    if r.status_code == 200:
        return Response(r.text, mimetype='text/plain')
    else:
        return f"Erro ao carregar README.md: {r.status_code}"
