# import io
# import qrcode

# from fastapi import FastAPI
# from starlette.responses import StreamingResponse
# from PIL import Image
# from app import create_qr
from dotenv import load_dotenv
import os

# app = FastAPI()

# @app.get("/generate")
# def generate():
#     payload = create_qr(1)
#     img = qrcode.make(payload)
#     buf = io.BytesIO()
#     img.save(buf)
#     buf.seek(0)
#     return StreamingResponse(buf, media_type="image/jpeg")
load_dotenv()
host = os.getenv('PORT')
print(host)