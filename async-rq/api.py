import uvicorn
from fastapi import FastAPI, File, UploadFile
import uuid
from aiofile import async_open
from redis import Redis
from rq import Queue
from ocr import read_img
import time
app = FastAPI()
q = Queue(connection=Redis(host='redis', port=6379),is_async=True, default_timeout=3600, async_timeout=3600, result_ttl=3600)

 
@app.get("/")
def mainPage():
    return {"message": "Use /upload to upload images"}




@app.post("/upload")
async def upload(image: UploadFile = File(...)):
    uuidName = str(uuid.uuid4())
    async with async_open(uuidName, 'wb+') as f:
        await f.write(image.file.read())
    text = q.enqueue(read_img, uuidName)

    print(text.description)
    return text.description


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
