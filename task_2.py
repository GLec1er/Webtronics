from fastapi import FastAPI
from urllib.parse import quote

app = FastAPI()

@app.post('/encode-url')
def encode_url(url: str):
    if not url:
        return 'Missing URL parameter', 400

    encoded_url = quote(url)
    return encoded_url
