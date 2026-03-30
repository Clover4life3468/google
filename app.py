from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    # Render fetches the raw HTML for you
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(target_url, headers=headers)
    return response.text  # Sends raw HTML back to your CLI
