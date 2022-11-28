# from minio import Minio
import os
from miniopy_async import Minio


async def Storage(miniClient, fileName):
    client = miniClient
    url = await client.fput_object(
        "ocr", fileName, fileName,
    )
    print(
        f"{fileName} is successfully uploaded to bucket ocr."
    )
    if os.path.exists(fileName):
        os.remove(fileName)
    else:
        print(f"{fileName} The file does not exist")
