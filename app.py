from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return "No URL provided", 400

    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(target_url, headers=headers, stream=True)
    
    return Response(
        response.content, 
        status=response.status_code,
        content_type=response.headers.get('Content-Type')
    )
