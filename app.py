from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    target_url = request.args.get('url')
    if not target_url:
        return {"error": "No URL provided"}, 400
    
    response = requests.get(target_url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return {
        "text": soup.get_text(separator="\n", strip=True),
        "links": [link.get('href') for link in soup.find_all('a', href=True) if link.get('href').startswith("http")]
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
