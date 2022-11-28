from python:3.9-alpine3.12
RUN apk update && apk add --no-cache  build-base  libffi-dev
COPY stress /api
WORKDIR /api
RUN pip install -r requirements.txt
ENTRYPOINT [ "locust","-f","stress.py"]