from python:3.9-alpine3.12
RUN apk update && apk add --no-cache  build-base tesseract-ocr zlib-dev jpeg-dev
RUN pip install python-multipart rq supervisor
WORKDIR /api
COPY async-rq/requirements.txt /api/requirements.txt
RUN pip install -r requirements.txt
COPY async-rq/objectsStorage.py /api/objectsStorage.py
COPY async-rq/ocr.py /api/ocr.py
COPY async-rq/api.py /api/api.py
COPY async-rq/supervisord.conf /api/supervisord.conf
ENTRYPOINT ["supervisord", "-c", "supervisord.conf" ,"-n"]