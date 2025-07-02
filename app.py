from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def show_readme():
    url = "https://raw.githubusercontent.com/RaDiTZz0/subdomain-takeover/refs/heads/main/takeover_poc.html"
    r = requests.get(url)
    if r.status_code == 200:
        return Response(r.text, mimetype='text/html')
    else:
        return f"Erro ao carregar takeover_poc.html: {r.status_code}"
