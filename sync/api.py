import uvicorn
from fastapi import FastAPI, File, UploadFile
import pytesseract
import uuid
from minio import Minio

from objectsStorage import Storage
app = FastAPI()


client = Minio(
    "minio:9000",
    access_key="dc6af2af-194f-47e2-9e6a-a6008158da81",
    secret_key="4c263f63-19dc-454e-ad93-dfddecdeaf12",
    secure=False,
)
found = client.bucket_exists("ocr")
if not found:
    client.make_bucket("ocr")
else:
    print("Bucket 'ocr' already exists")


@app.get("/")
def mainPage():
    return {"message": "Use /upload to upload images"}


def read_img(image):
    print(image, "--------")
    text = pytesseract.image_to_string(image, timeout=120)
    Storage(client, image)
    return text


@app.post("/upload")
def upload(image: UploadFile = File(...)):
    uuidName = str(uuid.uuid4())
    with open(uuidName, 'wb+') as f:
        f.write(image.file.read())
    text = read_img(uuidName)

    print(text)
    return text


# then add the following to the bottom of app.py
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
