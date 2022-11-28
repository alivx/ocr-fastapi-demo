# from minio import Minio
import os


def Storage(client, fileName):
    url = client.fput_object(
        "ocr", fileName, fileName,
    )
    print(
        f"{fileName} is successfully uploaded to bucket ocr."
    )
    if os.path.exists(fileName):
        os.remove(fileName)
    else:
        print(f"{fileName} The file does not exist")
