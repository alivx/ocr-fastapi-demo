from python:3.9-alpine3.12
RUN apk update && apk add --no-cache  build-base tesseract-ocr zlib-dev jpeg-dev
RUN pip install python-multipart
COPY async /api
WORKDIR /api
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python","api.py"]