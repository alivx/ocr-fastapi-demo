import aiopytesseract
from objectsStorage import Storage
from miniopy_async import Minio

client = Minio(
    "localhost:9000",
    access_key="dc6af2af-194f-47e2-9e6a-a6008158da81",
    secret_key="4c263f63-19dc-454e-ad93-dfddecdeaf12",
    secure=False,
)
found = client.bucket_exists("ocr")
if not found:
    client.make_bucket("ocr")
else:
    print("Bucket 'ocr' already exists")

async def read_img(image):
    print(image, "--------")
    text = await aiopytesseract.image_to_string(image, timeout=120)
    await Storage(client, image)
    return text